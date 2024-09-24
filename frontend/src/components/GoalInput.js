import React from 'react';

const GoalInput = ({ value, onChange }) => {
  return (
    <div className="mb-4">
      <label htmlFor="goal-input" className="block text-sm font-medium text-base-content">
        Goal (optional)
      </label>
      <textarea
        id="goal-input"
        className="mt-1 block w-full rounded-md bg-base-200 border-transparent focus:border-gray-500 focus:bg-white focus:ring-0"
        rows="2"
        placeholder="Enter your goal for this prompt"
        value={value}
        onChange={e => onChange(e.target.value)}
      ></textarea>
    </div>
  );
};

export default GoalInput;