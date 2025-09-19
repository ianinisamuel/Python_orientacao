class Movie:
    def __init__(self, name, yearLaunch, includePlan, durationMinutes):
        self.name = name
        self.yearLaunch = yearLaunch
        self.includedPlan = includePlan
        self.totalEvaluation = 0
        self.durationMinutes = durationMinutes
        self.evaluators = 0

    def __str__(self):
        return f"Filme: {self.name}"
    
    def techinal_sheet(self):
        print(" --- Dados do Filme ---")
        print(f"Nome do filme: {self.name}")
        print(f"Ano de lançamento: {self.yearLaunch}")
        print(f"Está no plano? {self.includedPlan}")
        print(f"Avaliação do filme: {self.totalEvaluation}")
        print(f"Duração do filme: {self.durationMinutes}")
        print(f"Total de avaliadores: {self.evaluators}")
    

    def evalute(self, note):
        self.totalEvaluation += note #totalEvaluation = totalEvaluation + note
        self.evaluators += 1

    def average(self):
        print(f"Média do filme {self.name}: {self.totalEvaluation / self.evaluators}")

mario = Movie("Super Mario", 2023, True, 130)
avatar = Movie("Avatar", 2023, False, 180)
mario.evalute(9.5)
mario.evalute(8.0)
mario.evalute(6)

mario.techinal_sheet()
mario.average()

avatar.techinal_sheet()
avatar.average()