import { table } from "console";
import Task from "./Task";
import { Todo } from "@/type";



export default async function TodoTable() {
  const response = await fetch('http://127.0.0.1:8080/getTodos')
  const  todo_list : Todo[] = await response.json()
  return (
    <table className=" w-full">
      <thead>
        <tr className=" flex justify-between items-center px-2 py-1 bg-gray-100 shadow-md">
          <th>Task</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        {
            todo_list.map((task:Todo) => (
                          <Task key={task.id} task={task} />
                        ))
        }
      </tbody>
    </table>
  );
}
