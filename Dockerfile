FROM python:3.9-slim

# Install SpaCy and the English language model
RUN pip install spacy
RUN python -m spacy download en_core_web_sm

# Clone the repository and change the working directory
RUN git clone https://github.com/tasgarner/compulsary_task1.git
WORKDIR /compulsary_task1

# Run the program
CMD ["python", "program.py"]