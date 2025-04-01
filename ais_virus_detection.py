import numpy as np
import matplotlib.pyplot as plt

# Step 1: Generate self points (representing normal system behavior)
# These points simulate normal network traffic or system activity.
self_points = np.random.rand(100, 2)  # 100 random 2D points in [0,1] x [0,1]

# Step 2: Define the matching radius
# This radius determines how close a point must be to be considered 'self' or 'normal'.
r = 0.1  # Radius for matching self points and detectors

# Step 3: Generate detectors (non-self regions)
# Detectors are points that do not match any self points and will detect anomalies.
def is_self(point, self_points, r):
    """Check if a point is within radius r of any self point."""
    for sp in self_points:
        if np.linalg.norm(point - sp) < r:
            return True
    return False

detectors = []
while len(detectors) < 50:  # Generate 50 detectors
    candidate = np.random.rand(2)
    if not is_self(candidate, self_points, r):
        detectors.append(candidate)
detectors = np.array(detectors)

# Step 4: Generate test points (to simulate new system behavior)
test_points = np.random.rand(40, 2)  # 40 test points

# Step 5: Define ground truth labels (0: normal, 1: anomalous)
# These labels help evaluate the AIS performance.
def is_normal(point, self_points, r):
    """Check if a point is normal (close to self points)."""
    for sp in self_points:
        if np.linalg.norm(point - sp) < r:
            return True
    return False

labels = [0 if is_normal(tp, self_points, r) else 1 for tp in test_points]

# Step 6: Classify test points using detectors
# If a test point is close to any detector, it’s classified as anomalous (1).
def is_detected(point, detectors, r):
    """Check if a point is detected as anomalous by any detector."""
    for d in detectors:
        if np.linalg.norm(point - d) < r:
            return True
    return False

predictions = [1 if is_detected(tp, detectors, r) else 0 for tp in test_points]

# Step 7: Evaluate performance
# Calculate accuracy, false positives, and false negatives.
accuracy = np.mean(np.array(predictions) == np.array(labels))
fp = sum(1 for pred, label in zip(predictions, labels) if pred == 1 and label == 0)
fn = sum(1 for pred, label in zip(predictions, labels) if pred == 0 and label == 1)

print(f"Accuracy: {accuracy:.2f}")
print(f"False Positives: {fp}")
print(f"False Negatives: {fn}")

# Step 8: Visualize results
# Plot self points, detectors, and test points with their true labels.
plt.figure(figsize=(8, 8))
plt.scatter(self_points[:, 0], self_points[:, 1], color='blue', label='Self (Normal)')
plt.scatter(detectors[:, 0], detectors[:, 1], color='red', label='Detectors')

# Plot test points based on true labels
normal_test = test_points[np.array(labels) == 0]
anomalous_test = test_points[np.array(labels) == 1]
plt.scatter(normal_test[:, 0], normal_test[:, 1], color='green', label='Test Normal')
plt.scatter(anomalous_test[:, 0], anomalous_test[:, 1], color='orange', label='Test Anomalous')

plt.title("AIS for Virus Detection: Negative Selection")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid(True)
plt.show()