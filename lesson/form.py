from django import forms


class BookForm(forms.Form):
    isbn = forms.CharField(label='ISBN', required=True, max_length=20)
    title = forms.CharField(label='書名', required=True, max_length=100)
    price = forms.IntegerField(label='価格', required=True, min_value=0)
    publisher = forms.ChoiceField(label='出版社', choices=[('A', 'AAA社'), ('B', 'BBB社'), ('C', 'CCC社'),],)
    published = forms.DateField(label='刊行日', required=True)