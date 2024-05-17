import { Todo } from "@/type";
import { Tooltip } from "@radix-ui/react-tooltip";
import { CiSquareCheck } from "react-icons/ci";
import { FiEdit } from "react-icons/fi";
import { FiTrash2 } from "react-icons/fi";
import ToolTip from "./Tooltip";
import { Modal } from "./Modal";
export default function Task({task}:{task:Todo}) {
  return (
    <tr className=" flex justify-between items-center border-b border-gray-300 px-2 py-2">
      <td>{task.name}</td>
      <td className=" flex gap-x-2">

      <ToolTip tool_tip_content="Mark as completed">
      <CiSquareCheck size={28} className={`${task.is_Completed ? "text-green-500" : "text-gray-300"}`} />
      </ToolTip>
      <Modal title="Edit Task" Editing={true}>
      <FiEdit size={24} className=" text-blue-500"/>
      </Modal>

      <FiTrash2 size={24} className=" text-red-600"/>
      </td>
    </tr>
  )
}
