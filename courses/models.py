from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_data = models.DateField()
    end_data = models.DateField()
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title

class Enrollment(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_data = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.course.title}"

class Review(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    review_data = models.DateField(auto_now_add=True)
    rating = models.PositiveIntegerField(
        choices=[(i, str(i)) for i in range(1, 6)]
    )
    comment = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.course.title} - {self.rating}"