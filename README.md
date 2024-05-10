# UCMA | Json Report Generator Plugin

Report generator plugin, which can be used to save the result of metrics calculation to a JSON file in a format of raw metrics tree.


**Install**

``` bash
poetry add git+https://github.com/Universal-code-metrics-analyzer/json-report-generator@v0.1.0
```

**Runner configuration**

``` yaml
# config.yml

report_generator:
  plugin: json_report_generator
  config:
    # path to a directory where report files will be saved
    # each file will be named after provided ref
    output_dir: reports
```
