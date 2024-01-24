from src.insights.jobs import ProcessJobs
from typing import List


class ProcessIndustries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_unique_industries(self) -> List[str]:
        """
        Retorna uma lista de valores únicos presentes na coluna `industry`,
        desconsiderando valores vazios.

        Returns:
            Uma lista de strings contendo tipos únicos de indústria.
        """

        industries = set()
        for job in self.jobs_list:
            industry = job["industry"]
            if industry:
                industries.add(industry)

        return list(industries)
