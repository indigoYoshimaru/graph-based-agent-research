import subprocess
from loguru import logger


def load_questions(question_file: str) -> dict:
    import json

    with open(question_file, "r") as file:
        data = json.load(file)
    return data


def get_answer(question, method):
    command = [
        "python",
        "-m",
        "graphrag.query",
        "--root",
        "./graph_rag/test/",
        "--method",
        f"{method}",
        f"Don't use the answers from the example, answer the question: {question}",
    ]
    subprocess.call(
        command,
        # stdout="graph_rag/test/output/answers.txt",
        text=True,
    )


if __name__ == "__main__":
    question_dict = load_questions(question_file="questions.json")
    # global questions
    # for global_question in question_dict["global_questions"]:
    #     logger.info(f"Q: {global_question}")
    #     get_answer(question=global_question, method="global")

    # local questions
    for doc_names, question_list in question_dict["local_questions"].items():
        logger.info(f"Local question in document: {doc_names}")
        for question in question_list:
            logger.info(f"Q: {question}")
            get_answer(question=question, method="global")
