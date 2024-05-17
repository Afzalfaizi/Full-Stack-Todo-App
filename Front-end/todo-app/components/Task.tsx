import { Todo } from "@/type";

export default function Task({task}:{task:Todo}) {
  return (
    <tr>
      <td>{task.email}</td>
    </tr>
  )
}
