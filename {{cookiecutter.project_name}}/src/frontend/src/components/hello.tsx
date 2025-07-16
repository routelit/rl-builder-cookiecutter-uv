interface HelloProps {
  name: string;
}

function Hello({ name }: HelloProps) {
  return <p>Hello, {name}!</p>;
}

export default Hello;
