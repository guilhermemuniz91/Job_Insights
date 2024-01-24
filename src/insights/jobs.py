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
        """
        Retorna uma lista de valores únicos presentes na coluna `job_type`.

        Args:
            jobs_list: A lista de dicionários contendo os dados do arquivo.

        Returns:
            Uma lista de strings contendo os tipos de emprego únicos.
        """

        unique_job_types = set()
        for job in self.jobs_list:
            job_type = job["job_type"]
            unique_job_types.add(job_type)

        return list(unique_job_types)

    def filter_by_multiple_criteria(
        self, jobs, filter_criteria: Dict
    ) -> List[Dict]:
        """
        Filtra uma lista de empregos por múltiplos critérios.

        Args:
            jobs: Uma lista de empregos a serem filtrados.
            filter_criteria: Um dicionário contendo os critérios de filtragem.

        Returns:
            Uma lista de empregos que correspondem a todos
            os critérios fornecidos.
        """

        filtered_jobs = []

        for job in jobs:
            filters = [
                job["industry"] == filter_criteria["industry"],
                job["job_type"] == filter_criteria["job_type"],
            ]

            if all(filters):
                filtered_jobs.append(
                    {
                        "id": job["id"],
                        "industry": job["industry"],
                        "job_type": job["job_type"],
                    }
                )

        return filtered_jobs
