# coding: UTF-8
import sys
bstack111ll1_opy_ = sys.version_info [0] == 2
bstack1l11l1_opy_ = 2048
bstack11111l_opy_ = 7
def bstack1ll1ll1_opy_ (bstack11lll1l_opy_):
    global bstack1ll11l1_opy_
    bstack1l1ll_opy_ = ord (bstack11lll1l_opy_ [-1])
    bstack1ll1l1l_opy_ = bstack11lll1l_opy_ [:-1]
    bstack1l1l1ll_opy_ = bstack1l1ll_opy_ % len (bstack1ll1l1l_opy_)
    bstack11ll1ll_opy_ = bstack1ll1l1l_opy_ [:bstack1l1l1ll_opy_] + bstack1ll1l1l_opy_ [bstack1l1l1ll_opy_:]
    if bstack111ll1_opy_:
        bstack111ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l11l1_opy_ - (bstack111111l_opy_ + bstack1l1ll_opy_) % bstack11111l_opy_) for bstack111111l_opy_, char in enumerate (bstack11ll1ll_opy_)])
    else:
        bstack111ll_opy_ = str () .join ([chr (ord (char) - bstack1l11l1_opy_ - (bstack111111l_opy_ + bstack1l1ll_opy_) % bstack11111l_opy_) for bstack111111l_opy_, char in enumerate (bstack11ll1ll_opy_)])
    return eval (bstack111ll_opy_)
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
from bstack_utils.constants import (bstack1ll1l1l11l_opy_, bstack111llll1l1_opy_, bstack1l11ll1ll1_opy_,
                                    bstack11l1l11l1ll_opy_, bstack11l11ll1lll_opy_, bstack11l1l11l11l_opy_, bstack11l1l1lll1l_opy_)
from bstack_utils.measure import measure
from bstack_utils.messages import bstack1l111l1ll_opy_, bstack1ll1111ll_opy_
from bstack_utils.proxy import bstack111ll1111l_opy_, bstack1ll1l1ll1_opy_
from bstack_utils.constants import *
from bstack_utils import bstack1l1l1ll111_opy_
from bstack_utils.bstack1l1l11ll1l_opy_ import bstack111l11l111_opy_
from browserstack_sdk._version import __version__
bstack11111l11_opy_ = Config.bstack1llllllll_opy_()
logger = bstack1l1l1ll111_opy_.get_logger(__name__, bstack1l1l1ll111_opy_.bstack1l1l1l1111l_opy_())
def bstack111l11l11ll_opy_(config):
    return config[bstack1ll1ll1_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧᯍ")]
def bstack1111l1ll1ll_opy_(config):
    return config[bstack1ll1ll1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩᯎ")]
def bstack11l11111l_opy_():
    try:
        import playwright
        return True
    except ImportError:
        return False
def bstack1111lllll11_opy_(obj):
    values = []
    bstack111ll111ll1_opy_ = re.compile(bstack1ll1ll1_opy_ (u"ࡲࠣࡠࡆ࡙ࡘ࡚ࡏࡎࡡࡗࡅࡌࡥ࡜ࡥ࠭ࠧࠦᯏ"), re.I)
    for key in obj.keys():
        if bstack111ll111ll1_opy_.match(key):
            values.append(obj[key])
    return values
def bstack111l1l1111l_opy_(config):
    tags = []
    tags.extend(bstack1111lllll11_opy_(os.environ))
    tags.extend(bstack1111lllll11_opy_(config))
    return tags
def bstack111l1ll1111_opy_(markers):
    tags = []
    for marker in markers:
        tags.append(marker.name)
    return tags
def bstack111l1ll111l_opy_(bstack1111ll11111_opy_):
    if not bstack1111ll11111_opy_:
        return bstack1ll1ll1_opy_ (u"ࠨࠩᯐ")
    return bstack1ll1ll1_opy_ (u"ࠤࡾࢁࠥ࠮ࡻࡾࠫࠥᯑ").format(bstack1111ll11111_opy_.name, bstack1111ll11111_opy_.email)
def bstack111l111ll1l_opy_():
    try:
        repo = git.Repo(search_parent_directories=True)
        bstack1111l1l11l1_opy_ = repo.common_dir
        info = {
            bstack1ll1ll1_opy_ (u"ࠥࡷ࡭ࡧࠢᯒ"): repo.head.commit.hexsha,
            bstack1ll1ll1_opy_ (u"ࠦࡸ࡮࡯ࡳࡶࡢࡷ࡭ࡧࠢᯓ"): repo.git.rev_parse(repo.head.commit, short=True),
            bstack1ll1ll1_opy_ (u"ࠧࡨࡲࡢࡰࡦ࡬ࠧᯔ"): repo.active_branch.name,
            bstack1ll1ll1_opy_ (u"ࠨࡴࡢࡩࠥᯕ"): repo.git.describe(all=True, tags=True, exact_match=True),
            bstack1ll1ll1_opy_ (u"ࠢࡤࡱࡰࡱ࡮ࡺࡴࡦࡴࠥᯖ"): bstack111l1ll111l_opy_(repo.head.commit.committer),
            bstack1ll1ll1_opy_ (u"ࠣࡥࡲࡱࡲ࡯ࡴࡵࡧࡵࡣࡩࡧࡴࡦࠤᯗ"): repo.head.commit.committed_datetime.isoformat(),
            bstack1ll1ll1_opy_ (u"ࠤࡤࡹࡹ࡮࡯ࡳࠤᯘ"): bstack111l1ll111l_opy_(repo.head.commit.author),
            bstack1ll1ll1_opy_ (u"ࠥࡥࡺࡺࡨࡰࡴࡢࡨࡦࡺࡥࠣᯙ"): repo.head.commit.authored_datetime.isoformat(),
            bstack1ll1ll1_opy_ (u"ࠦࡨࡵ࡭࡮࡫ࡷࡣࡲ࡫ࡳࡴࡣࡪࡩࠧᯚ"): repo.head.commit.message,
            bstack1ll1ll1_opy_ (u"ࠧࡸ࡯ࡰࡶࠥᯛ"): repo.git.rev_parse(bstack1ll1ll1_opy_ (u"ࠨ࠭࠮ࡵ࡫ࡳࡼ࠳ࡴࡰࡲ࡯ࡩࡻ࡫࡬ࠣᯜ")),
            bstack1ll1ll1_opy_ (u"ࠢࡤࡱࡰࡱࡴࡴ࡟ࡨ࡫ࡷࡣࡩ࡯ࡲࠣᯝ"): bstack1111l1l11l1_opy_,
            bstack1ll1ll1_opy_ (u"ࠣࡹࡲࡶࡰࡺࡲࡦࡧࡢ࡫࡮ࡺ࡟ࡥ࡫ࡵࠦᯞ"): subprocess.check_output([bstack1ll1ll1_opy_ (u"ࠤࡪ࡭ࡹࠨᯟ"), bstack1ll1ll1_opy_ (u"ࠥࡶࡪࡼ࠭ࡱࡣࡵࡷࡪࠨᯠ"), bstack1ll1ll1_opy_ (u"ࠦ࠲࠳ࡧࡪࡶ࠰ࡧࡴࡳ࡭ࡰࡰ࠰ࡨ࡮ࡸࠢᯡ")]).strip().decode(
                bstack1ll1ll1_opy_ (u"ࠬࡻࡴࡧ࠯࠻ࠫᯢ")),
            bstack1ll1ll1_opy_ (u"ࠨ࡬ࡢࡵࡷࡣࡹࡧࡧࠣᯣ"): repo.git.describe(tags=True, abbrev=0, always=True),
            bstack1ll1ll1_opy_ (u"ࠢࡤࡱࡰࡱ࡮ࡺࡳࡠࡵ࡬ࡲࡨ࡫࡟࡭ࡣࡶࡸࡤࡺࡡࡨࠤᯤ"): repo.git.rev_list(
                bstack1ll1ll1_opy_ (u"ࠣࡽࢀ࠲࠳ࢁࡽࠣᯥ").format(repo.head.commit, repo.git.describe(tags=True, abbrev=0, always=True)), count=True)
        }
        remotes = repo.remotes
        bstack111l11l11l1_opy_ = []
        for remote in remotes:
            bstack111l1lll1l1_opy_ = {
                bstack1ll1ll1_opy_ (u"ࠤࡱࡥࡲ࡫᯦ࠢ"): remote.name,
                bstack1ll1ll1_opy_ (u"ࠥࡹࡷࡲࠢᯧ"): remote.url,
            }
            bstack111l11l11l1_opy_.append(bstack111l1lll1l1_opy_)
        bstack1111lll11l1_opy_ = {
            bstack1ll1ll1_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᯨ"): bstack1ll1ll1_opy_ (u"ࠧ࡭ࡩࡵࠤᯩ"),
            **info,
            bstack1ll1ll1_opy_ (u"ࠨࡲࡦ࡯ࡲࡸࡪࡹࠢᯪ"): bstack111l11l11l1_opy_
        }
        bstack1111lll11l1_opy_ = bstack111l11l1l11_opy_(bstack1111lll11l1_opy_)
        return bstack1111lll11l1_opy_
    except git.InvalidGitRepositoryError:
        return {}
    except Exception as err:
        print(bstack1ll1ll1_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡰࡰࡲࡸࡰࡦࡺࡩ࡯ࡩࠣࡋ࡮ࡺࠠ࡮ࡧࡷࡥࡩࡧࡴࡢࠢࡺ࡭ࡹ࡮ࠠࡦࡴࡵࡳࡷࡀࠠࡼࡿࠥᯫ").format(err))
        return {}
def bstack11lll11lll1_opy_(bstack1111lll11ll_opy_=None):
    bstack1ll1ll1_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࡉࡨࡸࠥ࡭ࡩࡵࠢࡰࡩࡹࡧࡤࡢࡶࡤࠤࡸࡶࡥࡤ࡫ࡩ࡭ࡨࡧ࡬࡭ࡻࠣࡪࡴࡸ࡭ࡢࡶࡷࡩࡩࠦࡦࡰࡴࠣࡅࡎࠦࡳࡦ࡮ࡨࡧࡹ࡯࡯࡯ࠢࡸࡷࡪࠦࡣࡢࡵࡨࡷࠥ࡬࡯ࡳࠢࡨࡥࡨ࡮ࠠࡧࡱ࡯ࡨࡪࡸࠠࡪࡰࠣࡸ࡭࡫ࠠ࡭࡫ࡶࡸ࠳ࠐࠠࠡࠢࠣࡅࡷ࡭ࡳ࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࡪࡴࡲࡤࡦࡴࡶࠤ࠭ࡲࡩࡴࡶ࠯ࠤࡴࡶࡴࡪࡱࡱࡥࡱ࠯࠺ࠡࡎ࡬ࡷࡹࠦ࡯ࡧࠢࡩࡳࡱࡪࡥࡳࠢࡳࡥࡹ࡮ࡳࠡࡶࡲࠤࡪࡾࡴࡳࡣࡦࡸࠥ࡭ࡩࡵࠢࡰࡩࡹࡧࡤࡢࡶࡤࠤ࡫ࡸ࡯࡮࠰ࠣࡈࡪ࡬ࡡࡶ࡮ࡷࡷࠥࡺ࡯ࠡ࡝ࡲࡷ࠳࡭ࡥࡵࡥࡺࡨ࠭࠯࡝࠯ࠌࠣࠤࠥࠦࡒࡦࡶࡸࡶࡳࡹ࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢ࡯࡭ࡸࡺ࠺ࠡࡎ࡬ࡷࡹࠦ࡯ࡧࠢࡧ࡭ࡨࡺࡳ࠭ࠢࡨࡥࡨ࡮ࠠࡤࡱࡱࡸࡦ࡯࡮ࡪࡰࡪࠤ࡬࡯ࡴࠡ࡯ࡨࡸࡦࡪࡡࡵࡣࠣࡪࡴࡸࠠࡢࠢࡩࡳࡱࡪࡥࡳ࠰ࠍࠤࠥࠦࠠࠣࠤࠥᯬ")
    if bstack1111lll11ll_opy_ == None: # bstack111l1l111ll_opy_ for bstack11ll1ll1lll_opy_-repo
        bstack1111lll11ll_opy_ = [os.getcwd()]
    results = []
    for folder in bstack1111lll11ll_opy_:
        try:
            repo = git.Repo(folder, search_parent_directories=True)
            result = {
                bstack1ll1ll1_opy_ (u"ࠤࡳࡶࡎࡪࠢᯭ"): bstack1ll1ll1_opy_ (u"ࠥࠦᯮ"),
                bstack1ll1ll1_opy_ (u"ࠦ࡫࡯࡬ࡦࡵࡆ࡬ࡦࡴࡧࡦࡦࠥᯯ"): [],
                bstack1ll1ll1_opy_ (u"ࠧࡧࡵࡵࡪࡲࡶࡸࠨᯰ"): [],
                bstack1ll1ll1_opy_ (u"ࠨࡰࡳࡆࡤࡸࡪࠨᯱ"): bstack1ll1ll1_opy_ (u"᯲ࠢࠣ"),
                bstack1ll1ll1_opy_ (u"ࠣࡥࡲࡱࡲ࡯ࡴࡎࡧࡶࡷࡦ࡭ࡥࡴࠤ᯳"): [],
                bstack1ll1ll1_opy_ (u"ࠤࡳࡶ࡙࡯ࡴ࡭ࡧࠥ᯴"): bstack1ll1ll1_opy_ (u"ࠥࠦ᯵"),
                bstack1ll1ll1_opy_ (u"ࠦࡵࡸࡄࡦࡵࡦࡶ࡮ࡶࡴࡪࡱࡱࠦ᯶"): bstack1ll1ll1_opy_ (u"ࠧࠨ᯷"),
                bstack1ll1ll1_opy_ (u"ࠨࡰࡳࡔࡤࡻࡉ࡯ࡦࡧࠤ᯸"): bstack1ll1ll1_opy_ (u"ࠢࠣ᯹")
            }
            bstack1111llll1ll_opy_ = repo.active_branch.name
            bstack111l1ll1l1l_opy_ = repo.head.commit
            result[bstack1ll1ll1_opy_ (u"ࠣࡲࡵࡍࡩࠨ᯺")] = bstack111l1ll1l1l_opy_.hexsha
            bstack1111ll1llll_opy_ = _111l1l1llll_opy_(repo)
            logger.debug(bstack1ll1ll1_opy_ (u"ࠤࡅࡥࡸ࡫ࠠࡣࡴࡤࡲࡨ࡮ࠠࡧࡱࡵࠤࡨࡵ࡭ࡱࡣࡵ࡭ࡸࡵ࡮࠻ࠢࠥ᯻") + str(bstack1111ll1llll_opy_) + bstack1ll1ll1_opy_ (u"ࠥࠦ᯼"))
            if bstack1111ll1llll_opy_:
                try:
                    bstack1111ll1lll1_opy_ = repo.git.diff(bstack1ll1ll1_opy_ (u"ࠦ࠲࠳࡮ࡢ࡯ࡨ࠱ࡴࡴ࡬ࡺࠤ᯽"), bstack1lll1ll111l_opy_ (u"ࠧࢁࡢࡢࡵࡨࡣࡧࡸࡡ࡯ࡥ࡫ࢁ࠳࠴࠮ࡼࡥࡸࡶࡷ࡫࡮ࡵࡡࡥࡶࡦࡴࡣࡩࡿࠥ᯾")).split(bstack1ll1ll1_opy_ (u"࠭࡜࡯ࠩ᯿"))
                    logger.debug(bstack1ll1ll1_opy_ (u"ࠢࡄࡪࡤࡲ࡬࡫ࡤࠡࡨ࡬ࡰࡪࡹࠠࡣࡧࡷࡻࡪ࡫࡮ࠡࡽࡥࡥࡸ࡫࡟ࡣࡴࡤࡲࡨ࡮ࡽࠡࡣࡱࡨࠥࢁࡣࡶࡴࡵࡩࡳࡺ࡟ࡣࡴࡤࡲࡨ࡮ࡽ࠻ࠢࠥᰀ") + str(bstack1111ll1lll1_opy_) + bstack1ll1ll1_opy_ (u"ࠣࠤᰁ"))
                    result[bstack1ll1ll1_opy_ (u"ࠤࡩ࡭ࡱ࡫ࡳࡄࡪࡤࡲ࡬࡫ࡤࠣᰂ")] = [f.strip() for f in bstack1111ll1lll1_opy_ if f.strip()]
                    commits = list(repo.iter_commits(bstack1lll1ll111l_opy_ (u"ࠥࡿࡧࡧࡳࡦࡡࡥࡶࡦࡴࡣࡩࡿ࠱࠲ࢀࡩࡵࡳࡴࡨࡲࡹࡥࡢࡳࡣࡱࡧ࡭ࢃࠢᰃ")))
                except Exception:
                    logger.debug(bstack1ll1ll1_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡨࡧࡷࠤࡨ࡮ࡡ࡯ࡩࡨࡨࠥ࡬ࡩ࡭ࡧࡶࠤ࡫ࡸ࡯࡮ࠢࡥࡶࡦࡴࡣࡩࠢࡦࡳࡲࡶࡡࡳ࡫ࡶࡳࡳ࠴ࠠࡇࡣ࡯ࡰ࡮ࡴࡧࠡࡤࡤࡧࡰࠦࡴࡰࠢࡵࡩࡨ࡫࡮ࡵࠢࡦࡳࡲࡳࡩࡵࡵ࠱ࠦᰄ"))
                    commits = list(repo.iter_commits(max_count=10))
                    if commits:
                        result[bstack1ll1ll1_opy_ (u"ࠧ࡬ࡩ࡭ࡧࡶࡇ࡭ࡧ࡮ࡨࡧࡧࠦᰅ")] = _111l11ll1ll_opy_(commits[:5])
            else:
                commits = list(repo.iter_commits(max_count=10))
                if commits:
                    result[bstack1ll1ll1_opy_ (u"ࠨࡦࡪ࡮ࡨࡷࡈ࡮ࡡ࡯ࡩࡨࡨࠧᰆ")] = _111l11ll1ll_opy_(commits[:5])
            bstack1111l1ll1l1_opy_ = set()
            bstack111l1l1ll11_opy_ = []
            for commit in commits:
                logger.debug(bstack1ll1ll1_opy_ (u"ࠢࡑࡴࡲࡧࡪࡹࡳࡪࡰࡪࠤࡨࡵ࡭࡮࡫ࡷ࠾ࠥࠨᰇ") + str(commit.message) + bstack1ll1ll1_opy_ (u"ࠣࠤᰈ"))
                bstack111l1111l1l_opy_ = commit.author.name if commit.author else bstack1ll1ll1_opy_ (u"ࠤࡘࡲࡰࡴ࡯ࡸࡰࠥᰉ")
                bstack1111l1ll1l1_opy_.add(bstack111l1111l1l_opy_)
                bstack111l1l1ll11_opy_.append({
                    bstack1ll1ll1_opy_ (u"ࠥࡱࡪࡹࡳࡢࡩࡨࠦᰊ"): commit.message.strip(),
                    bstack1ll1ll1_opy_ (u"ࠦࡺࡹࡥࡳࠤᰋ"): bstack111l1111l1l_opy_
                })
            result[bstack1ll1ll1_opy_ (u"ࠧࡧࡵࡵࡪࡲࡶࡸࠨᰌ")] = list(bstack1111l1ll1l1_opy_)
            result[bstack1ll1ll1_opy_ (u"ࠨࡣࡰ࡯ࡰ࡭ࡹࡓࡥࡴࡵࡤ࡫ࡪࡹࠢᰍ")] = bstack111l1l1ll11_opy_
            result[bstack1ll1ll1_opy_ (u"ࠢࡱࡴࡇࡥࡹ࡫ࠢᰎ")] = bstack111l1ll1l1l_opy_.committed_datetime.strftime(bstack1ll1ll1_opy_ (u"ࠣࠧ࡜࠱ࠪࡳ࠭ࠦࡦࠥᰏ"))
            if (not result[bstack1ll1ll1_opy_ (u"ࠤࡳࡶ࡙࡯ࡴ࡭ࡧࠥᰐ")] or result[bstack1ll1ll1_opy_ (u"ࠥࡴࡷ࡚ࡩࡵ࡮ࡨࠦᰑ")].strip() == bstack1ll1ll1_opy_ (u"ࠦࠧᰒ")) and bstack111l1ll1l1l_opy_.message:
                bstack111ll111l1l_opy_ = bstack111l1ll1l1l_opy_.message.strip().splitlines()
                result[bstack1ll1ll1_opy_ (u"ࠧࡶࡲࡕ࡫ࡷࡰࡪࠨᰓ")] = bstack111ll111l1l_opy_[0] if bstack111ll111l1l_opy_ else bstack1ll1ll1_opy_ (u"ࠨࠢᰔ")
                if len(bstack111ll111l1l_opy_) > 2:
                    result[bstack1ll1ll1_opy_ (u"ࠢࡱࡴࡇࡩࡸࡩࡲࡪࡲࡷ࡭ࡴࡴࠢᰕ")] = bstack1ll1ll1_opy_ (u"ࠨ࡞ࡱࠫᰖ").join(bstack111ll111l1l_opy_[2:]).strip()
            results.append(result)
        except Exception as err:
            logger.info(bstack1ll1ll1_opy_ (u"ࠤ࡞࡫ࡪࡺ࡟ࡨ࡫ࡷࡣࡲ࡫ࡴࡢࡦࡤࡸࡦࡥࡦࡰࡴࡢࡥ࡮ࡥࡳࡦ࡮ࡨࡧࡹ࡯࡯࡯࡟ࠣࡇࡺࡸࡲࡦࡰࡷࠤࡕ࡝ࡄ࠻ࠢࡾࢁࠧᰗ").format(os.getcwd()))
            logger.error(bstack1ll1ll1_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡳࡳࡵࡻ࡬ࡢࡶ࡬ࡲ࡬ࠦࡇࡪࡶࠣࡱࡪࡺࡡࡥࡣࡷࡥࠥ࡬࡯ࡳࠢࡄࡍࠥࡹࡥ࡭ࡧࡦࡸ࡮ࡵ࡮ࠡࠪࡩࡳࡱࡪࡥࡳ࠼ࠣࡿࢂ࠯࠺ࠡࡽࢀࠦᰘ").format(folder, str(err)))
    filtered_results = [
        result
        for result in results
        if _1111l1l11ll_opy_(result)
    ]
    return filtered_results
def _1111l1l11ll_opy_(result):
    bstack1ll1ll1_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࡍ࡫࡬ࡱࡧࡵࠤࡹࡵࠠࡤࡪࡨࡧࡰࠦࡩࡧࠢࡤࠤ࡬࡯ࡴࠡ࡯ࡨࡸࡦࡪࡡࡵࡣࠣࡶࡪࡹࡵ࡭ࡶࠣ࡭ࡸࠦࡶࡢ࡮࡬ࡨࠥ࠮࡮ࡰࡰ࠰ࡩࡲࡶࡴࡺࠢࡩ࡭ࡱ࡫ࡳࡄࡪࡤࡲ࡬࡫ࡤࠡࡣࡱࡨࠥࡧࡵࡵࡪࡲࡶࡸ࠯࠮ࠋࠢࠣࠤࠥࠨࠢࠣᰙ")
    return (
        isinstance(result.get(bstack1ll1ll1_opy_ (u"ࠧ࡬ࡩ࡭ࡧࡶࡇ࡭ࡧ࡮ࡨࡧࡧࠦᰚ"), None), list)
        and len(result[bstack1ll1ll1_opy_ (u"ࠨࡦࡪ࡮ࡨࡷࡈ࡮ࡡ࡯ࡩࡨࡨࠧᰛ")]) > 0
        and isinstance(result.get(bstack1ll1ll1_opy_ (u"ࠢࡢࡷࡷ࡬ࡴࡸࡳࠣᰜ"), None), list)
        and len(result[bstack1ll1ll1_opy_ (u"ࠣࡣࡸࡸ࡭ࡵࡲࡴࠤᰝ")]) > 0
    )
def _111l1l1llll_opy_(repo):
    bstack1ll1ll1_opy_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࡗࡶࡾࠦࡴࡰࠢࡧࡩࡹ࡫ࡲ࡮࡫ࡱࡩࠥࡺࡨࡦࠢࡥࡥࡸ࡫ࠠࡣࡴࡤࡲࡨ࡮ࠠࡧࡱࡵࠤࡹ࡮ࡥࠡࡩ࡬ࡺࡪࡴࠠࡳࡧࡳࡳࠥࡽࡩࡵࡪࡲࡹࡹࠦࡨࡢࡴࡧࡧࡴࡪࡥࡥࠢࡱࡥࡲ࡫ࡳࠡࡣࡱࡨࠥࡽ࡯ࡳ࡭ࠣࡻ࡮ࡺࡨࠡࡣ࡯ࡰࠥ࡜ࡃࡔࠢࡳࡶࡴࡼࡩࡥࡧࡵࡷ࠳ࠐࠠࠡࠢࠣࡖࡪࡺࡵࡳࡰࡶࠤࡹ࡮ࡥࠡࡦࡨࡪࡦࡻ࡬ࡵࠢࡥࡶࡦࡴࡣࡩࠢ࡬ࡪࠥࡶ࡯ࡴࡵ࡬ࡦࡱ࡫ࠬࠡࡧ࡯ࡷࡪࠦࡎࡰࡰࡨ࠲ࠏࠦࠠࠡࠢࠥࠦࠧᰞ")
    try:
        try:
            origin = repo.remotes.origin
            bstack1111llll1l1_opy_ = origin.refs[bstack1ll1ll1_opy_ (u"ࠪࡌࡊࡇࡄࠨᰟ")]
            target = bstack1111llll1l1_opy_.reference.name
            if target.startswith(bstack1ll1ll1_opy_ (u"ࠫࡴࡸࡩࡨ࡫ࡱ࠳ࠬᰠ")):
                return target
        except Exception:
            pass
        if repo.remotes and repo.remotes.origin.refs:
            for ref in repo.remotes.origin.refs:
                if ref.name.startswith(bstack1ll1ll1_opy_ (u"ࠬࡵࡲࡪࡩ࡬ࡲ࠴࠭ᰡ")):
                    return ref.name
        if repo.heads:
            return repo.heads[0].name
    except Exception:
        pass
    return None
def _111l11ll1ll_opy_(commits):
    bstack1ll1ll1_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࡇࡦࡶࠣࡰ࡮ࡹࡴࠡࡱࡩࠤࡨ࡮ࡡ࡯ࡩࡨࡨࠥ࡬ࡩ࡭ࡧࡶࠤ࡫ࡸ࡯࡮ࠢࡤࠤࡱ࡯ࡳࡵࠢࡲࡪࠥࡩ࡯࡮࡯࡬ࡸࡸ࠴ࠊࠡࠢࠣࠤࠧࠨࠢᰢ")
    bstack1111ll1lll1_opy_ = set()
    try:
        for commit in commits:
            if commit.parents:
                for parent in commit.parents:
                    diff = commit.diff(parent)
                    for bstack1111ll1l11l_opy_ in diff:
                        if bstack1111ll1l11l_opy_.a_path:
                            bstack1111ll1lll1_opy_.add(bstack1111ll1l11l_opy_.a_path)
                        if bstack1111ll1l11l_opy_.b_path:
                            bstack1111ll1lll1_opy_.add(bstack1111ll1l11l_opy_.b_path)
    except Exception:
        pass
    return list(bstack1111ll1lll1_opy_)
def bstack111l11l1l11_opy_(bstack1111lll11l1_opy_):
    bstack111l11111l1_opy_ = bstack111l1ll1l11_opy_(bstack1111lll11l1_opy_)
    if bstack111l11111l1_opy_ and bstack111l11111l1_opy_ > bstack11l1l11l1ll_opy_:
        bstack111l11l1ll1_opy_ = bstack111l11111l1_opy_ - bstack11l1l11l1ll_opy_
        bstack1111ll111l1_opy_ = bstack111l111l1l1_opy_(bstack1111lll11l1_opy_[bstack1ll1ll1_opy_ (u"ࠢࡤࡱࡰࡱ࡮ࡺ࡟࡮ࡧࡶࡷࡦ࡭ࡥࠣᰣ")], bstack111l11l1ll1_opy_)
        bstack1111lll11l1_opy_[bstack1ll1ll1_opy_ (u"ࠣࡥࡲࡱࡲ࡯ࡴࡠ࡯ࡨࡷࡸࡧࡧࡦࠤᰤ")] = bstack1111ll111l1_opy_
        logger.info(bstack1ll1ll1_opy_ (u"ࠤࡗ࡬ࡪࠦࡣࡰ࡯ࡰ࡭ࡹࠦࡨࡢࡵࠣࡦࡪ࡫࡮ࠡࡶࡵࡹࡳࡩࡡࡵࡧࡧ࠲࡙ࠥࡩࡻࡧࠣࡳ࡫ࠦࡣࡰ࡯ࡰ࡭ࡹࠦࡡࡧࡶࡨࡶࠥࡺࡲࡶࡰࡦࡥࡹ࡯࡯࡯ࠢ࡬ࡷࠥࢁࡽࠡࡍࡅࠦᰥ")
                    .format(bstack111l1ll1l11_opy_(bstack1111lll11l1_opy_) / 1024))
    return bstack1111lll11l1_opy_
def bstack111l1ll1l11_opy_(json_data):
    try:
        if json_data:
            bstack111ll1111ll_opy_ = json.dumps(json_data)
            bstack1111lllll1l_opy_ = sys.getsizeof(bstack111ll1111ll_opy_)
            return bstack1111lllll1l_opy_
    except Exception as e:
        logger.debug(bstack1ll1ll1_opy_ (u"ࠥࡗࡴࡳࡥࡵࡪ࡬ࡲ࡬ࠦࡷࡦࡰࡷࠤࡼࡸ࡯࡯ࡩࠣࡻ࡭࡯࡬ࡦࠢࡦࡥࡱࡩࡵ࡭ࡣࡷ࡭ࡳ࡭ࠠࡴ࡫ࡽࡩࠥࡵࡦࠡࡌࡖࡓࡓࠦ࡯ࡣ࡬ࡨࡧࡹࡀࠠࡼࡿࠥᰦ").format(e))
    return -1
def bstack111l111l1l1_opy_(field, bstack111l1ll1lll_opy_):
    try:
        bstack111l1111ll1_opy_ = len(bytes(bstack11l11ll1lll_opy_, bstack1ll1ll1_opy_ (u"ࠫࡺࡺࡦ࠮࠺ࠪᰧ")))
        bstack1111l1ll111_opy_ = bytes(field, bstack1ll1ll1_opy_ (u"ࠬࡻࡴࡧ࠯࠻ࠫᰨ"))
        bstack111l1ll1ll1_opy_ = len(bstack1111l1ll111_opy_)
        bstack111l1llll1l_opy_ = ceil(bstack111l1ll1ll1_opy_ - bstack111l1ll1lll_opy_ - bstack111l1111ll1_opy_)
        if bstack111l1llll1l_opy_ > 0:
            bstack111l11ll111_opy_ = bstack1111l1ll111_opy_[:bstack111l1llll1l_opy_].decode(bstack1ll1ll1_opy_ (u"࠭ࡵࡵࡨ࠰࠼ࠬᰩ"), errors=bstack1ll1ll1_opy_ (u"ࠧࡪࡩࡱࡳࡷ࡫ࠧᰪ")) + bstack11l11ll1lll_opy_
            return bstack111l11ll111_opy_
    except Exception as e:
        logger.debug(bstack1ll1ll1_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡸࡪ࡬ࡰࡪࠦࡴࡳࡷࡱࡧࡦࡺࡩ࡯ࡩࠣࡪ࡮࡫࡬ࡥ࠮ࠣࡲࡴࡺࡨࡪࡰࡪࠤࡼࡧࡳࠡࡶࡵࡹࡳࡩࡡࡵࡧࡧࠤ࡭࡫ࡲࡦ࠼ࠣࡿࢂࠨᰫ").format(e))
    return field
def bstack1l1l111l11_opy_():
    env = os.environ
    if (bstack1ll1ll1_opy_ (u"ࠤࡍࡉࡓࡑࡉࡏࡕࡢ࡙ࡗࡒࠢᰬ") in env and len(env[bstack1ll1ll1_opy_ (u"ࠥࡎࡊࡔࡋࡊࡐࡖࡣ࡚ࡘࡌࠣᰭ")]) > 0) or (
            bstack1ll1ll1_opy_ (u"ࠦࡏࡋࡎࡌࡋࡑࡗࡤࡎࡏࡎࡇࠥᰮ") in env and len(env[bstack1ll1ll1_opy_ (u"ࠧࡐࡅࡏࡍࡌࡒࡘࡥࡈࡐࡏࡈࠦᰯ")]) > 0):
        return {
            bstack1ll1ll1_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᰰ"): bstack1ll1ll1_opy_ (u"ࠢࡋࡧࡱ࡯࡮ࡴࡳࠣᰱ"),
            bstack1ll1ll1_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᰲ"): env.get(bstack1ll1ll1_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡠࡗࡕࡐࠧᰳ")),
            bstack1ll1ll1_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᰴ"): env.get(bstack1ll1ll1_opy_ (u"ࠦࡏࡕࡂࡠࡐࡄࡑࡊࠨᰵ")),
            bstack1ll1ll1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᰶ"): env.get(bstack1ll1ll1_opy_ (u"ࠨࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖ᰷ࠧ"))
        }
    if env.get(bstack1ll1ll1_opy_ (u"ࠢࡄࡋࠥ᰸")) == bstack1ll1ll1_opy_ (u"ࠣࡶࡵࡹࡪࠨ᰹") and bstack1ll1l1llll_opy_(env.get(bstack1ll1ll1_opy_ (u"ࠤࡆࡍࡗࡉࡌࡆࡅࡌࠦ᰺"))):
        return {
            bstack1ll1ll1_opy_ (u"ࠥࡲࡦࡳࡥࠣ᰻"): bstack1ll1ll1_opy_ (u"ࠦࡈ࡯ࡲࡤ࡮ࡨࡇࡎࠨ᰼"),
            bstack1ll1ll1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣ᰽"): env.get(bstack1ll1ll1_opy_ (u"ࠨࡃࡊࡔࡆࡐࡊࡥࡂࡖࡋࡏࡈࡤ࡛ࡒࡍࠤ᰾")),
            bstack1ll1ll1_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤ᰿"): env.get(bstack1ll1ll1_opy_ (u"ࠣࡅࡌࡖࡈࡒࡅࡠࡌࡒࡆࠧ᱀")),
            bstack1ll1ll1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣ᱁"): env.get(bstack1ll1ll1_opy_ (u"ࠥࡇࡎࡘࡃࡍࡇࡢࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࠨ᱂"))
        }
    if env.get(bstack1ll1ll1_opy_ (u"ࠦࡈࡏࠢ᱃")) == bstack1ll1ll1_opy_ (u"ࠧࡺࡲࡶࡧࠥ᱄") and bstack1ll1l1llll_opy_(env.get(bstack1ll1ll1_opy_ (u"ࠨࡔࡓࡃ࡙ࡍࡘࠨ᱅"))):
        return {
            bstack1ll1ll1_opy_ (u"ࠢ࡯ࡣࡰࡩࠧ᱆"): bstack1ll1ll1_opy_ (u"ࠣࡖࡵࡥࡻ࡯ࡳࠡࡅࡌࠦ᱇"),
            bstack1ll1ll1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧ᱈"): env.get(bstack1ll1ll1_opy_ (u"ࠥࡘࡗࡇࡖࡊࡕࡢࡆ࡚ࡏࡌࡅࡡ࡚ࡉࡇࡥࡕࡓࡎࠥ᱉")),
            bstack1ll1ll1_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨ᱊"): env.get(bstack1ll1ll1_opy_ (u"࡚ࠧࡒࡂࡘࡌࡗࡤࡐࡏࡃࡡࡑࡅࡒࡋࠢ᱋")),
            bstack1ll1ll1_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧ᱌"): env.get(bstack1ll1ll1_opy_ (u"ࠢࡕࡔࡄ࡚ࡎ࡙࡟ࡃࡗࡌࡐࡉࡥࡎࡖࡏࡅࡉࡗࠨᱍ"))
        }
    if env.get(bstack1ll1ll1_opy_ (u"ࠣࡅࡌࠦᱎ")) == bstack1ll1ll1_opy_ (u"ࠤࡷࡶࡺ࡫ࠢᱏ") and env.get(bstack1ll1ll1_opy_ (u"ࠥࡇࡎࡥࡎࡂࡏࡈࠦ᱐")) == bstack1ll1ll1_opy_ (u"ࠦࡨࡵࡤࡦࡵ࡫࡭ࡵࠨ᱑"):
        return {
            bstack1ll1ll1_opy_ (u"ࠧࡴࡡ࡮ࡧࠥ᱒"): bstack1ll1ll1_opy_ (u"ࠨࡃࡰࡦࡨࡷ࡭࡯ࡰࠣ᱓"),
            bstack1ll1ll1_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥ᱔"): None,
            bstack1ll1ll1_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥ᱕"): None,
            bstack1ll1ll1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣ᱖"): None
        }
    if env.get(bstack1ll1ll1_opy_ (u"ࠥࡆࡎ࡚ࡂࡖࡅࡎࡉ࡙ࡥࡂࡓࡃࡑࡇࡍࠨ᱗")) and env.get(bstack1ll1ll1_opy_ (u"ࠦࡇࡏࡔࡃࡗࡆࡏࡊ࡚࡟ࡄࡑࡐࡑࡎ࡚ࠢ᱘")):
        return {
            bstack1ll1ll1_opy_ (u"ࠧࡴࡡ࡮ࡧࠥ᱙"): bstack1ll1ll1_opy_ (u"ࠨࡂࡪࡶࡥࡹࡨࡱࡥࡵࠤᱚ"),
            bstack1ll1ll1_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᱛ"): env.get(bstack1ll1ll1_opy_ (u"ࠣࡄࡌࡘࡇ࡛ࡃࡌࡇࡗࡣࡌࡏࡔࡠࡊࡗࡘࡕࡥࡏࡓࡋࡊࡍࡓࠨᱜ")),
            bstack1ll1ll1_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᱝ"): None,
            bstack1ll1ll1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤᱞ"): env.get(bstack1ll1ll1_opy_ (u"ࠦࡇࡏࡔࡃࡗࡆࡏࡊ࡚࡟ࡃࡗࡌࡐࡉࡥࡎࡖࡏࡅࡉࡗࠨᱟ"))
        }
    if env.get(bstack1ll1ll1_opy_ (u"ࠧࡉࡉࠣᱠ")) == bstack1ll1ll1_opy_ (u"ࠨࡴࡳࡷࡨࠦᱡ") and bstack1ll1l1llll_opy_(env.get(bstack1ll1ll1_opy_ (u"ࠢࡅࡔࡒࡒࡊࠨᱢ"))):
        return {
            bstack1ll1ll1_opy_ (u"ࠣࡰࡤࡱࡪࠨᱣ"): bstack1ll1ll1_opy_ (u"ࠤࡇࡶࡴࡴࡥࠣᱤ"),
            bstack1ll1ll1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᱥ"): env.get(bstack1ll1ll1_opy_ (u"ࠦࡉࡘࡏࡏࡇࡢࡆ࡚ࡏࡌࡅࡡࡏࡍࡓࡑࠢᱦ")),
            bstack1ll1ll1_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᱧ"): None,
            bstack1ll1ll1_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᱨ"): env.get(bstack1ll1ll1_opy_ (u"ࠢࡅࡔࡒࡒࡊࡥࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࠧᱩ"))
        }
    if env.get(bstack1ll1ll1_opy_ (u"ࠣࡅࡌࠦᱪ")) == bstack1ll1ll1_opy_ (u"ࠤࡷࡶࡺ࡫ࠢᱫ") and bstack1ll1l1llll_opy_(env.get(bstack1ll1ll1_opy_ (u"ࠥࡗࡊࡓࡁࡑࡊࡒࡖࡊࠨᱬ"))):
        return {
            bstack1ll1ll1_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᱭ"): bstack1ll1ll1_opy_ (u"࡙ࠧࡥ࡮ࡣࡳ࡬ࡴࡸࡥࠣᱮ"),
            bstack1ll1ll1_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᱯ"): env.get(bstack1ll1ll1_opy_ (u"ࠢࡔࡇࡐࡅࡕࡎࡏࡓࡇࡢࡓࡗࡍࡁࡏࡋ࡝ࡅ࡙ࡏࡏࡏࡡࡘࡖࡑࠨᱰ")),
            bstack1ll1ll1_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᱱ"): env.get(bstack1ll1ll1_opy_ (u"ࠤࡖࡉࡒࡇࡐࡉࡑࡕࡉࡤࡐࡏࡃࡡࡑࡅࡒࡋࠢᱲ")),
            bstack1ll1ll1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤᱳ"): env.get(bstack1ll1ll1_opy_ (u"ࠦࡘࡋࡍࡂࡒࡋࡓࡗࡋ࡟ࡋࡑࡅࡣࡎࡊࠢᱴ"))
        }
    if env.get(bstack1ll1ll1_opy_ (u"ࠧࡉࡉࠣᱵ")) == bstack1ll1ll1_opy_ (u"ࠨࡴࡳࡷࡨࠦᱶ") and bstack1ll1l1llll_opy_(env.get(bstack1ll1ll1_opy_ (u"ࠢࡈࡋࡗࡐࡆࡈ࡟ࡄࡋࠥᱷ"))):
        return {
            bstack1ll1ll1_opy_ (u"ࠣࡰࡤࡱࡪࠨᱸ"): bstack1ll1ll1_opy_ (u"ࠤࡊ࡭ࡹࡒࡡࡣࠤᱹ"),
            bstack1ll1ll1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᱺ"): env.get(bstack1ll1ll1_opy_ (u"ࠦࡈࡏ࡟ࡋࡑࡅࡣ࡚ࡘࡌࠣᱻ")),
            bstack1ll1ll1_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᱼ"): env.get(bstack1ll1ll1_opy_ (u"ࠨࡃࡊࡡࡍࡓࡇࡥࡎࡂࡏࡈࠦᱽ")),
            bstack1ll1ll1_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨ᱾"): env.get(bstack1ll1ll1_opy_ (u"ࠣࡅࡌࡣࡏࡕࡂࡠࡋࡇࠦ᱿"))
        }
    if env.get(bstack1ll1ll1_opy_ (u"ࠤࡆࡍࠧᲀ")) == bstack1ll1ll1_opy_ (u"ࠥࡸࡷࡻࡥࠣᲁ") and bstack1ll1l1llll_opy_(env.get(bstack1ll1ll1_opy_ (u"ࠦࡇ࡛ࡉࡍࡆࡎࡍ࡙ࡋࠢᲂ"))):
        return {
            bstack1ll1ll1_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᲃ"): bstack1ll1ll1_opy_ (u"ࠨࡂࡶ࡫࡯ࡨࡰ࡯ࡴࡦࠤᲄ"),
            bstack1ll1ll1_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᲅ"): env.get(bstack1ll1ll1_opy_ (u"ࠣࡄࡘࡍࡑࡊࡋࡊࡖࡈࡣࡇ࡛ࡉࡍࡆࡢ࡙ࡗࡒࠢᲆ")),
            bstack1ll1ll1_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᲇ"): env.get(bstack1ll1ll1_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡍࡌࡘࡊࡥࡌࡂࡄࡈࡐࠧᲈ")) or env.get(bstack1ll1ll1_opy_ (u"ࠦࡇ࡛ࡉࡍࡆࡎࡍ࡙ࡋ࡟ࡑࡋࡓࡉࡑࡏࡎࡆࡡࡑࡅࡒࡋࠢᲉ")),
            bstack1ll1ll1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᲊ"): env.get(bstack1ll1ll1_opy_ (u"ࠨࡂࡖࡋࡏࡈࡐࡏࡔࡆࡡࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࡇࡋࡒࠣ᲋"))
        }
    if bstack1ll1l1llll_opy_(env.get(bstack1ll1ll1_opy_ (u"ࠢࡕࡈࡢࡆ࡚ࡏࡌࡅࠤ᲌"))):
        return {
            bstack1ll1ll1_opy_ (u"ࠣࡰࡤࡱࡪࠨ᲍"): bstack1ll1ll1_opy_ (u"ࠤ࡙࡭ࡸࡻࡡ࡭ࠢࡖࡸࡺࡪࡩࡰࠢࡗࡩࡦࡳࠠࡔࡧࡵࡺ࡮ࡩࡥࡴࠤ᲎"),
            bstack1ll1ll1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨ᲏"): bstack1ll1ll1_opy_ (u"ࠦࢀࢃࡻࡾࠤᲐ").format(env.get(bstack1ll1ll1_opy_ (u"࡙࡙ࠬࡔࡖࡈࡑࡤ࡚ࡅࡂࡏࡉࡓ࡚ࡔࡄࡂࡖࡌࡓࡓ࡙ࡅࡓࡘࡈࡖ࡚ࡘࡉࠨᲑ")), env.get(bstack1ll1ll1_opy_ (u"࠭ࡓ࡚ࡕࡗࡉࡒࡥࡔࡆࡃࡐࡔࡗࡕࡊࡆࡅࡗࡍࡉ࠭Გ"))),
            bstack1ll1ll1_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᲓ"): env.get(bstack1ll1ll1_opy_ (u"ࠣࡕ࡜ࡗ࡙ࡋࡍࡠࡆࡈࡊࡎࡔࡉࡕࡋࡒࡒࡎࡊࠢᲔ")),
            bstack1ll1ll1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᲕ"): env.get(bstack1ll1ll1_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡡࡅ࡙ࡎࡒࡄࡊࡆࠥᲖ"))
        }
    if bstack1ll1l1llll_opy_(env.get(bstack1ll1ll1_opy_ (u"ࠦࡆࡖࡐࡗࡇ࡜ࡓࡗࠨᲗ"))):
        return {
            bstack1ll1ll1_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᲘ"): bstack1ll1ll1_opy_ (u"ࠨࡁࡱࡲࡹࡩࡾࡵࡲࠣᲙ"),
            bstack1ll1ll1_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᲚ"): bstack1ll1ll1_opy_ (u"ࠣࡽࢀ࠳ࡵࡸ࡯࡫ࡧࡦࡸ࠴ࢁࡽ࠰ࡽࢀ࠳ࡧࡻࡩ࡭ࡦࡶ࠳ࢀࢃࠢᲛ").format(env.get(bstack1ll1ll1_opy_ (u"ࠩࡄࡔࡕ࡜ࡅ࡚ࡑࡕࡣ࡚ࡘࡌࠨᲜ")), env.get(bstack1ll1ll1_opy_ (u"ࠪࡅࡕࡖࡖࡆ࡛ࡒࡖࡤࡇࡃࡄࡑࡘࡒ࡙ࡥࡎࡂࡏࡈࠫᲝ")), env.get(bstack1ll1ll1_opy_ (u"ࠫࡆࡖࡐࡗࡇ࡜ࡓࡗࡥࡐࡓࡑࡍࡉࡈ࡚࡟ࡔࡎࡘࡋࠬᲞ")), env.get(bstack1ll1ll1_opy_ (u"ࠬࡇࡐࡑࡘࡈ࡝ࡔࡘ࡟ࡃࡗࡌࡐࡉࡥࡉࡅࠩᲟ"))),
            bstack1ll1ll1_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᲠ"): env.get(bstack1ll1ll1_opy_ (u"ࠢࡂࡒࡓ࡚ࡊ࡟ࡏࡓࡡࡍࡓࡇࡥࡎࡂࡏࡈࠦᲡ")),
            bstack1ll1ll1_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᲢ"): env.get(bstack1ll1ll1_opy_ (u"ࠤࡄࡔࡕ࡜ࡅ࡚ࡑࡕࡣࡇ࡛ࡉࡍࡆࡢࡒ࡚ࡓࡂࡆࡔࠥᲣ"))
        }
    if env.get(bstack1ll1ll1_opy_ (u"ࠥࡅ࡟࡛ࡒࡆࡡࡋࡘ࡙ࡖ࡟ࡖࡕࡈࡖࡤࡇࡇࡆࡐࡗࠦᲤ")) and env.get(bstack1ll1ll1_opy_ (u"࡙ࠦࡌ࡟ࡃࡗࡌࡐࡉࠨᲥ")):
        return {
            bstack1ll1ll1_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᲦ"): bstack1ll1ll1_opy_ (u"ࠨࡁࡻࡷࡵࡩࠥࡉࡉࠣᲧ"),
            bstack1ll1ll1_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᲨ"): bstack1ll1ll1_opy_ (u"ࠣࡽࢀࡿࢂ࠵࡟ࡣࡷ࡬ࡰࡩ࠵ࡲࡦࡵࡸࡰࡹࡹ࠿ࡣࡷ࡬ࡰࡩࡏࡤ࠾ࡽࢀࠦᲩ").format(env.get(bstack1ll1ll1_opy_ (u"ࠩࡖ࡝ࡘ࡚ࡅࡎࡡࡗࡉࡆࡓࡆࡐࡗࡑࡈࡆ࡚ࡉࡐࡐࡖࡉࡗ࡜ࡅࡓࡗࡕࡍࠬᲪ")), env.get(bstack1ll1ll1_opy_ (u"ࠪࡗ࡞࡙ࡔࡆࡏࡢࡘࡊࡇࡍࡑࡔࡒࡎࡊࡉࡔࠨᲫ")), env.get(bstack1ll1ll1_opy_ (u"ࠫࡇ࡛ࡉࡍࡆࡢࡆ࡚ࡏࡌࡅࡋࡇࠫᲬ"))),
            bstack1ll1ll1_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᲭ"): env.get(bstack1ll1ll1_opy_ (u"ࠨࡂࡖࡋࡏࡈࡤࡈࡕࡊࡎࡇࡍࡉࠨᲮ")),
            bstack1ll1ll1_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᲯ"): env.get(bstack1ll1ll1_opy_ (u"ࠣࡄࡘࡍࡑࡊ࡟ࡃࡗࡌࡐࡉࡏࡄࠣᲰ"))
        }
    if any([env.get(bstack1ll1ll1_opy_ (u"ࠤࡆࡓࡉࡋࡂࡖࡋࡏࡈࡤࡈࡕࡊࡎࡇࡣࡎࡊࠢᲱ")), env.get(bstack1ll1ll1_opy_ (u"ࠥࡇࡔࡊࡅࡃࡗࡌࡐࡉࡥࡒࡆࡕࡒࡐ࡛ࡋࡄࡠࡕࡒ࡙ࡗࡉࡅࡠࡘࡈࡖࡘࡏࡏࡏࠤᲲ")), env.get(bstack1ll1ll1_opy_ (u"ࠦࡈࡕࡄࡆࡄࡘࡍࡑࡊ࡟ࡔࡑࡘࡖࡈࡋ࡟ࡗࡇࡕࡗࡎࡕࡎࠣᲳ"))]):
        return {
            bstack1ll1ll1_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᲴ"): bstack1ll1ll1_opy_ (u"ࠨࡁࡘࡕࠣࡇࡴࡪࡥࡃࡷ࡬ࡰࡩࠨᲵ"),
            bstack1ll1ll1_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᲶ"): env.get(bstack1ll1ll1_opy_ (u"ࠣࡅࡒࡈࡊࡈࡕࡊࡎࡇࡣࡕ࡛ࡂࡍࡋࡆࡣࡇ࡛ࡉࡍࡆࡢ࡙ࡗࡒࠢᲷ")),
            bstack1ll1ll1_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᲸ"): env.get(bstack1ll1ll1_opy_ (u"ࠥࡇࡔࡊࡅࡃࡗࡌࡐࡉࡥࡂࡖࡋࡏࡈࡤࡏࡄࠣᲹ")),
            bstack1ll1ll1_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᲺ"): env.get(bstack1ll1ll1_opy_ (u"ࠧࡉࡏࡅࡇࡅ࡙ࡎࡒࡄࡠࡄࡘࡍࡑࡊ࡟ࡊࡆࠥ᲻"))
        }
    if env.get(bstack1ll1ll1_opy_ (u"ࠨࡢࡢ࡯ࡥࡳࡴࡥࡢࡶ࡫࡯ࡨࡓࡻ࡭ࡣࡧࡵࠦ᲼")):
        return {
            bstack1ll1ll1_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᲽ"): bstack1ll1ll1_opy_ (u"ࠣࡄࡤࡱࡧࡵ࡯ࠣᲾ"),
            bstack1ll1ll1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᲿ"): env.get(bstack1ll1ll1_opy_ (u"ࠥࡦࡦࡳࡢࡰࡱࡢࡦࡺ࡯࡬ࡥࡔࡨࡷࡺࡲࡴࡴࡗࡵࡰࠧ᳀")),
            bstack1ll1ll1_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨ᳁"): env.get(bstack1ll1ll1_opy_ (u"ࠧࡨࡡ࡮ࡤࡲࡳࡤࡹࡨࡰࡴࡷࡎࡴࡨࡎࡢ࡯ࡨࠦ᳂")),
            bstack1ll1ll1_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧ᳃"): env.get(bstack1ll1ll1_opy_ (u"ࠢࡣࡣࡰࡦࡴࡵ࡟ࡣࡷ࡬ࡰࡩࡔࡵ࡮ࡤࡨࡶࠧ᳄"))
        }
    if env.get(bstack1ll1ll1_opy_ (u"࡙ࠣࡈࡖࡈࡑࡅࡓࠤ᳅")) or env.get(bstack1ll1ll1_opy_ (u"ࠤ࡚ࡉࡗࡉࡋࡆࡔࡢࡑࡆࡏࡎࡠࡒࡌࡔࡊࡒࡉࡏࡇࡢࡗ࡙ࡇࡒࡕࡇࡇࠦ᳆")):
        return {
            bstack1ll1ll1_opy_ (u"ࠥࡲࡦࡳࡥࠣ᳇"): bstack1ll1ll1_opy_ (u"ࠦ࡜࡫ࡲࡤ࡭ࡨࡶࠧ᳈"),
            bstack1ll1ll1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣ᳉"): env.get(bstack1ll1ll1_opy_ (u"ࠨࡗࡆࡔࡆࡏࡊࡘ࡟ࡃࡗࡌࡐࡉࡥࡕࡓࡎࠥ᳊")),
            bstack1ll1ll1_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤ᳋"): bstack1ll1ll1_opy_ (u"ࠣࡏࡤ࡭ࡳࠦࡐࡪࡲࡨࡰ࡮ࡴࡥࠣ᳌") if env.get(bstack1ll1ll1_opy_ (u"ࠤ࡚ࡉࡗࡉࡋࡆࡔࡢࡑࡆࡏࡎࡠࡒࡌࡔࡊࡒࡉࡏࡇࡢࡗ࡙ࡇࡒࡕࡇࡇࠦ᳍")) else None,
            bstack1ll1ll1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤ᳎"): env.get(bstack1ll1ll1_opy_ (u"ࠦ࡜ࡋࡒࡄࡍࡈࡖࡤࡍࡉࡕࡡࡆࡓࡒࡓࡉࡕࠤ᳏"))
        }
    if any([env.get(bstack1ll1ll1_opy_ (u"ࠧࡍࡃࡑࡡࡓࡖࡔࡐࡅࡄࡖࠥ᳐")), env.get(bstack1ll1ll1_opy_ (u"ࠨࡇࡄࡎࡒ࡙ࡉࡥࡐࡓࡑࡍࡉࡈ࡚ࠢ᳑")), env.get(bstack1ll1ll1_opy_ (u"ࠢࡈࡑࡒࡋࡑࡋ࡟ࡄࡎࡒ࡙ࡉࡥࡐࡓࡑࡍࡉࡈ࡚ࠢ᳒"))]):
        return {
            bstack1ll1ll1_opy_ (u"ࠣࡰࡤࡱࡪࠨ᳓"): bstack1ll1ll1_opy_ (u"ࠤࡊࡳࡴ࡭࡬ࡦࠢࡆࡰࡴࡻࡤ᳔ࠣ"),
            bstack1ll1ll1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨ᳕"): None,
            bstack1ll1ll1_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨ᳖"): env.get(bstack1ll1ll1_opy_ (u"ࠧࡖࡒࡐࡌࡈࡇ࡙ࡥࡉࡅࠤ᳗")),
            bstack1ll1ll1_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶ᳘ࠧ"): env.get(bstack1ll1ll1_opy_ (u"ࠢࡃࡗࡌࡐࡉࡥࡉࡅࠤ᳙"))
        }
    if env.get(bstack1ll1ll1_opy_ (u"ࠣࡕࡋࡍࡕࡖࡁࡃࡎࡈࠦ᳚")):
        return {
            bstack1ll1ll1_opy_ (u"ࠤࡱࡥࡲ࡫ࠢ᳛"): bstack1ll1ll1_opy_ (u"ࠥࡗ࡭࡯ࡰࡱࡣࡥࡰࡪࠨ᳜"),
            bstack1ll1ll1_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲ᳝ࠢ"): env.get(bstack1ll1ll1_opy_ (u"࡙ࠧࡈࡊࡒࡓࡅࡇࡒࡅࡠࡄࡘࡍࡑࡊ࡟ࡖࡔࡏ᳞ࠦ")),
            bstack1ll1ll1_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥ᳟ࠣ"): bstack1ll1ll1_opy_ (u"ࠢࡋࡱࡥࠤࠨࢁࡽࠣ᳠").format(env.get(bstack1ll1ll1_opy_ (u"ࠨࡕࡋࡍࡕࡖࡁࡃࡎࡈࡣࡏࡕࡂࡠࡋࡇࠫ᳡"))) if env.get(bstack1ll1ll1_opy_ (u"ࠤࡖࡌࡎࡖࡐࡂࡄࡏࡉࡤࡐࡏࡃࡡࡌࡈ᳢ࠧ")) else None,
            bstack1ll1ll1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤ᳣"): env.get(bstack1ll1ll1_opy_ (u"ࠦࡘࡎࡉࡑࡒࡄࡆࡑࡋ࡟ࡃࡗࡌࡐࡉࡥࡎࡖࡏࡅࡉࡗࠨ᳤"))
        }
    if bstack1ll1l1llll_opy_(env.get(bstack1ll1ll1_opy_ (u"ࠧࡔࡅࡕࡎࡌࡊ࡞ࠨ᳥"))):
        return {
            bstack1ll1ll1_opy_ (u"ࠨ࡮ࡢ࡯ࡨ᳦ࠦ"): bstack1ll1ll1_opy_ (u"ࠢࡏࡧࡷࡰ࡮࡬ࡹ᳧ࠣ"),
            bstack1ll1ll1_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯᳨ࠦ"): env.get(bstack1ll1ll1_opy_ (u"ࠤࡇࡉࡕࡒࡏ࡚ࡡࡘࡖࡑࠨᳩ")),
            bstack1ll1ll1_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᳪ"): env.get(bstack1ll1ll1_opy_ (u"ࠦࡘࡏࡔࡆࡡࡑࡅࡒࡋࠢᳫ")),
            bstack1ll1ll1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᳬ"): env.get(bstack1ll1ll1_opy_ (u"ࠨࡂࡖࡋࡏࡈࡤࡏࡄ᳭ࠣ"))
        }
    if bstack1ll1l1llll_opy_(env.get(bstack1ll1ll1_opy_ (u"ࠢࡈࡋࡗࡌ࡚ࡈ࡟ࡂࡅࡗࡍࡔࡔࡓࠣᳮ"))):
        return {
            bstack1ll1ll1_opy_ (u"ࠣࡰࡤࡱࡪࠨᳯ"): bstack1ll1ll1_opy_ (u"ࠤࡊ࡭ࡹࡎࡵࡣࠢࡄࡧࡹ࡯࡯࡯ࡵࠥᳰ"),
            bstack1ll1ll1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᳱ"): bstack1ll1ll1_opy_ (u"ࠦࢀࢃ࠯ࡼࡿ࠲ࡥࡨࡺࡩࡰࡰࡶ࠳ࡷࡻ࡮ࡴ࠱ࡾࢁࠧᳲ").format(env.get(bstack1ll1ll1_opy_ (u"ࠬࡍࡉࡕࡊࡘࡆࡤ࡙ࡅࡓࡘࡈࡖࡤ࡛ࡒࡍࠩᳳ")), env.get(bstack1ll1ll1_opy_ (u"࠭ࡇࡊࡖࡋ࡙ࡇࡥࡒࡆࡒࡒࡗࡎ࡚ࡏࡓ࡛ࠪ᳴")), env.get(bstack1ll1ll1_opy_ (u"ࠧࡈࡋࡗࡌ࡚ࡈ࡟ࡓࡗࡑࡣࡎࡊࠧᳵ"))),
            bstack1ll1ll1_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᳶ"): env.get(bstack1ll1ll1_opy_ (u"ࠤࡊࡍ࡙ࡎࡕࡃࡡ࡚ࡓࡗࡑࡆࡍࡑ࡚ࠦ᳷")),
            bstack1ll1ll1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤ᳸"): env.get(bstack1ll1ll1_opy_ (u"ࠦࡌࡏࡔࡉࡗࡅࡣࡗ࡛ࡎࡠࡋࡇࠦ᳹"))
        }
    if env.get(bstack1ll1ll1_opy_ (u"ࠧࡉࡉࠣᳺ")) == bstack1ll1ll1_opy_ (u"ࠨࡴࡳࡷࡨࠦ᳻") and env.get(bstack1ll1ll1_opy_ (u"ࠢࡗࡇࡕࡇࡊࡒࠢ᳼")) == bstack1ll1ll1_opy_ (u"ࠣ࠳ࠥ᳽"):
        return {
            bstack1ll1ll1_opy_ (u"ࠤࡱࡥࡲ࡫ࠢ᳾"): bstack1ll1ll1_opy_ (u"࡚ࠥࡪࡸࡣࡦ࡮ࠥ᳿"),
            bstack1ll1ll1_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᴀ"): bstack1ll1ll1_opy_ (u"ࠧ࡮ࡴࡵࡲ࠽࠳࠴ࢁࡽࠣᴁ").format(env.get(bstack1ll1ll1_opy_ (u"࠭ࡖࡆࡔࡆࡉࡑࡥࡕࡓࡎࠪᴂ"))),
            bstack1ll1ll1_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᴃ"): None,
            bstack1ll1ll1_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᴄ"): None,
        }
    if env.get(bstack1ll1ll1_opy_ (u"ࠤࡗࡉࡆࡓࡃࡊࡖ࡜ࡣ࡛ࡋࡒࡔࡋࡒࡒࠧᴅ")):
        return {
            bstack1ll1ll1_opy_ (u"ࠥࡲࡦࡳࡥࠣᴆ"): bstack1ll1ll1_opy_ (u"࡙ࠦ࡫ࡡ࡮ࡥ࡬ࡸࡾࠨᴇ"),
            bstack1ll1ll1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣᴈ"): None,
            bstack1ll1ll1_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᴉ"): env.get(bstack1ll1ll1_opy_ (u"ࠢࡕࡇࡄࡑࡈࡏࡔ࡚ࡡࡓࡖࡔࡐࡅࡄࡖࡢࡒࡆࡓࡅࠣᴊ")),
            bstack1ll1ll1_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᴋ"): env.get(bstack1ll1ll1_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࡇࡋࡒࠣᴌ"))
        }
    if any([env.get(bstack1ll1ll1_opy_ (u"ࠥࡇࡔࡔࡃࡐࡗࡕࡗࡊࠨᴍ")), env.get(bstack1ll1ll1_opy_ (u"ࠦࡈࡕࡎࡄࡑࡘࡖࡘࡋ࡟ࡖࡔࡏࠦᴎ")), env.get(bstack1ll1ll1_opy_ (u"ࠧࡉࡏࡏࡅࡒ࡙ࡗ࡙ࡅࡠࡗࡖࡉࡗࡔࡁࡎࡇࠥᴏ")), env.get(bstack1ll1ll1_opy_ (u"ࠨࡃࡐࡐࡆࡓ࡚ࡘࡓࡆࡡࡗࡉࡆࡓࠢᴐ"))]):
        return {
            bstack1ll1ll1_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᴑ"): bstack1ll1ll1_opy_ (u"ࠣࡅࡲࡲࡨࡵࡵࡳࡵࡨࠦᴒ"),
            bstack1ll1ll1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᴓ"): None,
            bstack1ll1ll1_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᴔ"): env.get(bstack1ll1ll1_opy_ (u"ࠦࡇ࡛ࡉࡍࡆࡢࡎࡔࡈ࡟ࡏࡃࡐࡉࠧᴕ")) or None,
            bstack1ll1ll1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᴖ"): env.get(bstack1ll1ll1_opy_ (u"ࠨࡂࡖࡋࡏࡈࡤࡏࡄࠣᴗ"), 0)
        }
    if env.get(bstack1ll1ll1_opy_ (u"ࠢࡈࡑࡢࡎࡔࡈ࡟ࡏࡃࡐࡉࠧᴘ")):
        return {
            bstack1ll1ll1_opy_ (u"ࠣࡰࡤࡱࡪࠨᴙ"): bstack1ll1ll1_opy_ (u"ࠤࡊࡳࡈࡊࠢᴚ"),
            bstack1ll1ll1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᴛ"): None,
            bstack1ll1ll1_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᴜ"): env.get(bstack1ll1ll1_opy_ (u"ࠧࡍࡏࡠࡌࡒࡆࡤࡔࡁࡎࡇࠥᴝ")),
            bstack1ll1ll1_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᴞ"): env.get(bstack1ll1ll1_opy_ (u"ࠢࡈࡑࡢࡔࡎࡖࡅࡍࡋࡑࡉࡤࡉࡏࡖࡐࡗࡉࡗࠨᴟ"))
        }
    if env.get(bstack1ll1ll1_opy_ (u"ࠣࡅࡉࡣࡇ࡛ࡉࡍࡆࡢࡍࡉࠨᴠ")):
        return {
            bstack1ll1ll1_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᴡ"): bstack1ll1ll1_opy_ (u"ࠥࡇࡴࡪࡥࡇࡴࡨࡷ࡭ࠨᴢ"),
            bstack1ll1ll1_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᴣ"): env.get(bstack1ll1ll1_opy_ (u"ࠧࡉࡆࡠࡄࡘࡍࡑࡊ࡟ࡖࡔࡏࠦᴤ")),
            bstack1ll1ll1_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᴥ"): env.get(bstack1ll1ll1_opy_ (u"ࠢࡄࡈࡢࡔࡎࡖࡅࡍࡋࡑࡉࡤࡔࡁࡎࡇࠥᴦ")),
            bstack1ll1ll1_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᴧ"): env.get(bstack1ll1ll1_opy_ (u"ࠤࡆࡊࡤࡈࡕࡊࡎࡇࡣࡎࡊࠢᴨ"))
        }
    return {bstack1ll1ll1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤᴩ"): None}
def get_host_info():
    return {
        bstack1ll1ll1_opy_ (u"ࠦ࡭ࡵࡳࡵࡰࡤࡱࡪࠨᴪ"): platform.node(),
        bstack1ll1ll1_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳࠢᴫ"): platform.system(),
        bstack1ll1ll1_opy_ (u"ࠨࡴࡺࡲࡨࠦᴬ"): platform.machine(),
        bstack1ll1ll1_opy_ (u"ࠢࡷࡧࡵࡷ࡮ࡵ࡮ࠣᴭ"): platform.version(),
        bstack1ll1ll1_opy_ (u"ࠣࡣࡵࡧ࡭ࠨᴮ"): platform.architecture()[0]
    }
def bstack11lll11111_opy_():
    try:
        import selenium
        return True
    except ImportError:
        return False
def bstack111l1lllll1_opy_():
    if bstack11111l11_opy_.get_property(bstack1ll1ll1_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡡࡶࡩࡸࡹࡩࡰࡰࠪᴯ")):
        return bstack1ll1ll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩᴰ")
    return bstack1ll1ll1_opy_ (u"ࠫࡺࡴ࡫࡯ࡱࡺࡲࡤ࡭ࡲࡪࡦࠪᴱ")
def bstack111l1lll1ll_opy_(driver):
    info = {
        bstack1ll1ll1_opy_ (u"ࠬࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠫᴲ"): driver.capabilities,
        bstack1ll1ll1_opy_ (u"࠭ࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡪࡦࠪᴳ"): driver.session_id,
        bstack1ll1ll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࠨᴴ"): driver.capabilities.get(bstack1ll1ll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭ᴵ"), None),
        bstack1ll1ll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡢࡺࡪࡸࡳࡪࡱࡱࠫᴶ"): driver.capabilities.get(bstack1ll1ll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫᴷ"), None),
        bstack1ll1ll1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲ࠭ᴸ"): driver.capabilities.get(bstack1ll1ll1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡎࡢ࡯ࡨࠫᴹ"), None),
        bstack1ll1ll1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡠࡸࡨࡶࡸ࡯࡯࡯ࠩᴺ"):driver.capabilities.get(bstack1ll1ll1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡘࡨࡶࡸ࡯࡯࡯ࠩᴻ"), None),
    }
    if bstack111l1lllll1_opy_() == bstack1ll1ll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧᴼ"):
        if bstack11l1ll1111_opy_():
            info[bstack1ll1ll1_opy_ (u"ࠩࡳࡶࡴࡪࡵࡤࡶࠪᴽ")] = bstack1ll1ll1_opy_ (u"ࠪࡥࡵࡶ࠭ࡢࡷࡷࡳࡲࡧࡴࡦࠩᴾ")
        elif driver.capabilities.get(bstack1ll1ll1_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬᴿ"), {}).get(bstack1ll1ll1_opy_ (u"ࠬࡺࡵࡳࡤࡲࡷࡨࡧ࡬ࡦࠩᵀ"), False):
            info[bstack1ll1ll1_opy_ (u"࠭ࡰࡳࡱࡧࡹࡨࡺࠧᵁ")] = bstack1ll1ll1_opy_ (u"ࠧࡵࡷࡵࡦࡴࡹࡣࡢ࡮ࡨࠫᵂ")
        else:
            info[bstack1ll1ll1_opy_ (u"ࠨࡲࡵࡳࡩࡻࡣࡵࠩᵃ")] = bstack1ll1ll1_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶࡨࠫᵄ")
    return info
def bstack11l1ll1111_opy_():
    if bstack11111l11_opy_.get_property(bstack1ll1ll1_opy_ (u"ࠪࡥࡵࡶ࡟ࡢࡷࡷࡳࡲࡧࡴࡦࠩᵅ")):
        return True
    if bstack1ll1l1llll_opy_(os.environ.get(bstack1ll1ll1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡍࡘࡥࡁࡑࡒࡢࡅ࡚࡚ࡏࡎࡃࡗࡉࠬᵆ"), None)):
        return True
    return False
def bstack111l1l11l1_opy_(bstack111l11l1l1l_opy_, url, data, config):
    headers = config.get(bstack1ll1ll1_opy_ (u"ࠬ࡮ࡥࡢࡦࡨࡶࡸ࠭ᵇ"), None)
    proxies = bstack111ll1111l_opy_(config, url)
    auth = config.get(bstack1ll1ll1_opy_ (u"࠭ࡡࡶࡶ࡫ࠫᵈ"), None)
    response = requests.request(
            bstack111l11l1l1l_opy_,
            url=url,
            headers=headers,
            auth=auth,
            json=data,
            proxies=proxies
        )
    return response
def bstack1lll1l1l1l_opy_(bstack111l11lll_opy_, size):
    bstack11l1ll1l1l_opy_ = []
    while len(bstack111l11lll_opy_) > size:
        bstack11l1l11111_opy_ = bstack111l11lll_opy_[:size]
        bstack11l1ll1l1l_opy_.append(bstack11l1l11111_opy_)
        bstack111l11lll_opy_ = bstack111l11lll_opy_[size:]
    bstack11l1ll1l1l_opy_.append(bstack111l11lll_opy_)
    return bstack11l1ll1l1l_opy_
def bstack1111ll1l1ll_opy_(message, bstack111l1l11111_opy_=False):
    os.write(1, bytes(message, bstack1ll1ll1_opy_ (u"ࠧࡶࡶࡩ࠱࠽࠭ᵉ")))
    os.write(1, bytes(bstack1ll1ll1_opy_ (u"ࠨ࡞ࡱࠫᵊ"), bstack1ll1ll1_opy_ (u"ࠩࡸࡸ࡫࠳࠸ࠨᵋ")))
    if bstack111l1l11111_opy_:
        with open(bstack1ll1ll1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠰ࡳ࠶࠷ࡹ࠮ࠩᵌ") + os.environ[bstack1ll1ll1_opy_ (u"ࠫࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡄࡘࡍࡑࡊ࡟ࡉࡃࡖࡌࡊࡊ࡟ࡊࡆࠪᵍ")] + bstack1ll1ll1_opy_ (u"ࠬ࠴࡬ࡰࡩࠪᵎ"), bstack1ll1ll1_opy_ (u"࠭ࡡࠨᵏ")) as f:
            f.write(message + bstack1ll1ll1_opy_ (u"ࠧ࡝ࡰࠪᵐ"))
def bstack1lll1ll1lll_opy_():
    return os.environ[bstack1ll1ll1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡂࡗࡗࡓࡒࡇࡔࡊࡑࡑࠫᵑ")].lower() == bstack1ll1ll1_opy_ (u"ࠩࡷࡶࡺ࡫ࠧᵒ")
def bstack1l11l1ll_opy_():
    return bstack1l1l1l11_opy_().replace(tzinfo=None).isoformat() + bstack1ll1ll1_opy_ (u"ࠪ࡞ࠬᵓ")
def bstack1111l1l1ll1_opy_(start, finish):
    return (datetime.datetime.fromisoformat(finish.rstrip(bstack1ll1ll1_opy_ (u"ࠫ࡟࠭ᵔ"))) - datetime.datetime.fromisoformat(start.rstrip(bstack1ll1ll1_opy_ (u"ࠬࡠࠧᵕ")))).total_seconds() * 1000
def bstack1111l1l1l1l_opy_(timestamp):
    return bstack111l1l11l1l_opy_(timestamp).isoformat() + bstack1ll1ll1_opy_ (u"࡚࠭ࠨᵖ")
def bstack1111llll111_opy_(bstack1111l1l1lll_opy_):
    date_format = bstack1ll1ll1_opy_ (u"࡛ࠧࠦࠨࡱࠪࡪࠠࠦࡊ࠽ࠩࡒࡀࠥࡔ࠰ࠨࡪࠬᵗ")
    bstack1111lll1ll1_opy_ = datetime.datetime.strptime(bstack1111l1l1lll_opy_, date_format)
    return bstack1111lll1ll1_opy_.isoformat() + bstack1ll1ll1_opy_ (u"ࠨ࡜ࠪᵘ")
def bstack111l1ll11ll_opy_(outcome):
    _, exception, _ = outcome.excinfo or (None, None, None)
    if exception:
        return bstack1ll1ll1_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩᵙ")
    else:
        return bstack1ll1ll1_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪᵚ")
def bstack1ll1l1llll_opy_(val):
    if val is None:
        return False
    return val.__str__().lower() == bstack1ll1ll1_opy_ (u"ࠫࡹࡸࡵࡦࠩᵛ")
def bstack111l11lllll_opy_(val):
    return val.__str__().lower() == bstack1ll1ll1_opy_ (u"ࠬ࡬ࡡ࡭ࡵࡨࠫᵜ")
def error_handler(bstack111l1111111_opy_=Exception, class_method=False, default_value=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except bstack111l1111111_opy_ as e:
                print(bstack1ll1ll1_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠠࡼࡿࠣ࠱ࡃࠦࡻࡾ࠼ࠣࡿࢂࠨᵝ").format(func.__name__, bstack111l1111111_opy_.__name__, str(e)))
                return default_value
        return wrapper
    def bstack111l111111l_opy_(bstack111l111l11l_opy_):
        def wrapped(cls, *args, **kwargs):
            try:
                return bstack111l111l11l_opy_(cls, *args, **kwargs)
            except bstack111l1111111_opy_ as e:
                print(bstack1ll1ll1_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠡࡽࢀࠤ࠲ࡄࠠࡼࡿ࠽ࠤࢀࢃࠢᵞ").format(bstack111l111l11l_opy_.__name__, bstack111l1111111_opy_.__name__, str(e)))
                return default_value
        return wrapped
    if class_method:
        return bstack111l111111l_opy_
    else:
        return decorator
def bstack11l1l111ll_opy_(bstack1111l1ll_opy_):
    if os.getenv(bstack1ll1ll1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡂࡗࡗࡓࡒࡇࡔࡊࡑࡑࠫᵟ")) is not None:
        return bstack1ll1l1llll_opy_(os.getenv(bstack1ll1ll1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡃࡘࡘࡔࡓࡁࡕࡋࡒࡒࠬᵠ")))
    if bstack1ll1ll1_opy_ (u"ࠪࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠧᵡ") in bstack1111l1ll_opy_ and bstack111l11lllll_opy_(bstack1111l1ll_opy_[bstack1ll1ll1_opy_ (u"ࠫࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠨᵢ")]):
        return False
    if bstack1ll1ll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠧᵣ") in bstack1111l1ll_opy_ and bstack111l11lllll_opy_(bstack1111l1ll_opy_[bstack1ll1ll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠨᵤ")]):
        return False
    return True
def bstack1llllll1l1_opy_():
    try:
        from pytest_bdd import reporting
        bstack111l1ll11l1_opy_ = os.environ.get(bstack1ll1ll1_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡕࡔࡇࡕࡣࡋࡘࡁࡎࡇ࡚ࡓࡗࡑࠢᵥ"), None)
        return bstack111l1ll11l1_opy_ is None or bstack111l1ll11l1_opy_ == bstack1ll1ll1_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠧᵦ")
    except Exception as e:
        return False
def bstack111ll1lll_opy_(hub_url, CONFIG):
    if bstack11lll11l1_opy_() <= version.parse(bstack1ll1ll1_opy_ (u"ࠩ࠶࠲࠶࠹࠮࠱ࠩᵧ")):
        if hub_url:
            return bstack1ll1ll1_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻࠱࠲ࠦᵨ") + hub_url + bstack1ll1ll1_opy_ (u"ࠦ࠿࠾࠰࠰ࡹࡧ࠳࡭ࡻࡢࠣᵩ")
        return bstack111llll1l1_opy_
    if hub_url:
        return bstack1ll1ll1_opy_ (u"ࠧ࡮ࡴࡵࡲࡶ࠾࠴࠵ࠢᵪ") + hub_url + bstack1ll1ll1_opy_ (u"ࠨ࠯ࡸࡦ࠲࡬ࡺࡨࠢᵫ")
    return bstack1l11ll1ll1_opy_
def bstack1111ll11ll1_opy_():
    return isinstance(os.getenv(bstack1ll1ll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐ࡚ࡖࡈࡗ࡙ࡥࡐࡍࡗࡊࡍࡓ࠭ᵬ")), str)
def bstack11ll1111l1_opy_(url):
    return urlparse(url).hostname
def bstack111ll111l1_opy_(hostname):
    for bstack111l111lll_opy_ in bstack1ll1l1l11l_opy_:
        regex = re.compile(bstack111l111lll_opy_)
        if regex.match(hostname):
            return True
    return False
def bstack11ll111ll1l_opy_(bstack1111l1lll11_opy_, file_name, logger):
    bstack1l1l1l111_opy_ = os.path.join(os.path.expanduser(bstack1ll1ll1_opy_ (u"ࠨࢀࠪᵭ")), bstack1111l1lll11_opy_)
    try:
        if not os.path.exists(bstack1l1l1l111_opy_):
            os.makedirs(bstack1l1l1l111_opy_)
        file_path = os.path.join(os.path.expanduser(bstack1ll1ll1_opy_ (u"ࠩࢁࠫᵮ")), bstack1111l1lll11_opy_, file_name)
        if not os.path.isfile(file_path):
            with open(file_path, bstack1ll1ll1_opy_ (u"ࠪࡻࠬᵯ")):
                pass
            with open(file_path, bstack1ll1ll1_opy_ (u"ࠦࡼ࠱ࠢᵰ")) as outfile:
                json.dump({}, outfile)
        return file_path
    except Exception as e:
        logger.debug(bstack1l111l1ll_opy_.format(str(e)))
def bstack11ll11l1111_opy_(file_name, key, value, logger):
    file_path = bstack11ll111ll1l_opy_(bstack1ll1ll1_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬᵱ"), file_name, logger)
    if file_path != None:
        if os.path.exists(file_path):
            bstack1ll111l11_opy_ = json.load(open(file_path, bstack1ll1ll1_opy_ (u"࠭ࡲࡣࠩᵲ")))
        else:
            bstack1ll111l11_opy_ = {}
        bstack1ll111l11_opy_[key] = value
        with open(file_path, bstack1ll1ll1_opy_ (u"ࠢࡸ࠭ࠥᵳ")) as outfile:
            json.dump(bstack1ll111l11_opy_, outfile)
def bstack11l111lll_opy_(file_name, logger):
    file_path = bstack11ll111ll1l_opy_(bstack1ll1ll1_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨᵴ"), file_name, logger)
    bstack1ll111l11_opy_ = {}
    if file_path != None and os.path.exists(file_path):
        with open(file_path, bstack1ll1ll1_opy_ (u"ࠩࡵࠫᵵ")) as bstack1l1111l111_opy_:
            bstack1ll111l11_opy_ = json.load(bstack1l1111l111_opy_)
    return bstack1ll111l11_opy_
def bstack11lll1ll1l_opy_(file_path, logger):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
    except Exception as e:
        logger.debug(bstack1ll1ll1_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡪࡥ࡭ࡧࡷ࡭ࡳ࡭ࠠࡧ࡫࡯ࡩ࠿ࠦࠧᵶ") + file_path + bstack1ll1ll1_opy_ (u"ࠫࠥ࠭ᵷ") + str(e))
def bstack11lll11l1_opy_():
    from selenium import webdriver
    return version.parse(webdriver.__version__)
class Notset:
    def __repr__(self):
        return bstack1ll1ll1_opy_ (u"ࠧࡂࡎࡐࡖࡖࡉ࡙ࡄࠢᵸ")
def bstack11l11llll_opy_(config):
    if bstack1ll1ll1_opy_ (u"࠭ࡩࡴࡒ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠬᵹ") in config:
        del (config[bstack1ll1ll1_opy_ (u"ࠧࡪࡵࡓࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹ࠭ᵺ")])
        return False
    if bstack11lll11l1_opy_() < version.parse(bstack1ll1ll1_opy_ (u"ࠨ࠵࠱࠸࠳࠶ࠧᵻ")):
        return False
    if bstack11lll11l1_opy_() >= version.parse(bstack1ll1ll1_opy_ (u"ࠩ࠷࠲࠶࠴࠵ࠨᵼ")):
        return True
    if bstack1ll1ll1_opy_ (u"ࠪࡹࡸ࡫ࡗ࠴ࡅࠪᵽ") in config and config[bstack1ll1ll1_opy_ (u"ࠫࡺࡹࡥࡘ࠵ࡆࠫᵾ")] is False:
        return False
    else:
        return True
def bstack1111ll11l1_opy_(args_list, bstack1111l1ll11l_opy_):
    index = -1
    for value in bstack1111l1ll11l_opy_:
        try:
            index = args_list.index(value)
            return index
        except Exception as e:
            return index
    return index
def bstack1111ll1ll1l_opy_(a, b):
  for k, v in b.items():
    if isinstance(v, dict) and k in a and isinstance(a[k], dict):
        bstack1111ll1ll1l_opy_(a[k], v)
    else:
        a[k] = v
class Result:
    def __init__(self, result=None, duration=None, exception=None, bstack1ll1111l_opy_=None):
        self.result = result
        self.duration = duration
        self.exception = exception
        self.exception_type = type(self.exception).__name__ if exception else None
        self.bstack1ll1111l_opy_ = bstack1ll1111l_opy_
    @classmethod
    def passed(cls):
        return Result(result=bstack1ll1ll1_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬᵿ"))
    @classmethod
    def failed(cls, exception=None):
        return Result(result=bstack1ll1ll1_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ᶀ"), exception=exception)
    def bstack11111l11l1_opy_(self):
        if self.result != bstack1ll1ll1_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧᶁ"):
            return None
        if isinstance(self.exception_type, str) and bstack1ll1ll1_opy_ (u"ࠣࡃࡶࡷࡪࡸࡴࡪࡱࡱࠦᶂ") in self.exception_type:
            return bstack1ll1ll1_opy_ (u"ࠤࡄࡷࡸ࡫ࡲࡵ࡫ࡲࡲࡊࡸࡲࡰࡴࠥᶃ")
        return bstack1ll1ll1_opy_ (u"࡙ࠥࡳ࡮ࡡ࡯ࡦ࡯ࡩࡩࡋࡲࡳࡱࡵࠦᶄ")
    def bstack111l11l1111_opy_(self):
        if self.result != bstack1ll1ll1_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫᶅ"):
            return None
        if self.bstack1ll1111l_opy_:
            return self.bstack1ll1111l_opy_
        return bstack111l11l111l_opy_(self.exception)
def bstack111l11l111l_opy_(exc):
    return [traceback.format_exception(exc)]
def bstack111l1l1ll1l_opy_(message):
    if isinstance(message, str):
        return not bool(message and message.strip())
    return True
def bstack1l1lll11_opy_(object, key, default_value):
    if not object or not object.__dict__:
        return default_value
    if key in object.__dict__.keys():
        return object.__dict__.get(key)
    return default_value
def bstack1111111ll_opy_(config, logger):
    try:
        import playwright
        bstack1111lll1lll_opy_ = playwright.__file__
        bstack1111llllll1_opy_ = os.path.split(bstack1111lll1lll_opy_)
        bstack111l11ll11l_opy_ = bstack1111llllll1_opy_[0] + bstack1ll1ll1_opy_ (u"ࠬ࠵ࡤࡳ࡫ࡹࡩࡷ࠵ࡰࡢࡥ࡮ࡥ࡬࡫࠯࡭࡫ࡥ࠳ࡨࡲࡩ࠰ࡥ࡯࡭࠳ࡰࡳࠨᶆ")
        os.environ[bstack1ll1ll1_opy_ (u"࠭ࡇࡍࡑࡅࡅࡑࡥࡁࡈࡇࡑࡘࡤࡎࡔࡕࡒࡢࡔࡗࡕࡘ࡚ࠩᶇ")] = bstack1ll1l1ll1_opy_(config)
        with open(bstack111l11ll11l_opy_, bstack1ll1ll1_opy_ (u"ࠧࡳࠩᶈ")) as f:
            file_content = f.read()
            bstack111l111lll1_opy_ = bstack1ll1ll1_opy_ (u"ࠨࡩ࡯ࡳࡧࡧ࡬࠮ࡣࡪࡩࡳࡺࠧᶉ")
            bstack1111l1llll1_opy_ = file_content.find(bstack111l111lll1_opy_)
            if bstack1111l1llll1_opy_ == -1:
              process = subprocess.Popen(bstack1ll1ll1_opy_ (u"ࠤࡱࡴࡲࠦࡩ࡯ࡵࡷࡥࡱࡲࠠࡨ࡮ࡲࡦࡦࡲ࠭ࡢࡩࡨࡲࡹࠨᶊ"), shell=True, cwd=bstack1111llllll1_opy_[0])
              process.wait()
              bstack111ll1111l1_opy_ = bstack1ll1ll1_opy_ (u"ࠪࠦࡺࡹࡥࠡࡵࡷࡶ࡮ࡩࡴࠣ࠽ࠪᶋ")
              bstack1111lll1l11_opy_ = bstack1ll1ll1_opy_ (u"ࠦࠧࠨࠠ࡝ࠤࡸࡷࡪࠦࡳࡵࡴ࡬ࡧࡹࡢࠢ࠼ࠢࡦࡳࡳࡹࡴࠡࡽࠣࡦࡴࡵࡴࡴࡶࡵࡥࡵࠦࡽࠡ࠿ࠣࡶࡪࡷࡵࡪࡴࡨࠬࠬ࡭࡬ࡰࡤࡤࡰ࠲ࡧࡧࡦࡰࡷࠫ࠮ࡁࠠࡪࡨࠣࠬࡵࡸ࡯ࡤࡧࡶࡷ࠳࡫࡮ࡷ࠰ࡊࡐࡔࡈࡁࡍࡡࡄࡋࡊࡔࡔࡠࡊࡗࡘࡕࡥࡐࡓࡑ࡛࡝࠮ࠦࡢࡰࡱࡷࡷࡹࡸࡡࡱࠪࠬ࠿ࠥࠨࠢࠣᶌ")
              bstack1111ll1ll11_opy_ = file_content.replace(bstack111ll1111l1_opy_, bstack1111lll1l11_opy_)
              with open(bstack111l11ll11l_opy_, bstack1ll1ll1_opy_ (u"ࠬࡽࠧᶍ")) as f:
                f.write(bstack1111ll1ll11_opy_)
    except Exception as e:
        logger.error(bstack1ll1111ll_opy_.format(str(e)))
def bstack11ll1lllll_opy_():
  try:
    bstack111l111llll_opy_ = os.path.join(tempfile.gettempdir(), bstack1ll1ll1_opy_ (u"࠭࡯ࡱࡶ࡬ࡱࡦࡲ࡟ࡩࡷࡥࡣࡺࡸ࡬࠯࡬ࡶࡳࡳ࠭ᶎ"))
    bstack1111lllllll_opy_ = []
    if os.path.exists(bstack111l111llll_opy_):
      with open(bstack111l111llll_opy_) as f:
        bstack1111lllllll_opy_ = json.load(f)
      os.remove(bstack111l111llll_opy_)
    return bstack1111lllllll_opy_
  except:
    pass
  return []
def bstack1l1l111l1_opy_(bstack1ll11111l1_opy_):
  try:
    bstack1111lllllll_opy_ = []
    bstack111l111llll_opy_ = os.path.join(tempfile.gettempdir(), bstack1ll1ll1_opy_ (u"ࠧࡰࡲࡷ࡭ࡲࡧ࡬ࡠࡪࡸࡦࡤࡻࡲ࡭࠰࡭ࡷࡴࡴࠧᶏ"))
    if os.path.exists(bstack111l111llll_opy_):
      with open(bstack111l111llll_opy_) as f:
        bstack1111lllllll_opy_ = json.load(f)
    bstack1111lllllll_opy_.append(bstack1ll11111l1_opy_)
    with open(bstack111l111llll_opy_, bstack1ll1ll1_opy_ (u"ࠨࡹࠪᶐ")) as f:
        json.dump(bstack1111lllllll_opy_, f)
  except:
    pass
def bstack1l1111lll1_opy_(logger, bstack111l1lll11l_opy_ = False):
  try:
    test_name = os.environ.get(bstack1ll1ll1_opy_ (u"ࠩࡓ࡝࡙ࡋࡓࡕࡡࡗࡉࡘ࡚࡟ࡏࡃࡐࡉࠬᶑ"), bstack1ll1ll1_opy_ (u"ࠪࠫᶒ"))
    if test_name == bstack1ll1ll1_opy_ (u"ࠫࠬᶓ"):
        test_name = threading.current_thread().__dict__.get(bstack1ll1ll1_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࡇࡪࡤࡠࡶࡨࡷࡹࡥ࡮ࡢ࡯ࡨࠫᶔ"), bstack1ll1ll1_opy_ (u"࠭ࠧᶕ"))
    bstack111l11l1lll_opy_ = bstack1ll1ll1_opy_ (u"ࠧ࠭ࠢࠪᶖ").join(threading.current_thread().bstackTestErrorMessages)
    if bstack111l1lll11l_opy_:
        bstack1l1lll111l_opy_ = os.environ.get(bstack1ll1ll1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡎࡄࡘࡋࡕࡒࡎࡡࡌࡒࡉࡋࡘࠨᶗ"), bstack1ll1ll1_opy_ (u"ࠩ࠳ࠫᶘ"))
        bstack11lllll1l1_opy_ = {bstack1ll1ll1_opy_ (u"ࠪࡲࡦࡳࡥࠨᶙ"): test_name, bstack1ll1ll1_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪᶚ"): bstack111l11l1lll_opy_, bstack1ll1ll1_opy_ (u"ࠬ࡯࡮ࡥࡧࡻࠫᶛ"): bstack1l1lll111l_opy_}
        bstack1111ll1l111_opy_ = []
        bstack111l1111l11_opy_ = os.path.join(tempfile.gettempdir(), bstack1ll1ll1_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹࡥࡰࡱࡲࡢࡩࡷࡸ࡯ࡳࡡ࡯࡭ࡸࡺ࠮࡫ࡵࡲࡲࠬᶜ"))
        if os.path.exists(bstack111l1111l11_opy_):
            with open(bstack111l1111l11_opy_) as f:
                bstack1111ll1l111_opy_ = json.load(f)
        bstack1111ll1l111_opy_.append(bstack11lllll1l1_opy_)
        with open(bstack111l1111l11_opy_, bstack1ll1ll1_opy_ (u"ࠧࡸࠩᶝ")) as f:
            json.dump(bstack1111ll1l111_opy_, f)
    else:
        bstack11lllll1l1_opy_ = {bstack1ll1ll1_opy_ (u"ࠨࡰࡤࡱࡪ࠭ᶞ"): test_name, bstack1ll1ll1_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨᶟ"): bstack111l11l1lll_opy_, bstack1ll1ll1_opy_ (u"ࠪ࡭ࡳࡪࡥࡹࠩᶠ"): str(multiprocessing.current_process().name)}
        if bstack1ll1ll1_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡣࡪࡸࡲࡰࡴࡢࡰ࡮ࡹࡴࠨᶡ") not in multiprocessing.current_process().__dict__.keys():
            multiprocessing.current_process().bstack_error_list = []
        multiprocessing.current_process().bstack_error_list.append(bstack11lllll1l1_opy_)
  except Exception as e:
      logger.warn(bstack1ll1ll1_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡵࡷࡳࡷ࡫ࠠࡱࡻࡷࡩࡸࡺࠠࡧࡷࡱࡲࡪࡲࠠࡥࡣࡷࡥ࠿ࠦࡻࡾࠤᶢ").format(e))
def bstack1ll11l11ll_opy_(error_message, test_name, index, logger):
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack1ll1ll1_opy_ (u"࠭ࡦࡪ࡮ࡨࡰࡴࡩ࡫ࠡࡰࡲࡸࠥࡧࡶࡢ࡫࡯ࡥࡧࡲࡥ࠭ࠢࡸࡷ࡮ࡴࡧࠡࡤࡤࡷ࡮ࡩࠠࡧ࡫࡯ࡩࠥࡵࡰࡦࡴࡤࡸ࡮ࡵ࡮ࡴࠩᶣ"))
    try:
      bstack111ll111111_opy_ = []
      bstack11lllll1l1_opy_ = {bstack1ll1ll1_opy_ (u"ࠧ࡯ࡣࡰࡩࠬᶤ"): test_name, bstack1ll1ll1_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧᶥ"): error_message, bstack1ll1ll1_opy_ (u"ࠩ࡬ࡲࡩ࡫ࡸࠨᶦ"): index}
      bstack1111llll11l_opy_ = os.path.join(tempfile.gettempdir(), bstack1ll1ll1_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࡡࡨࡶࡷࡵࡲࡠ࡮࡬ࡷࡹ࠴ࡪࡴࡱࡱࠫᶧ"))
      if os.path.exists(bstack1111llll11l_opy_):
          with open(bstack1111llll11l_opy_) as f:
              bstack111ll111111_opy_ = json.load(f)
      bstack111ll111111_opy_.append(bstack11lllll1l1_opy_)
      with open(bstack1111llll11l_opy_, bstack1ll1ll1_opy_ (u"ࠫࡼ࠭ᶨ")) as f:
          json.dump(bstack111ll111111_opy_, f)
    except Exception as e:
      logger.warn(bstack1ll1ll1_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡵࡷࡳࡷ࡫ࠠࡳࡱࡥࡳࡹࠦࡦࡶࡰࡱࡩࡱࠦࡤࡢࡶࡤ࠾ࠥࢁࡽࠣᶩ").format(e))
    return
  bstack111ll111111_opy_ = []
  bstack11lllll1l1_opy_ = {bstack1ll1ll1_opy_ (u"࠭࡮ࡢ࡯ࡨࠫᶪ"): test_name, bstack1ll1ll1_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭ᶫ"): error_message, bstack1ll1ll1_opy_ (u"ࠨ࡫ࡱࡨࡪࡾࠧᶬ"): index}
  bstack1111llll11l_opy_ = os.path.join(tempfile.gettempdir(), bstack1ll1ll1_opy_ (u"ࠩࡵࡳࡧࡵࡴࡠࡧࡵࡶࡴࡸ࡟࡭࡫ࡶࡸ࠳ࡰࡳࡰࡰࠪᶭ"))
  lock_file = bstack1111llll11l_opy_ + bstack1ll1ll1_opy_ (u"ࠪ࠲ࡱࡵࡣ࡬ࠩᶮ")
  try:
    with FileLock(lock_file, timeout=10):
      if os.path.exists(bstack1111llll11l_opy_):
          with open(bstack1111llll11l_opy_, bstack1ll1ll1_opy_ (u"ࠫࡷ࠭ᶯ")) as f:
              content = f.read().strip()
              if content:
                  bstack111ll111111_opy_ = json.load(open(bstack1111llll11l_opy_))
      bstack111ll111111_opy_.append(bstack11lllll1l1_opy_)
      with open(bstack1111llll11l_opy_, bstack1ll1ll1_opy_ (u"ࠬࡽࠧᶰ")) as f:
          json.dump(bstack111ll111111_opy_, f)
  except Exception as e:
    logger.warn(bstack1ll1ll1_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡶࡸࡴࡸࡥࠡࡴࡲࡦࡴࡺࠠࡧࡷࡱࡲࡪࡲࠠࡥࡣࡷࡥࠥࡽࡩࡵࡪࠣࡪ࡮ࡲࡥࠡ࡮ࡲࡧࡰ࡯࡮ࡨ࠼ࠣࡿࢂࠨᶱ").format(e))
def bstack1l11ll1l1_opy_(bstack11llll1ll1_opy_, name, logger):
  try:
    bstack11lllll1l1_opy_ = {bstack1ll1ll1_opy_ (u"ࠧ࡯ࡣࡰࡩࠬᶲ"): name, bstack1ll1ll1_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧᶳ"): bstack11llll1ll1_opy_, bstack1ll1ll1_opy_ (u"ࠩ࡬ࡲࡩ࡫ࡸࠨᶴ"): str(threading.current_thread()._name)}
    return bstack11lllll1l1_opy_
  except Exception as e:
    logger.warn(bstack1ll1ll1_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡳࡵࡱࡵࡩࠥࡨࡥࡩࡣࡹࡩࠥ࡬ࡵ࡯ࡰࡨࡰࠥࡪࡡࡵࡣ࠽ࠤࢀࢃࠢᶵ").format(e))
  return
def bstack111l1l1l1l1_opy_():
    return platform.system() == bstack1ll1ll1_opy_ (u"ࠫ࡜࡯࡮ࡥࡱࡺࡷࠬᶶ")
def bstack11l11l1l1l_opy_(bstack1111lll1l1l_opy_, config, logger):
    bstack111l111l111_opy_ = {}
    try:
        return {key: config[key] for key in config if bstack1111lll1l1l_opy_.match(key)}
    except Exception as e:
        logger.debug(bstack1ll1ll1_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡨ࡬ࡰࡹ࡫ࡲࠡࡥࡲࡲ࡫࡯ࡧࠡ࡭ࡨࡽࡸࠦࡢࡺࠢࡵࡩ࡬࡫ࡸࠡ࡯ࡤࡸࡨ࡮࠺ࠡࡽࢀࠦᶷ").format(e))
    return bstack111l111l111_opy_
def bstack11l1ll111ll_opy_(bstack111l111l1ll_opy_, bstack111l11ll1l1_opy_):
    bstack111l11llll1_opy_ = version.parse(bstack111l111l1ll_opy_)
    bstack111l1l1l111_opy_ = version.parse(bstack111l11ll1l1_opy_)
    if bstack111l11llll1_opy_ > bstack111l1l1l111_opy_:
        return 1
    elif bstack111l11llll1_opy_ < bstack111l1l1l111_opy_:
        return -1
    else:
        return 0
def bstack1l1l1l11_opy_():
    return datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None)
def bstack111l1l11l1l_opy_(timestamp):
    return datetime.datetime.fromtimestamp(timestamp, datetime.timezone.utc).replace(tzinfo=None)
def bstack1111lll111l_opy_(framework):
    from browserstack_sdk._version import __version__
    return str(framework) + str(__version__)
def bstack11ll1l1111_opy_(options, framework, config, bstack1ll1l1lll_opy_={}):
    if options is None:
        return
    if getattr(options, bstack1ll1ll1_opy_ (u"࠭ࡧࡦࡶࠪᶸ"), None):
        caps = options
    else:
        caps = options.to_capabilities()
    bstack1ll1lllll1_opy_ = caps.get(bstack1ll1ll1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨᶹ"))
    bstack1111l1lll1l_opy_ = True
    bstack1l11lllll_opy_ = os.environ[bstack1ll1ll1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭ᶺ")]
    bstack1l111lllll1_opy_ = config.get(bstack1ll1ll1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩᶻ"), False)
    if bstack1l111lllll1_opy_:
        bstack1l1l1ll11ll_opy_ = config.get(bstack1ll1ll1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪᶼ"), {})
        bstack1l1l1ll11ll_opy_[bstack1ll1ll1_opy_ (u"ࠫࡦࡻࡴࡩࡖࡲ࡯ࡪࡴࠧᶽ")] = os.getenv(bstack1ll1ll1_opy_ (u"ࠬࡈࡓࡠࡃ࠴࠵࡞ࡥࡊࡘࡖࠪᶾ"))
        bstack1111ll11l1l_opy_ = json.loads(os.getenv(bstack1ll1ll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡢࡅࡈࡉࡅࡔࡕࡌࡆࡎࡒࡉࡕ࡛ࡢࡇࡔࡔࡆࡊࡉࡘࡖࡆ࡚ࡉࡐࡐࡢ࡝ࡒࡒࠧᶿ"), bstack1ll1ll1_opy_ (u"ࠧࡼࡿࠪ᷀"))).get(bstack1ll1ll1_opy_ (u"ࠨࡵࡦࡥࡳࡴࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩ᷁"))
    if bstack111l11lllll_opy_(caps.get(bstack1ll1ll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡷࡶࡩ࡜࠹ࡃࠨ᷂"))) or bstack111l11lllll_opy_(caps.get(bstack1ll1ll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡸࡷࡪࡥࡷ࠴ࡥࠪ᷃"))):
        bstack1111l1lll1l_opy_ = False
    if bstack11l11llll_opy_({bstack1ll1ll1_opy_ (u"ࠦࡺࡹࡥࡘ࠵ࡆࠦ᷄"): bstack1111l1lll1l_opy_}):
        bstack1ll1lllll1_opy_ = bstack1ll1lllll1_opy_ or {}
        bstack1ll1lllll1_opy_[bstack1ll1ll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡗࡉࡑࠧ᷅")] = bstack1111lll111l_opy_(framework)
        bstack1ll1lllll1_opy_[bstack1ll1ll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠨ᷆")] = bstack1lll1ll1lll_opy_()
        bstack1ll1lllll1_opy_[bstack1ll1ll1_opy_ (u"ࠧࡵࡧࡶࡸ࡭ࡻࡢࡃࡷ࡬ࡰࡩ࡛ࡵࡪࡦࠪ᷇")] = bstack1l11lllll_opy_
        bstack1ll1lllll1_opy_[bstack1ll1ll1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡐࡳࡱࡧࡹࡨࡺࡍࡢࡲࠪ᷈")] = bstack1ll1l1lll_opy_
        if bstack1l111lllll1_opy_:
            bstack1ll1lllll1_opy_[bstack1ll1ll1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩ᷉")] = bstack1l111lllll1_opy_
            bstack1ll1lllll1_opy_[bstack1ll1ll1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵ᷊ࠪ")] = bstack1l1l1ll11ll_opy_
            bstack1ll1lllll1_opy_[bstack1ll1ll1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫ᷋")][bstack1ll1ll1_opy_ (u"ࠬࡹࡣࡢࡰࡱࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭᷌")] = bstack1111ll11l1l_opy_
        if getattr(options, bstack1ll1ll1_opy_ (u"࠭ࡳࡦࡶࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹࡿࠧ᷍"), None):
            options.set_capability(bstack1ll1ll1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨ᷎"), bstack1ll1lllll1_opy_)
        else:
            options[bstack1ll1ll1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴ᷏ࠩ")] = bstack1ll1lllll1_opy_
    else:
        if getattr(options, bstack1ll1ll1_opy_ (u"ࠩࡶࡩࡹࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵࡻ᷐ࠪ"), None):
            options.set_capability(bstack1ll1ll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡔࡆࡎࠫ᷑"), bstack1111lll111l_opy_(framework))
            options.set_capability(bstack1ll1ll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬ᷒"), bstack1lll1ll1lll_opy_())
            options.set_capability(bstack1ll1ll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡹ࡫ࡳࡵࡪࡸࡦࡇࡻࡩ࡭ࡦࡘࡹ࡮ࡪࠧᷓ"), bstack1l11lllll_opy_)
            options.set_capability(bstack1ll1ll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡨࡵࡪ࡮ࡧࡔࡷࡵࡤࡶࡥࡷࡑࡦࡶࠧᷔ"), bstack1ll1l1lll_opy_)
            if bstack1l111lllll1_opy_:
                options.set_capability(bstack1ll1ll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭ᷕ"), bstack1l111lllll1_opy_)
                options.set_capability(bstack1ll1ll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧᷖ"), bstack1l1l1ll11ll_opy_)
                options.set_capability(bstack1ll1ll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳ࠯ࡵࡦࡥࡳࡴࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩᷗ"), bstack1111ll11l1l_opy_)
        else:
            options[bstack1ll1ll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡔࡆࡎࠫᷘ")] = bstack1111lll111l_opy_(framework)
            options[bstack1ll1ll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬᷙ")] = bstack1lll1ll1lll_opy_()
            options[bstack1ll1ll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡹ࡫ࡳࡵࡪࡸࡦࡇࡻࡩ࡭ࡦࡘࡹ࡮ࡪࠧᷚ")] = bstack1l11lllll_opy_
            options[bstack1ll1ll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡨࡵࡪ࡮ࡧࡔࡷࡵࡤࡶࡥࡷࡑࡦࡶࠧᷛ")] = bstack1ll1l1lll_opy_
            if bstack1l111lllll1_opy_:
                options[bstack1ll1ll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭ᷜ")] = bstack1l111lllll1_opy_
                options[bstack1ll1ll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧᷝ")] = bstack1l1l1ll11ll_opy_
                options[bstack1ll1ll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨᷞ")][bstack1ll1ll1_opy_ (u"ࠪࡷࡨࡧ࡮࡯ࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫᷟ")] = bstack1111ll11l1l_opy_
    return options
def bstack111l11lll1l_opy_(ws_endpoint, framework):
    bstack1ll1l1lll_opy_ = bstack11111l11_opy_.get_property(bstack1ll1ll1_opy_ (u"ࠦࡕࡒࡁ࡚࡙ࡕࡍࡌࡎࡔࡠࡒࡕࡓࡉ࡛ࡃࡕࡡࡐࡅࡕࠨᷠ"))
    if ws_endpoint and len(ws_endpoint.split(bstack1ll1ll1_opy_ (u"ࠬࡩࡡࡱࡵࡀࠫᷡ"))) > 1:
        ws_url = ws_endpoint.split(bstack1ll1ll1_opy_ (u"࠭ࡣࡢࡲࡶࡁࠬᷢ"))[0]
        if bstack1ll1ll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯ࠪᷣ") in ws_url:
            from browserstack_sdk._version import __version__
            bstack1111ll111ll_opy_ = json.loads(urllib.parse.unquote(ws_endpoint.split(bstack1ll1ll1_opy_ (u"ࠨࡥࡤࡴࡸࡃࠧᷤ"))[1]))
            bstack1111ll111ll_opy_ = bstack1111ll111ll_opy_ or {}
            bstack1l11lllll_opy_ = os.environ[bstack1ll1ll1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧᷥ")]
            bstack1111ll111ll_opy_[bstack1ll1ll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡔࡆࡎࠫᷦ")] = str(framework) + str(__version__)
            bstack1111ll111ll_opy_[bstack1ll1ll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬᷧ")] = bstack1lll1ll1lll_opy_()
            bstack1111ll111ll_opy_[bstack1ll1ll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡹ࡫ࡳࡵࡪࡸࡦࡇࡻࡩ࡭ࡦࡘࡹ࡮ࡪࠧᷨ")] = bstack1l11lllll_opy_
            bstack1111ll111ll_opy_[bstack1ll1ll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡨࡵࡪ࡮ࡧࡔࡷࡵࡤࡶࡥࡷࡑࡦࡶࠧᷩ")] = bstack1ll1l1lll_opy_
            ws_endpoint = ws_endpoint.split(bstack1ll1ll1_opy_ (u"ࠧࡤࡣࡳࡷࡂ࠭ᷪ"))[0] + bstack1ll1ll1_opy_ (u"ࠨࡥࡤࡴࡸࡃࠧᷫ") + urllib.parse.quote(json.dumps(bstack1111ll111ll_opy_))
    return ws_endpoint
def bstack11111l1lll_opy_():
    global bstack1l1ll111l1_opy_
    from playwright._impl._browser_type import BrowserType
    bstack1l1ll111l1_opy_ = BrowserType.connect
    return bstack1l1ll111l1_opy_
def bstack1l1l111ll_opy_(framework_name):
    global bstack1l1ll1ll1l_opy_
    bstack1l1ll1ll1l_opy_ = framework_name
    return framework_name
def bstack1l11l11l1l_opy_(self, *args, **kwargs):
    global bstack1l1ll111l1_opy_
    try:
        global bstack1l1ll1ll1l_opy_
        if bstack1ll1ll1_opy_ (u"ࠩࡺࡷࡊࡴࡤࡱࡱ࡬ࡲࡹ࠭ᷬ") in kwargs:
            kwargs[bstack1ll1ll1_opy_ (u"ࠪࡻࡸࡋ࡮ࡥࡲࡲ࡭ࡳࡺࠧᷭ")] = bstack111l11lll1l_opy_(
                kwargs.get(bstack1ll1ll1_opy_ (u"ࠫࡼࡹࡅ࡯ࡦࡳࡳ࡮ࡴࡴࠨᷮ"), None),
                bstack1l1ll1ll1l_opy_
            )
    except Exception as e:
        logger.error(bstack1ll1ll1_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡥ࡯ࠢࡳࡶࡴࡩࡥࡴࡵ࡬ࡲ࡬ࠦࡓࡅࡍࠣࡧࡦࡶࡳ࠻ࠢࡾࢁࠧᷯ").format(str(e)))
    return bstack1l1ll111l1_opy_(self, *args, **kwargs)
def bstack1111ll11l11_opy_(bstack111l1111lll_opy_, proxies):
    proxy_settings = {}
    try:
        if not proxies:
            proxies = bstack111ll1111l_opy_(bstack111l1111lll_opy_, bstack1ll1ll1_opy_ (u"ࠨࠢᷰ"))
        if proxies and proxies.get(bstack1ll1ll1_opy_ (u"ࠢࡩࡶࡷࡴࡸࠨᷱ")):
            parsed_url = urlparse(proxies.get(bstack1ll1ll1_opy_ (u"ࠣࡪࡷࡸࡵࡹࠢᷲ")))
            if parsed_url and parsed_url.hostname: proxy_settings[bstack1ll1ll1_opy_ (u"ࠩࡳࡶࡴࡾࡹࡉࡱࡶࡸࠬᷳ")] = str(parsed_url.hostname)
            if parsed_url and parsed_url.port: proxy_settings[bstack1ll1ll1_opy_ (u"ࠪࡴࡷࡵࡸࡺࡒࡲࡶࡹ࠭ᷴ")] = str(parsed_url.port)
            if parsed_url and parsed_url.username: proxy_settings[bstack1ll1ll1_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡘࡷࡪࡸࠧ᷵")] = str(parsed_url.username)
            if parsed_url and parsed_url.password: proxy_settings[bstack1ll1ll1_opy_ (u"ࠬࡶࡲࡰࡺࡼࡔࡦࡹࡳࠨ᷶")] = str(parsed_url.password)
        return proxy_settings
    except:
        return proxy_settings
def bstack1l1lll1ll_opy_(bstack111l1111lll_opy_):
    bstack111l1l111l1_opy_ = {
        bstack11l1l1lll1l_opy_[bstack111l11111ll_opy_]: bstack111l1111lll_opy_[bstack111l11111ll_opy_]
        for bstack111l11111ll_opy_ in bstack111l1111lll_opy_
        if bstack111l11111ll_opy_ in bstack11l1l1lll1l_opy_
    }
    bstack111l1l111l1_opy_[bstack1ll1ll1_opy_ (u"ࠨࡰࡳࡱࡻࡽࡘ࡫ࡴࡵ࡫ࡱ࡫ࡸࠨ᷷")] = bstack1111ll11l11_opy_(bstack111l1111lll_opy_, bstack11111l11_opy_.get_property(bstack1ll1ll1_opy_ (u"ࠢࡱࡴࡲࡼࡾ࡙ࡥࡵࡶ࡬ࡲ࡬ࡹ᷸ࠢ")))
    bstack111ll11111l_opy_ = [element.lower() for element in bstack11l1l11l11l_opy_]
    bstack111l1l11lll_opy_(bstack111l1l111l1_opy_, bstack111ll11111l_opy_)
    return bstack111l1l111l1_opy_
def bstack111l1l11lll_opy_(d, keys):
    for key in list(d.keys()):
        if key.lower() in keys:
            d[key] = bstack1ll1ll1_opy_ (u"ࠣࠬ࠭࠮࠯ࠨ᷹")
    for value in d.values():
        if isinstance(value, dict):
            bstack111l1l11lll_opy_(value, keys)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    bstack111l1l11lll_opy_(item, keys)
def bstack1ll1l1lll11_opy_():
    bstack1111ll1l1l1_opy_ = [os.environ.get(bstack1ll1ll1_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡈࡌࡐࡊ࡙࡟ࡅࡋࡕ᷺ࠦ")), os.path.join(os.path.expanduser(bstack1ll1ll1_opy_ (u"ࠥࢂࠧ᷻")), bstack1ll1ll1_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫ᷼")), os.path.join(bstack1ll1ll1_opy_ (u"ࠬ࠵ࡴ࡮ࡲ᷽ࠪ"), bstack1ll1ll1_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭᷾"))]
    for path in bstack1111ll1l1l1_opy_:
        if path is None:
            continue
        try:
            if os.path.exists(path):
                logger.debug(bstack1ll1ll1_opy_ (u"ࠢࡇ࡫࡯ࡩ᷿ࠥ࠭ࠢ") + str(path) + bstack1ll1ll1_opy_ (u"ࠣࠩࠣࡩࡽ࡯ࡳࡵࡵ࠱ࠦḀ"))
                if not os.access(path, os.W_OK):
                    logger.debug(bstack1ll1ll1_opy_ (u"ࠤࡊ࡭ࡻ࡯࡮ࡨࠢࡳࡩࡷࡳࡩࡴࡵ࡬ࡳࡳࡹࠠࡧࡱࡵࠤࠬࠨḁ") + str(path) + bstack1ll1ll1_opy_ (u"ࠥࠫࠧḂ"))
                    os.chmod(path, 0o777)
                else:
                    logger.debug(bstack1ll1ll1_opy_ (u"ࠦࡋ࡯࡬ࡦࠢࠪࠦḃ") + str(path) + bstack1ll1ll1_opy_ (u"ࠧ࠭ࠠࡢ࡮ࡵࡩࡦࡪࡹࠡࡪࡤࡷࠥࡺࡨࡦࠢࡵࡩࡶࡻࡩࡳࡧࡧࠤࡵ࡫ࡲ࡮࡫ࡶࡷ࡮ࡵ࡮ࡴ࠰ࠥḄ"))
            else:
                logger.debug(bstack1ll1ll1_opy_ (u"ࠨࡃࡳࡧࡤࡸ࡮ࡴࡧࠡࡨ࡬ࡰࡪࠦࠧࠣḅ") + str(path) + bstack1ll1ll1_opy_ (u"ࠢࠨࠢࡺ࡭ࡹ࡮ࠠࡸࡴ࡬ࡸࡪࠦࡰࡦࡴࡰ࡭ࡸࡹࡩࡰࡰ࠱ࠦḆ"))
                os.makedirs(path, exist_ok=True)
                os.chmod(path, 0o777)
            logger.debug(bstack1ll1ll1_opy_ (u"ࠣࡑࡳࡩࡷࡧࡴࡪࡱࡱࠤࡸࡻࡣࡤࡧࡨࡨࡪࡪࠠࡧࡱࡵࠤࠬࠨḇ") + str(path) + bstack1ll1ll1_opy_ (u"ࠤࠪ࠲ࠧḈ"))
            return path
        except Exception as e:
            logger.debug(bstack1ll1ll1_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡳࡦࡶࠣࡹࡵࠦࡦࡪ࡮ࡨࠤࠬࢁࡰࡢࡶ࡫ࢁࠬࡀࠠࠣḉ") + str(e) + bstack1ll1ll1_opy_ (u"ࠦࠧḊ"))
    logger.debug(bstack1ll1ll1_opy_ (u"ࠧࡇ࡬࡭ࠢࡳࡥࡹ࡮ࡳࠡࡨࡤ࡭ࡱ࡫ࡤ࠯ࠤḋ"))
    return None
@measure(event_name=EVENTS.bstack11l1l1l111l_opy_, stage=STAGE.bstack111l1l111_opy_)
def bstack1l1l11ll11l_opy_(binary_path, bstack1l1l111ll1l_opy_, bs_config):
    logger.debug(bstack1ll1ll1_opy_ (u"ࠨࡃࡶࡴࡵࡩࡳࡺࠠࡄࡎࡌࠤࡕࡧࡴࡩࠢࡩࡳࡺࡴࡤ࠻ࠢࡾࢁࠧḌ").format(binary_path))
    bstack111l1l11ll1_opy_ = bstack1ll1ll1_opy_ (u"ࠧࠨḍ")
    bstack1111lll1111_opy_ = {
        bstack1ll1ll1_opy_ (u"ࠨࡵࡧ࡯ࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭Ḏ"): __version__,
        bstack1ll1ll1_opy_ (u"ࠤࡲࡷࠧḏ"): platform.system(),
        bstack1ll1ll1_opy_ (u"ࠥࡳࡸࡥࡡࡳࡥ࡫ࠦḐ"): platform.machine(),
        bstack1ll1ll1_opy_ (u"ࠦࡨࡲࡩࡠࡸࡨࡶࡸ࡯࡯࡯ࠤḑ"): bstack1ll1ll1_opy_ (u"ࠬ࠶ࠧḒ"),
        bstack1ll1ll1_opy_ (u"ࠨࡳࡥ࡭ࡢࡰࡦࡴࡧࡶࡣࡪࡩࠧḓ"): bstack1ll1ll1_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧḔ")
    }
    bstack111l1l1l11l_opy_(bstack1111lll1111_opy_)
    try:
        if binary_path:
            bstack1111lll1111_opy_[bstack1ll1ll1_opy_ (u"ࠨࡥ࡯࡭ࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭ḕ")] = subprocess.check_output([binary_path, bstack1ll1ll1_opy_ (u"ࠤࡹࡩࡷࡹࡩࡰࡰࠥḖ")]).strip().decode(bstack1ll1ll1_opy_ (u"ࠪࡹࡹ࡬࠭࠹ࠩḗ"))
        response = requests.request(
            bstack1ll1ll1_opy_ (u"ࠫࡌࡋࡔࠨḘ"),
            url=bstack111l11l111_opy_(bstack11l11ll1ll1_opy_),
            headers=None,
            auth=(bs_config[bstack1ll1ll1_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧḙ")], bs_config[bstack1ll1ll1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩḚ")]),
            json=None,
            params=bstack1111lll1111_opy_
        )
        data = response.json()
        if response.status_code == 200 and bstack1ll1ll1_opy_ (u"ࠧࡶࡴ࡯ࠫḛ") in data.keys() and bstack1ll1ll1_opy_ (u"ࠨࡷࡳࡨࡦࡺࡥࡥࡡࡦࡰ࡮ࡥࡶࡦࡴࡶ࡭ࡴࡴࠧḜ") in data.keys():
            logger.debug(bstack1ll1ll1_opy_ (u"ࠤࡑࡩࡪࡪࠠࡵࡱࠣࡹࡵࡪࡡࡵࡧࠣࡦ࡮ࡴࡡࡳࡻ࠯ࠤࡨࡻࡲࡳࡧࡱࡸࠥࡨࡩ࡯ࡣࡵࡽࠥࡼࡥࡳࡵ࡬ࡳࡳࡀࠠࡼࡿࠥḝ").format(bstack1111lll1111_opy_[bstack1ll1ll1_opy_ (u"ࠪࡧࡱ࡯࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨḞ")]))
            if bstack1ll1ll1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡆࡎࡔࡁࡓ࡛ࡢ࡙ࡗࡒࠧḟ") in os.environ:
                logger.debug(bstack1ll1ll1_opy_ (u"࡙ࠧ࡫ࡪࡲࡳ࡭ࡳ࡭ࠠࡣ࡫ࡱࡥࡷࡿࠠࡥࡱࡺࡲࡱࡵࡡࡥࠢࡤࡷࠥࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡇࡏࡎࡂࡔ࡜ࡣ࡚ࡘࡌࠡ࡫ࡶࠤࡸ࡫ࡴࠣḠ"))
                data[bstack1ll1ll1_opy_ (u"࠭ࡵࡳ࡮ࠪḡ")] = os.environ[bstack1ll1ll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡂࡊࡐࡄࡖ࡞ࡥࡕࡓࡎࠪḢ")]
            bstack111l11lll11_opy_ = bstack111l111ll11_opy_(data[bstack1ll1ll1_opy_ (u"ࠨࡷࡵࡰࠬḣ")], bstack1l1l111ll1l_opy_)
            bstack111l1l11ll1_opy_ = os.path.join(bstack1l1l111ll1l_opy_, bstack111l11lll11_opy_)
            os.chmod(bstack111l1l11ll1_opy_, 0o777) # bstack111ll111l11_opy_ permission
            return bstack111l1l11ll1_opy_
    except Exception as e:
        logger.debug(bstack1ll1ll1_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡹ࡫࡭ࡱ࡫ࠠࡥࡱࡺࡲࡱࡵࡡࡥ࡫ࡱ࡫ࠥࡴࡥࡸࠢࡖࡈࡐࠦࡻࡾࠤḤ").format(e))
    return binary_path
def bstack111l1l1l11l_opy_(bstack1111lll1111_opy_):
    try:
        if bstack1ll1ll1_opy_ (u"ࠪࡰ࡮ࡴࡵࡹࠩḥ") not in bstack1111lll1111_opy_[bstack1ll1ll1_opy_ (u"ࠫࡴࡹࠧḦ")].lower():
            return
        if os.path.exists(bstack1ll1ll1_opy_ (u"ࠧ࠵ࡥࡵࡥ࠲ࡳࡸ࠳ࡲࡦ࡮ࡨࡥࡸ࡫ࠢḧ")):
            with open(bstack1ll1ll1_opy_ (u"ࠨ࠯ࡦࡶࡦ࠳ࡴࡹ࠭ࡳࡧ࡯ࡩࡦࡹࡥࠣḨ"), bstack1ll1ll1_opy_ (u"ࠢࡳࠤḩ")) as f:
                bstack111l1l1lll1_opy_ = {}
                for line in f:
                    if bstack1ll1ll1_opy_ (u"ࠣ࠿ࠥḪ") in line:
                        key, value = line.rstrip().split(bstack1ll1ll1_opy_ (u"ࠤࡀࠦḫ"), 1)
                        bstack111l1l1lll1_opy_[key] = value.strip(bstack1ll1ll1_opy_ (u"ࠪࠦࡡ࠭ࠧḬ"))
                bstack1111lll1111_opy_[bstack1ll1ll1_opy_ (u"ࠫࡩ࡯ࡳࡵࡴࡲࠫḭ")] = bstack111l1l1lll1_opy_.get(bstack1ll1ll1_opy_ (u"ࠧࡏࡄࠣḮ"), bstack1ll1ll1_opy_ (u"ࠨࠢḯ"))
        elif os.path.exists(bstack1ll1ll1_opy_ (u"ࠢ࠰ࡧࡷࡧ࠴ࡧ࡬ࡱ࡫ࡱࡩ࠲ࡸࡥ࡭ࡧࡤࡷࡪࠨḰ")):
            bstack1111lll1111_opy_[bstack1ll1ll1_opy_ (u"ࠨࡦ࡬ࡷࡹࡸ࡯ࠨḱ")] = bstack1ll1ll1_opy_ (u"ࠩࡤࡰࡵ࡯࡮ࡦࠩḲ")
    except Exception as e:
        logger.debug(bstack1ll1ll1_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡧࡦࡶࠣࡨ࡮ࡹࡴࡳࡱࠣࡳ࡫ࠦ࡬ࡪࡰࡸࡼࠧḳ") + e)
@measure(event_name=EVENTS.bstack11l1l11ll1l_opy_, stage=STAGE.bstack111l1l111_opy_)
def bstack111l111ll11_opy_(bstack1111ll11lll_opy_, bstack1111l1l1l11_opy_):
    logger.debug(bstack1ll1ll1_opy_ (u"ࠦࡉࡵࡷ࡯࡮ࡲࡥࡩ࡯࡮ࡨࠢࡖࡈࡐࠦࡢࡪࡰࡤࡶࡾࠦࡦࡳࡱࡰ࠾ࠥࠨḴ") + str(bstack1111ll11lll_opy_) + bstack1ll1ll1_opy_ (u"ࠧࠨḵ"))
    zip_path = os.path.join(bstack1111l1l1l11_opy_, bstack1ll1ll1_opy_ (u"ࠨࡤࡰࡹࡱࡰࡴࡧࡤࡦࡦࡢࡪ࡮ࡲࡥ࠯ࡼ࡬ࡴࠧḶ"))
    bstack111l11lll11_opy_ = bstack1ll1ll1_opy_ (u"ࠧࠨḷ")
    with requests.get(bstack1111ll11lll_opy_, stream=True) as response:
        response.raise_for_status()
        with open(zip_path, bstack1ll1ll1_opy_ (u"ࠣࡹࡥࠦḸ")) as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
        logger.debug(bstack1ll1ll1_opy_ (u"ࠤࡉ࡭ࡱ࡫ࠠࡥࡱࡺࡲࡱࡵࡡࡥࡧࡧࠤࡸࡻࡣࡤࡧࡶࡷ࡫ࡻ࡬࡭ࡻ࠱ࠦḹ"))
    with zipfile.ZipFile(zip_path, bstack1ll1ll1_opy_ (u"ࠪࡶࠬḺ")) as zip_ref:
        bstack111l1llll11_opy_ = zip_ref.namelist()
        if len(bstack111l1llll11_opy_) > 0:
            bstack111l11lll11_opy_ = bstack111l1llll11_opy_[0] # bstack1111l1lllll_opy_ bstack11l1l111l11_opy_ will be bstack111l1l11l11_opy_ 1 file i.e. the binary in the zip
        zip_ref.extractall(bstack1111l1l1l11_opy_)
        logger.debug(bstack1ll1ll1_opy_ (u"ࠦࡋ࡯࡬ࡦࡵࠣࡷࡺࡩࡣࡦࡵࡶࡪࡺࡲ࡬ࡺࠢࡨࡼࡹࡸࡡࡤࡶࡨࡨࠥࡺ࡯ࠡࠩࠥḻ") + str(bstack1111l1l1l11_opy_) + bstack1ll1ll1_opy_ (u"ࠧ࠭ࠢḼ"))
    os.remove(zip_path)
    return bstack111l11lll11_opy_
def get_cli_dir():
    bstack111l1llllll_opy_ = bstack1ll1l1lll11_opy_()
    if bstack111l1llllll_opy_:
        bstack1l1l111ll1l_opy_ = os.path.join(bstack111l1llllll_opy_, bstack1ll1ll1_opy_ (u"ࠨࡣ࡭࡫ࠥḽ"))
        if not os.path.exists(bstack1l1l111ll1l_opy_):
            os.makedirs(bstack1l1l111ll1l_opy_, mode=0o777, exist_ok=True)
        return bstack1l1l111ll1l_opy_
    else:
        raise FileNotFoundError(bstack1ll1ll1_opy_ (u"ࠢࡏࡱࠣࡻࡷ࡯ࡴࡢࡤ࡯ࡩࠥࡪࡩࡳࡧࡦࡸࡴࡸࡹࠡࡣࡹࡥ࡮ࡲࡡࡣ࡮ࡨࠤ࡫ࡵࡲࠡࡶ࡫ࡩ࡙ࠥࡄࡌࠢࡥ࡭ࡳࡧࡲࡺ࠰ࠥḾ"))
def bstack1l11lll11ll_opy_(bstack1l1l111ll1l_opy_):
    bstack1ll1ll1_opy_ (u"ࠣࠤࠥࡋࡪࡺࠠࡵࡪࡨࠤࡵࡧࡴࡩࠢࡩࡳࡷࠦࡴࡩࡧࠣࡆࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࠢࡖࡈࡐࠦࡢࡪࡰࡤࡶࡾࠦࡩ࡯ࠢࡤࠤࡼࡸࡩࡵࡣࡥࡰࡪࠦࡤࡪࡴࡨࡧࡹࡵࡲࡺ࠰ࠥࠦࠧḿ")
    bstack111l1lll111_opy_ = [
        os.path.join(bstack1l1l111ll1l_opy_, f)
        for f in os.listdir(bstack1l1l111ll1l_opy_)
        if os.path.isfile(os.path.join(bstack1l1l111ll1l_opy_, f)) and f.startswith(bstack1ll1ll1_opy_ (u"ࠤࡥ࡭ࡳࡧࡲࡺ࠯ࠥṀ"))
    ]
    if len(bstack111l1lll111_opy_) > 0:
        return max(bstack111l1lll111_opy_, key=os.path.getmtime) # get bstack1111ll1111l_opy_ binary
    return bstack1ll1ll1_opy_ (u"ࠥࠦṁ")
def bstack111l1l1l1ll_opy_():
  from selenium import webdriver
  return version.parse(webdriver.__version__)
def bstack1l111l1l1l1_opy_(d, u):
  for k, v in u.items():
    if isinstance(v, collections.abc.Mapping):
      d[k] = bstack1l111l1l1l1_opy_(d.get(k, {}), v)
    else:
      if isinstance(v, list):
        d[k] = d.get(k, []) + v
      else:
        d[k] = v
  return d
def bstack11l1l1l11_opy_(data, keys, default=None):
    bstack1ll1ll1_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࡘࡧࡦࡦ࡮ࡼࠤ࡬࡫ࡴࠡࡣࠣࡲࡪࡹࡴࡦࡦࠣࡺࡦࡲࡵࡦࠢࡩࡶࡴࡳࠠࡢࠢࡧ࡭ࡨࡺࡩࡰࡰࡤࡶࡾࠦ࡯ࡳࠢ࡯࡭ࡸࡺ࠮ࠋࠢࠣࠤࠥࡀࡰࡢࡴࡤࡱࠥࡪࡡࡵࡣ࠽ࠤ࡙࡮ࡥࠡࡦ࡬ࡧࡹ࡯࡯࡯ࡣࡵࡽࠥࡵࡲࠡ࡮࡬ࡷࡹࠦࡴࡰࠢࡷࡶࡦࡼࡥࡳࡵࡨ࠲ࠏࠦࠠࠡࠢ࠽ࡴࡦࡸࡡ࡮ࠢ࡮ࡩࡾࡹ࠺ࠡࡃࠣࡰ࡮ࡹࡴࠡࡱࡩࠤࡰ࡫ࡹࡴ࠱࡬ࡲࡩ࡯ࡣࡦࡵࠣࡶࡪࡶࡲࡦࡵࡨࡲࡹ࡯࡮ࡨࠢࡷ࡬ࡪࠦࡰࡢࡶ࡫࠲ࠏࠦࠠࠡࠢ࠽ࡴࡦࡸࡡ࡮ࠢࡧࡩ࡫ࡧࡵ࡭ࡶ࠽ࠤ࡛ࡧ࡬ࡶࡧࠣࡸࡴࠦࡲࡦࡶࡸࡶࡳࠦࡩࡧࠢࡷ࡬ࡪࠦࡰࡢࡶ࡫ࠤࡩࡵࡥࡴࠢࡱࡳࡹࠦࡥࡹ࡫ࡶࡸ࠳ࠐࠠࠡࠢࠣ࠾ࡷ࡫ࡴࡶࡴࡱ࠾࡚ࠥࡨࡦࠢࡹࡥࡱࡻࡥࠡࡣࡷࠤࡹ࡮ࡥࠡࡰࡨࡷࡹ࡫ࡤࠡࡲࡤࡸ࡭࠲ࠠࡰࡴࠣࡨࡪ࡬ࡡࡶ࡮ࡷࠤ࡮࡬ࠠ࡯ࡱࡷࠤ࡫ࡵࡵ࡯ࡦ࠱ࠎࠥࠦࠠࠡࠤࠥࠦṂ")
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