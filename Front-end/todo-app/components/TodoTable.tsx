import { table } from "console";

const todo_list = [
  {
    id: 1,
    name: "Task 1",
    description: "Full Stack Developer",
    email: "afzaalm993@gmail.com",
    is_completed: false,
  },
  {
    id: 2,
    name: "Task 2",
    description: "Full Stack Developer",
    email: "task2@gmail.com",
    is_completed: false,
  },
  {
    id: 3,
    name: "Task 3",
    description: "Full Stack Developer",
    email: "task3@gmail.com",
    is_completed: false,
  },
];
export default function TodoTable() {
  return (
    <table className=" w-full">
      <thead>
        <tr className=" flex justify-between items-center px-2 py-1 bg-gray-100 shadow-md">
          <th>Task</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody></tbody>
    </table>
  );
}
