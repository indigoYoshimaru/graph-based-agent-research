import subprocess


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
        question,
    ]
    subprocess.call(
        command,
        # stdout="graph_rag/test/output/answers.txt",
        text=True,
    )


if __name__ == "__main__":
    question_dict = load_questions(question_file="questions.json")
    for global_question in question_dict["global_questions"]:
        print(global_question)
        get_answer(question=global_question, method="global")
