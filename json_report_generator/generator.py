from pathlib import Path

import aiofiles
from core.report_generator import ReportGenerator, ReportGenratorConfigShape


class JsonReportGenratorConfigShape(ReportGenratorConfigShape):
    output_dir: Path


class JsonReportGenerator(
    ReportGenerator[JsonReportGenratorConfigShape], config_shape=JsonReportGenratorConfigShape
):
    async def generate(self) -> None:
        if not self.config.output_dir.exists():
            self.config.output_dir.mkdir(parents=True, exist_ok=True)

        file_name = self.commit_sha + '.json'
        async with aiofiles.open(self.config.output_dir / file_name, 'w') as file:
            await file.write(self.tree_metrics.model_dump_json(indent=4))
