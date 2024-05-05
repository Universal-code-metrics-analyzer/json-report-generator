import aiofiles
from core.metrics_calculator import TreeMetrics
from core.report_generator import ReportGenerator, ReportGenratorConfigShape
from pydantic import FilePath


class JsonReportGenratorConfigShape(ReportGenratorConfigShape):
    output_path: FilePath


class JsonReportGenerator(
    ReportGenerator[JsonReportGenratorConfigShape], config_shape=JsonReportGenratorConfigShape
):
    async def generate(self, tree_metrics: TreeMetrics) -> None:
        async with aiofiles.open(self.config.output_path, 'w') as file:
            await file.write(tree_metrics.model_dump_json(indent=4))
