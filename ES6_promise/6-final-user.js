import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  const tasks = [
    signUpUser(firstName, lastName),
    uploadPhoto(fileName),
  ];
  return Promise.allSettled(tasks)
    .then((results) => {
      return results.map((r) => {
        if (r.status === 'fulfilled') {
          return { status: r.status, value: r.value  };
        }
        return { status: r.status, value: String(r.reason)};
      });
    });
}
