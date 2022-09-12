using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Security;
using Практика_задание2.Models;

namespace Практика_задание2.Providers
{
    public class CustomRoleProvider : RoleProvider
    {
        public override string[] GetRolesForUser(string username)
        {
            string[] role = new string[] { };
            using (UserContext db = new UserContext())
            {
                Users user = db.users.FirstOrDefault(u => u.Email == username);
                if(user != null)
                {
                    Role userRole = db.roles.Find(user.RoleId);
                    if(userRole != null)
                    {
                        role = new string[] { userRole.Name };
                    }
                }
            }
            return role;
        }
        public override void CreateRole(string roleName)
        {
            throw new NotImplementedException();
        }
        public override bool IsUserInRole(string username, string roleName)
        {
            bool outputResult = false;
            using(UserContext db = new UserContext())
            {
                Users user = db.users.FirstOrDefault(u => u.Email == username);
                if(user != null)
                {
                    Role userRole = db.roles.Find(user.RoleId);
                    if (userRole != null && userRole.Name == roleName)
                        return outputResult;
                }
            }
            return outputResult;
        }
        public override void AddUsersToRoles(string[] usernames, string[] roleNames)
        {
            throw new NotImplementedException();
        }

        public override string ApplicationName
        {
            get { throw new NotImplementedException(); }
            set { throw new NotImplementedException(); }
        }

        public override bool DeleteRole(string roleName, bool throwOnPopulatedRole)
        {
            throw new NotImplementedException();
        }

        public override string[] FindUsersInRole(string roleName, string usernameToMatch)
        {
            throw new NotImplementedException();
        }

        public override string[] GetAllRoles()
        {
            throw new NotImplementedException();
        }

        public override string[] GetUsersInRole(string roleName)
        {
            throw new NotImplementedException();
        }

        public override void RemoveUsersFromRoles(string[] usernames, string[] roleNames)
        {
            throw new NotImplementedException();
        }

        public override bool RoleExists(string roleName)
        {
            throw new NotImplementedException();
        }
    
}
}