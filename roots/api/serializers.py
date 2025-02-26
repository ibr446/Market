from django.conf import settings
from rest_framework import serializers
from .models import User, Address, Brand, Category, Product, ProductImage, Review, Supplier, Order, Wishlist, \
    Comment, CartItem, Deal


class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'phone_number', 'email', 'password', 'confirm_password')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({"confirm_password": "Passwords do not match."})
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')  # Remove confirm_password before saving
        user = User.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)




class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')



class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'  # Barcha maydonlarni qo'shamiz



class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('id', 'name')



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')



class ProductSerializer(serializers.ModelSerializer):
    # user = UserSerializer(write_only=True)

    class Meta:
        model = Product
        fields = ('id', 'user', 'name', 'description', 'price', 'stock')

    # def create(self, validated_data):
    #     user = self.context['request'].user  # Foydalanuvchini olamiz
    #     return Product.objects.create(user=user, **validated_data)



class ProductImageSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = ProductImage
        fields = ('id', 'product', 'image_url')

    def get_product(self, obj):
        return obj.product.name




class SupplierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Supplier
        fields = '__all__'



class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('id', 'user', 'product', 'rating', 'comment')



class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Order
        fields = ('id', 'user', 'brand', 'total_price', 'status', 'created_at')





class WishlistSerializer(serializers.ModelSerializer): # User nomi bilan keladi
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Wishlist
        fields = ['id', 'user','product', 'created_at']



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('user', 'message', 'status', 'created_at')




class CartItemSerializer(serializers.ModelSerializer):
    img = serializers.ImageField()
    class Meta:
        model = CartItem
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.img:
            representation['img'] = settings.BASE_URL + instance.img.url
        else:
            representation['img'] = None
        return representation




class DealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deal
        fields = ('id', 'start_time', 'end_time', 'img', 'discount', 'discount_time')