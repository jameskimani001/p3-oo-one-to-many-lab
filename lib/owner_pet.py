# lib/pet.py

class Pet:
    # Class variable to store all pet types
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    
    # Class variable to store all instances of pets
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        
        # Validate that the pet_type is one of the allowed types
        if self.pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {self.pet_type}. Must be one of {Pet.PET_TYPES}.")
        
        # Add this pet to the all list
        Pet.all.append(self)
        
        # If the pet has an owner, associate the pet with the owner
        if owner:
            self.add_owner(owner)

    def add_owner(self, owner):
        # Make sure the owner is of the correct type
        if not isinstance(owner, Owner):
            raise Exception("Owner must be an instance of the Owner class.")
        self.owner = owner
        owner.add_pet(self)


class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []  # Private list to store the owner's pets
    
    def pets(self):
        """Returns the list of pets owned by this owner."""
        return self._pets
    
    def add_pet(self, pet):
        """Adds a pet to the owner's list, checks if pet is a valid instance."""
        if not isinstance(pet, Pet):
            raise Exception("pet must be an instance of the Pet class.")
        # Check if the pet already belongs to another owner
        if pet.owner and pet.owner != self:
            raise Exception("This pet already belongs to another owner.")
        if pet not in self._pets:
            self._pets.append(pet)
            pet.add_owner(self)

    def get_sorted_pets(self):
        """Returns a list of the owner's pets sorted by their name."""
        return sorted(self._pets, key=lambda pet: pet.name)
