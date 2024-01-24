from typing import List, Dict
import csv


class ProcessJobs:
    def __init__(self) -> None:
        self.jobs_list = list()

    def read(self, path: str) -> List[Dict]:
        """
        Lê o arquivo CSV e armazena os dados no formato de
        uma lista de dicionários.

        Args:
            path: O caminho para o arquivo CSV.

        Returns:
            A lista de dicionários contendo os dados do arquivo.
        """

        with open(path, "r") as f:
            reader = csv.reader(f, delimiter=",")

            headers = next(reader)

            for row in reader:
                job = {header: value for header, value in zip(headers, row)}
                self.jobs_list.append(job)

            return self.jobs_list

    def get_unique_job_types(self) -> List[str]:
        pass

    def filter_by_multiple_criteria(self) -> List[dict]:
        pass
