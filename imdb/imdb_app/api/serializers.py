from rest_framework import serializers

from imdb_app.models import Review, WatchList, StreamPlatform


class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Review
        # fields = "__all__"
        exclude = ["watchlist"]


class WatchListSerializer(serializers.ModelSerializer):  
    reviews = ReviewSerializer(many=True, read_only=True)
    
    class Meta:
        model = WatchList
        fields = "__all__"

        
class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True) # watchlist = related_name in models.py return complete object
    # watchlist = serializers.StringRelatedField(many=True) # watchlist in response will be thr string field as in the models __str__ (movie title)
    # watchlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True)  # returns pk in watchlist
    # watchlist= serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='movie-detail') # create a watchlist URL
    
    class Meta:
        model = StreamPlatform
        fields = "__all__"





# ======= General Serializer

# # validator -> passed in model field
# def name_length(value):  
#     if len(value) < 2:
#         raise serializers.ValidationError("movie name is too short")


# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
        
#         instance.save()
        
#         return instance
    
#     # object level validation
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("name and description shouldn't be same")
#         else:
#             return data
    
    
    # field level validation (name field)
    # def validate_name(self, value):
        
    #     if len(value) < 2:
    #         raise serializers.ValidationError("movie name is too short")
    #     else:
    #         return value