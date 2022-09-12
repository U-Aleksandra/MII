using System;
using System.Collections.Generic;
using System.Data.Entity;
using System.Linq;
using System.Web;

namespace Практика_задание2.Models
{
    public class UserContext : DbContext
    {
        public UserContext() :
            base("News_PortalEntities")
        { }

        public DbSet<Users> users { get; set; }
        public DbSet<Role> roles { get; set; }
    }
}