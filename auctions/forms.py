from django import forms


categories = [
        ("0", "General"),
        ("1", "Fashion"),
        ("2", "Books"),
        ("3", "Health and Lifestyle"),
        ("4", "Home related"),
        ("5", "Electronics"),
        ("6", "Arts and Crafts")
    ]

class NewListingForm(forms.Form):
    title = forms.CharField(label="Listing Title", max_length=64)
    description = forms.CharField(widget=forms.Textarea, label="Item Description", max_length=500)
    bid = forms.DecimalField(decimal_places=2, label="Starting Bid")
    image = forms.URLField(required=False, label="Image URL")
    category = forms.CharField(max_length=64, required=False)
    
    category = forms.ChoiceField(choices=categories, label="Category")

