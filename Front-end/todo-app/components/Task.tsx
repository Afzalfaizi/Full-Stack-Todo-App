import { Todo } from "@/type";
import { CiSquareCheck } from "react-icons/ci";
import { FiEdit } from "react-icons/fi";
import { FiTrash2 } from "react-icons/fi";
export default function Task({task}:{task:Todo}) {
  return (
    <tr>
      <td>{task.name}</td>
      <td>
      <CiSquareCheck />
      <FiEdit />
      <FiTrash2 />
      </td>
    </tr>
  )
}
