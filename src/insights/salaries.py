from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    content = read(path)
    return max([
        int(salary["max_salary"])
        for salary in content
        if salary["max_salary"].isnumeric()
    ])


def get_min_salary(path: str) -> int:
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    content = read(path)
    return min([
        int(salary["min_salary"])
        for salary in content
        if salary["min_salary"].isnumeric()
    ])


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """

    # min_salary ou max_salary estao ausentes ou nao sao numericos
    try:
        min_salary = int(job["min_salary"])
        max_salary = int(job["max_salary"])
        salary = int(salary)  # salary tem valores não numéricos;
    except (KeyError, TypeError, ValueError):
        raise ValueError
    if min_salary > max_salary:  # min é maior que o valor de max;
        raise ValueError
    return min_salary <= salary <= max_salary
    # True se salary da faixa salarial ou False se não.


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    job_list = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                job_list.append(job)
        except ValueError:
            pass
    return job_list
