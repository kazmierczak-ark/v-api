SET api_definition=https://raw.githubusercontent.com/kazmierczak-ark/v-calculation/main/VCalculateApi/swagger_generated.yaml
SET version=0.1.1
md tmp
md ..\src\libs

REM use codegen
docker run --rm -v "%CD%:/local" openapitools/openapi-generator-cli generate ^
    -i %api_definition% ^
    -g python ^
    -o local/tmp ^
    --additional-properties=packageName=v_calculate_api_client,packageVersion=%version%

REM compile
cd tmp
pip install wheel
python setup.py sdist bdist_wheel
copy dist\v_calculate_api_client-%version%-py3-none-any.whl ..\..\libs\

REM cleanup
cd ..
rd /s /q tmp
