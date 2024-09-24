import React from 'react';

const TestPanel = ({ tests }) => {
  return (
    <div className="mt-4">
      <h3 className="text-lg font-semibold mb-2">Generated Tests</h3>
      {tests.map((test, index) => (
        <div key={index} className="bg-base-300 p-2 rounded mb-2">
          <p><strong>Input:</strong> {test.input}</p>
          <p><strong>Expected Output:</strong> {test.expected_output}</p>
          <p><strong>Goal Relevance:</strong> {test.goal_relevance}/5</p>
        </div>
      ))}
    </div>
  );
};

export default TestPanel;