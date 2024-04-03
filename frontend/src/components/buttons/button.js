import { Button } from "primereact/button"

import taskHandlerMain from "../../utils/taskHandler"

const genericButton = (
  buttonClassName,
  setVisible,
  setAnswer,
  part,
  task,
  variant
) => {
  return (
    <Button
      className={buttonClassName}
      label={`Вариант ${variant}`}
      key={`task-${task}-${variant}`}
      onClick={() =>
        taskHandlerMain({ part, task, variant }, setVisible, setAnswer)
      }
    />
  )
}

export default genericButton
