class StudentScores:
    def __init__(self):
        self.scores = {}

    def add_score(self, name, score):
        self.scores[name] = score

    def sort_by_name(self):
        sorted_scores = sorted(self.scores.items(), key=lambda x: x[0])
        return sorted_scores

    def sort_by_score(self):
        sorted_scores = sorted(self.scores.items(), key=lambda x: x[1], reverse=True)
        return sorted_scores

    def highest_scores(self):
        max_score = max(self.scores.values())
        highest_scorers = [name for name, score in self.scores.items() if score == max_score]
        return highest_scorers, max_score

    def statistics(self):
        num_students = len(self.scores)
        median_score = sorted(self.scores.values())[num_students // 2]
        min_score = min(self.scores.values())
        max_score = max(self.scores.values())

        excellent_count = sum(score >= 8 for score in self.scores.values())
        above_average_count = sum(score >= 5 for score in self.scores.values())
        below_average_count = num_students - above_average_count

        excellent_percentage = (excellent_count / num_students) * 100
        above_average_percentage = (above_average_count / num_students) * 100
        below_average_percentage = (below_average_count / num_students) * 100

        return {
            'num_students': num_students,
            'median_score': median_score,
            'min_score': min_score,
            'max_score': max_score,
            'excellent_percentage': excellent_percentage,
            'above_average_percentage': above_average_percentage,
            'below_average_percentage': below_average_percentage
        }

# Example usage:
if __name__ == "__main__":
    diem_12A = {
    "Nam": 3,
    "Hoài": 5,
    "Liên": 9,
    "Lan": 7,
    "Phương": 8,
    "Xuân": 9,
    "Mai": 1,
    "Tuyết": 9,
    "Bông": 1,
    "Tuyến": 6,
}

    scores_12A = StudentScores()
    for key, value in diem_12A.items():
        scores_12A.add_score(key, value)
    
    # Add other students and their scores here...
    scores_12A.add_score('Loan', 9)
    
    sorted_by_name = scores_12A.sort_by_name()
    sorted_by_score = scores_12A.sort_by_score()
    highest_scorers, max_score = scores_12A.highest_scores()
    statistics = scores_12A.statistics()

    print("Sorted by name:", sorted_by_name)
    print("Sorted by score:", sorted_by_score)
    print("Highest scorers:", highest_scorers, "with score", max_score)
    print("Statistics:")
    print(f"Number of students: {statistics['num_students']}")
    print(f"Median score: {statistics['median_score']}")
    print(f"Minimum score: {statistics['min_score']}")
    print(f"Maximum score: {statistics['max_score']}")
    print(f"Excellent students (%): {statistics['excellent_percentage']:.2f}%")
    print(f"Above average students (%): {statistics['above_average_percentage']:.2f}%")
    print(f"Below average students (%): {statistics['below_average_percentage']:.2f}%")
