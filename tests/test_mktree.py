import os
import unittest
import subprocess

class TestMktree(unittest.TestCase):
    def setUp(self):
        """Set up a temporary directory for testing."""
        self.test_dir = os.path.join(os.path.dirname(__file__), 'test_output')
        if not os.path.exists(self.test_dir):
            os.makedirs(self.test_dir)

    def tearDown(self):
        """Remove the temporary directory after tests."""
        for root, dirs, files in os.walk(self.test_dir, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.rmdir(self.test_dir)

    def test_mktree_structure(self):
        """Test creating a directory structure."""
        # Define a simple structure
        structure = """
        test_project/
            src/
                main.py 755
                utils.py 644
            tests/
                test_utils.py 644
            docs/
                README.md 644
        """

        # Create a temporary structure.txt file
        structure_file = os.path.join(self.test_dir, 'structure.txt')
        with open(structure_file, 'w') as f:
            f.write(structure.strip())

        # Run the mktree script
        result = subprocess.run(['python3', 'src/mktree.py', structure_file], cwd=self.test_dir)

        # Check if the directories and files were created
        expected_paths = [
            os.path.join(self.test_dir, 'test_project'),
            os.path.join(self.test_dir, 'test_project', 'src'),
            os.path.join(self.test_dir, 'test_project', 'tests'),
            os.path.join(self.test_dir, 'test_project', 'docs'),
            os.path.join(self.test_dir, 'test_project', 'src', 'main.py'),
            os.path.join(self.test_dir, 'test_project', 'src', 'utils.py'),
            os.path.join(self.test_dir, 'test_project', 'tests', 'test_utils.py'),
            os.path.join(self.test_dir, 'test_project', 'docs', 'README.md')
        ]

        for path in expected_paths:
            self.assertTrue(os.path.exists(path), f"Path does not exist: {path}")

    def test_file_permissions(self):
        """Test if the created files have the correct permissions."""
        structure = """
        test_project/
            test_file 755
        """

        structure_file = os.path.join(self.test_dir, 'structure.txt')
        with open(structure_file, 'w') as f:
            f.write(structure.strip())

        # Run the mktree script
        subprocess.run(['python3', 'src/mktree.py', structure_file], cwd=self.test_dir)

        # Check permissions
        file_path = os.path.join(self.test_dir, 'test_project', 'test_file')
        permissions = oct(os.stat(file_path).st_mode)[-3:]  # Get last three digits of the permission

        self.assertEqual(permissions, '755', f"Permissions for {file_path} should be 755 but got {permissions}")

if __name__ == '__main__':
    unittest.main()
