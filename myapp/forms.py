from django import forms
from .models import Post, Comment, GameUser

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'message']

class GameUserSignupForm(forms.ModelForm):
    class Meta:
        model = GameUser
        fields = ['server', 'username']

    def clean_username(self):
        return self.cleaned_data.get('username', '').strip()

    # def clean_username(self):
    #     username = self.cleaned_data.get('username', '').strip()
    #     if len(username) < 3:
    #         raise forms.ValidationError('3글자 이상 입력해주세요.')
    #     return username
    #
    # def clean(self):
    #     cleaned_data = super().clean()
    #     if self.check_exist(cleaned_data['server'], cleaned_data['username']):
    #         raise forms.ValidationError('서버에 이미 등록된 username입니다.')
    #     return cleaned_data
    #
    # def check_exist(self, server, username):
    #     return GameUser.objects.filter(server=server, username=username).exist()



























