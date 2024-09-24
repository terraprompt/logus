import React from 'react';
import ReactMarkdown from 'react-markdown';

const Output = ({ content }) => {
  return (
    <div className="mt-4">
      <h3 className="text-lg font-semibold mb-2">Output</h3>
      <div className="bg-base-300 p-4 rounded overflow-auto max-h-96">
        <ReactMarkdown>{content}</ReactMarkdown>
      </div>
    </div>
  );
};

export default Output;