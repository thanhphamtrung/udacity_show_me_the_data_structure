class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    
    for u in group.get_users():
        if u == user:
            return True
    
    for g in group.get_groups():
        if is_user_in_group(user, g):
            return True
    
    return False

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
parentGr = Group("parent")
childGr = Group("child")
sub_childGr = Group("subchild")

sub_child_user = "marry"
sub_childGr.add_user(sub_child_user)

childGr.add_group(sub_childGr)
parentGr.add_group(childGr)

print(is_user_in_group('marry', parentGr))  # expect True
print(is_user_in_group('henry', parentGr))  # expect False

child_user = "child_user"
childGr.add_user(child_user)

# Test Case 2
print(is_user_in_group(child_user, sub_childGr))  # False

# Test Case 3
print(is_user_in_group(child_user, childGr))  # True

# Test Case 4
print(is_user_in_group(child_user, parentGr))  # True

