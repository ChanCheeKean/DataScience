FROM public.ecr.aws/lambda/python:3.9

# Install the function's dependencies using file requirements.txt
# from your project folder.
COPY pg2_similarity_search_lambda/requirements.txt  .
RUN  pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

# Copy function code
COPY pg2_similarity_search_lambda/*.py ${LAMBDA_TASK_ROOT}
COPY pg2_similarity_search_lambda/models ${LAMBDA_TASK_ROOT}/models

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "main.handler" ]