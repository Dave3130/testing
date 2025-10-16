# coding: UTF-8
import sys
bstack1llllll_opy_ = sys.version_info [0] == 2
bstack11l1l1l_opy_ = 2048
bstack1111ll_opy_ = 7
def bstack1lllll1_opy_ (bstack1l1_opy_):
    global bstack111ll11_opy_
    bstackl_opy_ = ord (bstack1l1_opy_ [-1])
    bstack1l1l_opy_ = bstack1l1_opy_ [:-1]
    bstack111ll_opy_ = bstackl_opy_ % len (bstack1l1l_opy_)
    bstack111l_opy_ = bstack1l1l_opy_ [:bstack111ll_opy_] + bstack1l1l_opy_ [bstack111ll_opy_:]
    if bstack1llllll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1lll1ll_opy_)
import collections
import datetime
import json
import os
import platform
import re
import subprocess
import traceback
import tempfile
import multiprocessing
import threading
import sys
import logging
from math import ceil
from unittest import result
import urllib
from urllib.parse import urlparse
import copy
import zipfile
import git
import requests
from packaging import version
from bstack_utils.config import Config
from bstack_utils.constants import (bstack1l11111111_opy_, bstack111l1ll111_opy_, bstack1l11lll1l1_opy_,
                                    bstack11l1l1l1lll_opy_, bstack11l1l111l1l_opy_, bstack11l1l111lll_opy_, bstack11l11lll11l_opy_)
from bstack_utils.measure import measure
from bstack_utils.messages import bstack1lll1llll1_opy_, bstack111l11l1l1_opy_
from bstack_utils.proxy import bstack111l111l1_opy_, bstack1ll1ll1lll_opy_
from bstack_utils.constants import *
from bstack_utils import bstack1ll11111l1_opy_
from bstack_utils.bstack11111ll1l_opy_ import bstack1lll1ll11l_opy_
from browserstack_sdk._version import __version__
bstack11l1111l_opy_ = Config.bstack11111l1l_opy_()
logger = bstack1ll11111l1_opy_.get_logger(__name__, bstack1ll11111l1_opy_.bstack1l1l111l111_opy_())
def bstack111l1111l1l_opy_(config):
    return config[bstack1lllll1_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬᯋ")]
def bstack1111ll1ll11_opy_(config):
    return config[bstack1lllll1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧᯌ")]
def bstack11l1l1lll_opy_():
    try:
        import playwright
        return True
    except ImportError:
        return False
def bstack111l11111ll_opy_(obj):
    values = []
    bstack111ll1111l1_opy_ = re.compile(bstack1lllll1_opy_ (u"ࡷࠨ࡞ࡄࡗࡖࡘࡔࡓ࡟ࡕࡃࡊࡣࡡࡪࠫࠥࠤᯍ"), re.I)
    for key in obj.keys():
        if bstack111ll1111l1_opy_.match(key):
            values.append(obj[key])
    return values
def bstack1111l1l1ll1_opy_(config):
    tags = []
    tags.extend(bstack111l11111ll_opy_(os.environ))
    tags.extend(bstack111l11111ll_opy_(config))
    return tags
def bstack111l111l1ll_opy_(markers):
    tags = []
    for marker in markers:
        tags.append(marker.name)
    return tags
def bstack111l1l111l1_opy_(bstack111l1111lll_opy_):
    if not bstack111l1111lll_opy_:
        return bstack1lllll1_opy_ (u"࠭ࠧᯎ")
    return bstack1lllll1_opy_ (u"ࠢࡼࡿࠣࠬࢀࢃࠩࠣᯏ").format(bstack111l1111lll_opy_.name, bstack111l1111lll_opy_.email)
def bstack111l1llll1l_opy_():
    try:
        repo = git.Repo(search_parent_directories=True)
        bstack111ll111ll1_opy_ = repo.common_dir
        info = {
            bstack1lllll1_opy_ (u"ࠣࡵ࡫ࡥࠧᯐ"): repo.head.commit.hexsha,
            bstack1lllll1_opy_ (u"ࠤࡶ࡬ࡴࡸࡴࡠࡵ࡫ࡥࠧᯑ"): repo.git.rev_parse(repo.head.commit, short=True),
            bstack1lllll1_opy_ (u"ࠥࡦࡷࡧ࡮ࡤࡪࠥᯒ"): repo.active_branch.name,
            bstack1lllll1_opy_ (u"ࠦࡹࡧࡧࠣᯓ"): repo.git.describe(all=True, tags=True, exact_match=True),
            bstack1lllll1_opy_ (u"ࠧࡩ࡯࡮࡯࡬ࡸࡹ࡫ࡲࠣᯔ"): bstack111l1l111l1_opy_(repo.head.commit.committer),
            bstack1lllll1_opy_ (u"ࠨࡣࡰ࡯ࡰ࡭ࡹࡺࡥࡳࡡࡧࡥࡹ࡫ࠢᯕ"): repo.head.commit.committed_datetime.isoformat(),
            bstack1lllll1_opy_ (u"ࠢࡢࡷࡷ࡬ࡴࡸࠢᯖ"): bstack111l1l111l1_opy_(repo.head.commit.author),
            bstack1lllll1_opy_ (u"ࠣࡣࡸࡸ࡭ࡵࡲࡠࡦࡤࡸࡪࠨᯗ"): repo.head.commit.authored_datetime.isoformat(),
            bstack1lllll1_opy_ (u"ࠤࡦࡳࡲࡳࡩࡵࡡࡰࡩࡸࡹࡡࡨࡧࠥᯘ"): repo.head.commit.message,
            bstack1lllll1_opy_ (u"ࠥࡶࡴࡵࡴࠣᯙ"): repo.git.rev_parse(bstack1lllll1_opy_ (u"ࠦ࠲࠳ࡳࡩࡱࡺ࠱ࡹࡵࡰ࡭ࡧࡹࡩࡱࠨᯚ")),
            bstack1lllll1_opy_ (u"ࠧࡩ࡯࡮࡯ࡲࡲࡤ࡭ࡩࡵࡡࡧ࡭ࡷࠨᯛ"): bstack111ll111ll1_opy_,
            bstack1lllll1_opy_ (u"ࠨࡷࡰࡴ࡮ࡸࡷ࡫ࡥࡠࡩ࡬ࡸࡤࡪࡩࡳࠤᯜ"): subprocess.check_output([bstack1lllll1_opy_ (u"ࠢࡨ࡫ࡷࠦᯝ"), bstack1lllll1_opy_ (u"ࠣࡴࡨࡺ࠲ࡶࡡࡳࡵࡨࠦᯞ"), bstack1lllll1_opy_ (u"ࠤ࠰࠱࡬࡯ࡴ࠮ࡥࡲࡱࡲࡵ࡮࠮ࡦ࡬ࡶࠧᯟ")]).strip().decode(
                bstack1lllll1_opy_ (u"ࠪࡹࡹ࡬࠭࠹ࠩᯠ")),
            bstack1lllll1_opy_ (u"ࠦࡱࡧࡳࡵࡡࡷࡥ࡬ࠨᯡ"): repo.git.describe(tags=True, abbrev=0, always=True),
            bstack1lllll1_opy_ (u"ࠧࡩ࡯࡮࡯࡬ࡸࡸࡥࡳࡪࡰࡦࡩࡤࡲࡡࡴࡶࡢࡸࡦ࡭ࠢᯢ"): repo.git.rev_list(
                bstack1lllll1_opy_ (u"ࠨࡻࡾ࠰࠱ࡿࢂࠨᯣ").format(repo.head.commit, repo.git.describe(tags=True, abbrev=0, always=True)), count=True)
        }
        remotes = repo.remotes
        bstack111ll111l1l_opy_ = []
        for remote in remotes:
            bstack1111l1lllll_opy_ = {
                bstack1lllll1_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᯤ"): remote.name,
                bstack1lllll1_opy_ (u"ࠣࡷࡵࡰࠧᯥ"): remote.url,
            }
            bstack111ll111l1l_opy_.append(bstack1111l1lllll_opy_)
        bstack111l1llll11_opy_ = {
            bstack1lllll1_opy_ (u"ࠤࡱࡥࡲ࡫᯦ࠢ"): bstack1lllll1_opy_ (u"ࠥ࡫࡮ࡺࠢᯧ"),
            **info,
            bstack1lllll1_opy_ (u"ࠦࡷ࡫࡭ࡰࡶࡨࡷࠧᯨ"): bstack111ll111l1l_opy_
        }
        bstack111l1llll11_opy_ = bstack1111ll1l11l_opy_(bstack111l1llll11_opy_)
        return bstack111l1llll11_opy_
    except git.InvalidGitRepositoryError:
        return {}
    except Exception as err:
        print(bstack1lllll1_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡵࡵࡰࡶ࡮ࡤࡸ࡮ࡴࡧࠡࡉ࡬ࡸࠥࡳࡥࡵࡣࡧࡥࡹࡧࠠࡸ࡫ࡷ࡬ࠥ࡫ࡲࡳࡱࡵ࠾ࠥࢁࡽࠣᯩ").format(err))
        return {}
def bstack11lll11l1ll_opy_(bstack1111l1l11l1_opy_=None):
    bstack1lllll1_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࡇࡦࡶࠣ࡫࡮ࡺࠠ࡮ࡧࡷࡥࡩࡧࡴࡢࠢࡶࡴࡪࡩࡩࡧ࡫ࡦࡥࡱࡲࡹࠡࡨࡲࡶࡲࡧࡴࡵࡧࡧࠤ࡫ࡵࡲࠡࡃࡌࠤࡸ࡫࡬ࡦࡥࡷ࡭ࡴࡴࠠࡶࡵࡨࠤࡨࡧࡳࡦࡵࠣࡪࡴࡸࠠࡦࡣࡦ࡬ࠥ࡬࡯࡭ࡦࡨࡶࠥ࡯࡮ࠡࡶ࡫ࡩࠥࡲࡩࡴࡶ࠱ࠎࠥࠦࠠࠡࡃࡵ࡫ࡸࡀࠊࠡࠢࠣࠤࠥࠦࠠࠡࡨࡲࡰࡩ࡫ࡲࡴࠢࠫࡰ࡮ࡹࡴ࠭ࠢࡲࡴࡹ࡯࡯࡯ࡣ࡯࠭࠿ࠦࡌࡪࡵࡷࠤࡴ࡬ࠠࡧࡱ࡯ࡨࡪࡸࠠࡱࡣࡷ࡬ࡸࠦࡴࡰࠢࡨࡼࡹࡸࡡࡤࡶࠣ࡫࡮ࡺࠠ࡮ࡧࡷࡥࡩࡧࡴࡢࠢࡩࡶࡴࡳ࠮ࠡࡆࡨࡪࡦࡻ࡬ࡵࡵࠣࡸࡴ࡛ࠦࡰࡵ࠱࡫ࡪࡺࡣࡸࡦࠫ࠭ࡢ࠴ࠊࠡࠢࠣࠤࡗ࡫ࡴࡶࡴࡱࡷ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠ࡭࡫ࡶࡸ࠿ࠦࡌࡪࡵࡷࠤࡴ࡬ࠠࡥ࡫ࡦࡸࡸ࠲ࠠࡦࡣࡦ࡬ࠥࡩ࡯࡯ࡶࡤ࡭ࡳ࡯࡮ࡨࠢࡪ࡭ࡹࠦ࡭ࡦࡶࡤࡨࡦࡺࡡࠡࡨࡲࡶࠥࡧࠠࡧࡱ࡯ࡨࡪࡸ࠮ࠋࠢࠣࠤࠥࠨࠢࠣᯪ")
    if bstack1111l1l11l1_opy_ == None: # bstack1111ll11111_opy_ for bstack11lll1111l1_opy_-repo
        bstack1111l1l11l1_opy_ = [os.getcwd()]
    results = []
    for folder in bstack1111l1l11l1_opy_:
        try:
            repo = git.Repo(folder, search_parent_directories=True)
            result = {
                bstack1lllll1_opy_ (u"ࠢࡱࡴࡌࡨࠧᯫ"): bstack1lllll1_opy_ (u"ࠣࠤᯬ"),
                bstack1lllll1_opy_ (u"ࠤࡩ࡭ࡱ࡫ࡳࡄࡪࡤࡲ࡬࡫ࡤࠣᯭ"): [],
                bstack1lllll1_opy_ (u"ࠥࡥࡺࡺࡨࡰࡴࡶࠦᯮ"): [],
                bstack1lllll1_opy_ (u"ࠦࡵࡸࡄࡢࡶࡨࠦᯯ"): bstack1lllll1_opy_ (u"ࠧࠨᯰ"),
                bstack1lllll1_opy_ (u"ࠨࡣࡰ࡯ࡰ࡭ࡹࡓࡥࡴࡵࡤ࡫ࡪࡹࠢᯱ"): [],
                bstack1lllll1_opy_ (u"ࠢࡱࡴࡗ࡭ࡹࡲࡥ᯲ࠣ"): bstack1lllll1_opy_ (u"ࠣࠤ᯳"),
                bstack1lllll1_opy_ (u"ࠤࡳࡶࡉ࡫ࡳࡤࡴ࡬ࡴࡹ࡯࡯࡯ࠤ᯴"): bstack1lllll1_opy_ (u"ࠥࠦ᯵"),
                bstack1lllll1_opy_ (u"ࠦࡵࡸࡒࡢࡹࡇ࡭࡫࡬ࠢ᯶"): bstack1lllll1_opy_ (u"ࠧࠨ᯷")
            }
            bstack111l11l111l_opy_ = repo.active_branch.name
            bstack1111llll11l_opy_ = repo.head.commit
            result[bstack1lllll1_opy_ (u"ࠨࡰࡳࡋࡧࠦ᯸")] = bstack1111llll11l_opy_.hexsha
            bstack111l1l1ll11_opy_ = _1111l1ll1ll_opy_(repo)
            logger.debug(bstack1lllll1_opy_ (u"ࠢࡃࡣࡶࡩࠥࡨࡲࡢࡰࡦ࡬ࠥ࡬࡯ࡳࠢࡦࡳࡲࡶࡡࡳ࡫ࡶࡳࡳࡀࠠࠣ᯹") + str(bstack111l1l1ll11_opy_) + bstack1lllll1_opy_ (u"ࠣࠤ᯺"))
            if bstack111l1l1ll11_opy_:
                try:
                    bstack1111llll1l1_opy_ = repo.git.diff(bstack1lllll1_opy_ (u"ࠤ࠰࠱ࡳࡧ࡭ࡦ࠯ࡲࡲࡱࡿࠢ᯻"), bstack1lll1lll11l_opy_ (u"ࠥࡿࡧࡧࡳࡦࡡࡥࡶࡦࡴࡣࡩࡿ࠱࠲࠳ࢁࡣࡶࡴࡵࡩࡳࡺ࡟ࡣࡴࡤࡲࡨ࡮ࡽࠣ᯼")).split(bstack1lllll1_opy_ (u"ࠫࡡࡴࠧ᯽"))
                    logger.debug(bstack1lllll1_opy_ (u"ࠧࡉࡨࡢࡰࡪࡩࡩࠦࡦࡪ࡮ࡨࡷࠥࡨࡥࡵࡹࡨࡩࡳࠦࡻࡣࡣࡶࡩࡤࡨࡲࡢࡰࡦ࡬ࢂࠦࡡ࡯ࡦࠣࡿࡨࡻࡲࡳࡧࡱࡸࡤࡨࡲࡢࡰࡦ࡬ࢂࡀࠠࠣ᯾") + str(bstack1111llll1l1_opy_) + bstack1lllll1_opy_ (u"ࠨࠢ᯿"))
                    result[bstack1lllll1_opy_ (u"ࠢࡧ࡫࡯ࡩࡸࡉࡨࡢࡰࡪࡩࡩࠨᰀ")] = [f.strip() for f in bstack1111llll1l1_opy_ if f.strip()]
                    commits = list(repo.iter_commits(bstack1lll1lll11l_opy_ (u"ࠣࡽࡥࡥࡸ࡫࡟ࡣࡴࡤࡲࡨ࡮ࡽ࠯࠰ࡾࡧࡺࡸࡲࡦࡰࡷࡣࡧࡸࡡ࡯ࡥ࡫ࢁࠧᰁ")))
                except Exception:
                    logger.debug(bstack1lllll1_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥ࡭ࡥࡵࠢࡦ࡬ࡦࡴࡧࡦࡦࠣࡪ࡮ࡲࡥࡴࠢࡩࡶࡴࡳࠠࡣࡴࡤࡲࡨ࡮ࠠࡤࡱࡰࡴࡦࡸࡩࡴࡱࡱ࠲ࠥࡌࡡ࡭࡮࡬ࡲ࡬ࠦࡢࡢࡥ࡮ࠤࡹࡵࠠࡳࡧࡦࡩࡳࡺࠠࡤࡱࡰࡱ࡮ࡺࡳ࠯ࠤᰂ"))
                    commits = list(repo.iter_commits(max_count=10))
                    if commits:
                        result[bstack1lllll1_opy_ (u"ࠥࡪ࡮ࡲࡥࡴࡅ࡫ࡥࡳ࡭ࡥࡥࠤᰃ")] = _1111lll1111_opy_(commits[:5])
            else:
                commits = list(repo.iter_commits(max_count=10))
                if commits:
                    result[bstack1lllll1_opy_ (u"ࠦ࡫࡯࡬ࡦࡵࡆ࡬ࡦࡴࡧࡦࡦࠥᰄ")] = _1111lll1111_opy_(commits[:5])
            bstack1111l1l1lll_opy_ = set()
            bstack111l11lll1l_opy_ = []
            for commit in commits:
                logger.debug(bstack1lllll1_opy_ (u"ࠧࡖࡲࡰࡥࡨࡷࡸ࡯࡮ࡨࠢࡦࡳࡲࡳࡩࡵ࠼ࠣࠦᰅ") + str(commit.message) + bstack1lllll1_opy_ (u"ࠨࠢᰆ"))
                bstack111l1l11l1l_opy_ = commit.author.name if commit.author else bstack1lllll1_opy_ (u"ࠢࡖࡰ࡮ࡲࡴࡽ࡮ࠣᰇ")
                bstack1111l1l1lll_opy_.add(bstack111l1l11l1l_opy_)
                bstack111l11lll1l_opy_.append({
                    bstack1lllll1_opy_ (u"ࠣ࡯ࡨࡷࡸࡧࡧࡦࠤᰈ"): commit.message.strip(),
                    bstack1lllll1_opy_ (u"ࠤࡸࡷࡪࡸࠢᰉ"): bstack111l1l11l1l_opy_
                })
            result[bstack1lllll1_opy_ (u"ࠥࡥࡺࡺࡨࡰࡴࡶࠦᰊ")] = list(bstack1111l1l1lll_opy_)
            result[bstack1lllll1_opy_ (u"ࠦࡨࡵ࡭࡮࡫ࡷࡑࡪࡹࡳࡢࡩࡨࡷࠧᰋ")] = bstack111l11lll1l_opy_
            result[bstack1lllll1_opy_ (u"ࠧࡶࡲࡅࡣࡷࡩࠧᰌ")] = bstack1111llll11l_opy_.committed_datetime.strftime(bstack1lllll1_opy_ (u"ࠨ࡚ࠥ࠯ࠨࡱ࠲ࠫࡤࠣᰍ"))
            if (not result[bstack1lllll1_opy_ (u"ࠢࡱࡴࡗ࡭ࡹࡲࡥࠣᰎ")] or result[bstack1lllll1_opy_ (u"ࠣࡲࡵࡘ࡮ࡺ࡬ࡦࠤᰏ")].strip() == bstack1lllll1_opy_ (u"ࠤࠥᰐ")) and bstack1111llll11l_opy_.message:
                bstack111l111llll_opy_ = bstack1111llll11l_opy_.message.strip().splitlines()
                result[bstack1lllll1_opy_ (u"ࠥࡴࡷ࡚ࡩࡵ࡮ࡨࠦᰑ")] = bstack111l111llll_opy_[0] if bstack111l111llll_opy_ else bstack1lllll1_opy_ (u"ࠦࠧᰒ")
                if len(bstack111l111llll_opy_) > 2:
                    result[bstack1lllll1_opy_ (u"ࠧࡶࡲࡅࡧࡶࡧࡷ࡯ࡰࡵ࡫ࡲࡲࠧᰓ")] = bstack1lllll1_opy_ (u"࠭࡜࡯ࠩᰔ").join(bstack111l111llll_opy_[2:]).strip()
            results.append(result)
        except Exception as err:
            logger.error(bstack1lllll1_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡰࡰࡲࡸࡰࡦࡺࡩ࡯ࡩࠣࡋ࡮ࡺࠠ࡮ࡧࡷࡥࡩࡧࡴࡢࠢࡩࡳࡷࠦࡁࡊࠢࡶࡩࡱ࡫ࡣࡵ࡫ࡲࡲࠥ࠮ࡦࡰ࡮ࡧࡩࡷࡀࠠࡼࡨࡲࡰࡩ࡫ࡲࡾࠫ࠽ࠤࠧᰕ") + str(err) + bstack1lllll1_opy_ (u"ࠣࠤᰖ"))
    filtered_results = [
        result
        for result in results
        if _111l1l1llll_opy_(result)
    ]
    return filtered_results
def _111l1l1llll_opy_(result):
    bstack1lllll1_opy_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࡋࡩࡱࡶࡥࡳࠢࡷࡳࠥࡩࡨࡦࡥ࡮ࠤ࡮࡬ࠠࡢࠢࡪ࡭ࡹࠦ࡭ࡦࡶࡤࡨࡦࡺࡡࠡࡴࡨࡷࡺࡲࡴࠡ࡫ࡶࠤࡻࡧ࡬ࡪࡦࠣࠬࡳࡵ࡮࠮ࡧࡰࡴࡹࡿࠠࡧ࡫࡯ࡩࡸࡉࡨࡢࡰࡪࡩࡩࠦࡡ࡯ࡦࠣࡥࡺࡺࡨࡰࡴࡶ࠭࠳ࠐࠠࠡࠢࠣࠦࠧࠨᰗ")
    return (
        isinstance(result.get(bstack1lllll1_opy_ (u"ࠥࡪ࡮ࡲࡥࡴࡅ࡫ࡥࡳ࡭ࡥࡥࠤᰘ"), None), list)
        and len(result[bstack1lllll1_opy_ (u"ࠦ࡫࡯࡬ࡦࡵࡆ࡬ࡦࡴࡧࡦࡦࠥᰙ")]) > 0
        and isinstance(result.get(bstack1lllll1_opy_ (u"ࠧࡧࡵࡵࡪࡲࡶࡸࠨᰚ"), None), list)
        and len(result[bstack1lllll1_opy_ (u"ࠨࡡࡶࡶ࡫ࡳࡷࡹࠢᰛ")]) > 0
    )
def _1111l1ll1ll_opy_(repo):
    bstack1lllll1_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࡕࡴࡼࠤࡹࡵࠠࡥࡧࡷࡩࡷࡳࡩ࡯ࡧࠣࡸ࡭࡫ࠠࡣࡣࡶࡩࠥࡨࡲࡢࡰࡦ࡬ࠥ࡬࡯ࡳࠢࡷ࡬ࡪࠦࡧࡪࡸࡨࡲࠥࡸࡥࡱࡱࠣࡻ࡮ࡺࡨࡰࡷࡷࠤ࡭ࡧࡲࡥࡥࡲࡨࡪࡪࠠ࡯ࡣࡰࡩࡸࠦࡡ࡯ࡦࠣࡻࡴࡸ࡫ࠡࡹ࡬ࡸ࡭ࠦࡡ࡭࡮࡚ࠣࡈ࡙ࠠࡱࡴࡲࡺ࡮ࡪࡥࡳࡵ࠱ࠎࠥࠦࠠࠡࡔࡨࡸࡺࡸ࡮ࡴࠢࡷ࡬ࡪࠦࡤࡦࡨࡤࡹࡱࡺࠠࡣࡴࡤࡲࡨ࡮ࠠࡪࡨࠣࡴࡴࡹࡳࡪࡤ࡯ࡩ࠱ࠦࡥ࡭ࡵࡨࠤࡓࡵ࡮ࡦ࠰ࠍࠤࠥࠦࠠࠣࠤࠥᰜ")
    try:
        try:
            origin = repo.remotes.origin
            bstack111l1ll1111_opy_ = origin.refs[bstack1lllll1_opy_ (u"ࠨࡊࡈࡅࡉ࠭ᰝ")]
            target = bstack111l1ll1111_opy_.reference.name
            if target.startswith(bstack1lllll1_opy_ (u"ࠩࡲࡶ࡮࡭ࡩ࡯࠱ࠪᰞ")):
                return target
        except Exception:
            pass
        if repo.remotes and repo.remotes.origin.refs:
            for ref in repo.remotes.origin.refs:
                if ref.name.startswith(bstack1lllll1_opy_ (u"ࠪࡳࡷ࡯ࡧࡪࡰ࠲ࠫᰟ")):
                    return ref.name
        if repo.heads:
            return repo.heads[0].name
    except Exception:
        pass
    return None
def _1111lll1111_opy_(commits):
    bstack1lllll1_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࡌ࡫ࡴࠡ࡮࡬ࡷࡹࠦ࡯ࡧࠢࡦ࡬ࡦࡴࡧࡦࡦࠣࡪ࡮ࡲࡥࡴࠢࡩࡶࡴࡳࠠࡢࠢ࡯࡭ࡸࡺࠠࡰࡨࠣࡧࡴࡳ࡭ࡪࡶࡶ࠲ࠏࠦࠠࠡࠢࠥࠦࠧᰠ")
    bstack1111llll1l1_opy_ = set()
    try:
        for commit in commits:
            if commit.parents:
                for parent in commit.parents:
                    diff = commit.diff(parent)
                    for bstack111l1lllll1_opy_ in diff:
                        if bstack111l1lllll1_opy_.a_path:
                            bstack1111llll1l1_opy_.add(bstack111l1lllll1_opy_.a_path)
                        if bstack111l1lllll1_opy_.b_path:
                            bstack1111llll1l1_opy_.add(bstack111l1lllll1_opy_.b_path)
    except Exception:
        pass
    return list(bstack1111llll1l1_opy_)
def bstack1111ll1l11l_opy_(bstack111l1llll11_opy_):
    bstack111l1l1l1l1_opy_ = bstack1111ll1111l_opy_(bstack111l1llll11_opy_)
    if bstack111l1l1l1l1_opy_ and bstack111l1l1l1l1_opy_ > bstack11l1l1l1lll_opy_:
        bstack111l1ll11ll_opy_ = bstack111l1l1l1l1_opy_ - bstack11l1l1l1lll_opy_
        bstack111l1l1l11l_opy_ = bstack1111ll111ll_opy_(bstack111l1llll11_opy_[bstack1lllll1_opy_ (u"ࠧࡩ࡯࡮࡯࡬ࡸࡤࡳࡥࡴࡵࡤ࡫ࡪࠨᰡ")], bstack111l1ll11ll_opy_)
        bstack111l1llll11_opy_[bstack1lllll1_opy_ (u"ࠨࡣࡰ࡯ࡰ࡭ࡹࡥ࡭ࡦࡵࡶࡥ࡬࡫ࠢᰢ")] = bstack111l1l1l11l_opy_
        logger.info(bstack1lllll1_opy_ (u"ࠢࡕࡪࡨࠤࡨࡵ࡭࡮࡫ࡷࠤ࡭ࡧࡳࠡࡤࡨࡩࡳࠦࡴࡳࡷࡱࡧࡦࡺࡥࡥ࠰ࠣࡗ࡮ࢀࡥࠡࡱࡩࠤࡨࡵ࡭࡮࡫ࡷࠤࡦ࡬ࡴࡦࡴࠣࡸࡷࡻ࡮ࡤࡣࡷ࡭ࡴࡴࠠࡪࡵࠣࡿࢂࠦࡋࡃࠤᰣ")
                    .format(bstack1111ll1111l_opy_(bstack111l1llll11_opy_) / 1024))
    return bstack111l1llll11_opy_
def bstack1111ll1111l_opy_(json_data):
    try:
        if json_data:
            bstack1111ll11ll1_opy_ = json.dumps(json_data)
            bstack111l1l1111l_opy_ = sys.getsizeof(bstack1111ll11ll1_opy_)
            return bstack111l1l1111l_opy_
    except Exception as e:
        logger.debug(bstack1lllll1_opy_ (u"ࠣࡕࡲࡱࡪࡺࡨࡪࡰࡪࠤࡼ࡫࡮ࡵࠢࡺࡶࡴࡴࡧࠡࡹ࡫࡭ࡱ࡫ࠠࡤࡣ࡯ࡧࡺࡲࡡࡵ࡫ࡱ࡫ࠥࡹࡩࡻࡧࠣࡳ࡫ࠦࡊࡔࡑࡑࠤࡴࡨࡪࡦࡥࡷ࠾ࠥࢁࡽࠣᰤ").format(e))
    return -1
def bstack1111ll111ll_opy_(field, bstack1111lll11ll_opy_):
    try:
        bstack111l11l1ll1_opy_ = len(bytes(bstack11l1l111l1l_opy_, bstack1lllll1_opy_ (u"ࠩࡸࡸ࡫࠳࠸ࠨᰥ")))
        bstack111l1111111_opy_ = bytes(field, bstack1lllll1_opy_ (u"ࠪࡹࡹ࡬࠭࠹ࠩᰦ"))
        bstack111l1l1ll1l_opy_ = len(bstack111l1111111_opy_)
        bstack111ll11111l_opy_ = ceil(bstack111l1l1ll1l_opy_ - bstack1111lll11ll_opy_ - bstack111l11l1ll1_opy_)
        if bstack111ll11111l_opy_ > 0:
            bstack1111lll1l1l_opy_ = bstack111l1111111_opy_[:bstack111ll11111l_opy_].decode(bstack1lllll1_opy_ (u"ࠫࡺࡺࡦ࠮࠺ࠪᰧ"), errors=bstack1lllll1_opy_ (u"ࠬ࡯ࡧ࡯ࡱࡵࡩࠬᰨ")) + bstack11l1l111l1l_opy_
            return bstack1111lll1l1l_opy_
    except Exception as e:
        logger.debug(bstack1lllll1_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡽࡨࡪ࡮ࡨࠤࡹࡸࡵ࡯ࡥࡤࡸ࡮ࡴࡧࠡࡨ࡬ࡩࡱࡪࠬࠡࡰࡲࡸ࡭࡯࡮ࡨࠢࡺࡥࡸࠦࡴࡳࡷࡱࡧࡦࡺࡥࡥࠢ࡫ࡩࡷ࡫࠺ࠡࡽࢀࠦᰩ").format(e))
    return field
def bstack1ll111111l_opy_():
    env = os.environ
    if (bstack1lllll1_opy_ (u"ࠢࡋࡇࡑࡏࡎࡔࡓࡠࡗࡕࡐࠧᰪ") in env and len(env[bstack1lllll1_opy_ (u"ࠣࡌࡈࡒࡐࡏࡎࡔࡡࡘࡖࡑࠨᰫ")]) > 0) or (
            bstack1lllll1_opy_ (u"ࠤࡍࡉࡓࡑࡉࡏࡕࡢࡌࡔࡓࡅࠣᰬ") in env and len(env[bstack1lllll1_opy_ (u"ࠥࡎࡊࡔࡋࡊࡐࡖࡣࡍࡕࡍࡆࠤᰭ")]) > 0):
        return {
            bstack1lllll1_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᰮ"): bstack1lllll1_opy_ (u"ࠧࡐࡥ࡯࡭࡬ࡲࡸࠨᰯ"),
            bstack1lllll1_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᰰ"): env.get(bstack1lllll1_opy_ (u"ࠢࡃࡗࡌࡐࡉࡥࡕࡓࡎࠥᰱ")),
            bstack1lllll1_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᰲ"): env.get(bstack1lllll1_opy_ (u"ࠤࡍࡓࡇࡥࡎࡂࡏࡈࠦᰳ")),
            bstack1lllll1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤᰴ"): env.get(bstack1lllll1_opy_ (u"ࠦࡇ࡛ࡉࡍࡆࡢࡒ࡚ࡓࡂࡆࡔࠥᰵ"))
        }
    if env.get(bstack1lllll1_opy_ (u"ࠧࡉࡉࠣᰶ")) == bstack1lllll1_opy_ (u"ࠨࡴࡳࡷࡨ᰷ࠦ") and bstack11l11l111l_opy_(env.get(bstack1lllll1_opy_ (u"ࠢࡄࡋࡕࡇࡑࡋࡃࡊࠤ᰸"))):
        return {
            bstack1lllll1_opy_ (u"ࠣࡰࡤࡱࡪࠨ᰹"): bstack1lllll1_opy_ (u"ࠤࡆ࡭ࡷࡩ࡬ࡦࡅࡌࠦ᰺"),
            bstack1lllll1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨ᰻"): env.get(bstack1lllll1_opy_ (u"ࠦࡈࡏࡒࡄࡎࡈࡣࡇ࡛ࡉࡍࡆࡢ࡙ࡗࡒࠢ᰼")),
            bstack1lllll1_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢ᰽"): env.get(bstack1lllll1_opy_ (u"ࠨࡃࡊࡔࡆࡐࡊࡥࡊࡐࡄࠥ᰾")),
            bstack1lllll1_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨ᰿"): env.get(bstack1lllll1_opy_ (u"ࠣࡅࡌࡖࡈࡒࡅࡠࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࠦ᱀"))
        }
    if env.get(bstack1lllll1_opy_ (u"ࠤࡆࡍࠧ᱁")) == bstack1lllll1_opy_ (u"ࠥࡸࡷࡻࡥࠣ᱂") and bstack11l11l111l_opy_(env.get(bstack1lllll1_opy_ (u"࡙ࠦࡘࡁࡗࡋࡖࠦ᱃"))):
        return {
            bstack1lllll1_opy_ (u"ࠧࡴࡡ࡮ࡧࠥ᱄"): bstack1lllll1_opy_ (u"ࠨࡔࡳࡣࡹ࡭ࡸࠦࡃࡊࠤ᱅"),
            bstack1lllll1_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥ᱆"): env.get(bstack1lllll1_opy_ (u"ࠣࡖࡕࡅ࡛ࡏࡓࡠࡄࡘࡍࡑࡊ࡟ࡘࡇࡅࡣ࡚ࡘࡌࠣ᱇")),
            bstack1lllll1_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦ᱈"): env.get(bstack1lllll1_opy_ (u"ࠥࡘࡗࡇࡖࡊࡕࡢࡎࡔࡈ࡟ࡏࡃࡐࡉࠧ᱉")),
            bstack1lllll1_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥ᱊"): env.get(bstack1lllll1_opy_ (u"࡚ࠧࡒࡂࡘࡌࡗࡤࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࡃࡇࡕࠦ᱋"))
        }
    if env.get(bstack1lllll1_opy_ (u"ࠨࡃࡊࠤ᱌")) == bstack1lllll1_opy_ (u"ࠢࡵࡴࡸࡩࠧᱍ") and env.get(bstack1lllll1_opy_ (u"ࠣࡅࡌࡣࡓࡇࡍࡆࠤᱎ")) == bstack1lllll1_opy_ (u"ࠤࡦࡳࡩ࡫ࡳࡩ࡫ࡳࠦᱏ"):
        return {
            bstack1lllll1_opy_ (u"ࠥࡲࡦࡳࡥࠣ᱐"): bstack1lllll1_opy_ (u"ࠦࡈࡵࡤࡦࡵ࡫࡭ࡵࠨ᱑"),
            bstack1lllll1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣ᱒"): None,
            bstack1lllll1_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣ᱓"): None,
            bstack1lllll1_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨ᱔"): None
        }
    if env.get(bstack1lllll1_opy_ (u"ࠣࡄࡌࡘࡇ࡛ࡃࡌࡇࡗࡣࡇࡘࡁࡏࡅࡋࠦ᱕")) and env.get(bstack1lllll1_opy_ (u"ࠤࡅࡍ࡙ࡈࡕࡄࡍࡈࡘࡤࡉࡏࡎࡏࡌࡘࠧ᱖")):
        return {
            bstack1lllll1_opy_ (u"ࠥࡲࡦࡳࡥࠣ᱗"): bstack1lllll1_opy_ (u"ࠦࡇ࡯ࡴࡣࡷࡦ࡯ࡪࡺࠢ᱘"),
            bstack1lllll1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣ᱙"): env.get(bstack1lllll1_opy_ (u"ࠨࡂࡊࡖࡅ࡙ࡈࡑࡅࡕࡡࡊࡍ࡙ࡥࡈࡕࡖࡓࡣࡔࡘࡉࡈࡋࡑࠦᱚ")),
            bstack1lllll1_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᱛ"): None,
            bstack1lllll1_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᱜ"): env.get(bstack1lllll1_opy_ (u"ࠤࡅࡍ࡙ࡈࡕࡄࡍࡈࡘࡤࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࡃࡇࡕࠦᱝ"))
        }
    if env.get(bstack1lllll1_opy_ (u"ࠥࡇࡎࠨᱞ")) == bstack1lllll1_opy_ (u"ࠦࡹࡸࡵࡦࠤᱟ") and bstack11l11l111l_opy_(env.get(bstack1lllll1_opy_ (u"ࠧࡊࡒࡐࡐࡈࠦᱠ"))):
        return {
            bstack1lllll1_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᱡ"): bstack1lllll1_opy_ (u"ࠢࡅࡴࡲࡲࡪࠨᱢ"),
            bstack1lllll1_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᱣ"): env.get(bstack1lllll1_opy_ (u"ࠤࡇࡖࡔࡔࡅࡠࡄࡘࡍࡑࡊ࡟ࡍࡋࡑࡏࠧᱤ")),
            bstack1lllll1_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᱥ"): None,
            bstack1lllll1_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᱦ"): env.get(bstack1lllll1_opy_ (u"ࠧࡊࡒࡐࡐࡈࡣࡇ࡛ࡉࡍࡆࡢࡒ࡚ࡓࡂࡆࡔࠥᱧ"))
        }
    if env.get(bstack1lllll1_opy_ (u"ࠨࡃࡊࠤᱨ")) == bstack1lllll1_opy_ (u"ࠢࡵࡴࡸࡩࠧᱩ") and bstack11l11l111l_opy_(env.get(bstack1lllll1_opy_ (u"ࠣࡕࡈࡑࡆࡖࡈࡐࡔࡈࠦᱪ"))):
        return {
            bstack1lllll1_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᱫ"): bstack1lllll1_opy_ (u"ࠥࡗࡪࡳࡡࡱࡪࡲࡶࡪࠨᱬ"),
            bstack1lllll1_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᱭ"): env.get(bstack1lllll1_opy_ (u"࡙ࠧࡅࡎࡃࡓࡌࡔࡘࡅࡠࡑࡕࡋࡆࡔࡉ࡛ࡃࡗࡍࡔࡔ࡟ࡖࡔࡏࠦᱮ")),
            bstack1lllll1_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᱯ"): env.get(bstack1lllll1_opy_ (u"ࠢࡔࡇࡐࡅࡕࡎࡏࡓࡇࡢࡎࡔࡈ࡟ࡏࡃࡐࡉࠧᱰ")),
            bstack1lllll1_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᱱ"): env.get(bstack1lllll1_opy_ (u"ࠤࡖࡉࡒࡇࡐࡉࡑࡕࡉࡤࡐࡏࡃࡡࡌࡈࠧᱲ"))
        }
    if env.get(bstack1lllll1_opy_ (u"ࠥࡇࡎࠨᱳ")) == bstack1lllll1_opy_ (u"ࠦࡹࡸࡵࡦࠤᱴ") and bstack11l11l111l_opy_(env.get(bstack1lllll1_opy_ (u"ࠧࡍࡉࡕࡎࡄࡆࡤࡉࡉࠣᱵ"))):
        return {
            bstack1lllll1_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᱶ"): bstack1lllll1_opy_ (u"ࠢࡈ࡫ࡷࡐࡦࡨࠢᱷ"),
            bstack1lllll1_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᱸ"): env.get(bstack1lllll1_opy_ (u"ࠤࡆࡍࡤࡐࡏࡃࡡࡘࡖࡑࠨᱹ")),
            bstack1lllll1_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᱺ"): env.get(bstack1lllll1_opy_ (u"ࠦࡈࡏ࡟ࡋࡑࡅࡣࡓࡇࡍࡆࠤᱻ")),
            bstack1lllll1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᱼ"): env.get(bstack1lllll1_opy_ (u"ࠨࡃࡊࡡࡍࡓࡇࡥࡉࡅࠤᱽ"))
        }
    if env.get(bstack1lllll1_opy_ (u"ࠢࡄࡋࠥ᱾")) == bstack1lllll1_opy_ (u"ࠣࡶࡵࡹࡪࠨ᱿") and bstack11l11l111l_opy_(env.get(bstack1lllll1_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡌࡋࡗࡉࠧᲀ"))):
        return {
            bstack1lllll1_opy_ (u"ࠥࡲࡦࡳࡥࠣᲁ"): bstack1lllll1_opy_ (u"ࠦࡇࡻࡩ࡭ࡦ࡮࡭ࡹ࡫ࠢᲂ"),
            bstack1lllll1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣᲃ"): env.get(bstack1lllll1_opy_ (u"ࠨࡂࡖࡋࡏࡈࡐࡏࡔࡆࡡࡅ࡙ࡎࡒࡄࡠࡗࡕࡐࠧᲄ")),
            bstack1lllll1_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᲅ"): env.get(bstack1lllll1_opy_ (u"ࠣࡄࡘࡍࡑࡊࡋࡊࡖࡈࡣࡑࡇࡂࡆࡎࠥᲆ")) or env.get(bstack1lllll1_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡌࡋࡗࡉࡤࡖࡉࡑࡇࡏࡍࡓࡋ࡟ࡏࡃࡐࡉࠧᲇ")),
            bstack1lllll1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤᲈ"): env.get(bstack1lllll1_opy_ (u"ࠦࡇ࡛ࡉࡍࡆࡎࡍ࡙ࡋ࡟ࡃࡗࡌࡐࡉࡥࡎࡖࡏࡅࡉࡗࠨᲉ"))
        }
    if bstack11l11l111l_opy_(env.get(bstack1lllll1_opy_ (u"࡚ࠧࡆࡠࡄࡘࡍࡑࡊࠢᲊ"))):
        return {
            bstack1lllll1_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦ᲋"): bstack1lllll1_opy_ (u"ࠢࡗ࡫ࡶࡹࡦࡲࠠࡔࡶࡸࡨ࡮ࡵࠠࡕࡧࡤࡱ࡙ࠥࡥࡳࡸ࡬ࡧࡪࡹࠢ᲌"),
            bstack1lllll1_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦ᲍"): bstack1lllll1_opy_ (u"ࠤࡾࢁࢀࢃࠢ᲎").format(env.get(bstack1lllll1_opy_ (u"ࠪࡗ࡞࡙ࡔࡆࡏࡢࡘࡊࡇࡍࡇࡑࡘࡒࡉࡇࡔࡊࡑࡑࡗࡊࡘࡖࡆࡔࡘࡖࡎ࠭᲏")), env.get(bstack1lllll1_opy_ (u"ࠫࡘ࡟ࡓࡕࡇࡐࡣ࡙ࡋࡁࡎࡒࡕࡓࡏࡋࡃࡕࡋࡇࠫᲐ"))),
            bstack1lllll1_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᲑ"): env.get(bstack1lllll1_opy_ (u"ࠨࡓ࡚ࡕࡗࡉࡒࡥࡄࡆࡈࡌࡒࡎ࡚ࡉࡐࡐࡌࡈࠧᲒ")),
            bstack1lllll1_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᲓ"): env.get(bstack1lllll1_opy_ (u"ࠣࡄࡘࡍࡑࡊ࡟ࡃࡗࡌࡐࡉࡏࡄࠣᲔ"))
        }
    if bstack11l11l111l_opy_(env.get(bstack1lllll1_opy_ (u"ࠤࡄࡔࡕ࡜ࡅ࡚ࡑࡕࠦᲕ"))):
        return {
            bstack1lllll1_opy_ (u"ࠥࡲࡦࡳࡥࠣᲖ"): bstack1lllll1_opy_ (u"ࠦࡆࡶࡰࡷࡧࡼࡳࡷࠨᲗ"),
            bstack1lllll1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣᲘ"): bstack1lllll1_opy_ (u"ࠨࡻࡾ࠱ࡳࡶࡴࡰࡥࡤࡶ࠲ࡿࢂ࠵ࡻࡾ࠱ࡥࡹ࡮ࡲࡤࡴ࠱ࡾࢁࠧᲙ").format(env.get(bstack1lllll1_opy_ (u"ࠧࡂࡒࡓ࡚ࡊ࡟ࡏࡓࡡࡘࡖࡑ࠭Ლ")), env.get(bstack1lllll1_opy_ (u"ࠨࡃࡓࡔ࡛ࡋ࡙ࡐࡔࡢࡅࡈࡉࡏࡖࡐࡗࡣࡓࡇࡍࡆࠩᲛ")), env.get(bstack1lllll1_opy_ (u"ࠩࡄࡔࡕ࡜ࡅ࡚ࡑࡕࡣࡕࡘࡏࡋࡇࡆࡘࡤ࡙ࡌࡖࡉࠪᲜ")), env.get(bstack1lllll1_opy_ (u"ࠪࡅࡕࡖࡖࡆ࡛ࡒࡖࡤࡈࡕࡊࡎࡇࡣࡎࡊࠧᲝ"))),
            bstack1lllll1_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᲞ"): env.get(bstack1lllll1_opy_ (u"ࠧࡇࡐࡑࡘࡈ࡝ࡔࡘ࡟ࡋࡑࡅࡣࡓࡇࡍࡆࠤᲟ")),
            bstack1lllll1_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᲠ"): env.get(bstack1lllll1_opy_ (u"ࠢࡂࡒࡓ࡚ࡊ࡟ࡏࡓࡡࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࡇࡋࡒࠣᲡ"))
        }
    if env.get(bstack1lllll1_opy_ (u"ࠣࡃ࡝࡙ࡗࡋ࡟ࡉࡖࡗࡔࡤ࡛ࡓࡆࡔࡢࡅࡌࡋࡎࡕࠤᲢ")) and env.get(bstack1lllll1_opy_ (u"ࠤࡗࡊࡤࡈࡕࡊࡎࡇࠦᲣ")):
        return {
            bstack1lllll1_opy_ (u"ࠥࡲࡦࡳࡥࠣᲤ"): bstack1lllll1_opy_ (u"ࠦࡆࢀࡵࡳࡧࠣࡇࡎࠨᲥ"),
            bstack1lllll1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣᲦ"): bstack1lllll1_opy_ (u"ࠨࡻࡾࡽࢀ࠳ࡤࡨࡵࡪ࡮ࡧ࠳ࡷ࡫ࡳࡶ࡮ࡷࡷࡄࡨࡵࡪ࡮ࡧࡍࡩࡃࡻࡾࠤᲧ").format(env.get(bstack1lllll1_opy_ (u"ࠧࡔ࡛ࡖࡘࡊࡓ࡟ࡕࡇࡄࡑࡋࡕࡕࡏࡆࡄࡘࡎࡕࡎࡔࡇࡕ࡚ࡊࡘࡕࡓࡋࠪᲨ")), env.get(bstack1lllll1_opy_ (u"ࠨࡕ࡜ࡗ࡙ࡋࡍࡠࡖࡈࡅࡒࡖࡒࡐࡌࡈࡇ࡙࠭Ჩ")), env.get(bstack1lllll1_opy_ (u"ࠩࡅ࡙ࡎࡒࡄࡠࡄࡘࡍࡑࡊࡉࡅࠩᲪ"))),
            bstack1lllll1_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᲫ"): env.get(bstack1lllll1_opy_ (u"ࠦࡇ࡛ࡉࡍࡆࡢࡆ࡚ࡏࡌࡅࡋࡇࠦᲬ")),
            bstack1lllll1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᲭ"): env.get(bstack1lllll1_opy_ (u"ࠨࡂࡖࡋࡏࡈࡤࡈࡕࡊࡎࡇࡍࡉࠨᲮ"))
        }
    if any([env.get(bstack1lllll1_opy_ (u"ࠢࡄࡑࡇࡉࡇ࡛ࡉࡍࡆࡢࡆ࡚ࡏࡌࡅࡡࡌࡈࠧᲯ")), env.get(bstack1lllll1_opy_ (u"ࠣࡅࡒࡈࡊࡈࡕࡊࡎࡇࡣࡗࡋࡓࡐࡎ࡙ࡉࡉࡥࡓࡐࡗࡕࡇࡊࡥࡖࡆࡔࡖࡍࡔࡔࠢᲰ")), env.get(bstack1lllll1_opy_ (u"ࠤࡆࡓࡉࡋࡂࡖࡋࡏࡈࡤ࡙ࡏࡖࡔࡆࡉࡤ࡜ࡅࡓࡕࡌࡓࡓࠨᲱ"))]):
        return {
            bstack1lllll1_opy_ (u"ࠥࡲࡦࡳࡥࠣᲲ"): bstack1lllll1_opy_ (u"ࠦࡆ࡝ࡓࠡࡅࡲࡨࡪࡈࡵࡪ࡮ࡧࠦᲳ"),
            bstack1lllll1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣᲴ"): env.get(bstack1lllll1_opy_ (u"ࠨࡃࡐࡆࡈࡆ࡚ࡏࡌࡅࡡࡓ࡙ࡇࡒࡉࡄࡡࡅ࡙ࡎࡒࡄࡠࡗࡕࡐࠧᲵ")),
            bstack1lllll1_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᲶ"): env.get(bstack1lllll1_opy_ (u"ࠣࡅࡒࡈࡊࡈࡕࡊࡎࡇࡣࡇ࡛ࡉࡍࡆࡢࡍࡉࠨᲷ")),
            bstack1lllll1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᲸ"): env.get(bstack1lllll1_opy_ (u"ࠥࡇࡔࡊࡅࡃࡗࡌࡐࡉࡥࡂࡖࡋࡏࡈࡤࡏࡄࠣᲹ"))
        }
    if env.get(bstack1lllll1_opy_ (u"ࠦࡧࡧ࡭ࡣࡱࡲࡣࡧࡻࡩ࡭ࡦࡑࡹࡲࡨࡥࡳࠤᲺ")):
        return {
            bstack1lllll1_opy_ (u"ࠧࡴࡡ࡮ࡧࠥ᲻"): bstack1lllll1_opy_ (u"ࠨࡂࡢ࡯ࡥࡳࡴࠨ᲼"),
            bstack1lllll1_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᲽ"): env.get(bstack1lllll1_opy_ (u"ࠣࡤࡤࡱࡧࡵ࡯ࡠࡤࡸ࡭ࡱࡪࡒࡦࡵࡸࡰࡹࡹࡕࡳ࡮ࠥᲾ")),
            bstack1lllll1_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᲿ"): env.get(bstack1lllll1_opy_ (u"ࠥࡦࡦࡳࡢࡰࡱࡢࡷ࡭ࡵࡲࡵࡌࡲࡦࡓࡧ࡭ࡦࠤ᳀")),
            bstack1lllll1_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥ᳁"): env.get(bstack1lllll1_opy_ (u"ࠧࡨࡡ࡮ࡤࡲࡳࡤࡨࡵࡪ࡮ࡧࡒࡺࡳࡢࡦࡴࠥ᳂"))
        }
    if env.get(bstack1lllll1_opy_ (u"ࠨࡗࡆࡔࡆࡏࡊࡘࠢ᳃")) or env.get(bstack1lllll1_opy_ (u"ࠢࡘࡇࡕࡇࡐࡋࡒࡠࡏࡄࡍࡓࡥࡐࡊࡒࡈࡐࡎࡔࡅࡠࡕࡗࡅࡗ࡚ࡅࡅࠤ᳄")):
        return {
            bstack1lllll1_opy_ (u"ࠣࡰࡤࡱࡪࠨ᳅"): bstack1lllll1_opy_ (u"ࠤ࡚ࡩࡷࡩ࡫ࡦࡴࠥ᳆"),
            bstack1lllll1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨ᳇"): env.get(bstack1lllll1_opy_ (u"ࠦ࡜ࡋࡒࡄࡍࡈࡖࡤࡈࡕࡊࡎࡇࡣ࡚ࡘࡌࠣ᳈")),
            bstack1lllll1_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢ᳉"): bstack1lllll1_opy_ (u"ࠨࡍࡢ࡫ࡱࠤࡕ࡯ࡰࡦ࡮࡬ࡲࡪࠨ᳊") if env.get(bstack1lllll1_opy_ (u"ࠢࡘࡇࡕࡇࡐࡋࡒࡠࡏࡄࡍࡓࡥࡐࡊࡒࡈࡐࡎࡔࡅࡠࡕࡗࡅࡗ࡚ࡅࡅࠤ᳋")) else None,
            bstack1lllll1_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢ᳌"): env.get(bstack1lllll1_opy_ (u"ࠤ࡚ࡉࡗࡉࡋࡆࡔࡢࡋࡎ࡚࡟ࡄࡑࡐࡑࡎ࡚ࠢ᳍"))
        }
    if any([env.get(bstack1lllll1_opy_ (u"ࠥࡋࡈࡖ࡟ࡑࡔࡒࡎࡊࡉࡔࠣ᳎")), env.get(bstack1lllll1_opy_ (u"ࠦࡌࡉࡌࡐࡗࡇࡣࡕࡘࡏࡋࡇࡆࡘࠧ᳏")), env.get(bstack1lllll1_opy_ (u"ࠧࡍࡏࡐࡉࡏࡉࡤࡉࡌࡐࡗࡇࡣࡕࡘࡏࡋࡇࡆࡘࠧ᳐"))]):
        return {
            bstack1lllll1_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦ᳑"): bstack1lllll1_opy_ (u"ࠢࡈࡱࡲ࡫ࡱ࡫ࠠࡄ࡮ࡲࡹࡩࠨ᳒"),
            bstack1lllll1_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦ᳓"): None,
            bstack1lllll1_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨ᳔ࠦ"): env.get(bstack1lllll1_opy_ (u"ࠥࡔࡗࡕࡊࡆࡅࡗࡣࡎࡊ᳕ࠢ")),
            bstack1lllll1_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴ᳖ࠥ"): env.get(bstack1lllll1_opy_ (u"ࠧࡈࡕࡊࡎࡇࡣࡎࡊ᳗ࠢ"))
        }
    if env.get(bstack1lllll1_opy_ (u"ࠨࡓࡉࡋࡓࡔࡆࡈࡌࡆࠤ᳘")):
        return {
            bstack1lllll1_opy_ (u"ࠢ࡯ࡣࡰࡩ᳙ࠧ"): bstack1lllll1_opy_ (u"ࠣࡕ࡫࡭ࡵࡶࡡࡣ࡮ࡨࠦ᳚"),
            bstack1lllll1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧ᳛"): env.get(bstack1lllll1_opy_ (u"ࠥࡗࡍࡏࡐࡑࡃࡅࡐࡊࡥࡂࡖࡋࡏࡈࡤ࡛ࡒࡍࠤ᳜")),
            bstack1lllll1_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨ᳝"): bstack1lllll1_opy_ (u"ࠧࡐ࡯ࡣࠢࠦࡿࢂࠨ᳞").format(env.get(bstack1lllll1_opy_ (u"࠭ࡓࡉࡋࡓࡔࡆࡈࡌࡆࡡࡍࡓࡇࡥࡉࡅ᳟ࠩ"))) if env.get(bstack1lllll1_opy_ (u"ࠢࡔࡊࡌࡔࡕࡇࡂࡍࡇࡢࡎࡔࡈ࡟ࡊࡆࠥ᳠")) else None,
            bstack1lllll1_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢ᳡"): env.get(bstack1lllll1_opy_ (u"ࠤࡖࡌࡎࡖࡐࡂࡄࡏࡉࡤࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࡃࡇࡕ᳢ࠦ"))
        }
    if bstack11l11l111l_opy_(env.get(bstack1lllll1_opy_ (u"ࠥࡒࡊ࡚ࡌࡊࡈ࡜᳣ࠦ"))):
        return {
            bstack1lllll1_opy_ (u"ࠦࡳࡧ࡭ࡦࠤ᳤"): bstack1lllll1_opy_ (u"ࠧࡔࡥࡵ࡮࡬ࡪࡾࠨ᳥"),
            bstack1lllll1_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤ᳦"): env.get(bstack1lllll1_opy_ (u"ࠢࡅࡇࡓࡐࡔ࡟࡟ࡖࡔࡏ᳧ࠦ")),
            bstack1lllll1_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧ᳨ࠥ"): env.get(bstack1lllll1_opy_ (u"ࠤࡖࡍ࡙ࡋ࡟ࡏࡃࡐࡉࠧᳩ")),
            bstack1lllll1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤᳪ"): env.get(bstack1lllll1_opy_ (u"ࠦࡇ࡛ࡉࡍࡆࡢࡍࡉࠨᳫ"))
        }
    if bstack11l11l111l_opy_(env.get(bstack1lllll1_opy_ (u"ࠧࡍࡉࡕࡊࡘࡆࡤࡇࡃࡕࡋࡒࡒࡘࠨᳬ"))):
        return {
            bstack1lllll1_opy_ (u"ࠨ࡮ࡢ࡯ࡨ᳭ࠦ"): bstack1lllll1_opy_ (u"ࠢࡈ࡫ࡷࡌࡺࡨࠠࡂࡥࡷ࡭ࡴࡴࡳࠣᳮ"),
            bstack1lllll1_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᳯ"): bstack1lllll1_opy_ (u"ࠤࡾࢁ࠴ࢁࡽ࠰ࡣࡦࡸ࡮ࡵ࡮ࡴ࠱ࡵࡹࡳࡹ࠯ࡼࡿࠥᳰ").format(env.get(bstack1lllll1_opy_ (u"ࠪࡋࡎ࡚ࡈࡖࡄࡢࡗࡊࡘࡖࡆࡔࡢ࡙ࡗࡒࠧᳱ")), env.get(bstack1lllll1_opy_ (u"ࠫࡌࡏࡔࡉࡗࡅࡣࡗࡋࡐࡐࡕࡌࡘࡔࡘ࡙ࠨᳲ")), env.get(bstack1lllll1_opy_ (u"ࠬࡍࡉࡕࡊࡘࡆࡤࡘࡕࡏࡡࡌࡈࠬᳳ"))),
            bstack1lllll1_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣ᳴"): env.get(bstack1lllll1_opy_ (u"ࠢࡈࡋࡗࡌ࡚ࡈ࡟ࡘࡑࡕࡏࡋࡒࡏࡘࠤᳵ")),
            bstack1lllll1_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᳶ"): env.get(bstack1lllll1_opy_ (u"ࠤࡊࡍ࡙ࡎࡕࡃࡡࡕ࡙ࡓࡥࡉࡅࠤ᳷"))
        }
    if env.get(bstack1lllll1_opy_ (u"ࠥࡇࡎࠨ᳸")) == bstack1lllll1_opy_ (u"ࠦࡹࡸࡵࡦࠤ᳹") and env.get(bstack1lllll1_opy_ (u"ࠧ࡜ࡅࡓࡅࡈࡐࠧᳺ")) == bstack1lllll1_opy_ (u"ࠨ࠱ࠣ᳻"):
        return {
            bstack1lllll1_opy_ (u"ࠢ࡯ࡣࡰࡩࠧ᳼"): bstack1lllll1_opy_ (u"ࠣࡘࡨࡶࡨ࡫࡬ࠣ᳽"),
            bstack1lllll1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧ᳾"): bstack1lllll1_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻࠱࠲ࡿࢂࠨ᳿").format(env.get(bstack1lllll1_opy_ (u"࡛ࠫࡋࡒࡄࡇࡏࡣ࡚ࡘࡌࠨᴀ"))),
            bstack1lllll1_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᴁ"): None,
            bstack1lllll1_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᴂ"): None,
        }
    if env.get(bstack1lllll1_opy_ (u"ࠢࡕࡇࡄࡑࡈࡏࡔ࡚ࡡ࡙ࡉࡗ࡙ࡉࡐࡐࠥᴃ")):
        return {
            bstack1lllll1_opy_ (u"ࠣࡰࡤࡱࡪࠨᴄ"): bstack1lllll1_opy_ (u"ࠤࡗࡩࡦࡳࡣࡪࡶࡼࠦᴅ"),
            bstack1lllll1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᴆ"): None,
            bstack1lllll1_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᴇ"): env.get(bstack1lllll1_opy_ (u"࡚ࠧࡅࡂࡏࡆࡍ࡙࡟࡟ࡑࡔࡒࡎࡊࡉࡔࡠࡐࡄࡑࡊࠨᴈ")),
            bstack1lllll1_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᴉ"): env.get(bstack1lllll1_opy_ (u"ࠢࡃࡗࡌࡐࡉࡥࡎࡖࡏࡅࡉࡗࠨᴊ"))
        }
    if any([env.get(bstack1lllll1_opy_ (u"ࠣࡅࡒࡒࡈࡕࡕࡓࡕࡈࠦᴋ")), env.get(bstack1lllll1_opy_ (u"ࠤࡆࡓࡓࡉࡏࡖࡔࡖࡉࡤ࡛ࡒࡍࠤᴌ")), env.get(bstack1lllll1_opy_ (u"ࠥࡇࡔࡔࡃࡐࡗࡕࡗࡊࡥࡕࡔࡇࡕࡒࡆࡓࡅࠣᴍ")), env.get(bstack1lllll1_opy_ (u"ࠦࡈࡕࡎࡄࡑࡘࡖࡘࡋ࡟ࡕࡇࡄࡑࠧᴎ"))]):
        return {
            bstack1lllll1_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᴏ"): bstack1lllll1_opy_ (u"ࠨࡃࡰࡰࡦࡳࡺࡸࡳࡦࠤᴐ"),
            bstack1lllll1_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᴑ"): None,
            bstack1lllll1_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᴒ"): env.get(bstack1lllll1_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡠࡌࡒࡆࡤࡔࡁࡎࡇࠥᴓ")) or None,
            bstack1lllll1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤᴔ"): env.get(bstack1lllll1_opy_ (u"ࠦࡇ࡛ࡉࡍࡆࡢࡍࡉࠨᴕ"), 0)
        }
    if env.get(bstack1lllll1_opy_ (u"ࠧࡍࡏࡠࡌࡒࡆࡤࡔࡁࡎࡇࠥᴖ")):
        return {
            bstack1lllll1_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᴗ"): bstack1lllll1_opy_ (u"ࠢࡈࡱࡆࡈࠧᴘ"),
            bstack1lllll1_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᴙ"): None,
            bstack1lllll1_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᴚ"): env.get(bstack1lllll1_opy_ (u"ࠥࡋࡔࡥࡊࡐࡄࡢࡒࡆࡓࡅࠣᴛ")),
            bstack1lllll1_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᴜ"): env.get(bstack1lllll1_opy_ (u"ࠧࡍࡏࡠࡒࡌࡔࡊࡒࡉࡏࡇࡢࡇࡔ࡛ࡎࡕࡇࡕࠦᴝ"))
        }
    if env.get(bstack1lllll1_opy_ (u"ࠨࡃࡇࡡࡅ࡙ࡎࡒࡄࡠࡋࡇࠦᴞ")):
        return {
            bstack1lllll1_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᴟ"): bstack1lllll1_opy_ (u"ࠣࡅࡲࡨࡪࡌࡲࡦࡵ࡫ࠦᴠ"),
            bstack1lllll1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᴡ"): env.get(bstack1lllll1_opy_ (u"ࠥࡇࡋࡥࡂࡖࡋࡏࡈࡤ࡛ࡒࡍࠤᴢ")),
            bstack1lllll1_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᴣ"): env.get(bstack1lllll1_opy_ (u"ࠧࡉࡆࡠࡒࡌࡔࡊࡒࡉࡏࡇࡢࡒࡆࡓࡅࠣᴤ")),
            bstack1lllll1_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᴥ"): env.get(bstack1lllll1_opy_ (u"ࠢࡄࡈࡢࡆ࡚ࡏࡌࡅࡡࡌࡈࠧᴦ"))
        }
    return {bstack1lllll1_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᴧ"): None}
def get_host_info():
    return {
        bstack1lllll1_opy_ (u"ࠤ࡫ࡳࡸࡺ࡮ࡢ࡯ࡨࠦᴨ"): platform.node(),
        bstack1lllll1_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱࠧᴩ"): platform.system(),
        bstack1lllll1_opy_ (u"ࠦࡹࡿࡰࡦࠤᴪ"): platform.machine(),
        bstack1lllll1_opy_ (u"ࠧࡼࡥࡳࡵ࡬ࡳࡳࠨᴫ"): platform.version(),
        bstack1lllll1_opy_ (u"ࠨࡡࡳࡥ࡫ࠦᴬ"): platform.architecture()[0]
    }
def bstack1ll11ll1l_opy_():
    try:
        import selenium
        return True
    except ImportError:
        return False
def bstack1111l1lll1l_opy_():
    if bstack11l1111l_opy_.get_property(bstack1lllll1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࠨᴭ")):
        return bstack1lllll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧᴮ")
    return bstack1lllll1_opy_ (u"ࠩࡸࡲࡰࡴ࡯ࡸࡰࡢ࡫ࡷ࡯ࡤࠨᴯ")
def bstack1111lll1l11_opy_(driver):
    info = {
        bstack1lllll1_opy_ (u"ࠪࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠩᴰ"): driver.capabilities,
        bstack1lllll1_opy_ (u"ࠫࡸ࡫ࡳࡴ࡫ࡲࡲࡤ࡯ࡤࠨᴱ"): driver.session_id,
        bstack1lllll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࠭ᴲ"): driver.capabilities.get(bstack1lllll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫᴳ"), None),
        bstack1lllll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡠࡸࡨࡶࡸ࡯࡯࡯ࠩᴴ"): driver.capabilities.get(bstack1lllll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩᴵ"), None),
        bstack1lllll1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࠫᴶ"): driver.capabilities.get(bstack1lllll1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡓࡧ࡭ࡦࠩᴷ"), None),
        bstack1lllll1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡥࡶࡦࡴࡶ࡭ࡴࡴࠧᴸ"):driver.capabilities.get(bstack1lllll1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡖࡦࡴࡶ࡭ࡴࡴࠧᴹ"), None),
    }
    if bstack1111l1lll1l_opy_() == bstack1lllll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬᴺ"):
        if bstack11ll111ll_opy_():
            info[bstack1lllll1_opy_ (u"ࠧࡱࡴࡲࡨࡺࡩࡴࠨᴻ")] = bstack1lllll1_opy_ (u"ࠨࡣࡳࡴ࠲ࡧࡵࡵࡱࡰࡥࡹ࡫ࠧᴼ")
        elif driver.capabilities.get(bstack1lllll1_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪᴽ"), {}).get(bstack1lllll1_opy_ (u"ࠪࡸࡺࡸࡢࡰࡵࡦࡥࡱ࡫ࠧᴾ"), False):
            info[bstack1lllll1_opy_ (u"ࠫࡵࡸ࡯ࡥࡷࡦࡸࠬᴿ")] = bstack1lllll1_opy_ (u"ࠬࡺࡵࡳࡤࡲࡷࡨࡧ࡬ࡦࠩᵀ")
        else:
            info[bstack1lllll1_opy_ (u"࠭ࡰࡳࡱࡧࡹࡨࡺࠧᵁ")] = bstack1lllll1_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡦࠩᵂ")
    return info
def bstack11ll111ll_opy_():
    if bstack11l1111l_opy_.get_property(bstack1lllll1_opy_ (u"ࠨࡣࡳࡴࡤࡧࡵࡵࡱࡰࡥࡹ࡫ࠧᵃ")):
        return True
    if bstack11l11l111l_opy_(os.environ.get(bstack1lllll1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡋࡖࡣࡆࡖࡐࡠࡃࡘࡘࡔࡓࡁࡕࡇࠪᵄ"), None)):
        return True
    return False
def bstack1l1111111_opy_(bstack111l1111ll1_opy_, url, data, config):
    headers = config.get(bstack1lllll1_opy_ (u"ࠪ࡬ࡪࡧࡤࡦࡴࡶࠫᵅ"), None)
    proxies = bstack111l111l1_opy_(config, url)
    auth = config.get(bstack1lllll1_opy_ (u"ࠫࡦࡻࡴࡩࠩᵆ"), None)
    response = requests.request(
            bstack111l1111ll1_opy_,
            url=url,
            headers=headers,
            auth=auth,
            json=data,
            proxies=proxies
        )
    return response
def bstack11111ll1l1_opy_(bstack111l1llll1_opy_, size):
    bstack111lll1l11_opy_ = []
    while len(bstack111l1llll1_opy_) > size:
        bstack111l1l111_opy_ = bstack111l1llll1_opy_[:size]
        bstack111lll1l11_opy_.append(bstack111l1l111_opy_)
        bstack111l1llll1_opy_ = bstack111l1llll1_opy_[size:]
    bstack111lll1l11_opy_.append(bstack111l1llll1_opy_)
    return bstack111lll1l11_opy_
def bstack1111lll11l1_opy_(message, bstack1111ll1l111_opy_=False):
    os.write(1, bytes(message, bstack1lllll1_opy_ (u"ࠬࡻࡴࡧ࠯࠻ࠫᵇ")))
    os.write(1, bytes(bstack1lllll1_opy_ (u"࠭࡜࡯ࠩᵈ"), bstack1lllll1_opy_ (u"ࠧࡶࡶࡩ࠱࠽࠭ᵉ")))
    if bstack1111ll1l111_opy_:
        with open(bstack1lllll1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠮ࡱ࠴࠵ࡾ࠳ࠧᵊ") + os.environ[bstack1lllll1_opy_ (u"ࠩࡅࡗࡤ࡚ࡅࡔࡖࡒࡔࡘࡥࡂࡖࡋࡏࡈࡤࡎࡁࡔࡊࡈࡈࡤࡏࡄࠨᵋ")] + bstack1lllll1_opy_ (u"ࠪ࠲ࡱࡵࡧࠨᵌ"), bstack1lllll1_opy_ (u"ࠫࡦ࠭ᵍ")) as f:
            f.write(message + bstack1lllll1_opy_ (u"ࠬࡢ࡮ࠨᵎ"))
def bstack1lll1l1l11l_opy_():
    return os.environ[bstack1lllll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡇࡕࡕࡑࡐࡅ࡙ࡏࡏࡏࠩᵏ")].lower() == bstack1lllll1_opy_ (u"ࠧࡵࡴࡸࡩࠬᵐ")
def bstack1llll11l_opy_():
    return bstack1l1ll1l1_opy_().replace(tzinfo=None).isoformat() + bstack1lllll1_opy_ (u"ࠨ࡜ࠪᵑ")
def bstack111l1ll1lll_opy_(start, finish):
    return (datetime.datetime.fromisoformat(finish.rstrip(bstack1lllll1_opy_ (u"ࠩ࡝ࠫᵒ"))) - datetime.datetime.fromisoformat(start.rstrip(bstack1lllll1_opy_ (u"ࠪ࡞ࠬᵓ")))).total_seconds() * 1000
def bstack111l1l1lll1_opy_(timestamp):
    return bstack1111ll11lll_opy_(timestamp).isoformat() + bstack1lllll1_opy_ (u"ࠫ࡟࠭ᵔ")
def bstack111l11ll11l_opy_(bstack1111lll1lll_opy_):
    date_format = bstack1lllll1_opy_ (u"࡙ࠬࠫࠦ࡯ࠨࡨࠥࠫࡈ࠻ࠧࡐ࠾࡙ࠪ࠮ࠦࡨࠪᵕ")
    bstack111ll1111ll_opy_ = datetime.datetime.strptime(bstack1111lll1lll_opy_, date_format)
    return bstack111ll1111ll_opy_.isoformat() + bstack1lllll1_opy_ (u"࡚࠭ࠨᵖ")
def bstack1111llll111_opy_(outcome):
    _, exception, _ = outcome.excinfo or (None, None, None)
    if exception:
        return bstack1lllll1_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧᵗ")
    else:
        return bstack1lllll1_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨᵘ")
def bstack11l11l111l_opy_(val):
    if val is None:
        return False
    return val.__str__().lower() == bstack1lllll1_opy_ (u"ࠩࡷࡶࡺ࡫ࠧᵙ")
def bstack111l1ll1l11_opy_(val):
    return val.__str__().lower() == bstack1lllll1_opy_ (u"ࠪࡪࡦࡲࡳࡦࠩᵚ")
def error_handler(bstack111l11l1l1l_opy_=Exception, class_method=False, default_value=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except bstack111l11l1l1l_opy_ as e:
                print(bstack1lllll1_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡪࡺࡴࡣࡵ࡫ࡲࡲࠥࢁࡽࠡ࠯ࡁࠤࢀࢃ࠺ࠡࡽࢀࠦᵛ").format(func.__name__, bstack111l11l1l1l_opy_.__name__, str(e)))
                return default_value
        return wrapper
    def bstack1111l1lll11_opy_(bstack111l11111l1_opy_):
        def wrapped(cls, *args, **kwargs):
            try:
                return bstack111l11111l1_opy_(cls, *args, **kwargs)
            except bstack111l11l1l1l_opy_ as e:
                print(bstack1lllll1_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࠦࡻࡾࠢ࠰ࡂࠥࢁࡽ࠻ࠢࡾࢁࠧᵜ").format(bstack111l11111l1_opy_.__name__, bstack111l11l1l1l_opy_.__name__, str(e)))
                return default_value
        return wrapped
    if class_method:
        return bstack1111l1lll11_opy_
    else:
        return decorator
def bstack11ll11111_opy_(bstack11l1l111_opy_):
    if os.getenv(bstack1lllll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡇࡕࡕࡑࡐࡅ࡙ࡏࡏࡏࠩᵝ")) is not None:
        return bstack11l11l111l_opy_(os.getenv(bstack1lllll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡁࡖࡖࡒࡑࡆ࡚ࡉࡐࡐࠪᵞ")))
    if bstack1lllll1_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬᵟ") in bstack11l1l111_opy_ and bstack111l1ll1l11_opy_(bstack11l1l111_opy_[bstack1lllll1_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳ࠭ᵠ")]):
        return False
    if bstack1lllll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬᵡ") in bstack11l1l111_opy_ and bstack111l1ll1l11_opy_(bstack11l1l111_opy_[bstack1lllll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳ࠭ᵢ")]):
        return False
    return True
def bstack1ll11llll1_opy_():
    try:
        from pytest_bdd import reporting
        bstack1111ll1l1l1_opy_ = os.environ.get(bstack1lllll1_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡚࡙ࡅࡓࡡࡉࡖࡆࡓࡅࡘࡑࡕࡏࠧᵣ"), None)
        return bstack1111ll1l1l1_opy_ is None or bstack1111ll1l1l1_opy_ == bstack1lllll1_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠥᵤ")
    except Exception as e:
        return False
def bstack1lll1ll111_opy_(hub_url, CONFIG):
    if bstack11l1l1lll1_opy_() <= version.parse(bstack1lllll1_opy_ (u"ࠧ࠴࠰࠴࠷࠳࠶ࠧᵥ")):
        if hub_url:
            return bstack1lllll1_opy_ (u"ࠣࡪࡷࡸࡵࡀ࠯࠰ࠤᵦ") + hub_url + bstack1lllll1_opy_ (u"ࠤ࠽࠼࠵࠵ࡷࡥ࠱࡫ࡹࡧࠨᵧ")
        return bstack111l1ll111_opy_
    if hub_url:
        return bstack1lllll1_opy_ (u"ࠥ࡬ࡹࡺࡰࡴ࠼࠲࠳ࠧᵨ") + hub_url + bstack1lllll1_opy_ (u"ࠦ࠴ࡽࡤ࠰ࡪࡸࡦࠧᵩ")
    return bstack1l11lll1l1_opy_
def bstack111l1ll1l1l_opy_():
    return isinstance(os.getenv(bstack1lllll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕ࡟ࡔࡆࡕࡗࡣࡕࡒࡕࡈࡋࡑࠫᵪ")), str)
def bstack1ll1l1l1ll_opy_(url):
    return urlparse(url).hostname
def bstack1l11ll111l_opy_(hostname):
    for bstack1ll111ll11_opy_ in bstack1l11111111_opy_:
        regex = re.compile(bstack1ll111ll11_opy_)
        if regex.match(hostname):
            return True
    return False
def bstack11ll11l111l_opy_(bstack1111lllll1l_opy_, file_name, logger):
    bstack1ll1l1l1l1_opy_ = os.path.join(os.path.expanduser(bstack1lllll1_opy_ (u"࠭ࡾࠨᵫ")), bstack1111lllll1l_opy_)
    try:
        if not os.path.exists(bstack1ll1l1l1l1_opy_):
            os.makedirs(bstack1ll1l1l1l1_opy_)
        file_path = os.path.join(os.path.expanduser(bstack1lllll1_opy_ (u"ࠧࡿࠩᵬ")), bstack1111lllll1l_opy_, file_name)
        if not os.path.isfile(file_path):
            with open(file_path, bstack1lllll1_opy_ (u"ࠨࡹࠪᵭ")):
                pass
            with open(file_path, bstack1lllll1_opy_ (u"ࠤࡺ࠯ࠧᵮ")) as outfile:
                json.dump({}, outfile)
        return file_path
    except Exception as e:
        logger.debug(bstack1lll1llll1_opy_.format(str(e)))
def bstack11ll11l11l1_opy_(file_name, key, value, logger):
    file_path = bstack11ll11l111l_opy_(bstack1lllll1_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪᵯ"), file_name, logger)
    if file_path != None:
        if os.path.exists(file_path):
            bstack1l11l1l1ll_opy_ = json.load(open(file_path, bstack1lllll1_opy_ (u"ࠫࡷࡨࠧᵰ")))
        else:
            bstack1l11l1l1ll_opy_ = {}
        bstack1l11l1l1ll_opy_[key] = value
        with open(file_path, bstack1lllll1_opy_ (u"ࠧࡽࠫࠣᵱ")) as outfile:
            json.dump(bstack1l11l1l1ll_opy_, outfile)
def bstack1l11l1ll1l_opy_(file_name, logger):
    file_path = bstack11ll11l111l_opy_(bstack1lllll1_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ᵲ"), file_name, logger)
    bstack1l11l1l1ll_opy_ = {}
    if file_path != None and os.path.exists(file_path):
        with open(file_path, bstack1lllll1_opy_ (u"ࠧࡳࠩᵳ")) as bstack1ll1ll111_opy_:
            bstack1l11l1l1ll_opy_ = json.load(bstack1ll1ll111_opy_)
    return bstack1l11l1l1ll_opy_
def bstack1l1ll111l1_opy_(file_path, logger):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
    except Exception as e:
        logger.debug(bstack1lllll1_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡨࡪࡲࡥࡵ࡫ࡱ࡫ࠥ࡬ࡩ࡭ࡧ࠽ࠤࠬᵴ") + file_path + bstack1lllll1_opy_ (u"ࠩࠣࠫᵵ") + str(e))
def bstack11l1l1lll1_opy_():
    from selenium import webdriver
    return version.parse(webdriver.__version__)
class Notset:
    def __repr__(self):
        return bstack1lllll1_opy_ (u"ࠥࡀࡓࡕࡔࡔࡇࡗࡂࠧᵶ")
def bstack1111l1lll_opy_(config):
    if bstack1lllll1_opy_ (u"ࠫ࡮ࡹࡐ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠪᵷ") in config:
        del (config[bstack1lllll1_opy_ (u"ࠬ࡯ࡳࡑ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠫᵸ")])
        return False
    if bstack11l1l1lll1_opy_() < version.parse(bstack1lllll1_opy_ (u"࠭࠳࠯࠶࠱࠴ࠬᵹ")):
        return False
    if bstack11l1l1lll1_opy_() >= version.parse(bstack1lllll1_opy_ (u"ࠧ࠵࠰࠴࠲࠺࠭ᵺ")):
        return True
    if bstack1lllll1_opy_ (u"ࠨࡷࡶࡩ࡜࠹ࡃࠨᵻ") in config and config[bstack1lllll1_opy_ (u"ࠩࡸࡷࡪ࡝࠳ࡄࠩᵼ")] is False:
        return False
    else:
        return True
def bstack1111l1l1l_opy_(args_list, bstack1111l1llll1_opy_):
    index = -1
    for value in bstack1111l1llll1_opy_:
        try:
            index = args_list.index(value)
            return index
        except Exception as e:
            return index
    return index
def bstack111l1l1l1ll_opy_(a, b):
  for k, v in b.items():
    if isinstance(v, dict) and k in a and isinstance(a[k], dict):
        bstack111l1l1l1ll_opy_(a[k], v)
    else:
        a[k] = v
class Result:
    def __init__(self, result=None, duration=None, exception=None, bstack1llll1l1_opy_=None):
        self.result = result
        self.duration = duration
        self.exception = exception
        self.exception_type = type(self.exception).__name__ if exception else None
        self.bstack1llll1l1_opy_ = bstack1llll1l1_opy_
    @classmethod
    def passed(cls):
        return Result(result=bstack1lllll1_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪᵽ"))
    @classmethod
    def failed(cls, exception=None):
        return Result(result=bstack1lllll1_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫᵾ"), exception=exception)
    def bstack11111l11ll_opy_(self):
        if self.result != bstack1lllll1_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬᵿ"):
            return None
        if isinstance(self.exception_type, str) and bstack1lllll1_opy_ (u"ࠨࡁࡴࡵࡨࡶࡹ࡯࡯࡯ࠤᶀ") in self.exception_type:
            return bstack1lllll1_opy_ (u"ࠢࡂࡵࡶࡩࡷࡺࡩࡰࡰࡈࡶࡷࡵࡲࠣᶁ")
        return bstack1lllll1_opy_ (u"ࠣࡗࡱ࡬ࡦࡴࡤ࡭ࡧࡧࡉࡷࡸ࡯ࡳࠤᶂ")
    def bstack111l1l11l11_opy_(self):
        if self.result != bstack1lllll1_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩᶃ"):
            return None
        if self.bstack1llll1l1_opy_:
            return self.bstack1llll1l1_opy_
        return bstack1111l1ll111_opy_(self.exception)
def bstack1111l1ll111_opy_(exc):
    return [traceback.format_exception(exc)]
def bstack111l1llllll_opy_(message):
    if isinstance(message, str):
        return not bool(message and message.strip())
    return True
def bstack1lll1l11_opy_(object, key, default_value):
    if not object or not object.__dict__:
        return default_value
    if key in object.__dict__.keys():
        return object.__dict__.get(key)
    return default_value
def bstack1l11l1111_opy_(config, logger):
    try:
        import playwright
        bstack1111lll1ll1_opy_ = playwright.__file__
        bstack1111lllll11_opy_ = os.path.split(bstack1111lll1ll1_opy_)
        bstack111l11ll1l1_opy_ = bstack1111lllll11_opy_[0] + bstack1lllll1_opy_ (u"ࠪ࠳ࡩࡸࡩࡷࡧࡵ࠳ࡵࡧࡣ࡬ࡣࡪࡩ࠴ࡲࡩࡣ࠱ࡦࡰ࡮࠵ࡣ࡭࡫࠱࡮ࡸ࠭ᶄ")
        os.environ[bstack1lllll1_opy_ (u"ࠫࡌࡒࡏࡃࡃࡏࡣࡆࡍࡅࡏࡖࡢࡌ࡙࡚ࡐࡠࡒࡕࡓ࡝࡟ࠧᶅ")] = bstack1ll1ll1lll_opy_(config)
        with open(bstack111l11ll1l1_opy_, bstack1lllll1_opy_ (u"ࠬࡸࠧᶆ")) as f:
            file_content = f.read()
            bstack111l1ll111l_opy_ = bstack1lllll1_opy_ (u"࠭ࡧ࡭ࡱࡥࡥࡱ࠳ࡡࡨࡧࡱࡸࠬᶇ")
            bstack111l1l11111_opy_ = file_content.find(bstack111l1ll111l_opy_)
            if bstack111l1l11111_opy_ == -1:
              process = subprocess.Popen(bstack1lllll1_opy_ (u"ࠢ࡯ࡲࡰࠤ࡮ࡴࡳࡵࡣ࡯ࡰࠥ࡭࡬ࡰࡤࡤࡰ࠲ࡧࡧࡦࡰࡷࠦᶈ"), shell=True, cwd=bstack1111lllll11_opy_[0])
              process.wait()
              bstack1111l1l11ll_opy_ = bstack1lllll1_opy_ (u"ࠨࠤࡸࡷࡪࠦࡳࡵࡴ࡬ࡧࡹࠨ࠻ࠨᶉ")
              bstack111l111l111_opy_ = bstack1lllll1_opy_ (u"ࠤࠥࠦࠥࡢࠢࡶࡵࡨࠤࡸࡺࡲࡪࡥࡷࡠࠧࡁࠠࡤࡱࡱࡷࡹࠦࡻࠡࡤࡲࡳࡹࡹࡴࡳࡣࡳࠤࢂࠦ࠽ࠡࡴࡨࡵࡺ࡯ࡲࡦࠪࠪ࡫ࡱࡵࡢࡢ࡮࠰ࡥ࡬࡫࡮ࡵࠩࠬ࠿ࠥ࡯ࡦࠡࠪࡳࡶࡴࡩࡥࡴࡵ࠱ࡩࡳࡼ࠮ࡈࡎࡒࡆࡆࡒ࡟ࡂࡉࡈࡒ࡙ࡥࡈࡕࡖࡓࡣࡕࡘࡏ࡙࡛ࠬࠤࡧࡵ࡯ࡵࡵࡷࡶࡦࡶࠨࠪ࠽ࠣࠦࠧࠨᶊ")
              bstack1111ll1l1ll_opy_ = file_content.replace(bstack1111l1l11ll_opy_, bstack111l111l111_opy_)
              with open(bstack111l11ll1l1_opy_, bstack1lllll1_opy_ (u"ࠪࡻࠬᶋ")) as f:
                f.write(bstack1111ll1l1ll_opy_)
    except Exception as e:
        logger.error(bstack111l11l1l1_opy_.format(str(e)))
def bstack1llllllll1_opy_():
  try:
    bstack111l1111l11_opy_ = os.path.join(tempfile.gettempdir(), bstack1lllll1_opy_ (u"ࠫࡴࡶࡴࡪ࡯ࡤࡰࡤ࡮ࡵࡣࡡࡸࡶࡱ࠴ࡪࡴࡱࡱࠫᶌ"))
    bstack111l1ll11l1_opy_ = []
    if os.path.exists(bstack111l1111l11_opy_):
      with open(bstack111l1111l11_opy_) as f:
        bstack111l1ll11l1_opy_ = json.load(f)
      os.remove(bstack111l1111l11_opy_)
    return bstack111l1ll11l1_opy_
  except:
    pass
  return []
def bstack11l1lll11_opy_(bstack1l11llll1_opy_):
  try:
    bstack111l1ll11l1_opy_ = []
    bstack111l1111l11_opy_ = os.path.join(tempfile.gettempdir(), bstack1lllll1_opy_ (u"ࠬࡵࡰࡵ࡫ࡰࡥࡱࡥࡨࡶࡤࡢࡹࡷࡲ࠮࡫ࡵࡲࡲࠬᶍ"))
    if os.path.exists(bstack111l1111l11_opy_):
      with open(bstack111l1111l11_opy_) as f:
        bstack111l1ll11l1_opy_ = json.load(f)
    bstack111l1ll11l1_opy_.append(bstack1l11llll1_opy_)
    with open(bstack111l1111l11_opy_, bstack1lllll1_opy_ (u"࠭ࡷࠨᶎ")) as f:
        json.dump(bstack111l1ll11l1_opy_, f)
  except:
    pass
def bstack1ll1ll11l1_opy_(logger, bstack111l11l11ll_opy_ = False):
  try:
    test_name = os.environ.get(bstack1lllll1_opy_ (u"ࠧࡑ࡛ࡗࡉࡘ࡚࡟ࡕࡇࡖࡘࡤࡔࡁࡎࡇࠪᶏ"), bstack1lllll1_opy_ (u"ࠨࠩᶐ"))
    if test_name == bstack1lllll1_opy_ (u"ࠩࠪᶑ"):
        test_name = threading.current_thread().__dict__.get(bstack1lllll1_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࡅࡨࡩࡥࡴࡦࡵࡷࡣࡳࡧ࡭ࡦࠩᶒ"), bstack1lllll1_opy_ (u"ࠫࠬᶓ"))
    bstack111l1lll1ll_opy_ = bstack1lllll1_opy_ (u"ࠬ࠲ࠠࠨᶔ").join(threading.current_thread().bstackTestErrorMessages)
    if bstack111l11l11ll_opy_:
        bstack1l11l111l_opy_ = os.environ.get(bstack1lllll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝࠭ᶕ"), bstack1lllll1_opy_ (u"ࠧ࠱ࠩᶖ"))
        bstack11ll111l1_opy_ = {bstack1lllll1_opy_ (u"ࠨࡰࡤࡱࡪ࠭ᶗ"): test_name, bstack1lllll1_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨᶘ"): bstack111l1lll1ll_opy_, bstack1lllll1_opy_ (u"ࠪ࡭ࡳࡪࡥࡹࠩᶙ"): bstack1l11l111l_opy_}
        bstack1111ll1lll1_opy_ = []
        bstack111l11llll1_opy_ = os.path.join(tempfile.gettempdir(), bstack1lllll1_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࡣࡵࡶࡰࡠࡧࡵࡶࡴࡸ࡟࡭࡫ࡶࡸ࠳ࡰࡳࡰࡰࠪᶚ"))
        if os.path.exists(bstack111l11llll1_opy_):
            with open(bstack111l11llll1_opy_) as f:
                bstack1111ll1lll1_opy_ = json.load(f)
        bstack1111ll1lll1_opy_.append(bstack11ll111l1_opy_)
        with open(bstack111l11llll1_opy_, bstack1lllll1_opy_ (u"ࠬࡽࠧᶛ")) as f:
            json.dump(bstack1111ll1lll1_opy_, f)
    else:
        bstack11ll111l1_opy_ = {bstack1lllll1_opy_ (u"࠭࡮ࡢ࡯ࡨࠫᶜ"): test_name, bstack1lllll1_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭ᶝ"): bstack111l1lll1ll_opy_, bstack1lllll1_opy_ (u"ࠨ࡫ࡱࡨࡪࡾࠧᶞ"): str(multiprocessing.current_process().name)}
        if bstack1lllll1_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡡࡨࡶࡷࡵࡲࡠ࡮࡬ࡷࡹ࠭ᶟ") not in multiprocessing.current_process().__dict__.keys():
            multiprocessing.current_process().bstack_error_list = []
        multiprocessing.current_process().bstack_error_list.append(bstack11ll111l1_opy_)
  except Exception as e:
      logger.warn(bstack1lllll1_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡳࡵࡱࡵࡩࠥࡶࡹࡵࡧࡶࡸࠥ࡬ࡵ࡯ࡰࡨࡰࠥࡪࡡࡵࡣ࠽ࠤࢀࢃࠢᶠ").format(e))
def bstack1ll1llll1l_opy_(error_message, test_name, index, logger):
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack1lllll1_opy_ (u"ࠫ࡫࡯࡬ࡦ࡮ࡲࡧࡰࠦ࡮ࡰࡶࠣࡥࡻࡧࡩ࡭ࡣࡥࡰࡪ࠲ࠠࡶࡵ࡬ࡲ࡬ࠦࡢࡢࡵ࡬ࡧࠥ࡬ࡩ࡭ࡧࠣࡳࡵ࡫ࡲࡢࡶ࡬ࡳࡳࡹࠧᶡ"))
    try:
      bstack111l11lll11_opy_ = []
      bstack11ll111l1_opy_ = {bstack1lllll1_opy_ (u"ࠬࡴࡡ࡮ࡧࠪᶢ"): test_name, bstack1lllll1_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬᶣ"): error_message, bstack1lllll1_opy_ (u"ࠧࡪࡰࡧࡩࡽ࠭ᶤ"): index}
      bstack1111l1l1l1l_opy_ = os.path.join(tempfile.gettempdir(), bstack1lllll1_opy_ (u"ࠨࡴࡲࡦࡴࡺ࡟ࡦࡴࡵࡳࡷࡥ࡬ࡪࡵࡷ࠲࡯ࡹ࡯࡯ࠩᶥ"))
      if os.path.exists(bstack1111l1l1l1l_opy_):
          with open(bstack1111l1l1l1l_opy_) as f:
              bstack111l11lll11_opy_ = json.load(f)
      bstack111l11lll11_opy_.append(bstack11ll111l1_opy_)
      with open(bstack1111l1l1l1l_opy_, bstack1lllll1_opy_ (u"ࠩࡺࠫᶦ")) as f:
          json.dump(bstack111l11lll11_opy_, f)
    except Exception as e:
      logger.warn(bstack1lllll1_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡳࡵࡱࡵࡩࠥࡸ࡯ࡣࡱࡷࠤ࡫ࡻ࡮࡯ࡧ࡯ࠤࡩࡧࡴࡢ࠼ࠣࡿࢂࠨᶧ").format(e))
    return
  bstack111l11lll11_opy_ = []
  bstack11ll111l1_opy_ = {bstack1lllll1_opy_ (u"ࠫࡳࡧ࡭ࡦࠩᶨ"): test_name, bstack1lllll1_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫᶩ"): error_message, bstack1lllll1_opy_ (u"࠭ࡩ࡯ࡦࡨࡼࠬᶪ"): index}
  bstack1111l1l1l1l_opy_ = os.path.join(tempfile.gettempdir(), bstack1lllll1_opy_ (u"ࠧࡳࡱࡥࡳࡹࡥࡥࡳࡴࡲࡶࡤࡲࡩࡴࡶ࠱࡮ࡸࡵ࡮ࠨᶫ"))
  lock_file = bstack1111l1l1l1l_opy_ + bstack1lllll1_opy_ (u"ࠨ࠰࡯ࡳࡨࡱࠧᶬ")
  try:
    with FileLock(lock_file, timeout=10):
      if os.path.exists(bstack1111l1l1l1l_opy_):
          with open(bstack1111l1l1l1l_opy_, bstack1lllll1_opy_ (u"ࠩࡵࠫᶭ")) as f:
              content = f.read().strip()
              if content:
                  bstack111l11lll11_opy_ = json.load(open(bstack1111l1l1l1l_opy_))
      bstack111l11lll11_opy_.append(bstack11ll111l1_opy_)
      with open(bstack1111l1l1l1l_opy_, bstack1lllll1_opy_ (u"ࠪࡻࠬᶮ")) as f:
          json.dump(bstack111l11lll11_opy_, f)
  except Exception as e:
    logger.warn(bstack1lllll1_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡴࡶࡲࡶࡪࠦࡲࡰࡤࡲࡸࠥ࡬ࡵ࡯ࡰࡨࡰࠥࡪࡡࡵࡣࠣࡻ࡮ࡺࡨࠡࡨ࡬ࡰࡪࠦ࡬ࡰࡥ࡮࡭ࡳ࡭࠺ࠡࡽࢀࠦᶯ").format(e))
def bstack1lll111l11_opy_(bstack111l11llll_opy_, name, logger):
  try:
    bstack11ll111l1_opy_ = {bstack1lllll1_opy_ (u"ࠬࡴࡡ࡮ࡧࠪᶰ"): name, bstack1lllll1_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬᶱ"): bstack111l11llll_opy_, bstack1lllll1_opy_ (u"ࠧࡪࡰࡧࡩࡽ࠭ᶲ"): str(threading.current_thread()._name)}
    return bstack11ll111l1_opy_
  except Exception as e:
    logger.warn(bstack1lllll1_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡸࡺ࡯ࡳࡧࠣࡦࡪ࡮ࡡࡷࡧࠣࡪࡺࡴ࡮ࡦ࡮ࠣࡨࡦࡺࡡ࠻ࠢࡾࢁࠧᶳ").format(e))
  return
def bstack111l11l1l11_opy_():
    return platform.system() == bstack1lllll1_opy_ (u"࡚ࠩ࡭ࡳࡪ࡯ࡸࡵࠪᶴ")
def bstack1111llll11_opy_(bstack1111ll1llll_opy_, config, logger):
    bstack111l111l11l_opy_ = {}
    try:
        return {key: config[key] for key in config if bstack1111ll1llll_opy_.match(key)}
    except Exception as e:
        logger.debug(bstack1lllll1_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡦࡪ࡮ࡷࡩࡷࠦࡣࡰࡰࡩ࡭࡬ࠦ࡫ࡦࡻࡶࠤࡧࡿࠠࡳࡧࡪࡩࡽࠦ࡭ࡢࡶࡦ࡬࠿ࠦࡻࡾࠤᶵ").format(e))
    return bstack111l111l11l_opy_
def bstack11l1ll111ll_opy_(bstack111l111111l_opy_, bstack111ll111l11_opy_):
    bstack111l1l111ll_opy_ = version.parse(bstack111l111111l_opy_)
    bstack1111l1l1l11_opy_ = version.parse(bstack111ll111l11_opy_)
    if bstack111l1l111ll_opy_ > bstack1111l1l1l11_opy_:
        return 1
    elif bstack111l1l111ll_opy_ < bstack1111l1l1l11_opy_:
        return -1
    else:
        return 0
def bstack1l1ll1l1_opy_():
    return datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None)
def bstack1111ll11lll_opy_(timestamp):
    return datetime.datetime.fromtimestamp(timestamp, datetime.timezone.utc).replace(tzinfo=None)
def bstack111l111lll1_opy_(framework):
    from browserstack_sdk._version import __version__
    return str(framework) + str(__version__)
def bstack1ll1l1111l_opy_(options, framework, config, bstack1l1l1l1l11_opy_={}):
    if options is None:
        return
    if getattr(options, bstack1lllll1_opy_ (u"ࠫ࡬࡫ࡴࠨᶶ"), None):
        caps = options
    else:
        caps = options.to_capabilities()
    bstack1lll1ll1ll_opy_ = caps.get(bstack1lllll1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭ᶷ"))
    bstack111l111ll11_opy_ = True
    bstack11ll1lll1_opy_ = os.environ[bstack1lllll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫᶸ")]
    bstack1l111l1111l_opy_ = config.get(bstack1lllll1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧᶹ"), False)
    if bstack1l111l1111l_opy_:
        bstack1l1l1ll1l1l_opy_ = config.get(bstack1lllll1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨᶺ"), {})
        bstack1l1l1ll1l1l_opy_[bstack1lllll1_opy_ (u"ࠩࡤࡹࡹ࡮ࡔࡰ࡭ࡨࡲࠬᶻ")] = os.getenv(bstack1lllll1_opy_ (u"ࠪࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠨᶼ"))
        bstack111l1l1l111_opy_ = json.loads(os.getenv(bstack1lllll1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡠࡃࡆࡇࡊ࡙ࡓࡊࡄࡌࡐࡎ࡚࡙ࡠࡅࡒࡒࡋࡏࡇࡖࡔࡄࡘࡎࡕࡎࡠ࡛ࡐࡐࠬᶽ"), bstack1lllll1_opy_ (u"ࠬࢁࡽࠨᶾ"))).get(bstack1lllll1_opy_ (u"࠭ࡳࡤࡣࡱࡲࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧᶿ"))
    if bstack111l1ll1l11_opy_(caps.get(bstack1lllll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡵࡴࡧ࡚࠷ࡈ࠭᷀"))) or bstack111l1ll1l11_opy_(caps.get(bstack1lllll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡶࡵࡨࡣࡼ࠹ࡣࠨ᷁"))):
        bstack111l111ll11_opy_ = False
    if bstack1111l1lll_opy_({bstack1lllll1_opy_ (u"ࠤࡸࡷࡪ࡝࠳ࡄࠤ᷂"): bstack111l111ll11_opy_}):
        bstack1lll1ll1ll_opy_ = bstack1lll1ll1ll_opy_ or {}
        bstack1lll1ll1ll_opy_[bstack1lllll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡕࡇࡏࠬ᷃")] = bstack111l111lll1_opy_(framework)
        bstack1lll1ll1ll_opy_[bstack1lllll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳ࠭᷄")] = bstack1lll1l1l11l_opy_()
        bstack1lll1ll1ll_opy_[bstack1lllll1_opy_ (u"ࠬࡺࡥࡴࡶ࡫ࡹࡧࡈࡵࡪ࡮ࡧ࡙ࡺ࡯ࡤࠨ᷅")] = bstack11ll1lll1_opy_
        bstack1lll1ll1ll_opy_[bstack1lllll1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡕࡸ࡯ࡥࡷࡦࡸࡒࡧࡰࠨ᷆")] = bstack1l1l1l1l11_opy_
        if bstack1l111l1111l_opy_:
            bstack1lll1ll1ll_opy_[bstack1lllll1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ᷇")] = bstack1l111l1111l_opy_
            bstack1lll1ll1ll_opy_[bstack1lllll1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨ᷈")] = bstack1l1l1ll1l1l_opy_
            bstack1lll1ll1ll_opy_[bstack1lllll1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩ᷉")][bstack1lllll1_opy_ (u"ࠪࡷࡨࡧ࡮࡯ࡧࡵ࡚ࡪࡸࡳࡪࡱࡱ᷊ࠫ")] = bstack111l1l1l111_opy_
        if getattr(options, bstack1lllll1_opy_ (u"ࠫࡸ࡫ࡴࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷࡽࠬ᷋"), None):
            options.set_capability(bstack1lllll1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭᷌"), bstack1lll1ll1ll_opy_)
        else:
            options[bstack1lllll1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧ᷍")] = bstack1lll1ll1ll_opy_
    else:
        if getattr(options, bstack1lllll1_opy_ (u"ࠧࡴࡧࡷࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡹࠨ᷎"), None):
            options.set_capability(bstack1lllll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࡙ࡄࡌ᷏ࠩ"), bstack111l111lll1_opy_(framework))
            options.set_capability(bstack1lllll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰ᷐ࠪ"), bstack1lll1l1l11l_opy_())
            options.set_capability(bstack1lllll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡷࡩࡸࡺࡨࡶࡤࡅࡹ࡮ࡲࡤࡖࡷ࡬ࡨࠬ᷑"), bstack11ll1lll1_opy_)
            options.set_capability(bstack1lllll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡦࡺ࡯࡬ࡥࡒࡵࡳࡩࡻࡣࡵࡏࡤࡴࠬ᷒"), bstack1l1l1l1l11_opy_)
            if bstack1l111l1111l_opy_:
                options.set_capability(bstack1lllll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫᷓ"), bstack1l111l1111l_opy_)
                options.set_capability(bstack1lllll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷࠬᷔ"), bstack1l1l1ll1l1l_opy_)
                options.set_capability(bstack1lllll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ࠴ࡳࡤࡣࡱࡲࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧᷕ"), bstack111l1l1l111_opy_)
        else:
            options[bstack1lllll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࡙ࡄࡌࠩᷖ")] = bstack111l111lll1_opy_(framework)
            options[bstack1lllll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠪᷗ")] = bstack1lll1l1l11l_opy_()
            options[bstack1lllll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡷࡩࡸࡺࡨࡶࡤࡅࡹ࡮ࡲࡤࡖࡷ࡬ࡨࠬᷘ")] = bstack11ll1lll1_opy_
            options[bstack1lllll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡦࡺ࡯࡬ࡥࡒࡵࡳࡩࡻࡣࡵࡏࡤࡴࠬᷙ")] = bstack1l1l1l1l11_opy_
            if bstack1l111l1111l_opy_:
                options[bstack1lllll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫᷚ")] = bstack1l111l1111l_opy_
                options[bstack1lllll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷࠬᷛ")] = bstack1l1l1ll1l1l_opy_
                options[bstack1lllll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭ᷜ")][bstack1lllll1_opy_ (u"ࠨࡵࡦࡥࡳࡴࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩᷝ")] = bstack111l1l1l111_opy_
    return options
def bstack1111ll1ll1l_opy_(ws_endpoint, framework):
    bstack1l1l1l1l11_opy_ = bstack11l1111l_opy_.get_property(bstack1lllll1_opy_ (u"ࠤࡓࡐࡆ࡟ࡗࡓࡋࡊࡌ࡙ࡥࡐࡓࡑࡇ࡙ࡈ࡚࡟ࡎࡃࡓࠦᷞ"))
    if ws_endpoint and len(ws_endpoint.split(bstack1lllll1_opy_ (u"ࠪࡧࡦࡶࡳ࠾ࠩᷟ"))) > 1:
        ws_url = ws_endpoint.split(bstack1lllll1_opy_ (u"ࠫࡨࡧࡰࡴ࠿ࠪᷠ"))[0]
        if bstack1lllll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭ࠨᷡ") in ws_url:
            from browserstack_sdk._version import __version__
            bstack1111lllllll_opy_ = json.loads(urllib.parse.unquote(ws_endpoint.split(bstack1lllll1_opy_ (u"࠭ࡣࡢࡲࡶࡁࠬᷢ"))[1]))
            bstack1111lllllll_opy_ = bstack1111lllllll_opy_ or {}
            bstack11ll1lll1_opy_ = os.environ[bstack1lllll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬᷣ")]
            bstack1111lllllll_opy_[bstack1lllll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࡙ࡄࡌࠩᷤ")] = str(framework) + str(__version__)
            bstack1111lllllll_opy_[bstack1lllll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠪᷥ")] = bstack1lll1l1l11l_opy_()
            bstack1111lllllll_opy_[bstack1lllll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡷࡩࡸࡺࡨࡶࡤࡅࡹ࡮ࡲࡤࡖࡷ࡬ࡨࠬᷦ")] = bstack11ll1lll1_opy_
            bstack1111lllllll_opy_[bstack1lllll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡦࡺ࡯࡬ࡥࡒࡵࡳࡩࡻࡣࡵࡏࡤࡴࠬᷧ")] = bstack1l1l1l1l11_opy_
            ws_endpoint = ws_endpoint.split(bstack1lllll1_opy_ (u"ࠬࡩࡡࡱࡵࡀࠫᷨ"))[0] + bstack1lllll1_opy_ (u"࠭ࡣࡢࡲࡶࡁࠬᷩ") + urllib.parse.quote(json.dumps(bstack1111lllllll_opy_))
    return ws_endpoint
def bstack1lll1l1ll1_opy_():
    global bstack111l11l11_opy_
    from playwright._impl._browser_type import BrowserType
    bstack111l11l11_opy_ = BrowserType.connect
    return bstack111l11l11_opy_
def bstack1lll11l1l_opy_(framework_name):
    global bstack11l1ll1l1_opy_
    bstack11l1ll1l1_opy_ = framework_name
    return framework_name
def bstack11111l11l_opy_(self, *args, **kwargs):
    global bstack111l11l11_opy_
    try:
        global bstack11l1ll1l1_opy_
        if bstack1lllll1_opy_ (u"ࠧࡸࡵࡈࡲࡩࡶ࡯ࡪࡰࡷࠫᷪ") in kwargs:
            kwargs[bstack1lllll1_opy_ (u"ࠨࡹࡶࡉࡳࡪࡰࡰ࡫ࡱࡸࠬᷫ")] = bstack1111ll1ll1l_opy_(
                kwargs.get(bstack1lllll1_opy_ (u"ࠩࡺࡷࡊࡴࡤࡱࡱ࡬ࡲࡹ࠭ᷬ"), None),
                bstack11l1ll1l1_opy_
            )
    except Exception as e:
        logger.error(bstack1lllll1_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡺ࡬ࡪࡴࠠࡱࡴࡲࡧࡪࡹࡳࡪࡰࡪࠤࡘࡊࡋࠡࡥࡤࡴࡸࡀࠠࡼࡿࠥᷭ").format(str(e)))
    return bstack111l11l11_opy_(self, *args, **kwargs)
def bstack1111llll1ll_opy_(bstack1111l1ll1l1_opy_, proxies):
    proxy_settings = {}
    try:
        if not proxies:
            proxies = bstack111l111l1_opy_(bstack1111l1ll1l1_opy_, bstack1lllll1_opy_ (u"ࠦࠧᷮ"))
        if proxies and proxies.get(bstack1lllll1_opy_ (u"ࠧ࡮ࡴࡵࡲࡶࠦᷯ")):
            parsed_url = urlparse(proxies.get(bstack1lllll1_opy_ (u"ࠨࡨࡵࡶࡳࡷࠧᷰ")))
            if parsed_url and parsed_url.hostname: proxy_settings[bstack1lllll1_opy_ (u"ࠧࡱࡴࡲࡼࡾࡎ࡯ࡴࡶࠪᷱ")] = str(parsed_url.hostname)
            if parsed_url and parsed_url.port: proxy_settings[bstack1lllll1_opy_ (u"ࠨࡲࡵࡳࡽࡿࡐࡰࡴࡷࠫᷲ")] = str(parsed_url.port)
            if parsed_url and parsed_url.username: proxy_settings[bstack1lllll1_opy_ (u"ࠩࡳࡶࡴࡾࡹࡖࡵࡨࡶࠬᷳ")] = str(parsed_url.username)
            if parsed_url and parsed_url.password: proxy_settings[bstack1lllll1_opy_ (u"ࠪࡴࡷࡵࡸࡺࡒࡤࡷࡸ࠭ᷴ")] = str(parsed_url.password)
        return proxy_settings
    except:
        return proxy_settings
def bstack11ll1ll11l_opy_(bstack1111l1ll1l1_opy_):
    bstack111l111l1l1_opy_ = {
        bstack11l11lll11l_opy_[bstack111l11lllll_opy_]: bstack1111l1ll1l1_opy_[bstack111l11lllll_opy_]
        for bstack111l11lllll_opy_ in bstack1111l1ll1l1_opy_
        if bstack111l11lllll_opy_ in bstack11l11lll11l_opy_
    }
    bstack111l111l1l1_opy_[bstack1lllll1_opy_ (u"ࠦࡵࡸ࡯ࡹࡻࡖࡩࡹࡺࡩ࡯ࡩࡶࠦ᷵")] = bstack1111llll1ll_opy_(bstack1111l1ll1l1_opy_, bstack11l1111l_opy_.get_property(bstack1lllll1_opy_ (u"ࠧࡶࡲࡰࡺࡼࡗࡪࡺࡴࡪࡰࡪࡷࠧ᷶")))
    bstack111l11l11l1_opy_ = [element.lower() for element in bstack11l1l111lll_opy_]
    bstack1111ll111l1_opy_(bstack111l111l1l1_opy_, bstack111l11l11l1_opy_)
    return bstack111l111l1l1_opy_
def bstack1111ll111l1_opy_(d, keys):
    for key in list(d.keys()):
        if key.lower() in keys:
            d[key] = bstack1lllll1_opy_ (u"ࠨ᷷ࠪࠫࠬ࠭ࠦ")
    for value in d.values():
        if isinstance(value, dict):
            bstack1111ll111l1_opy_(value, keys)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    bstack1111ll111l1_opy_(item, keys)
def bstack1ll1111l1ll_opy_():
    bstack111l11ll1ll_opy_ = [os.environ.get(bstack1lllll1_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡆࡊࡎࡈࡗࡤࡊࡉࡓࠤ᷸")), os.path.join(os.path.expanduser(bstack1lllll1_opy_ (u"ࠣࢀ᷹ࠥ")), bstack1lllll1_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬᷺ࠩ")), os.path.join(bstack1lllll1_opy_ (u"ࠪ࠳ࡹࡳࡰࠨ᷻"), bstack1lllll1_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫ᷼"))]
    for path in bstack111l11ll1ll_opy_:
        if path is None:
            continue
        try:
            if os.path.exists(path):
                logger.debug(bstack1lllll1_opy_ (u"ࠧࡌࡩ࡭ࡧ᷽ࠣࠫࠧ") + str(path) + bstack1lllll1_opy_ (u"ࠨࠧࠡࡧࡻ࡭ࡸࡺࡳ࠯ࠤ᷾"))
                if not os.access(path, os.W_OK):
                    logger.debug(bstack1lllll1_opy_ (u"ࠢࡈ࡫ࡹ࡭ࡳ࡭ࠠࡱࡧࡵࡱ࡮ࡹࡳࡪࡱࡱࡷࠥ࡬࡯ࡳ᷿ࠢࠪࠦ") + str(path) + bstack1lllll1_opy_ (u"ࠣࠩࠥḀ"))
                    os.chmod(path, 0o777)
                else:
                    logger.debug(bstack1lllll1_opy_ (u"ࠤࡉ࡭ࡱ࡫ࠠࠨࠤḁ") + str(path) + bstack1lllll1_opy_ (u"ࠥࠫࠥࡧ࡬ࡳࡧࡤࡨࡾࠦࡨࡢࡵࠣࡸ࡭࡫ࠠࡳࡧࡴࡹ࡮ࡸࡥࡥࠢࡳࡩࡷࡳࡩࡴࡵ࡬ࡳࡳࡹ࠮ࠣḂ"))
            else:
                logger.debug(bstack1lllll1_opy_ (u"ࠦࡈࡸࡥࡢࡶ࡬ࡲ࡬ࠦࡦࡪ࡮ࡨࠤࠬࠨḃ") + str(path) + bstack1lllll1_opy_ (u"ࠧ࠭ࠠࡸ࡫ࡷ࡬ࠥࡽࡲࡪࡶࡨࠤࡵ࡫ࡲ࡮࡫ࡶࡷ࡮ࡵ࡮࠯ࠤḄ"))
                os.makedirs(path, exist_ok=True)
                os.chmod(path, 0o777)
            logger.debug(bstack1lllll1_opy_ (u"ࠨࡏࡱࡧࡵࡥࡹ࡯࡯࡯ࠢࡶࡹࡨࡩࡥࡦࡦࡨࡨࠥ࡬࡯ࡳࠢࠪࠦḅ") + str(path) + bstack1lllll1_opy_ (u"ࠢࠨ࠰ࠥḆ"))
            return path
        except Exception as e:
            logger.debug(bstack1lllll1_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡸ࡫ࡴࠡࡷࡳࠤ࡫࡯࡬ࡦࠢࠪࡿࡵࡧࡴࡩࡿࠪ࠾ࠥࠨḇ") + str(e) + bstack1lllll1_opy_ (u"ࠤࠥḈ"))
    logger.debug(bstack1lllll1_opy_ (u"ࠥࡅࡱࡲࠠࡱࡣࡷ࡬ࡸࠦࡦࡢ࡫࡯ࡩࡩ࠴ࠢḉ"))
    return None
@measure(event_name=EVENTS.bstack11l1l11llll_opy_, stage=STAGE.bstack11l1l111l1_opy_)
def bstack1l11lll1l1l_opy_(binary_path, bstack1l1l1l11lll_opy_, bs_config):
    logger.debug(bstack1lllll1_opy_ (u"ࠦࡈࡻࡲࡳࡧࡱࡸࠥࡉࡌࡊࠢࡓࡥࡹ࡮ࠠࡧࡱࡸࡲࡩࡀࠠࡼࡿࠥḊ").format(binary_path))
    bstack1111ll11l11_opy_ = bstack1lllll1_opy_ (u"ࠬ࠭ḋ")
    bstack111l1lll111_opy_ = {
        bstack1lllll1_opy_ (u"࠭ࡳࡥ࡭ࡢࡺࡪࡸࡳࡪࡱࡱࠫḌ"): __version__,
        bstack1lllll1_opy_ (u"ࠢࡰࡵࠥḍ"): platform.system(),
        bstack1lllll1_opy_ (u"ࠣࡱࡶࡣࡦࡸࡣࡩࠤḎ"): platform.machine(),
        bstack1lllll1_opy_ (u"ࠤࡦࡰ࡮ࡥࡶࡦࡴࡶ࡭ࡴࡴࠢḏ"): bstack1lllll1_opy_ (u"ࠪ࠴ࠬḐ"),
        bstack1lllll1_opy_ (u"ࠦࡸࡪ࡫ࡠ࡮ࡤࡲ࡬ࡻࡡࡨࡧࠥḑ"): bstack1lllll1_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲࠬḒ")
    }
    bstack111l11ll111_opy_(bstack111l1lll111_opy_)
    try:
        if binary_path:
            bstack111l1lll111_opy_[bstack1lllll1_opy_ (u"࠭ࡣ࡭࡫ࡢࡺࡪࡸࡳࡪࡱࡱࠫḓ")] = subprocess.check_output([binary_path, bstack1lllll1_opy_ (u"ࠢࡷࡧࡵࡷ࡮ࡵ࡮ࠣḔ")]).strip().decode(bstack1lllll1_opy_ (u"ࠨࡷࡷࡪ࠲࠾ࠧḕ"))
        response = requests.request(
            bstack1lllll1_opy_ (u"ࠩࡊࡉ࡙࠭Ḗ"),
            url=bstack1lll1ll11l_opy_(bstack11l1l111111_opy_),
            headers=None,
            auth=(bs_config[bstack1lllll1_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬḗ")], bs_config[bstack1lllll1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧḘ")]),
            json=None,
            params=bstack111l1lll111_opy_
        )
        data = response.json()
        if response.status_code == 200 and bstack1lllll1_opy_ (u"ࠬࡻࡲ࡭ࠩḙ") in data.keys() and bstack1lllll1_opy_ (u"࠭ࡵࡱࡦࡤࡸࡪࡪ࡟ࡤ࡮࡬ࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬḚ") in data.keys():
            logger.debug(bstack1lllll1_opy_ (u"ࠢࡏࡧࡨࡨࠥࡺ࡯ࠡࡷࡳࡨࡦࡺࡥࠡࡤ࡬ࡲࡦࡸࡹ࠭ࠢࡦࡹࡷࡸࡥ࡯ࡶࠣࡦ࡮ࡴࡡࡳࡻࠣࡺࡪࡸࡳࡪࡱࡱ࠾ࠥࢁࡽࠣḛ").format(bstack111l1lll111_opy_[bstack1lllll1_opy_ (u"ࠨࡥ࡯࡭ࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭Ḝ")]))
            if bstack1lllll1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡄࡌࡒࡆࡘ࡙ࡠࡗࡕࡐࠬḝ") in os.environ:
                logger.debug(bstack1lllll1_opy_ (u"ࠥࡗࡰ࡯ࡰࡱ࡫ࡱ࡫ࠥࡨࡩ࡯ࡣࡵࡽࠥࡪ࡯ࡸࡰ࡯ࡳࡦࡪࠠࡢࡵࠣࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡅࡍࡓࡇࡒ࡚ࡡࡘࡖࡑࠦࡩࡴࠢࡶࡩࡹࠨḞ"))
                data[bstack1lllll1_opy_ (u"ࠫࡺࡸ࡬ࠨḟ")] = os.environ[bstack1lllll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡇࡏࡎࡂࡔ࡜ࡣ࡚ࡘࡌࠨḠ")]
            bstack1111llllll1_opy_ = bstack111l1l11lll_opy_(data[bstack1lllll1_opy_ (u"࠭ࡵࡳ࡮ࠪḡ")], bstack1l1l1l11lll_opy_)
            bstack1111ll11l11_opy_ = os.path.join(bstack1l1l1l11lll_opy_, bstack1111llllll1_opy_)
            os.chmod(bstack1111ll11l11_opy_, 0o777) # bstack111l1ll1ll1_opy_ permission
            return bstack1111ll11l11_opy_
    except Exception as e:
        logger.debug(bstack1lllll1_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡷࡩ࡫࡯ࡩࠥࡪ࡯ࡸࡰ࡯ࡳࡦࡪࡩ࡯ࡩࠣࡲࡪࡽࠠࡔࡆࡎࠤࢀࢃࠢḢ").format(e))
    return binary_path
def bstack111l11ll111_opy_(bstack111l1lll111_opy_):
    try:
        if bstack1lllll1_opy_ (u"ࠨ࡮࡬ࡲࡺࡾࠧḣ") not in bstack111l1lll111_opy_[bstack1lllll1_opy_ (u"ࠩࡲࡷࠬḤ")].lower():
            return
        if os.path.exists(bstack1lllll1_opy_ (u"ࠥ࠳ࡪࡺࡣ࠰ࡱࡶ࠱ࡷ࡫࡬ࡦࡣࡶࡩࠧḥ")):
            with open(bstack1lllll1_opy_ (u"ࠦ࠴࡫ࡴࡤ࠱ࡲࡷ࠲ࡸࡥ࡭ࡧࡤࡷࡪࠨḦ"), bstack1lllll1_opy_ (u"ࠧࡸࠢḧ")) as f:
                bstack111l111ll1l_opy_ = {}
                for line in f:
                    if bstack1lllll1_opy_ (u"ࠨ࠽ࠣḨ") in line:
                        key, value = line.rstrip().split(bstack1lllll1_opy_ (u"ࠢ࠾ࠤḩ"), 1)
                        bstack111l111ll1l_opy_[key] = value.strip(bstack1lllll1_opy_ (u"ࠨࠤ࡟ࠫࠬḪ"))
                bstack111l1lll111_opy_[bstack1lllll1_opy_ (u"ࠩࡧ࡭ࡸࡺࡲࡰࠩḫ")] = bstack111l111ll1l_opy_.get(bstack1lllll1_opy_ (u"ࠥࡍࡉࠨḬ"), bstack1lllll1_opy_ (u"ࠦࠧḭ"))
        elif os.path.exists(bstack1lllll1_opy_ (u"ࠧ࠵ࡥࡵࡥ࠲ࡥࡱࡶࡩ࡯ࡧ࠰ࡶࡪࡲࡥࡢࡵࡨࠦḮ")):
            bstack111l1lll111_opy_[bstack1lllll1_opy_ (u"࠭ࡤࡪࡵࡷࡶࡴ࠭ḯ")] = bstack1lllll1_opy_ (u"ࠧࡢ࡮ࡳ࡭ࡳ࡫ࠧḰ")
    except Exception as e:
        logger.debug(bstack1lllll1_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤ࡬࡫ࡴࠡࡦ࡬ࡷࡹࡸ࡯ࠡࡱࡩࠤࡱ࡯࡮ࡶࡺࠥḱ") + e)
@measure(event_name=EVENTS.bstack11l11llllll_opy_, stage=STAGE.bstack11l1l111l1_opy_)
def bstack111l1l11lll_opy_(bstack111l1l11ll1_opy_, bstack111l11l1lll_opy_):
    logger.debug(bstack1lllll1_opy_ (u"ࠤࡇࡳࡼࡴ࡬ࡰࡣࡧ࡭ࡳ࡭ࠠࡔࡆࡎࠤࡧ࡯࡮ࡢࡴࡼࠤ࡫ࡸ࡯࡮࠼ࠣࠦḲ") + str(bstack111l1l11ll1_opy_) + bstack1lllll1_opy_ (u"ࠥࠦḳ"))
    zip_path = os.path.join(bstack111l11l1lll_opy_, bstack1lllll1_opy_ (u"ࠦࡩࡵࡷ࡯࡮ࡲࡥࡩ࡫ࡤࡠࡨ࡬ࡰࡪ࠴ࡺࡪࡲࠥḴ"))
    bstack1111llllll1_opy_ = bstack1lllll1_opy_ (u"ࠬ࠭ḵ")
    with requests.get(bstack111l1l11ll1_opy_, stream=True) as response:
        response.raise_for_status()
        with open(zip_path, bstack1lllll1_opy_ (u"ࠨࡷࡣࠤḶ")) as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
        logger.debug(bstack1lllll1_opy_ (u"ࠢࡇ࡫࡯ࡩࠥࡪ࡯ࡸࡰ࡯ࡳࡦࡪࡥࡥࠢࡶࡹࡨࡩࡥࡴࡵࡩࡹࡱࡲࡹ࠯ࠤḷ"))
    with zipfile.ZipFile(zip_path, bstack1lllll1_opy_ (u"ࠨࡴࠪḸ")) as zip_ref:
        bstack111l11l1111_opy_ = zip_ref.namelist()
        if len(bstack111l11l1111_opy_) > 0:
            bstack1111llllll1_opy_ = bstack111l11l1111_opy_[0] # bstack1111ll11l1l_opy_ bstack11l1l1ll1l1_opy_ will be bstack111l1lll1l1_opy_ 1 file i.e. the binary in the zip
        zip_ref.extractall(bstack111l11l1lll_opy_)
        logger.debug(bstack1lllll1_opy_ (u"ࠤࡉ࡭ࡱ࡫ࡳࠡࡵࡸࡧࡨ࡫ࡳࡴࡨࡸࡰࡱࡿࠠࡦࡺࡷࡶࡦࡩࡴࡦࡦࠣࡸࡴࠦࠧࠣḹ") + str(bstack111l11l1lll_opy_) + bstack1lllll1_opy_ (u"ࠥࠫࠧḺ"))
    os.remove(zip_path)
    return bstack1111llllll1_opy_
def get_cli_dir():
    bstack1111lll111l_opy_ = bstack1ll1111l1ll_opy_()
    if bstack1111lll111l_opy_:
        bstack1l1l1l11lll_opy_ = os.path.join(bstack1111lll111l_opy_, bstack1lllll1_opy_ (u"ࠦࡨࡲࡩࠣḻ"))
        if not os.path.exists(bstack1l1l1l11lll_opy_):
            os.makedirs(bstack1l1l1l11lll_opy_, mode=0o777, exist_ok=True)
        return bstack1l1l1l11lll_opy_
    else:
        raise FileNotFoundError(bstack1lllll1_opy_ (u"ࠧࡔ࡯ࠡࡹࡵ࡭ࡹࡧࡢ࡭ࡧࠣࡨ࡮ࡸࡥࡤࡶࡲࡶࡾࠦࡡࡷࡣ࡬ࡰࡦࡨ࡬ࡦࠢࡩࡳࡷࠦࡴࡩࡧࠣࡗࡉࡑࠠࡣ࡫ࡱࡥࡷࡿ࠮ࠣḼ"))
def bstack1l1l111l1ll_opy_(bstack1l1l1l11lll_opy_):
    bstack1lllll1_opy_ (u"ࠨࠢࠣࡉࡨࡸࠥࡺࡨࡦࠢࡳࡥࡹ࡮ࠠࡧࡱࡵࠤࡹ࡮ࡥࠡࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠠࡔࡆࡎࠤࡧ࡯࡮ࡢࡴࡼࠤ࡮ࡴࠠࡢࠢࡺࡶ࡮ࡺࡡࡣ࡮ࡨࠤࡩ࡯ࡲࡦࡥࡷࡳࡷࡿ࠮ࠣࠤࠥḽ")
    bstack111ll111111_opy_ = [
        os.path.join(bstack1l1l1l11lll_opy_, f)
        for f in os.listdir(bstack1l1l1l11lll_opy_)
        if os.path.isfile(os.path.join(bstack1l1l1l11lll_opy_, f)) and f.startswith(bstack1lllll1_opy_ (u"ࠢࡣ࡫ࡱࡥࡷࡿ࠭ࠣḾ"))
    ]
    if len(bstack111ll111111_opy_) > 0:
        return max(bstack111ll111111_opy_, key=os.path.getmtime) # get bstack111l1lll11l_opy_ binary
    return bstack1lllll1_opy_ (u"ࠣࠤḿ")
def bstack1111l1ll11l_opy_():
  from selenium import webdriver
  return version.parse(webdriver.__version__)
def bstack1l1111ll1l1_opy_(d, u):
  for k, v in u.items():
    if isinstance(v, collections.abc.Mapping):
      d[k] = bstack1l1111ll1l1_opy_(d.get(k, {}), v)
    else:
      if isinstance(v, list):
        d[k] = d.get(k, []) + v
      else:
        d[k] = v
  return d
def bstack1l111ll111_opy_(data, keys, default=None):
    bstack1lllll1_opy_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࡖࡥ࡫࡫࡬ࡺࠢࡪࡩࡹࠦࡡࠡࡰࡨࡷࡹ࡫ࡤࠡࡸࡤࡰࡺ࡫ࠠࡧࡴࡲࡱࠥࡧࠠࡥ࡫ࡦࡸ࡮ࡵ࡮ࡢࡴࡼࠤࡴࡸࠠ࡭࡫ࡶࡸ࠳ࠐࠠࠡࠢࠣ࠾ࡵࡧࡲࡢ࡯ࠣࡨࡦࡺࡡ࠻ࠢࡗ࡬ࡪࠦࡤࡪࡥࡷ࡭ࡴࡴࡡࡳࡻࠣࡳࡷࠦ࡬ࡪࡵࡷࠤࡹࡵࠠࡵࡴࡤࡺࡪࡸࡳࡦ࠰ࠍࠤࠥࠦࠠ࠻ࡲࡤࡶࡦࡳࠠ࡬ࡧࡼࡷ࠿ࠦࡁࠡ࡮࡬ࡷࡹࠦ࡯ࡧࠢ࡮ࡩࡾࡹ࠯ࡪࡰࡧ࡭ࡨ࡫ࡳࠡࡴࡨࡴࡷ࡫ࡳࡦࡰࡷ࡭ࡳ࡭ࠠࡵࡪࡨࠤࡵࡧࡴࡩ࠰ࠍࠤࠥࠦࠠ࠻ࡲࡤࡶࡦࡳࠠࡥࡧࡩࡥࡺࡲࡴ࠻࡙ࠢࡥࡱࡻࡥࠡࡶࡲࠤࡷ࡫ࡴࡶࡴࡱࠤ࡮࡬ࠠࡵࡪࡨࠤࡵࡧࡴࡩࠢࡧࡳࡪࡹࠠ࡯ࡱࡷࠤࡪࡾࡩࡴࡶ࠱ࠎࠥࠦࠠࠡ࠼ࡵࡩࡹࡻࡲ࡯࠼ࠣࡘ࡭࡫ࠠࡷࡣ࡯ࡹࡪࠦࡡࡵࠢࡷ࡬ࡪࠦ࡮ࡦࡵࡷࡩࡩࠦࡰࡢࡶ࡫࠰ࠥࡵࡲࠡࡦࡨࡪࡦࡻ࡬ࡵࠢ࡬ࡪࠥࡴ࡯ࡵࠢࡩࡳࡺࡴࡤ࠯ࠌࠣࠤࠥࠦࠢࠣࠤṀ")
    if not data:
        return default
    current = data
    try:
        for key in keys:
            if isinstance(current, dict):
                current = current[key]
            elif isinstance(current, list) and isinstance(key, int):
                current = current[key]
            else:
                return default
        return current
    except (KeyError, IndexError, TypeError):
        return default