FROM public.ecr.aws/lambda/python:3.9

# Install the function's dependencies using file requirements.txt
# from project folder.
COPY pg1_fig_output_lambda/requirements.txt  .
RUN  pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

# Copy function code
COPY pg1_fig_output_lambda/*.py utils/constants.py ${LAMBDA_TASK_ROOT}

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "main.handler" ]