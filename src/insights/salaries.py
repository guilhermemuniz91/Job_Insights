from typing import Union, List, Dict
from src.insights.jobs import ProcessJobs


class ProcessSalaries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_max_salary(self) -> int:
        """
        Retorna o maior salário presente na coluna `max_salary`.

        Desconsidera valores ausentes.

        Returns:
            Um valor inteiro com o maior salário.
        """

        max_salary = 0
        for job in self.jobs_list:
            # método isdigit verifica se a string é um número, retorno booleano
            if job["max_salary"].isdigit():
                max_salary = max(max_salary, int(job["max_salary"]))

        return max_salary

    def get_min_salary(self) -> int:
        """
        Retorna o menor salário presente na coluna `min_salary`.

        Desconsidera valores ausentes.

        Returns:
            Um valor inteiro com o menor salário.
        """

        # inicializa a variável com o maior valor possível
        min_salary = self.get_max_salary()

        for job in self.jobs_list:
            if job["min_salary"].isdigit():
                min_salary = min(min_salary, int(job["min_salary"]))

        return min_salary

    def matches_salary_range(self, job: Dict, salary: Union[int, str]) -> bool:
        # Verificar se as chaves 'min_salary' e 'max_salary' estão presentes
        if "min_salary" not in job or "max_salary" not in job:
            raise ValueError(
                "As chaves min_salary e max_salary devem estar presentes"
            )

        min_salary = job["min_salary"]
        max_salary = job["max_salary"]

        # Verificar se os valores de 'min_salary', 'max_salary' e 'salary'
        # são numéricos
        try:
            min_salary = int(min_salary)
            max_salary = int(max_salary)
            salary = int(salary)
        except (TypeError, ValueError):
            raise ValueError(
                "Os valores de min_salary e max_salary devem ser numéricos"
                )

        # Verificar se 'min_salary' é menor que 'max_salary'
        if min_salary > max_salary:
            raise ValueError(
                "O valor de min_salary deve ser menor que o de max_salary"
            )

        # Verifica se o critério 'salary' está dentro do
        # range de 'min_salary' e 'max_salary'
        return min_salary <= salary <= max_salary

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        pass
