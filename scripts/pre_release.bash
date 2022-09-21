export CODECOV_TOKEN="241e63ea-25aa-4a6d-a4cb-dd207e1f2806"

echo "Generate Coverage Report"
coverage run -m pytest

echo "Convert report to XML"
coverage xml

echo "upload coverage report"
codecov -vt $CODECOV_TOKEN