import React from 'react';

const ConsoleLog = ({ logs }) => {
  return (
    <div className="mt-4 bg-base-300 p-2 rounded">
      <h3 className="text-lg font-semibold mb-2">Console Log</h3>
      {logs.map((log, index) => (
        <div key={index} className={`text-${log.type === 'error' ? 'error' : 'info'}`}>
          {log.message}
        </div>
      ))}
    </div>
  );
};

export default ConsoleLog;