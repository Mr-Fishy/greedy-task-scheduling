import unittest
import heapq

def min_missed_penalty(tasks: list[tuple[int, int]]) -> int:
    """
    Calculates the minimum total penalty for missed unit-time tasks.

    Args:
        tasks (list[tuple[int, int]]): The list of tasks. Each task is interpreted as `(deadline, penalty)`.
                                       Deadlines are assumed to be strictly positive integers (>= 1).

    Returns:
        int: The minimum possible penalty incurred from missed deadlines.
    """
    # Sort the tasks by deadline (monotonically increasing)
    sorted_tasks = sorted(tasks, key = lambda x: x[0])
    
    accepted_tasks_heap = []
    total_missed_penalty = 0
    
    for deadline, penalty in sorted_tasks:
        # Push the current task's penalty onto the heap
        heapq.heappush(accepted_tasks_heap, penalty)
        
        # The size of the heap represents the time required to complete all accepted tasks. 
        # If it exceeds the current deadline, drop the task with the smallest penalty.
        if len(accepted_tasks_heap) > deadline:
            dropped_penalty = heapq.heappop(accepted_tasks_heap)
            total_missed_penalty += dropped_penalty
    
    # Return the accumulated penalties.
    return total_missed_penalty

class TestTaskScheduling(unittest.TestCase):
    """
    The testing runtime class.
    """
    
    def test_standard_case(self):
        """
        Tests a mix of deadlines and penalties.
        
        Tasks: (1, 10), (1, 20), (2, 30), (2, 40)  
        Scheduled: (2, 30), (2, 40)  
        Missed: (1, 10), (1, 20)  
        Penalty: 30
        """ 
        tasks = [(1, 10), (1, 20), (2, 20), (2, 40)]
        
        self.assertEqual(min_missed_penalty(tasks), 30)
    
    def test_all_completed_on_time(self):
        """
        Tests with plenty of time to finish everything.
        
        Tasks: (1, 10), (2, 20), (3, 30)  
        Scheduled: (1, 10), (2, 20), (3, 30)  
        Missed: None  
        Penalty: 0
        """
        tasks = [(1, 10), (2, 20), (3, 30)]
        
        self.assertEqual(min_missed_penalty(tasks), 0)
    
    def test_all_same_deadline(self):
        """
        Everything is due at `t = 1`. Can only complete the highest penalty task.
        
        Tasks: (1, 10), (1, 50), (1, 20)  
        Scheduled: (1, 50)  
        Missed: (1, 10), (1, 20)  
        Penalty: 30
        """
        tasks = [(1, 10), (1, 50), (1, 20)]
        
        self.assertEqual(min_missed_penalty(tasks), 30)
    
    def test_empty_task_list(self):
        """
        Edge case of no tasks to schedule.
        """
        tasks = []
        
        self.assertEqual(min_missed_penalty(tasks), 0)
    
    def test_zero_penalties(self):
        """
        Tasks have deadlines but no penalty for missing them.
        """
        tasks = [(1, 0), (2, 0), (1, 0)]
        
        self.assertEqual(min_missed_penalty(tasks), 0)
    
    def test_large_deadlines(self):
        """
        Deadlines are much larger than the number of tasks.
        """
        tasks = [(100, 10), (200, 20), (300, 30)]
        
        self.assertEqual(min_missed_penalty(tasks), 0)
    
    def test_complex_unsorted_input(self):
        """
        A more complex array of tasks that are unsorted.
        
        Tasks: (4, 70), (2, 60), (4, 50), (3, 40), (1, 30), (4, 20), (6, 10)
        Expected: 
        """
        tasks = [(4, 70), (2, 60), (4, 50), (3, 40), (1, 30), (4, 20), (6, 10)]
        
        self.assertEqual(min_missed_penalty(tasks), 50)

if __name__ == "__main__":
    unittest.main()
