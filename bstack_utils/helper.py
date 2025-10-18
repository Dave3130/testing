# coding: UTF-8
import sys
bstack11ll1l1_opy_ = sys.version_info [0] == 2
bstack11111ll_opy_ = 2048
bstack111lll1_opy_ = 7
def bstack1l1lll1_opy_ (bstack1lllll_opy_):
    global bstack111111l_opy_
    bstack1llll_opy_ = ord (bstack1lllll_opy_ [-1])
    bstack11lll1l_opy_ = bstack1lllll_opy_ [:-1]
    bstack1111_opy_ = bstack1llll_opy_ % len (bstack11lll1l_opy_)
    bstack11ll11l_opy_ = bstack11lll1l_opy_ [:bstack1111_opy_] + bstack11lll1l_opy_ [bstack1111_opy_:]
    if bstack11ll1l1_opy_:
        bstack1llll1_opy_ = unicode () .join ([unichr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    else:
        bstack1llll1_opy_ = str () .join ([chr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    return eval (bstack1llll1_opy_)
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
from bstack_utils.constants import (bstack1lll1111ll_opy_, bstack111lllll11_opy_, bstack1111llll11_opy_,
                                    bstack11l11llll1l_opy_, bstack11l1l111111_opy_, bstack11l1l1ll1ll_opy_, bstack11l1l1ll111_opy_)
from bstack_utils.measure import measure
from bstack_utils.messages import bstack1ll111l111_opy_, bstack11111l11l1_opy_
from bstack_utils.proxy import bstack11l1l11ll_opy_, bstack11lll11ll_opy_
from bstack_utils.constants import *
from bstack_utils import bstack111l11l1l_opy_
from bstack_utils.bstack1l1111llll_opy_ import bstack1l111l11l_opy_
from browserstack_sdk._version import __version__
bstack1111111l_opy_ = Config.bstack11l11l1l_opy_()
logger = bstack111l11l1l_opy_.get_logger(__name__, bstack111l11l1l_opy_.bstack1l11lllll1l_opy_())
def bstack111l1111l1l_opy_(config):
    return config[bstack1l1lll1_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧᯆ")]
def bstack111l11ll1ll_opy_(config):
    return config[bstack1l1lll1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩᯇ")]
def bstack1l11l1l1l_opy_():
    try:
        import playwright
        return True
    except ImportError:
        return False
def bstack1111ll1l1ll_opy_(obj):
    values = []
    bstack1111lll1lll_opy_ = re.compile(bstack1l1lll1_opy_ (u"ࡲࠣࡠࡆ࡙ࡘ࡚ࡏࡎࡡࡗࡅࡌࡥ࡜ࡥ࠭ࠧࠦᯈ"), re.I)
    for key in obj.keys():
        if bstack1111lll1lll_opy_.match(key):
            values.append(obj[key])
    return values
def bstack111l1llllll_opy_(config):
    tags = []
    tags.extend(bstack1111ll1l1ll_opy_(os.environ))
    tags.extend(bstack1111ll1l1ll_opy_(config))
    return tags
def bstack1111lllll1l_opy_(markers):
    tags = []
    for marker in markers:
        tags.append(marker.name)
    return tags
def bstack1111ll11ll1_opy_(bstack111l1l1l11l_opy_):
    if not bstack111l1l1l11l_opy_:
        return bstack1l1lll1_opy_ (u"ࠨࠩᯉ")
    return bstack1l1lll1_opy_ (u"ࠤࡾࢁࠥ࠮ࡻࡾࠫࠥᯊ").format(bstack111l1l1l11l_opy_.name, bstack111l1l1l11l_opy_.email)
def bstack1111llll1ll_opy_():
    try:
        repo = git.Repo(search_parent_directories=True)
        bstack111l1lllll1_opy_ = repo.common_dir
        info = {
            bstack1l1lll1_opy_ (u"ࠥࡷ࡭ࡧࠢᯋ"): repo.head.commit.hexsha,
            bstack1l1lll1_opy_ (u"ࠦࡸ࡮࡯ࡳࡶࡢࡷ࡭ࡧࠢᯌ"): repo.git.rev_parse(repo.head.commit, short=True),
            bstack1l1lll1_opy_ (u"ࠧࡨࡲࡢࡰࡦ࡬ࠧᯍ"): repo.active_branch.name,
            bstack1l1lll1_opy_ (u"ࠨࡴࡢࡩࠥᯎ"): repo.git.describe(all=True, tags=True, exact_match=True),
            bstack1l1lll1_opy_ (u"ࠢࡤࡱࡰࡱ࡮ࡺࡴࡦࡴࠥᯏ"): bstack1111ll11ll1_opy_(repo.head.commit.committer),
            bstack1l1lll1_opy_ (u"ࠣࡥࡲࡱࡲ࡯ࡴࡵࡧࡵࡣࡩࡧࡴࡦࠤᯐ"): repo.head.commit.committed_datetime.isoformat(),
            bstack1l1lll1_opy_ (u"ࠤࡤࡹࡹ࡮࡯ࡳࠤᯑ"): bstack1111ll11ll1_opy_(repo.head.commit.author),
            bstack1l1lll1_opy_ (u"ࠥࡥࡺࡺࡨࡰࡴࡢࡨࡦࡺࡥࠣᯒ"): repo.head.commit.authored_datetime.isoformat(),
            bstack1l1lll1_opy_ (u"ࠦࡨࡵ࡭࡮࡫ࡷࡣࡲ࡫ࡳࡴࡣࡪࡩࠧᯓ"): repo.head.commit.message,
            bstack1l1lll1_opy_ (u"ࠧࡸ࡯ࡰࡶࠥᯔ"): repo.git.rev_parse(bstack1l1lll1_opy_ (u"ࠨ࠭࠮ࡵ࡫ࡳࡼ࠳ࡴࡰࡲ࡯ࡩࡻ࡫࡬ࠣᯕ")),
            bstack1l1lll1_opy_ (u"ࠢࡤࡱࡰࡱࡴࡴ࡟ࡨ࡫ࡷࡣࡩ࡯ࡲࠣᯖ"): bstack111l1lllll1_opy_,
            bstack1l1lll1_opy_ (u"ࠣࡹࡲࡶࡰࡺࡲࡦࡧࡢ࡫࡮ࡺ࡟ࡥ࡫ࡵࠦᯗ"): subprocess.check_output([bstack1l1lll1_opy_ (u"ࠤࡪ࡭ࡹࠨᯘ"), bstack1l1lll1_opy_ (u"ࠥࡶࡪࡼ࠭ࡱࡣࡵࡷࡪࠨᯙ"), bstack1l1lll1_opy_ (u"ࠦ࠲࠳ࡧࡪࡶ࠰ࡧࡴࡳ࡭ࡰࡰ࠰ࡨ࡮ࡸࠢᯚ")]).strip().decode(
                bstack1l1lll1_opy_ (u"ࠬࡻࡴࡧ࠯࠻ࠫᯛ")),
            bstack1l1lll1_opy_ (u"ࠨ࡬ࡢࡵࡷࡣࡹࡧࡧࠣᯜ"): repo.git.describe(tags=True, abbrev=0, always=True),
            bstack1l1lll1_opy_ (u"ࠢࡤࡱࡰࡱ࡮ࡺࡳࡠࡵ࡬ࡲࡨ࡫࡟࡭ࡣࡶࡸࡤࡺࡡࡨࠤᯝ"): repo.git.rev_list(
                bstack1l1lll1_opy_ (u"ࠣࡽࢀ࠲࠳ࢁࡽࠣᯞ").format(repo.head.commit, repo.git.describe(tags=True, abbrev=0, always=True)), count=True)
        }
        remotes = repo.remotes
        bstack111l1l1111l_opy_ = []
        for remote in remotes:
            bstack111l1l1lll1_opy_ = {
                bstack1l1lll1_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᯟ"): remote.name,
                bstack1l1lll1_opy_ (u"ࠥࡹࡷࡲࠢᯠ"): remote.url,
            }
            bstack111l1l1111l_opy_.append(bstack111l1l1lll1_opy_)
        bstack111l111l1l1_opy_ = {
            bstack1l1lll1_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᯡ"): bstack1l1lll1_opy_ (u"ࠧ࡭ࡩࡵࠤᯢ"),
            **info,
            bstack1l1lll1_opy_ (u"ࠨࡲࡦ࡯ࡲࡸࡪࡹࠢᯣ"): bstack111l1l1111l_opy_
        }
        bstack111l111l1l1_opy_ = bstack1111llll1l1_opy_(bstack111l111l1l1_opy_)
        return bstack111l111l1l1_opy_
    except git.InvalidGitRepositoryError:
        return {}
    except Exception as err:
        print(bstack1l1lll1_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡰࡰࡲࡸࡰࡦࡺࡩ࡯ࡩࠣࡋ࡮ࡺࠠ࡮ࡧࡷࡥࡩࡧࡴࡢࠢࡺ࡭ࡹ࡮ࠠࡦࡴࡵࡳࡷࡀࠠࡼࡿࠥᯤ").format(err))
        return {}
def bstack11lll11l11l_opy_(bstack111l1lll1l1_opy_=None):
    bstack1l1lll1_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࡉࡨࡸࠥ࡭ࡩࡵࠢࡰࡩࡹࡧࡤࡢࡶࡤࠤࡸࡶࡥࡤ࡫ࡩ࡭ࡨࡧ࡬࡭ࡻࠣࡪࡴࡸ࡭ࡢࡶࡷࡩࡩࠦࡦࡰࡴࠣࡅࡎࠦࡳࡦ࡮ࡨࡧࡹ࡯࡯࡯ࠢࡸࡷࡪࠦࡣࡢࡵࡨࡷࠥ࡬࡯ࡳࠢࡨࡥࡨ࡮ࠠࡧࡱ࡯ࡨࡪࡸࠠࡪࡰࠣࡸ࡭࡫ࠠ࡭࡫ࡶࡸ࠳ࠐࠠࠡࠢࠣࡅࡷ࡭ࡳ࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࡪࡴࡲࡤࡦࡴࡶࠤ࠭ࡲࡩࡴࡶ࠯ࠤࡴࡶࡴࡪࡱࡱࡥࡱ࠯࠺ࠡࡎ࡬ࡷࡹࠦ࡯ࡧࠢࡩࡳࡱࡪࡥࡳࠢࡳࡥࡹ࡮ࡳࠡࡶࡲࠤࡪࡾࡴࡳࡣࡦࡸࠥ࡭ࡩࡵࠢࡰࡩࡹࡧࡤࡢࡶࡤࠤ࡫ࡸ࡯࡮࠰ࠣࡈࡪ࡬ࡡࡶ࡮ࡷࡷࠥࡺ࡯ࠡ࡝ࡲࡷ࠳࡭ࡥࡵࡥࡺࡨ࠭࠯࡝࠯ࠌࠣࠤࠥࠦࡒࡦࡶࡸࡶࡳࡹ࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢ࡯࡭ࡸࡺ࠺ࠡࡎ࡬ࡷࡹࠦ࡯ࡧࠢࡧ࡭ࡨࡺࡳ࠭ࠢࡨࡥࡨ࡮ࠠࡤࡱࡱࡸࡦ࡯࡮ࡪࡰࡪࠤ࡬࡯ࡴࠡ࡯ࡨࡸࡦࡪࡡࡵࡣࠣࡪࡴࡸࠠࡢࠢࡩࡳࡱࡪࡥࡳ࠰ࠍࠤࠥࠦࠠࠣࠤࠥᯥ")
    if bstack111l1lll1l1_opy_ == None: # bstack111l11l11ll_opy_ for bstack11lll1111ll_opy_-repo
        bstack111l1lll1l1_opy_ = [os.getcwd()]
    results = []
    for folder in bstack111l1lll1l1_opy_:
        try:
            repo = git.Repo(folder, search_parent_directories=True)
            result = {
                bstack1l1lll1_opy_ (u"ࠤࡳࡶࡎࡪ᯦ࠢ"): bstack1l1lll1_opy_ (u"ࠥࠦᯧ"),
                bstack1l1lll1_opy_ (u"ࠦ࡫࡯࡬ࡦࡵࡆ࡬ࡦࡴࡧࡦࡦࠥᯨ"): [],
                bstack1l1lll1_opy_ (u"ࠧࡧࡵࡵࡪࡲࡶࡸࠨᯩ"): [],
                bstack1l1lll1_opy_ (u"ࠨࡰࡳࡆࡤࡸࡪࠨᯪ"): bstack1l1lll1_opy_ (u"ࠢࠣᯫ"),
                bstack1l1lll1_opy_ (u"ࠣࡥࡲࡱࡲ࡯ࡴࡎࡧࡶࡷࡦ࡭ࡥࡴࠤᯬ"): [],
                bstack1l1lll1_opy_ (u"ࠤࡳࡶ࡙࡯ࡴ࡭ࡧࠥᯭ"): bstack1l1lll1_opy_ (u"ࠥࠦᯮ"),
                bstack1l1lll1_opy_ (u"ࠦࡵࡸࡄࡦࡵࡦࡶ࡮ࡶࡴࡪࡱࡱࠦᯯ"): bstack1l1lll1_opy_ (u"ࠧࠨᯰ"),
                bstack1l1lll1_opy_ (u"ࠨࡰࡳࡔࡤࡻࡉ࡯ࡦࡧࠤᯱ"): bstack1l1lll1_opy_ (u"᯲ࠢࠣ")
            }
            bstack111l11l1l1l_opy_ = repo.active_branch.name
            bstack1111l1l11ll_opy_ = repo.head.commit
            result[bstack1l1lll1_opy_ (u"ࠣࡲࡵࡍࡩࠨ᯳")] = bstack1111l1l11ll_opy_.hexsha
            bstack1111ll11l1l_opy_ = _111l1l11l1l_opy_(repo)
            logger.debug(bstack1l1lll1_opy_ (u"ࠤࡅࡥࡸ࡫ࠠࡣࡴࡤࡲࡨ࡮ࠠࡧࡱࡵࠤࡨࡵ࡭ࡱࡣࡵ࡭ࡸࡵ࡮࠻ࠢࠥ᯴") + str(bstack1111ll11l1l_opy_) + bstack1l1lll1_opy_ (u"ࠥࠦ᯵"))
            if bstack1111ll11l1l_opy_:
                try:
                    bstack1111l1l1l1l_opy_ = repo.git.diff(bstack1l1lll1_opy_ (u"ࠦ࠲࠳࡮ࡢ࡯ࡨ࠱ࡴࡴ࡬ࡺࠤ᯶"), bstack1lll1ll1l11_opy_ (u"ࠧࢁࡢࡢࡵࡨࡣࡧࡸࡡ࡯ࡥ࡫ࢁ࠳࠴࠮ࡼࡥࡸࡶࡷ࡫࡮ࡵࡡࡥࡶࡦࡴࡣࡩࡿࠥ᯷")).split(bstack1l1lll1_opy_ (u"࠭࡜࡯ࠩ᯸"))
                    logger.debug(bstack1l1lll1_opy_ (u"ࠢࡄࡪࡤࡲ࡬࡫ࡤࠡࡨ࡬ࡰࡪࡹࠠࡣࡧࡷࡻࡪ࡫࡮ࠡࡽࡥࡥࡸ࡫࡟ࡣࡴࡤࡲࡨ࡮ࡽࠡࡣࡱࡨࠥࢁࡣࡶࡴࡵࡩࡳࡺ࡟ࡣࡴࡤࡲࡨ࡮ࡽ࠻ࠢࠥ᯹") + str(bstack1111l1l1l1l_opy_) + bstack1l1lll1_opy_ (u"ࠣࠤ᯺"))
                    result[bstack1l1lll1_opy_ (u"ࠤࡩ࡭ࡱ࡫ࡳࡄࡪࡤࡲ࡬࡫ࡤࠣ᯻")] = [f.strip() for f in bstack1111l1l1l1l_opy_ if f.strip()]
                    commits = list(repo.iter_commits(bstack1lll1ll1l11_opy_ (u"ࠥࡿࡧࡧࡳࡦࡡࡥࡶࡦࡴࡣࡩࡿ࠱࠲ࢀࡩࡵࡳࡴࡨࡲࡹࡥࡢࡳࡣࡱࡧ࡭ࢃࠢ᯼")))
                except Exception:
                    logger.debug(bstack1l1lll1_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡨࡧࡷࠤࡨ࡮ࡡ࡯ࡩࡨࡨࠥ࡬ࡩ࡭ࡧࡶࠤ࡫ࡸ࡯࡮ࠢࡥࡶࡦࡴࡣࡩࠢࡦࡳࡲࡶࡡࡳ࡫ࡶࡳࡳ࠴ࠠࡇࡣ࡯ࡰ࡮ࡴࡧࠡࡤࡤࡧࡰࠦࡴࡰࠢࡵࡩࡨ࡫࡮ࡵࠢࡦࡳࡲࡳࡩࡵࡵ࠱ࠦ᯽"))
                    commits = list(repo.iter_commits(max_count=10))
                    if commits:
                        result[bstack1l1lll1_opy_ (u"ࠧ࡬ࡩ࡭ࡧࡶࡇ࡭ࡧ࡮ࡨࡧࡧࠦ᯾")] = _1111lll11l1_opy_(commits[:5])
            else:
                commits = list(repo.iter_commits(max_count=10))
                if commits:
                    result[bstack1l1lll1_opy_ (u"ࠨࡦࡪ࡮ࡨࡷࡈ࡮ࡡ࡯ࡩࡨࡨࠧ᯿")] = _1111lll11l1_opy_(commits[:5])
            bstack111l1l1l111_opy_ = set()
            bstack1111ll1lll1_opy_ = []
            for commit in commits:
                logger.debug(bstack1l1lll1_opy_ (u"ࠢࡑࡴࡲࡧࡪࡹࡳࡪࡰࡪࠤࡨࡵ࡭࡮࡫ࡷ࠾ࠥࠨᰀ") + str(commit.message) + bstack1l1lll1_opy_ (u"ࠣࠤᰁ"))
                bstack111l111l11l_opy_ = commit.author.name if commit.author else bstack1l1lll1_opy_ (u"ࠤࡘࡲࡰࡴ࡯ࡸࡰࠥᰂ")
                bstack111l1l1l111_opy_.add(bstack111l111l11l_opy_)
                bstack1111ll1lll1_opy_.append({
                    bstack1l1lll1_opy_ (u"ࠥࡱࡪࡹࡳࡢࡩࡨࠦᰃ"): commit.message.strip(),
                    bstack1l1lll1_opy_ (u"ࠦࡺࡹࡥࡳࠤᰄ"): bstack111l111l11l_opy_
                })
            result[bstack1l1lll1_opy_ (u"ࠧࡧࡵࡵࡪࡲࡶࡸࠨᰅ")] = list(bstack111l1l1l111_opy_)
            result[bstack1l1lll1_opy_ (u"ࠨࡣࡰ࡯ࡰ࡭ࡹࡓࡥࡴࡵࡤ࡫ࡪࡹࠢᰆ")] = bstack1111ll1lll1_opy_
            result[bstack1l1lll1_opy_ (u"ࠢࡱࡴࡇࡥࡹ࡫ࠢᰇ")] = bstack1111l1l11ll_opy_.committed_datetime.strftime(bstack1l1lll1_opy_ (u"ࠣࠧ࡜࠱ࠪࡳ࠭ࠦࡦࠥᰈ"))
            if (not result[bstack1l1lll1_opy_ (u"ࠤࡳࡶ࡙࡯ࡴ࡭ࡧࠥᰉ")] or result[bstack1l1lll1_opy_ (u"ࠥࡴࡷ࡚ࡩࡵ࡮ࡨࠦᰊ")].strip() == bstack1l1lll1_opy_ (u"ࠦࠧᰋ")) and bstack1111l1l11ll_opy_.message:
                bstack111l11ll111_opy_ = bstack1111l1l11ll_opy_.message.strip().splitlines()
                result[bstack1l1lll1_opy_ (u"ࠧࡶࡲࡕ࡫ࡷࡰࡪࠨᰌ")] = bstack111l11ll111_opy_[0] if bstack111l11ll111_opy_ else bstack1l1lll1_opy_ (u"ࠨࠢᰍ")
                if len(bstack111l11ll111_opy_) > 2:
                    result[bstack1l1lll1_opy_ (u"ࠢࡱࡴࡇࡩࡸࡩࡲࡪࡲࡷ࡭ࡴࡴࠢᰎ")] = bstack1l1lll1_opy_ (u"ࠨ࡞ࡱࠫᰏ").join(bstack111l11ll111_opy_[2:]).strip()
            results.append(result)
        except Exception as err:
            logger.info(bstack1l1lll1_opy_ (u"ࠤ࡞ࡎࡉࡣࠠࡄࡷࡵࡶࡪࡴࡴࠡࡒ࡚ࡈࠥࡖࡡࡵࡪ࠽ࠤࠧᰐ") + str(os.getcwd()) + bstack1l1lll1_opy_ (u"ࠥࠦᰑ"))
            logger.error(bstack1l1lll1_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡴࡶࡵ࡭ࡣࡷ࡭ࡳ࡭ࠠࡈ࡫ࡷࠤࡲ࡫ࡴࡢࡦࡤࡸࡦࠦࡦࡰࡴࠣࡅࡎࠦࡳࡦ࡮ࡨࡧࡹ࡯࡯࡯ࠢࠫࡪࡴࡲࡤࡦࡴ࠽ࠤࢀ࡬࡯࡭ࡦࡨࡶࢂ࠯࠺ࠡࠤᰒ") + str(str(err)) + bstack1l1lll1_opy_ (u"ࠧࠨᰓ"))
    filtered_results = [
        result
        for result in results
        if _1111l1l111l_opy_(result)
    ]
    return filtered_results
def _1111l1l111l_opy_(result):
    bstack1l1lll1_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࡈࡦ࡮ࡳࡩࡷࠦࡴࡰࠢࡦ࡬ࡪࡩ࡫ࠡ࡫ࡩࠤࡦࠦࡧࡪࡶࠣࡱࡪࡺࡡࡥࡣࡷࡥࠥࡸࡥࡴࡷ࡯ࡸࠥ࡯ࡳࠡࡸࡤࡰ࡮ࡪࠠࠩࡰࡲࡲ࠲࡫࡭ࡱࡶࡼࠤ࡫࡯࡬ࡦࡵࡆ࡬ࡦࡴࡧࡦࡦࠣࡥࡳࡪࠠࡢࡷࡷ࡬ࡴࡸࡳࠪ࠰ࠍࠤࠥࠦࠠࠣࠤࠥᰔ")
    return (
        isinstance(result.get(bstack1l1lll1_opy_ (u"ࠢࡧ࡫࡯ࡩࡸࡉࡨࡢࡰࡪࡩࡩࠨᰕ"), None), list)
        and len(result[bstack1l1lll1_opy_ (u"ࠣࡨ࡬ࡰࡪࡹࡃࡩࡣࡱ࡫ࡪࡪࠢᰖ")]) > 0
        and isinstance(result.get(bstack1l1lll1_opy_ (u"ࠤࡤࡹࡹ࡮࡯ࡳࡵࠥᰗ"), None), list)
        and len(result[bstack1l1lll1_opy_ (u"ࠥࡥࡺࡺࡨࡰࡴࡶࠦᰘ")]) > 0
    )
def _111l1l11l1l_opy_(repo):
    bstack1l1lll1_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤ࡙ࡸࡹࠡࡶࡲࠤࡩ࡫ࡴࡦࡴࡰ࡭ࡳ࡫ࠠࡵࡪࡨࠤࡧࡧࡳࡦࠢࡥࡶࡦࡴࡣࡩࠢࡩࡳࡷࠦࡴࡩࡧࠣ࡫࡮ࡼࡥ࡯ࠢࡵࡩࡵࡵࠠࡸ࡫ࡷ࡬ࡴࡻࡴࠡࡪࡤࡶࡩࡩ࡯ࡥࡧࡧࠤࡳࡧ࡭ࡦࡵࠣࡥࡳࡪࠠࡸࡱࡵ࡯ࠥࡽࡩࡵࡪࠣࡥࡱࡲࠠࡗࡅࡖࠤࡵࡸ࡯ࡷ࡫ࡧࡩࡷࡹ࠮ࠋࠢࠣࠤࠥࡘࡥࡵࡷࡵࡲࡸࠦࡴࡩࡧࠣࡨࡪ࡬ࡡࡶ࡮ࡷࠤࡧࡸࡡ࡯ࡥ࡫ࠤ࡮࡬ࠠࡱࡱࡶࡷ࡮ࡨ࡬ࡦ࠮ࠣࡩࡱࡹࡥࠡࡐࡲࡲࡪ࠴ࠊࠡࠢࠣࠤࠧࠨࠢᰙ")
    try:
        try:
            origin = repo.remotes.origin
            bstack111l1ll1ll1_opy_ = origin.refs[bstack1l1lll1_opy_ (u"ࠬࡎࡅࡂࡆࠪᰚ")]
            target = bstack111l1ll1ll1_opy_.reference.name
            if target.startswith(bstack1l1lll1_opy_ (u"࠭࡯ࡳ࡫ࡪ࡭ࡳ࠵ࠧᰛ")):
                return target
        except Exception:
            pass
        if repo.remotes and repo.remotes.origin.refs:
            for ref in repo.remotes.origin.refs:
                if ref.name.startswith(bstack1l1lll1_opy_ (u"ࠧࡰࡴ࡬࡫࡮ࡴ࠯ࠨᰜ")):
                    return ref.name
        if repo.heads:
            return repo.heads[0].name
    except Exception:
        pass
    return None
def _1111lll11l1_opy_(commits):
    bstack1l1lll1_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࡉࡨࡸࠥࡲࡩࡴࡶࠣࡳ࡫ࠦࡣࡩࡣࡱ࡫ࡪࡪࠠࡧ࡫࡯ࡩࡸࠦࡦࡳࡱࡰࠤࡦࠦ࡬ࡪࡵࡷࠤࡴ࡬ࠠࡤࡱࡰࡱ࡮ࡺࡳ࠯ࠌࠣࠤࠥࠦࠢࠣࠤᰝ")
    bstack1111l1l1l1l_opy_ = set()
    try:
        for commit in commits:
            if commit.parents:
                for parent in commit.parents:
                    diff = commit.diff(parent)
                    for bstack111l11ll1l1_opy_ in diff:
                        if bstack111l11ll1l1_opy_.a_path:
                            bstack1111l1l1l1l_opy_.add(bstack111l11ll1l1_opy_.a_path)
                        if bstack111l11ll1l1_opy_.b_path:
                            bstack1111l1l1l1l_opy_.add(bstack111l11ll1l1_opy_.b_path)
    except Exception:
        pass
    return list(bstack1111l1l1l1l_opy_)
def bstack1111llll1l1_opy_(bstack111l111l1l1_opy_):
    bstack111ll11111l_opy_ = bstack1111ll1ll11_opy_(bstack111l111l1l1_opy_)
    if bstack111ll11111l_opy_ and bstack111ll11111l_opy_ > bstack11l11llll1l_opy_:
        bstack111l11ll11l_opy_ = bstack111ll11111l_opy_ - bstack11l11llll1l_opy_
        bstack111l111llll_opy_ = bstack111l1ll1111_opy_(bstack111l111l1l1_opy_[bstack1l1lll1_opy_ (u"ࠤࡦࡳࡲࡳࡩࡵࡡࡰࡩࡸࡹࡡࡨࡧࠥᰞ")], bstack111l11ll11l_opy_)
        bstack111l111l1l1_opy_[bstack1l1lll1_opy_ (u"ࠥࡧࡴࡳ࡭ࡪࡶࡢࡱࡪࡹࡳࡢࡩࡨࠦᰟ")] = bstack111l111llll_opy_
        logger.info(bstack1l1lll1_opy_ (u"࡙ࠦ࡮ࡥࠡࡥࡲࡱࡲ࡯ࡴࠡࡪࡤࡷࠥࡨࡥࡦࡰࠣࡸࡷࡻ࡮ࡤࡣࡷࡩࡩ࠴ࠠࡔ࡫ࡽࡩࠥࡵࡦࠡࡥࡲࡱࡲ࡯ࡴࠡࡣࡩࡸࡪࡸࠠࡵࡴࡸࡲࡨࡧࡴࡪࡱࡱࠤ࡮ࡹࠠࡼࡿࠣࡏࡇࠨᰠ")
                    .format(bstack1111ll1ll11_opy_(bstack111l111l1l1_opy_) / 1024))
    return bstack111l111l1l1_opy_
def bstack1111ll1ll11_opy_(json_data):
    try:
        if json_data:
            bstack111ll1111l1_opy_ = json.dumps(json_data)
            bstack1111llll111_opy_ = sys.getsizeof(bstack111ll1111l1_opy_)
            return bstack1111llll111_opy_
    except Exception as e:
        logger.debug(bstack1l1lll1_opy_ (u"࡙ࠧ࡯࡮ࡧࡷ࡬࡮ࡴࡧࠡࡹࡨࡲࡹࠦࡷࡳࡱࡱ࡫ࠥࡽࡨࡪ࡮ࡨࠤࡨࡧ࡬ࡤࡷ࡯ࡥࡹ࡯࡮ࡨࠢࡶ࡭ࡿ࡫ࠠࡰࡨࠣࡎࡘࡕࡎࠡࡱࡥ࡮ࡪࡩࡴ࠻ࠢࡾࢁࠧᰡ").format(e))
    return -1
def bstack111l1ll1111_opy_(field, bstack111l1111ll1_opy_):
    try:
        bstack111l11l111l_opy_ = len(bytes(bstack11l1l111111_opy_, bstack1l1lll1_opy_ (u"࠭ࡵࡵࡨ࠰࠼ࠬᰢ")))
        bstack111l1l1ll1l_opy_ = bytes(field, bstack1l1lll1_opy_ (u"ࠧࡶࡶࡩ࠱࠽࠭ᰣ"))
        bstack111l1l11111_opy_ = len(bstack111l1l1ll1l_opy_)
        bstack111l11l1l11_opy_ = ceil(bstack111l1l11111_opy_ - bstack111l1111ll1_opy_ - bstack111l11l111l_opy_)
        if bstack111l11l1l11_opy_ > 0:
            bstack1111l1lllll_opy_ = bstack111l1l1ll1l_opy_[:bstack111l11l1l11_opy_].decode(bstack1l1lll1_opy_ (u"ࠨࡷࡷࡪ࠲࠾ࠧᰤ"), errors=bstack1l1lll1_opy_ (u"ࠩ࡬࡫ࡳࡵࡲࡦࠩᰥ")) + bstack11l1l111111_opy_
            return bstack1111l1lllll_opy_
    except Exception as e:
        logger.debug(bstack1l1lll1_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡺ࡬࡮ࡲࡥࠡࡶࡵࡹࡳࡩࡡࡵ࡫ࡱ࡫ࠥ࡬ࡩࡦ࡮ࡧ࠰ࠥࡴ࡯ࡵࡪ࡬ࡲ࡬ࠦࡷࡢࡵࠣࡸࡷࡻ࡮ࡤࡣࡷࡩࡩࠦࡨࡦࡴࡨ࠾ࠥࢁࡽࠣᰦ").format(e))
    return field
def bstack11lll11l11_opy_():
    env = os.environ
    if (bstack1l1lll1_opy_ (u"ࠦࡏࡋࡎࡌࡋࡑࡗࡤ࡛ࡒࡍࠤᰧ") in env and len(env[bstack1l1lll1_opy_ (u"ࠧࡐࡅࡏࡍࡌࡒࡘࡥࡕࡓࡎࠥᰨ")]) > 0) or (
            bstack1l1lll1_opy_ (u"ࠨࡊࡆࡐࡎࡍࡓ࡙࡟ࡉࡑࡐࡉࠧᰩ") in env and len(env[bstack1l1lll1_opy_ (u"ࠢࡋࡇࡑࡏࡎࡔࡓࡠࡊࡒࡑࡊࠨᰪ")]) > 0):
        return {
            bstack1l1lll1_opy_ (u"ࠣࡰࡤࡱࡪࠨᰫ"): bstack1l1lll1_opy_ (u"ࠤࡍࡩࡳࡱࡩ࡯ࡵࠥᰬ"),
            bstack1l1lll1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᰭ"): env.get(bstack1l1lll1_opy_ (u"ࠦࡇ࡛ࡉࡍࡆࡢ࡙ࡗࡒࠢᰮ")),
            bstack1l1lll1_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᰯ"): env.get(bstack1l1lll1_opy_ (u"ࠨࡊࡐࡄࡢࡒࡆࡓࡅࠣᰰ")),
            bstack1l1lll1_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᰱ"): env.get(bstack1l1lll1_opy_ (u"ࠣࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘࠢᰲ"))
        }
    if env.get(bstack1l1lll1_opy_ (u"ࠤࡆࡍࠧᰳ")) == bstack1l1lll1_opy_ (u"ࠥࡸࡷࡻࡥࠣᰴ") and bstack111ll11ll_opy_(env.get(bstack1l1lll1_opy_ (u"ࠦࡈࡏࡒࡄࡎࡈࡇࡎࠨᰵ"))):
        return {
            bstack1l1lll1_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᰶ"): bstack1l1lll1_opy_ (u"ࠨࡃࡪࡴࡦࡰࡪࡉࡉ᰷ࠣ"),
            bstack1l1lll1_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥ᰸"): env.get(bstack1l1lll1_opy_ (u"ࠣࡅࡌࡖࡈࡒࡅࡠࡄࡘࡍࡑࡊ࡟ࡖࡔࡏࠦ᰹")),
            bstack1l1lll1_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦ᰺"): env.get(bstack1l1lll1_opy_ (u"ࠥࡇࡎࡘࡃࡍࡇࡢࡎࡔࡈࠢ᰻")),
            bstack1l1lll1_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥ᰼"): env.get(bstack1l1lll1_opy_ (u"ࠧࡉࡉࡓࡅࡏࡉࡤࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࠣ᰽"))
        }
    if env.get(bstack1l1lll1_opy_ (u"ࠨࡃࡊࠤ᰾")) == bstack1l1lll1_opy_ (u"ࠢࡵࡴࡸࡩࠧ᰿") and bstack111ll11ll_opy_(env.get(bstack1l1lll1_opy_ (u"ࠣࡖࡕࡅ࡛ࡏࡓࠣ᱀"))):
        return {
            bstack1l1lll1_opy_ (u"ࠤࡱࡥࡲ࡫ࠢ᱁"): bstack1l1lll1_opy_ (u"ࠥࡘࡷࡧࡶࡪࡵࠣࡇࡎࠨ᱂"),
            bstack1l1lll1_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢ᱃"): env.get(bstack1l1lll1_opy_ (u"࡚ࠧࡒࡂࡘࡌࡗࡤࡈࡕࡊࡎࡇࡣ࡜ࡋࡂࡠࡗࡕࡐࠧ᱄")),
            bstack1l1lll1_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣ᱅"): env.get(bstack1l1lll1_opy_ (u"ࠢࡕࡔࡄ࡚ࡎ࡙࡟ࡋࡑࡅࡣࡓࡇࡍࡆࠤ᱆")),
            bstack1l1lll1_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢ᱇"): env.get(bstack1l1lll1_opy_ (u"ࠤࡗࡖࡆ࡜ࡉࡔࡡࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࡇࡋࡒࠣ᱈"))
        }
    if env.get(bstack1l1lll1_opy_ (u"ࠥࡇࡎࠨ᱉")) == bstack1l1lll1_opy_ (u"ࠦࡹࡸࡵࡦࠤ᱊") and env.get(bstack1l1lll1_opy_ (u"ࠧࡉࡉࡠࡐࡄࡑࡊࠨ᱋")) == bstack1l1lll1_opy_ (u"ࠨࡣࡰࡦࡨࡷ࡭࡯ࡰࠣ᱌"):
        return {
            bstack1l1lll1_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᱍ"): bstack1l1lll1_opy_ (u"ࠣࡅࡲࡨࡪࡹࡨࡪࡲࠥᱎ"),
            bstack1l1lll1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᱏ"): None,
            bstack1l1lll1_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧ᱐"): None,
            bstack1l1lll1_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥ᱑"): None
        }
    if env.get(bstack1l1lll1_opy_ (u"ࠧࡈࡉࡕࡄࡘࡇࡐࡋࡔࡠࡄࡕࡅࡓࡉࡈࠣ᱒")) and env.get(bstack1l1lll1_opy_ (u"ࠨࡂࡊࡖࡅ࡙ࡈࡑࡅࡕࡡࡆࡓࡒࡓࡉࡕࠤ᱓")):
        return {
            bstack1l1lll1_opy_ (u"ࠢ࡯ࡣࡰࡩࠧ᱔"): bstack1l1lll1_opy_ (u"ࠣࡄ࡬ࡸࡧࡻࡣ࡬ࡧࡷࠦ᱕"),
            bstack1l1lll1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧ᱖"): env.get(bstack1l1lll1_opy_ (u"ࠥࡆࡎ࡚ࡂࡖࡅࡎࡉ࡙ࡥࡇࡊࡖࡢࡌ࡙࡚ࡐࡠࡑࡕࡍࡌࡏࡎࠣ᱗")),
            bstack1l1lll1_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨ᱘"): None,
            bstack1l1lll1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦ᱙"): env.get(bstack1l1lll1_opy_ (u"ࠨࡂࡊࡖࡅ࡙ࡈࡑࡅࡕࡡࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࡇࡋࡒࠣᱚ"))
        }
    if env.get(bstack1l1lll1_opy_ (u"ࠢࡄࡋࠥᱛ")) == bstack1l1lll1_opy_ (u"ࠣࡶࡵࡹࡪࠨᱜ") and bstack111ll11ll_opy_(env.get(bstack1l1lll1_opy_ (u"ࠤࡇࡖࡔࡔࡅࠣᱝ"))):
        return {
            bstack1l1lll1_opy_ (u"ࠥࡲࡦࡳࡥࠣᱞ"): bstack1l1lll1_opy_ (u"ࠦࡉࡸ࡯࡯ࡧࠥᱟ"),
            bstack1l1lll1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣᱠ"): env.get(bstack1l1lll1_opy_ (u"ࠨࡄࡓࡑࡑࡉࡤࡈࡕࡊࡎࡇࡣࡑࡏࡎࡌࠤᱡ")),
            bstack1l1lll1_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᱢ"): None,
            bstack1l1lll1_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᱣ"): env.get(bstack1l1lll1_opy_ (u"ࠤࡇࡖࡔࡔࡅࡠࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘࠢᱤ"))
        }
    if env.get(bstack1l1lll1_opy_ (u"ࠥࡇࡎࠨᱥ")) == bstack1l1lll1_opy_ (u"ࠦࡹࡸࡵࡦࠤᱦ") and bstack111ll11ll_opy_(env.get(bstack1l1lll1_opy_ (u"࡙ࠧࡅࡎࡃࡓࡌࡔࡘࡅࠣᱧ"))):
        return {
            bstack1l1lll1_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᱨ"): bstack1l1lll1_opy_ (u"ࠢࡔࡧࡰࡥࡵ࡮࡯ࡳࡧࠥᱩ"),
            bstack1l1lll1_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᱪ"): env.get(bstack1l1lll1_opy_ (u"ࠤࡖࡉࡒࡇࡐࡉࡑࡕࡉࡤࡕࡒࡈࡃࡑࡍ࡟ࡇࡔࡊࡑࡑࡣ࡚ࡘࡌࠣᱫ")),
            bstack1l1lll1_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᱬ"): env.get(bstack1l1lll1_opy_ (u"ࠦࡘࡋࡍࡂࡒࡋࡓࡗࡋ࡟ࡋࡑࡅࡣࡓࡇࡍࡆࠤᱭ")),
            bstack1l1lll1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᱮ"): env.get(bstack1l1lll1_opy_ (u"ࠨࡓࡆࡏࡄࡔࡍࡕࡒࡆࡡࡍࡓࡇࡥࡉࡅࠤᱯ"))
        }
    if env.get(bstack1l1lll1_opy_ (u"ࠢࡄࡋࠥᱰ")) == bstack1l1lll1_opy_ (u"ࠣࡶࡵࡹࡪࠨᱱ") and bstack111ll11ll_opy_(env.get(bstack1l1lll1_opy_ (u"ࠤࡊࡍ࡙ࡒࡁࡃࡡࡆࡍࠧᱲ"))):
        return {
            bstack1l1lll1_opy_ (u"ࠥࡲࡦࡳࡥࠣᱳ"): bstack1l1lll1_opy_ (u"ࠦࡌ࡯ࡴࡍࡣࡥࠦᱴ"),
            bstack1l1lll1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣᱵ"): env.get(bstack1l1lll1_opy_ (u"ࠨࡃࡊࡡࡍࡓࡇࡥࡕࡓࡎࠥᱶ")),
            bstack1l1lll1_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᱷ"): env.get(bstack1l1lll1_opy_ (u"ࠣࡅࡌࡣࡏࡕࡂࡠࡐࡄࡑࡊࠨᱸ")),
            bstack1l1lll1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᱹ"): env.get(bstack1l1lll1_opy_ (u"ࠥࡇࡎࡥࡊࡐࡄࡢࡍࡉࠨᱺ"))
        }
    if env.get(bstack1l1lll1_opy_ (u"ࠦࡈࡏࠢᱻ")) == bstack1l1lll1_opy_ (u"ࠧࡺࡲࡶࡧࠥᱼ") and bstack111ll11ll_opy_(env.get(bstack1l1lll1_opy_ (u"ࠨࡂࡖࡋࡏࡈࡐࡏࡔࡆࠤᱽ"))):
        return {
            bstack1l1lll1_opy_ (u"ࠢ࡯ࡣࡰࡩࠧ᱾"): bstack1l1lll1_opy_ (u"ࠣࡄࡸ࡭ࡱࡪ࡫ࡪࡶࡨࠦ᱿"),
            bstack1l1lll1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᲀ"): env.get(bstack1l1lll1_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡍࡌࡘࡊࡥࡂࡖࡋࡏࡈࡤ࡛ࡒࡍࠤᲁ")),
            bstack1l1lll1_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᲂ"): env.get(bstack1l1lll1_opy_ (u"ࠧࡈࡕࡊࡎࡇࡏࡎ࡚ࡅࡠࡎࡄࡆࡊࡒࠢᲃ")) or env.get(bstack1l1lll1_opy_ (u"ࠨࡂࡖࡋࡏࡈࡐࡏࡔࡆࡡࡓࡍࡕࡋࡌࡊࡐࡈࡣࡓࡇࡍࡆࠤᲄ")),
            bstack1l1lll1_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᲅ"): env.get(bstack1l1lll1_opy_ (u"ࠣࡄࡘࡍࡑࡊࡋࡊࡖࡈࡣࡇ࡛ࡉࡍࡆࡢࡒ࡚ࡓࡂࡆࡔࠥᲆ"))
        }
    if bstack111ll11ll_opy_(env.get(bstack1l1lll1_opy_ (u"ࠤࡗࡊࡤࡈࡕࡊࡎࡇࠦᲇ"))):
        return {
            bstack1l1lll1_opy_ (u"ࠥࡲࡦࡳࡥࠣᲈ"): bstack1l1lll1_opy_ (u"࡛ࠦ࡯ࡳࡶࡣ࡯ࠤࡘࡺࡵࡥ࡫ࡲࠤ࡙࡫ࡡ࡮ࠢࡖࡩࡷࡼࡩࡤࡧࡶࠦᲉ"),
            bstack1l1lll1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣᲊ"): bstack1l1lll1_opy_ (u"ࠨࡻࡾࡽࢀࠦ᲋").format(env.get(bstack1l1lll1_opy_ (u"ࠧࡔ࡛ࡖࡘࡊࡓ࡟ࡕࡇࡄࡑࡋࡕࡕࡏࡆࡄࡘࡎࡕࡎࡔࡇࡕ࡚ࡊࡘࡕࡓࡋࠪ᲌")), env.get(bstack1l1lll1_opy_ (u"ࠨࡕ࡜ࡗ࡙ࡋࡍࡠࡖࡈࡅࡒࡖࡒࡐࡌࡈࡇ࡙ࡏࡄࠨ᲍"))),
            bstack1l1lll1_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦ᲎"): env.get(bstack1l1lll1_opy_ (u"ࠥࡗ࡞࡙ࡔࡆࡏࡢࡈࡊࡌࡉࡏࡋࡗࡍࡔࡔࡉࡅࠤ᲏")),
            bstack1l1lll1_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᲐ"): env.get(bstack1l1lll1_opy_ (u"ࠧࡈࡕࡊࡎࡇࡣࡇ࡛ࡉࡍࡆࡌࡈࠧᲑ"))
        }
    if bstack111ll11ll_opy_(env.get(bstack1l1lll1_opy_ (u"ࠨࡁࡑࡒ࡙ࡉ࡞ࡕࡒࠣᲒ"))):
        return {
            bstack1l1lll1_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᲓ"): bstack1l1lll1_opy_ (u"ࠣࡃࡳࡴࡻ࡫ࡹࡰࡴࠥᲔ"),
            bstack1l1lll1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᲕ"): bstack1l1lll1_opy_ (u"ࠥࡿࢂ࠵ࡰࡳࡱ࡭ࡩࡨࡺ࠯ࡼࡿ࠲ࡿࢂ࠵ࡢࡶ࡫࡯ࡨࡸ࠵ࡻࡾࠤᲖ").format(env.get(bstack1l1lll1_opy_ (u"ࠫࡆࡖࡐࡗࡇ࡜ࡓࡗࡥࡕࡓࡎࠪᲗ")), env.get(bstack1l1lll1_opy_ (u"ࠬࡇࡐࡑࡘࡈ࡝ࡔࡘ࡟ࡂࡅࡆࡓ࡚ࡔࡔࡠࡐࡄࡑࡊ࠭Ი")), env.get(bstack1l1lll1_opy_ (u"࠭ࡁࡑࡒ࡙ࡉ࡞ࡕࡒࡠࡒࡕࡓࡏࡋࡃࡕࡡࡖࡐ࡚ࡍࠧᲙ")), env.get(bstack1l1lll1_opy_ (u"ࠧࡂࡒࡓ࡚ࡊ࡟ࡏࡓࡡࡅ࡙ࡎࡒࡄࡠࡋࡇࠫᲚ"))),
            bstack1l1lll1_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᲛ"): env.get(bstack1l1lll1_opy_ (u"ࠤࡄࡔࡕ࡜ࡅ࡚ࡑࡕࡣࡏࡕࡂࡠࡐࡄࡑࡊࠨᲜ")),
            bstack1l1lll1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤᲝ"): env.get(bstack1l1lll1_opy_ (u"ࠦࡆࡖࡐࡗࡇ࡜ࡓࡗࡥࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࠧᲞ"))
        }
    if env.get(bstack1l1lll1_opy_ (u"ࠧࡇ࡚ࡖࡔࡈࡣࡍ࡚ࡔࡑࡡࡘࡗࡊࡘ࡟ࡂࡉࡈࡒ࡙ࠨᲟ")) and env.get(bstack1l1lll1_opy_ (u"ࠨࡔࡇࡡࡅ࡙ࡎࡒࡄࠣᲠ")):
        return {
            bstack1l1lll1_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᲡ"): bstack1l1lll1_opy_ (u"ࠣࡃࡽࡹࡷ࡫ࠠࡄࡋࠥᲢ"),
            bstack1l1lll1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᲣ"): bstack1l1lll1_opy_ (u"ࠥࡿࢂࢁࡽ࠰ࡡࡥࡹ࡮ࡲࡤ࠰ࡴࡨࡷࡺࡲࡴࡴࡁࡥࡹ࡮ࡲࡤࡊࡦࡀࡿࢂࠨᲤ").format(env.get(bstack1l1lll1_opy_ (u"ࠫࡘ࡟ࡓࡕࡇࡐࡣ࡙ࡋࡁࡎࡈࡒ࡙ࡓࡊࡁࡕࡋࡒࡒࡘࡋࡒࡗࡇࡕ࡙ࡗࡏࠧᲥ")), env.get(bstack1l1lll1_opy_ (u"࡙࡙ࠬࡔࡖࡈࡑࡤ࡚ࡅࡂࡏࡓࡖࡔࡐࡅࡄࡖࠪᲦ")), env.get(bstack1l1lll1_opy_ (u"࠭ࡂࡖࡋࡏࡈࡤࡈࡕࡊࡎࡇࡍࡉ࠭Ყ"))),
            bstack1l1lll1_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᲨ"): env.get(bstack1l1lll1_opy_ (u"ࠣࡄࡘࡍࡑࡊ࡟ࡃࡗࡌࡐࡉࡏࡄࠣᲩ")),
            bstack1l1lll1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᲪ"): env.get(bstack1l1lll1_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡡࡅ࡙ࡎࡒࡄࡊࡆࠥᲫ"))
        }
    if any([env.get(bstack1l1lll1_opy_ (u"ࠦࡈࡕࡄࡆࡄࡘࡍࡑࡊ࡟ࡃࡗࡌࡐࡉࡥࡉࡅࠤᲬ")), env.get(bstack1l1lll1_opy_ (u"ࠧࡉࡏࡅࡇࡅ࡙ࡎࡒࡄࡠࡔࡈࡗࡔࡒࡖࡆࡆࡢࡗࡔ࡛ࡒࡄࡇࡢ࡚ࡊࡘࡓࡊࡑࡑࠦᲭ")), env.get(bstack1l1lll1_opy_ (u"ࠨࡃࡐࡆࡈࡆ࡚ࡏࡌࡅࡡࡖࡓ࡚ࡘࡃࡆࡡ࡙ࡉࡗ࡙ࡉࡐࡐࠥᲮ"))]):
        return {
            bstack1l1lll1_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᲯ"): bstack1l1lll1_opy_ (u"ࠣࡃ࡚ࡗࠥࡉ࡯ࡥࡧࡅࡹ࡮ࡲࡤࠣᲰ"),
            bstack1l1lll1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᲱ"): env.get(bstack1l1lll1_opy_ (u"ࠥࡇࡔࡊࡅࡃࡗࡌࡐࡉࡥࡐࡖࡄࡏࡍࡈࡥࡂࡖࡋࡏࡈࡤ࡛ࡒࡍࠤᲲ")),
            bstack1l1lll1_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᲳ"): env.get(bstack1l1lll1_opy_ (u"ࠧࡉࡏࡅࡇࡅ࡙ࡎࡒࡄࡠࡄࡘࡍࡑࡊ࡟ࡊࡆࠥᲴ")),
            bstack1l1lll1_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᲵ"): env.get(bstack1l1lll1_opy_ (u"ࠢࡄࡑࡇࡉࡇ࡛ࡉࡍࡆࡢࡆ࡚ࡏࡌࡅࡡࡌࡈࠧᲶ"))
        }
    if env.get(bstack1l1lll1_opy_ (u"ࠣࡤࡤࡱࡧࡵ࡯ࡠࡤࡸ࡭ࡱࡪࡎࡶ࡯ࡥࡩࡷࠨᲷ")):
        return {
            bstack1l1lll1_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᲸ"): bstack1l1lll1_opy_ (u"ࠥࡆࡦࡳࡢࡰࡱࠥᲹ"),
            bstack1l1lll1_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᲺ"): env.get(bstack1l1lll1_opy_ (u"ࠧࡨࡡ࡮ࡤࡲࡳࡤࡨࡵࡪ࡮ࡧࡖࡪࡹࡵ࡭ࡶࡶ࡙ࡷࡲࠢ᲻")),
            bstack1l1lll1_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣ᲼"): env.get(bstack1l1lll1_opy_ (u"ࠢࡣࡣࡰࡦࡴࡵ࡟ࡴࡪࡲࡶࡹࡐ࡯ࡣࡐࡤࡱࡪࠨᲽ")),
            bstack1l1lll1_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᲾ"): env.get(bstack1l1lll1_opy_ (u"ࠤࡥࡥࡲࡨ࡯ࡰࡡࡥࡹ࡮ࡲࡤࡏࡷࡰࡦࡪࡸࠢᲿ"))
        }
    if env.get(bstack1l1lll1_opy_ (u"࡛ࠥࡊࡘࡃࡌࡇࡕࠦ᳀")) or env.get(bstack1l1lll1_opy_ (u"ࠦ࡜ࡋࡒࡄࡍࡈࡖࡤࡓࡁࡊࡐࡢࡔࡎࡖࡅࡍࡋࡑࡉࡤ࡙ࡔࡂࡔࡗࡉࡉࠨ᳁")):
        return {
            bstack1l1lll1_opy_ (u"ࠧࡴࡡ࡮ࡧࠥ᳂"): bstack1l1lll1_opy_ (u"ࠨࡗࡦࡴࡦ࡯ࡪࡸࠢ᳃"),
            bstack1l1lll1_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥ᳄"): env.get(bstack1l1lll1_opy_ (u"࡙ࠣࡈࡖࡈࡑࡅࡓࡡࡅ࡙ࡎࡒࡄࡠࡗࡕࡐࠧ᳅")),
            bstack1l1lll1_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦ᳆"): bstack1l1lll1_opy_ (u"ࠥࡑࡦ࡯࡮ࠡࡒ࡬ࡴࡪࡲࡩ࡯ࡧࠥ᳇") if env.get(bstack1l1lll1_opy_ (u"ࠦ࡜ࡋࡒࡄࡍࡈࡖࡤࡓࡁࡊࡐࡢࡔࡎࡖࡅࡍࡋࡑࡉࡤ࡙ࡔࡂࡔࡗࡉࡉࠨ᳈")) else None,
            bstack1l1lll1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦ᳉"): env.get(bstack1l1lll1_opy_ (u"ࠨࡗࡆࡔࡆࡏࡊࡘ࡟ࡈࡋࡗࡣࡈࡕࡍࡎࡋࡗࠦ᳊"))
        }
    if any([env.get(bstack1l1lll1_opy_ (u"ࠢࡈࡅࡓࡣࡕࡘࡏࡋࡇࡆࡘࠧ᳋")), env.get(bstack1l1lll1_opy_ (u"ࠣࡉࡆࡐࡔ࡛ࡄࡠࡒࡕࡓࡏࡋࡃࡕࠤ᳌")), env.get(bstack1l1lll1_opy_ (u"ࠤࡊࡓࡔࡍࡌࡆࡡࡆࡐࡔ࡛ࡄࡠࡒࡕࡓࡏࡋࡃࡕࠤ᳍"))]):
        return {
            bstack1l1lll1_opy_ (u"ࠥࡲࡦࡳࡥࠣ᳎"): bstack1l1lll1_opy_ (u"ࠦࡌࡵ࡯ࡨ࡮ࡨࠤࡈࡲ࡯ࡶࡦࠥ᳏"),
            bstack1l1lll1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣ᳐"): None,
            bstack1l1lll1_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣ᳑"): env.get(bstack1l1lll1_opy_ (u"ࠢࡑࡔࡒࡎࡊࡉࡔࡠࡋࡇࠦ᳒")),
            bstack1l1lll1_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢ᳓"): env.get(bstack1l1lll1_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡠࡋࡇ᳔ࠦ"))
        }
    if env.get(bstack1l1lll1_opy_ (u"ࠥࡗࡍࡏࡐࡑࡃࡅࡐࡊࠨ᳕")):
        return {
            bstack1l1lll1_opy_ (u"ࠦࡳࡧ࡭ࡦࠤ᳖"): bstack1l1lll1_opy_ (u"࡙ࠧࡨࡪࡲࡳࡥࡧࡲࡥ᳗ࠣ"),
            bstack1l1lll1_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤ᳘"): env.get(bstack1l1lll1_opy_ (u"ࠢࡔࡊࡌࡔࡕࡇࡂࡍࡇࡢࡆ࡚ࡏࡌࡅࡡࡘࡖࡑࠨ᳙")),
            bstack1l1lll1_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥ᳚"): bstack1l1lll1_opy_ (u"ࠤࡍࡳࡧࠦࠣࡼࡿࠥ᳛").format(env.get(bstack1l1lll1_opy_ (u"ࠪࡗࡍࡏࡐࡑࡃࡅࡐࡊࡥࡊࡐࡄࡢࡍࡉ᳜࠭"))) if env.get(bstack1l1lll1_opy_ (u"ࠦࡘࡎࡉࡑࡒࡄࡆࡑࡋ࡟ࡋࡑࡅࡣࡎࡊ᳝ࠢ")) else None,
            bstack1l1lll1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵ᳞ࠦ"): env.get(bstack1l1lll1_opy_ (u"ࠨࡓࡉࡋࡓࡔࡆࡈࡌࡆࡡࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࡇࡋࡒ᳟ࠣ"))
        }
    if bstack111ll11ll_opy_(env.get(bstack1l1lll1_opy_ (u"ࠢࡏࡇࡗࡐࡎࡌ࡙ࠣ᳠"))):
        return {
            bstack1l1lll1_opy_ (u"ࠣࡰࡤࡱࡪࠨ᳡"): bstack1l1lll1_opy_ (u"ࠤࡑࡩࡹࡲࡩࡧࡻ᳢ࠥ"),
            bstack1l1lll1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨ᳣"): env.get(bstack1l1lll1_opy_ (u"ࠦࡉࡋࡐࡍࡑ࡜ࡣ࡚ࡘࡌ᳤ࠣ")),
            bstack1l1lll1_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫᳥ࠢ"): env.get(bstack1l1lll1_opy_ (u"ࠨࡓࡊࡖࡈࡣࡓࡇࡍࡆࠤ᳦")),
            bstack1l1lll1_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨ᳧"): env.get(bstack1l1lll1_opy_ (u"ࠣࡄࡘࡍࡑࡊ࡟ࡊࡆ᳨ࠥ"))
        }
    if bstack111ll11ll_opy_(env.get(bstack1l1lll1_opy_ (u"ࠤࡊࡍ࡙ࡎࡕࡃࡡࡄࡇ࡙ࡏࡏࡏࡕࠥᳩ"))):
        return {
            bstack1l1lll1_opy_ (u"ࠥࡲࡦࡳࡥࠣᳪ"): bstack1l1lll1_opy_ (u"ࠦࡌ࡯ࡴࡉࡷࡥࠤࡆࡩࡴࡪࡱࡱࡷࠧᳫ"),
            bstack1l1lll1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣᳬ"): bstack1l1lll1_opy_ (u"ࠨࡻࡾ࠱ࡾࢁ࠴ࡧࡣࡵ࡫ࡲࡲࡸ࠵ࡲࡶࡰࡶ࠳ࢀࢃ᳭ࠢ").format(env.get(bstack1l1lll1_opy_ (u"ࠧࡈࡋࡗࡌ࡚ࡈ࡟ࡔࡇࡕ࡚ࡊࡘ࡟ࡖࡔࡏࠫᳮ")), env.get(bstack1l1lll1_opy_ (u"ࠨࡉࡌࡘࡍ࡛ࡂࡠࡔࡈࡔࡔ࡙ࡉࡕࡑࡕ࡝ࠬᳯ")), env.get(bstack1l1lll1_opy_ (u"ࠩࡊࡍ࡙ࡎࡕࡃࡡࡕ࡙ࡓࡥࡉࡅࠩᳰ"))),
            bstack1l1lll1_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᳱ"): env.get(bstack1l1lll1_opy_ (u"ࠦࡌࡏࡔࡉࡗࡅࡣ࡜ࡕࡒࡌࡈࡏࡓ࡜ࠨᳲ")),
            bstack1l1lll1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᳳ"): env.get(bstack1l1lll1_opy_ (u"ࠨࡇࡊࡖࡋ࡙ࡇࡥࡒࡖࡐࡢࡍࡉࠨ᳴"))
        }
    if env.get(bstack1l1lll1_opy_ (u"ࠢࡄࡋࠥᳵ")) == bstack1l1lll1_opy_ (u"ࠣࡶࡵࡹࡪࠨᳶ") and env.get(bstack1l1lll1_opy_ (u"ࠤ࡙ࡉࡗࡉࡅࡍࠤ᳷")) == bstack1l1lll1_opy_ (u"ࠥ࠵ࠧ᳸"):
        return {
            bstack1l1lll1_opy_ (u"ࠦࡳࡧ࡭ࡦࠤ᳹"): bstack1l1lll1_opy_ (u"ࠧ࡜ࡥࡳࡥࡨࡰࠧᳺ"),
            bstack1l1lll1_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤ᳻"): bstack1l1lll1_opy_ (u"ࠢࡩࡶࡷࡴ࠿࠵࠯ࡼࡿࠥ᳼").format(env.get(bstack1l1lll1_opy_ (u"ࠨࡘࡈࡖࡈࡋࡌࡠࡗࡕࡐࠬ᳽"))),
            bstack1l1lll1_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦ᳾"): None,
            bstack1l1lll1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤ᳿"): None,
        }
    if env.get(bstack1l1lll1_opy_ (u"࡙ࠦࡋࡁࡎࡅࡌࡘ࡞ࡥࡖࡆࡔࡖࡍࡔࡔࠢᴀ")):
        return {
            bstack1l1lll1_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᴁ"): bstack1l1lll1_opy_ (u"ࠨࡔࡦࡣࡰࡧ࡮ࡺࡹࠣᴂ"),
            bstack1l1lll1_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᴃ"): None,
            bstack1l1lll1_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᴄ"): env.get(bstack1l1lll1_opy_ (u"ࠤࡗࡉࡆࡓࡃࡊࡖ࡜ࡣࡕࡘࡏࡋࡇࡆࡘࡤࡔࡁࡎࡇࠥᴅ")),
            bstack1l1lll1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤᴆ"): env.get(bstack1l1lll1_opy_ (u"ࠦࡇ࡛ࡉࡍࡆࡢࡒ࡚ࡓࡂࡆࡔࠥᴇ"))
        }
    if any([env.get(bstack1l1lll1_opy_ (u"ࠧࡉࡏࡏࡅࡒ࡙ࡗ࡙ࡅࠣᴈ")), env.get(bstack1l1lll1_opy_ (u"ࠨࡃࡐࡐࡆࡓ࡚ࡘࡓࡆࡡࡘࡖࡑࠨᴉ")), env.get(bstack1l1lll1_opy_ (u"ࠢࡄࡑࡑࡇࡔ࡛ࡒࡔࡇࡢ࡙ࡘࡋࡒࡏࡃࡐࡉࠧᴊ")), env.get(bstack1l1lll1_opy_ (u"ࠣࡅࡒࡒࡈࡕࡕࡓࡕࡈࡣ࡙ࡋࡁࡎࠤᴋ"))]):
        return {
            bstack1l1lll1_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᴌ"): bstack1l1lll1_opy_ (u"ࠥࡇࡴࡴࡣࡰࡷࡵࡷࡪࠨᴍ"),
            bstack1l1lll1_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᴎ"): None,
            bstack1l1lll1_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᴏ"): env.get(bstack1l1lll1_opy_ (u"ࠨࡂࡖࡋࡏࡈࡤࡐࡏࡃࡡࡑࡅࡒࡋࠢᴐ")) or None,
            bstack1l1lll1_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᴑ"): env.get(bstack1l1lll1_opy_ (u"ࠣࡄࡘࡍࡑࡊ࡟ࡊࡆࠥᴒ"), 0)
        }
    if env.get(bstack1l1lll1_opy_ (u"ࠤࡊࡓࡤࡐࡏࡃࡡࡑࡅࡒࡋࠢᴓ")):
        return {
            bstack1l1lll1_opy_ (u"ࠥࡲࡦࡳࡥࠣᴔ"): bstack1l1lll1_opy_ (u"ࠦࡌࡵࡃࡅࠤᴕ"),
            bstack1l1lll1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣᴖ"): None,
            bstack1l1lll1_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᴗ"): env.get(bstack1l1lll1_opy_ (u"ࠢࡈࡑࡢࡎࡔࡈ࡟ࡏࡃࡐࡉࠧᴘ")),
            bstack1l1lll1_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᴙ"): env.get(bstack1l1lll1_opy_ (u"ࠤࡊࡓࡤࡖࡉࡑࡇࡏࡍࡓࡋ࡟ࡄࡑࡘࡒ࡙ࡋࡒࠣᴚ"))
        }
    if env.get(bstack1l1lll1_opy_ (u"ࠥࡇࡋࡥࡂࡖࡋࡏࡈࡤࡏࡄࠣᴛ")):
        return {
            bstack1l1lll1_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᴜ"): bstack1l1lll1_opy_ (u"ࠧࡉ࡯ࡥࡧࡉࡶࡪࡹࡨࠣᴝ"),
            bstack1l1lll1_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᴞ"): env.get(bstack1l1lll1_opy_ (u"ࠢࡄࡈࡢࡆ࡚ࡏࡌࡅࡡࡘࡖࡑࠨᴟ")),
            bstack1l1lll1_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᴠ"): env.get(bstack1l1lll1_opy_ (u"ࠤࡆࡊࡤࡖࡉࡑࡇࡏࡍࡓࡋ࡟ࡏࡃࡐࡉࠧᴡ")),
            bstack1l1lll1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤᴢ"): env.get(bstack1l1lll1_opy_ (u"ࠦࡈࡌ࡟ࡃࡗࡌࡐࡉࡥࡉࡅࠤᴣ"))
        }
    return {bstack1l1lll1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᴤ"): None}
def get_host_info():
    return {
        bstack1l1lll1_opy_ (u"ࠨࡨࡰࡵࡷࡲࡦࡳࡥࠣᴥ"): platform.node(),
        bstack1l1lll1_opy_ (u"ࠢࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࠤᴦ"): platform.system(),
        bstack1l1lll1_opy_ (u"ࠣࡶࡼࡴࡪࠨᴧ"): platform.machine(),
        bstack1l1lll1_opy_ (u"ࠤࡹࡩࡷࡹࡩࡰࡰࠥᴨ"): platform.version(),
        bstack1l1lll1_opy_ (u"ࠥࡥࡷࡩࡨࠣᴩ"): platform.architecture()[0]
    }
def bstack111l1l11ll_opy_():
    try:
        import selenium
        return True
    except ImportError:
        return False
def bstack111l1l11l11_opy_():
    if bstack1111111l_opy_.get_property(bstack1l1lll1_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡣࡸ࡫ࡳࡴ࡫ࡲࡲࠬᴪ")):
        return bstack1l1lll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫᴫ")
    return bstack1l1lll1_opy_ (u"࠭ࡵ࡯࡭ࡱࡳࡼࡴ࡟ࡨࡴ࡬ࡨࠬᴬ")
def bstack111l1lll1ll_opy_(driver):
    info = {
        bstack1l1lll1_opy_ (u"ࠧࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸ࠭ᴭ"): driver.capabilities,
        bstack1l1lll1_opy_ (u"ࠨࡵࡨࡷࡸ࡯࡯࡯ࡡ࡬ࡨࠬᴮ"): driver.session_id,
        bstack1l1lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࠪᴯ"): driver.capabilities.get(bstack1l1lll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨᴰ"), None),
        bstack1l1lll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭ᴱ"): driver.capabilities.get(bstack1l1lll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ᴲ"), None),
        bstack1l1lll1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࠨᴳ"): driver.capabilities.get(bstack1l1lll1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡐࡤࡱࡪ࠭ᴴ"), None),
        bstack1l1lll1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡢࡺࡪࡸࡳࡪࡱࡱࠫᴵ"):driver.capabilities.get(bstack1l1lll1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰ࡚ࡪࡸࡳࡪࡱࡱࠫᴶ"), None),
    }
    if bstack111l1l11l11_opy_() == bstack1l1lll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩᴷ"):
        if bstack1l1111l1ll_opy_():
            info[bstack1l1lll1_opy_ (u"ࠫࡵࡸ࡯ࡥࡷࡦࡸࠬᴸ")] = bstack1l1lll1_opy_ (u"ࠬࡧࡰࡱ࠯ࡤࡹࡹࡵ࡭ࡢࡶࡨࠫᴹ")
        elif driver.capabilities.get(bstack1l1lll1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧᴺ"), {}).get(bstack1l1lll1_opy_ (u"ࠧࡵࡷࡵࡦࡴࡹࡣࡢ࡮ࡨࠫᴻ"), False):
            info[bstack1l1lll1_opy_ (u"ࠨࡲࡵࡳࡩࡻࡣࡵࠩᴼ")] = bstack1l1lll1_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡴࡥࡤࡰࡪ࠭ᴽ")
        else:
            info[bstack1l1lll1_opy_ (u"ࠪࡴࡷࡵࡤࡶࡥࡷࠫᴾ")] = bstack1l1lll1_opy_ (u"ࠫࡦࡻࡴࡰ࡯ࡤࡸࡪ࠭ᴿ")
    return info
def bstack1l1111l1ll_opy_():
    if bstack1111111l_opy_.get_property(bstack1l1lll1_opy_ (u"ࠬࡧࡰࡱࡡࡤࡹࡹࡵ࡭ࡢࡶࡨࠫᵀ")):
        return True
    if bstack111ll11ll_opy_(os.environ.get(bstack1l1lll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡏࡓࡠࡃࡓࡔࡤࡇࡕࡕࡑࡐࡅ࡙ࡋࠧᵁ"), None)):
        return True
    return False
def bstack1l1l1l1l1l_opy_(bstack1111ll1111l_opy_, url, data, config):
    headers = config.get(bstack1l1lll1_opy_ (u"ࠧࡩࡧࡤࡨࡪࡸࡳࠨᵂ"), None)
    proxies = bstack11l1l11ll_opy_(config, url)
    auth = config.get(bstack1l1lll1_opy_ (u"ࠨࡣࡸࡸ࡭࠭ᵃ"), None)
    response = requests.request(
            bstack1111ll1111l_opy_,
            url=url,
            headers=headers,
            auth=auth,
            json=data,
            proxies=proxies
        )
    return response
def bstack1l1111111_opy_(bstack11l1ll111_opy_, size):
    bstack1ll11llll1_opy_ = []
    while len(bstack11l1ll111_opy_) > size:
        bstack111l11l11l_opy_ = bstack11l1ll111_opy_[:size]
        bstack1ll11llll1_opy_.append(bstack111l11l11l_opy_)
        bstack11l1ll111_opy_ = bstack11l1ll111_opy_[size:]
    bstack1ll11llll1_opy_.append(bstack11l1ll111_opy_)
    return bstack1ll11llll1_opy_
def bstack1111l1ll111_opy_(message, bstack111l1llll11_opy_=False):
    os.write(1, bytes(message, bstack1l1lll1_opy_ (u"ࠩࡸࡸ࡫࠳࠸ࠨᵄ")))
    os.write(1, bytes(bstack1l1lll1_opy_ (u"ࠪࡠࡳ࠭ᵅ"), bstack1l1lll1_opy_ (u"ࠫࡺࡺࡦ࠮࠺ࠪᵆ")))
    if bstack111l1llll11_opy_:
        with open(bstack1l1lll1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠲ࡵ࠱࠲ࡻ࠰ࠫᵇ") + os.environ[bstack1l1lll1_opy_ (u"࠭ࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡆ࡚ࡏࡌࡅࡡࡋࡅࡘࡎࡅࡅࡡࡌࡈࠬᵈ")] + bstack1l1lll1_opy_ (u"ࠧ࠯࡮ࡲ࡫ࠬᵉ"), bstack1l1lll1_opy_ (u"ࠨࡣࠪᵊ")) as f:
            f.write(message + bstack1l1lll1_opy_ (u"ࠩ࡟ࡲࠬᵋ"))
def bstack1llll1111ll_opy_():
    return os.environ[bstack1l1lll1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡄ࡙࡙ࡕࡍࡂࡖࡌࡓࡓ࠭ᵌ")].lower() == bstack1l1lll1_opy_ (u"ࠫࡹࡸࡵࡦࠩᵍ")
def bstack1ll1llll_opy_():
    return bstack1l11111l_opy_().replace(tzinfo=None).isoformat() + bstack1l1lll1_opy_ (u"ࠬࡠࠧᵎ")
def bstack111l11l1lll_opy_(start, finish):
    return (datetime.datetime.fromisoformat(finish.rstrip(bstack1l1lll1_opy_ (u"࡚࠭ࠨᵏ"))) - datetime.datetime.fromisoformat(start.rstrip(bstack1l1lll1_opy_ (u"࡛ࠧࠩᵐ")))).total_seconds() * 1000
def bstack111l1llll1l_opy_(timestamp):
    return bstack1111l1l1l11_opy_(timestamp).isoformat() + bstack1l1lll1_opy_ (u"ࠨ࡜ࠪᵑ")
def bstack111l1111lll_opy_(bstack111l11111ll_opy_):
    date_format = bstack1l1lll1_opy_ (u"ࠩࠨ࡝ࠪࡳࠥࡥࠢࠨࡌ࠿ࠫࡍ࠻ࠧࡖ࠲ࠪ࡬ࠧᵒ")
    bstack111l1l111ll_opy_ = datetime.datetime.strptime(bstack111l11111ll_opy_, date_format)
    return bstack111l1l111ll_opy_.isoformat() + bstack1l1lll1_opy_ (u"ࠪ࡞ࠬᵓ")
def bstack1111ll111ll_opy_(outcome):
    _, exception, _ = outcome.excinfo or (None, None, None)
    if exception:
        return bstack1l1lll1_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫᵔ")
    else:
        return bstack1l1lll1_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬᵕ")
def bstack111ll11ll_opy_(val):
    if val is None:
        return False
    return val.__str__().lower() == bstack1l1lll1_opy_ (u"࠭ࡴࡳࡷࡨࠫᵖ")
def bstack1111lll1l1l_opy_(val):
    return val.__str__().lower() == bstack1l1lll1_opy_ (u"ࠧࡧࡣ࡯ࡷࡪ࠭ᵗ")
def error_handler(bstack111l1l1llll_opy_=Exception, class_method=False, default_value=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except bstack111l1l1llll_opy_ as e:
                print(bstack1l1lll1_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡧࡷࡱࡧࡹ࡯࡯࡯ࠢࡾࢁࠥ࠳࠾ࠡࡽࢀ࠾ࠥࢁࡽࠣᵘ").format(func.__name__, bstack111l1l1llll_opy_.__name__, str(e)))
                return default_value
        return wrapper
    def bstack1111l1l1111_opy_(bstack111l1ll111l_opy_):
        def wrapped(cls, *args, **kwargs):
            try:
                return bstack111l1ll111l_opy_(cls, *args, **kwargs)
            except bstack111l1l1llll_opy_ as e:
                print(bstack1l1lll1_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡨࡸࡲࡨࡺࡩࡰࡰࠣࡿࢂࠦ࠭࠿ࠢࡾࢁ࠿ࠦࡻࡾࠤᵙ").format(bstack111l1ll111l_opy_.__name__, bstack111l1l1llll_opy_.__name__, str(e)))
                return default_value
        return wrapped
    if class_method:
        return bstack1111l1l1111_opy_
    else:
        return decorator
def bstack1l1l1l1l1_opy_(bstack1lll1lll1_opy_):
    if os.getenv(bstack1l1lll1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡄ࡙࡙ࡕࡍࡂࡖࡌࡓࡓ࠭ᵚ")) is not None:
        return bstack111ll11ll_opy_(os.getenv(bstack1l1lll1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡅ࡚࡚ࡏࡎࡃࡗࡍࡔࡔࠧᵛ")))
    if bstack1l1lll1_opy_ (u"ࠬࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠩᵜ") in bstack1lll1lll1_opy_ and bstack1111lll1l1l_opy_(bstack1lll1lll1_opy_[bstack1l1lll1_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࠪᵝ")]):
        return False
    if bstack1l1lll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠩᵞ") in bstack1lll1lll1_opy_ and bstack1111lll1l1l_opy_(bstack1lll1lll1_opy_[bstack1l1lll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠪᵟ")]):
        return False
    return True
def bstack1l1l1lll1_opy_():
    try:
        from pytest_bdd import reporting
        bstack111l1ll11l1_opy_ = os.environ.get(bstack1l1lll1_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡗࡖࡉࡗࡥࡆࡓࡃࡐࡉ࡜ࡕࡒࡌࠤᵠ"), None)
        return bstack111l1ll11l1_opy_ is None or bstack111l1ll11l1_opy_ == bstack1l1lll1_opy_ (u"ࠥࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠢᵡ")
    except Exception as e:
        return False
def bstack111ll1ll1l_opy_(hub_url, CONFIG):
    if bstack1ll1ll11ll_opy_() <= version.parse(bstack1l1lll1_opy_ (u"ࠫ࠸࠴࠱࠴࠰࠳ࠫᵢ")):
        if hub_url:
            return bstack1l1lll1_opy_ (u"ࠧ࡮ࡴࡵࡲ࠽࠳࠴ࠨᵣ") + hub_url + bstack1l1lll1_opy_ (u"ࠨ࠺࠹࠲࠲ࡻࡩ࠵ࡨࡶࡤࠥᵤ")
        return bstack111lllll11_opy_
    if hub_url:
        return bstack1l1lll1_opy_ (u"ࠢࡩࡶࡷࡴࡸࡀ࠯࠰ࠤᵥ") + hub_url + bstack1l1lll1_opy_ (u"ࠣ࠱ࡺࡨ࠴࡮ࡵࡣࠤᵦ")
    return bstack1111llll11_opy_
def bstack1111ll11111_opy_():
    return isinstance(os.getenv(bstack1l1lll1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒ࡜ࡘࡊ࡙ࡔࡠࡒࡏ࡙ࡌࡏࡎࠨᵧ")), str)
def bstack1l111111l_opy_(url):
    return urlparse(url).hostname
def bstack1l1lll1l11_opy_(hostname):
    for bstack11ll11l1ll_opy_ in bstack1lll1111ll_opy_:
        regex = re.compile(bstack11ll11l1ll_opy_)
        if regex.match(hostname):
            return True
    return False
def bstack11ll111l1ll_opy_(bstack111l1ll1lll_opy_, file_name, logger):
    bstack111l1lll1l_opy_ = os.path.join(os.path.expanduser(bstack1l1lll1_opy_ (u"ࠪࢂࠬᵨ")), bstack111l1ll1lll_opy_)
    try:
        if not os.path.exists(bstack111l1lll1l_opy_):
            os.makedirs(bstack111l1lll1l_opy_)
        file_path = os.path.join(os.path.expanduser(bstack1l1lll1_opy_ (u"ࠫࢃ࠭ᵩ")), bstack111l1ll1lll_opy_, file_name)
        if not os.path.isfile(file_path):
            with open(file_path, bstack1l1lll1_opy_ (u"ࠬࡽࠧᵪ")):
                pass
            with open(file_path, bstack1l1lll1_opy_ (u"ࠨࡷࠬࠤᵫ")) as outfile:
                json.dump({}, outfile)
        return file_path
    except Exception as e:
        logger.debug(bstack1ll111l111_opy_.format(str(e)))
def bstack11ll111lll1_opy_(file_name, key, value, logger):
    file_path = bstack11ll111l1ll_opy_(bstack1l1lll1_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧᵬ"), file_name, logger)
    if file_path != None:
        if os.path.exists(file_path):
            bstack1l11l1ll1l_opy_ = json.load(open(file_path, bstack1l1lll1_opy_ (u"ࠨࡴࡥࠫᵭ")))
        else:
            bstack1l11l1ll1l_opy_ = {}
        bstack1l11l1ll1l_opy_[key] = value
        with open(file_path, bstack1l1lll1_opy_ (u"ࠤࡺ࠯ࠧᵮ")) as outfile:
            json.dump(bstack1l11l1ll1l_opy_, outfile)
def bstack1lll11111_opy_(file_name, logger):
    file_path = bstack11ll111l1ll_opy_(bstack1l1lll1_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪᵯ"), file_name, logger)
    bstack1l11l1ll1l_opy_ = {}
    if file_path != None and os.path.exists(file_path):
        with open(file_path, bstack1l1lll1_opy_ (u"ࠫࡷ࠭ᵰ")) as bstack11l1ll1ll_opy_:
            bstack1l11l1ll1l_opy_ = json.load(bstack11l1ll1ll_opy_)
    return bstack1l11l1ll1l_opy_
def bstack111ll1111_opy_(file_path, logger):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
    except Exception as e:
        logger.debug(bstack1l1lll1_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡥࡧ࡯ࡩࡹ࡯࡮ࡨࠢࡩ࡭ࡱ࡫࠺ࠡࠩᵱ") + file_path + bstack1l1lll1_opy_ (u"࠭ࠠࠨᵲ") + str(e))
def bstack1ll1ll11ll_opy_():
    from selenium import webdriver
    return version.parse(webdriver.__version__)
class Notset:
    def __repr__(self):
        return bstack1l1lll1_opy_ (u"ࠢ࠽ࡐࡒࡘࡘࡋࡔ࠿ࠤᵳ")
def bstack1111lll1l1_opy_(config):
    if bstack1l1lll1_opy_ (u"ࠨ࡫ࡶࡔࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠧᵴ") in config:
        del (config[bstack1l1lll1_opy_ (u"ࠩ࡬ࡷࡕࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠨᵵ")])
        return False
    if bstack1ll1ll11ll_opy_() < version.parse(bstack1l1lll1_opy_ (u"ࠪ࠷࠳࠺࠮࠱ࠩᵶ")):
        return False
    if bstack1ll1ll11ll_opy_() >= version.parse(bstack1l1lll1_opy_ (u"ࠫ࠹࠴࠱࠯࠷ࠪᵷ")):
        return True
    if bstack1l1lll1_opy_ (u"ࠬࡻࡳࡦ࡙࠶ࡇࠬᵸ") in config and config[bstack1l1lll1_opy_ (u"࠭ࡵࡴࡧ࡚࠷ࡈ࠭ᵹ")] is False:
        return False
    else:
        return True
def bstack1111ll1l1_opy_(args_list, bstack111l1ll1l11_opy_):
    index = -1
    for value in bstack111l1ll1l11_opy_:
        try:
            index = args_list.index(value)
            return index
        except Exception as e:
            return index
    return index
def bstack1111l1ll1ll_opy_(a, b):
  for k, v in b.items():
    if isinstance(v, dict) and k in a and isinstance(a[k], dict):
        bstack1111l1ll1ll_opy_(a[k], v)
    else:
        a[k] = v
class Result:
    def __init__(self, result=None, duration=None, exception=None, bstack1l111l1l_opy_=None):
        self.result = result
        self.duration = duration
        self.exception = exception
        self.exception_type = type(self.exception).__name__ if exception else None
        self.bstack1l111l1l_opy_ = bstack1l111l1l_opy_
    @classmethod
    def passed(cls):
        return Result(result=bstack1l1lll1_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧᵺ"))
    @classmethod
    def failed(cls, exception=None):
        return Result(result=bstack1l1lll1_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨᵻ"), exception=exception)
    def bstack11111l1111_opy_(self):
        if self.result != bstack1l1lll1_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩᵼ"):
            return None
        if isinstance(self.exception_type, str) and bstack1l1lll1_opy_ (u"ࠥࡅࡸࡹࡥࡳࡶ࡬ࡳࡳࠨᵽ") in self.exception_type:
            return bstack1l1lll1_opy_ (u"ࠦࡆࡹࡳࡦࡴࡷ࡭ࡴࡴࡅࡳࡴࡲࡶࠧᵾ")
        return bstack1l1lll1_opy_ (u"࡛ࠧ࡮ࡩࡣࡱࡨࡱ࡫ࡤࡆࡴࡵࡳࡷࠨᵿ")
    def bstack111l1lll111_opy_(self):
        if self.result != bstack1l1lll1_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ᶀ"):
            return None
        if self.bstack1l111l1l_opy_:
            return self.bstack1l111l1l_opy_
        return bstack1111l1lll11_opy_(self.exception)
def bstack1111l1lll11_opy_(exc):
    return [traceback.format_exception(exc)]
def bstack1111ll1l1l1_opy_(message):
    if isinstance(message, str):
        return not bool(message and message.strip())
    return True
def bstack1l1l1l1l_opy_(object, key, default_value):
    if not object or not object.__dict__:
        return default_value
    if key in object.__dict__.keys():
        return object.__dict__.get(key)
    return default_value
def bstack1l11ll1l1_opy_(config, logger):
    try:
        import playwright
        bstack1111l1l1lll_opy_ = playwright.__file__
        bstack111l11lll11_opy_ = os.path.split(bstack1111l1l1lll_opy_)
        bstack111l1lll11l_opy_ = bstack111l11lll11_opy_[0] + bstack1l1lll1_opy_ (u"ࠧ࠰ࡦࡵ࡭ࡻ࡫ࡲ࠰ࡲࡤࡧࡰࡧࡧࡦ࠱࡯࡭ࡧ࠵ࡣ࡭࡫࠲ࡧࡱ࡯࠮࡫ࡵࠪᶁ")
        os.environ[bstack1l1lll1_opy_ (u"ࠨࡉࡏࡓࡇࡇࡌࡠࡃࡊࡉࡓ࡚࡟ࡉࡖࡗࡔࡤࡖࡒࡐ࡚࡜ࠫᶂ")] = bstack11lll11ll_opy_(config)
        with open(bstack111l1lll11l_opy_, bstack1l1lll1_opy_ (u"ࠩࡵࠫᶃ")) as f:
            file_content = f.read()
            bstack111l1111111_opy_ = bstack1l1lll1_opy_ (u"ࠪ࡫ࡱࡵࡢࡢ࡮࠰ࡥ࡬࡫࡮ࡵࠩᶄ")
            bstack111l11lllll_opy_ = file_content.find(bstack111l1111111_opy_)
            if bstack111l11lllll_opy_ == -1:
              process = subprocess.Popen(bstack1l1lll1_opy_ (u"ࠦࡳࡶ࡭ࠡ࡫ࡱࡷࡹࡧ࡬࡭ࠢࡪࡰࡴࡨࡡ࡭࠯ࡤ࡫ࡪࡴࡴࠣᶅ"), shell=True, cwd=bstack111l11lll11_opy_[0])
              process.wait()
              bstack111l11l1ll1_opy_ = bstack1l1lll1_opy_ (u"ࠬࠨࡵࡴࡧࠣࡷࡹࡸࡩࡤࡶࠥ࠿ࠬᶆ")
              bstack1111lll11ll_opy_ = bstack1l1lll1_opy_ (u"ࠨࠢࠣࠢ࡟ࠦࡺࡹࡥࠡࡵࡷࡶ࡮ࡩࡴ࡝ࠤ࠾ࠤࡨࡵ࡮ࡴࡶࠣࡿࠥࡨ࡯ࡰࡶࡶࡸࡷࡧࡰࠡࡿࠣࡁࠥࡸࡥࡲࡷ࡬ࡶࡪ࠮ࠧࡨ࡮ࡲࡦࡦࡲ࠭ࡢࡩࡨࡲࡹ࠭ࠩ࠼ࠢ࡬ࡪࠥ࠮ࡰࡳࡱࡦࡩࡸࡹ࠮ࡦࡰࡹ࠲ࡌࡒࡏࡃࡃࡏࡣࡆࡍࡅࡏࡖࡢࡌ࡙࡚ࡐࡠࡒࡕࡓ࡝࡟ࠩࠡࡤࡲࡳࡹࡹࡴࡳࡣࡳࠬ࠮ࡁࠠࠣࠤࠥᶇ")
              bstack111l111l111_opy_ = file_content.replace(bstack111l11l1ll1_opy_, bstack1111lll11ll_opy_)
              with open(bstack111l1lll11l_opy_, bstack1l1lll1_opy_ (u"ࠧࡸࠩᶈ")) as f:
                f.write(bstack111l111l111_opy_)
    except Exception as e:
        logger.error(bstack11111l11l1_opy_.format(str(e)))
def bstack1l1l1ll11l_opy_():
  try:
    bstack1111lll1l11_opy_ = os.path.join(tempfile.gettempdir(), bstack1l1lll1_opy_ (u"ࠨࡱࡳࡸ࡮ࡳࡡ࡭ࡡ࡫ࡹࡧࡥࡵࡳ࡮࠱࡮ࡸࡵ࡮ࠨᶉ"))
    bstack1111lll1111_opy_ = []
    if os.path.exists(bstack1111lll1l11_opy_):
      with open(bstack1111lll1l11_opy_) as f:
        bstack1111lll1111_opy_ = json.load(f)
      os.remove(bstack1111lll1l11_opy_)
    return bstack1111lll1111_opy_
  except:
    pass
  return []
def bstack11ll1l11ll_opy_(bstack1lll1l1ll1_opy_):
  try:
    bstack1111lll1111_opy_ = []
    bstack1111lll1l11_opy_ = os.path.join(tempfile.gettempdir(), bstack1l1lll1_opy_ (u"ࠩࡲࡴࡹ࡯࡭ࡢ࡮ࡢ࡬ࡺࡨ࡟ࡶࡴ࡯࠲࡯ࡹ࡯࡯ࠩᶊ"))
    if os.path.exists(bstack1111lll1l11_opy_):
      with open(bstack1111lll1l11_opy_) as f:
        bstack1111lll1111_opy_ = json.load(f)
    bstack1111lll1111_opy_.append(bstack1lll1l1ll1_opy_)
    with open(bstack1111lll1l11_opy_, bstack1l1lll1_opy_ (u"ࠪࡻࠬᶋ")) as f:
        json.dump(bstack1111lll1111_opy_, f)
  except:
    pass
def bstack1l111llll1_opy_(logger, bstack111l11l1111_opy_ = False):
  try:
    test_name = os.environ.get(bstack1l1lll1_opy_ (u"ࠫࡕ࡟ࡔࡆࡕࡗࡣ࡙ࡋࡓࡕࡡࡑࡅࡒࡋࠧᶌ"), bstack1l1lll1_opy_ (u"ࠬ࠭ᶍ"))
    if test_name == bstack1l1lll1_opy_ (u"࠭ࠧᶎ"):
        test_name = threading.current_thread().__dict__.get(bstack1l1lll1_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࡂࡥࡦࡢࡸࡪࡹࡴࡠࡰࡤࡱࡪ࠭ᶏ"), bstack1l1lll1_opy_ (u"ࠨࠩᶐ"))
    bstack1111l1ll11l_opy_ = bstack1l1lll1_opy_ (u"ࠩ࠯ࠤࠬᶑ").join(threading.current_thread().bstackTestErrorMessages)
    if bstack111l11l1111_opy_:
        bstack1l11l1lll_opy_ = os.environ.get(bstack1l1lll1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡎࡔࡄࡆ࡚ࠪᶒ"), bstack1l1lll1_opy_ (u"ࠫ࠵࠭ᶓ"))
        bstack11lll1111_opy_ = {bstack1l1lll1_opy_ (u"ࠬࡴࡡ࡮ࡧࠪᶔ"): test_name, bstack1l1lll1_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬᶕ"): bstack1111l1ll11l_opy_, bstack1l1lll1_opy_ (u"ࠧࡪࡰࡧࡩࡽ࠭ᶖ"): bstack1l11l1lll_opy_}
        bstack111ll1111ll_opy_ = []
        bstack111l111lll1_opy_ = os.path.join(tempfile.gettempdir(), bstack1l1lll1_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࡠࡲࡳࡴࡤ࡫ࡲࡳࡱࡵࡣࡱ࡯ࡳࡵ࠰࡭ࡷࡴࡴࠧᶗ"))
        if os.path.exists(bstack111l111lll1_opy_):
            with open(bstack111l111lll1_opy_) as f:
                bstack111ll1111ll_opy_ = json.load(f)
        bstack111ll1111ll_opy_.append(bstack11lll1111_opy_)
        with open(bstack111l111lll1_opy_, bstack1l1lll1_opy_ (u"ࠩࡺࠫᶘ")) as f:
            json.dump(bstack111ll1111ll_opy_, f)
    else:
        bstack11lll1111_opy_ = {bstack1l1lll1_opy_ (u"ࠪࡲࡦࡳࡥࠨᶙ"): test_name, bstack1l1lll1_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪᶚ"): bstack1111l1ll11l_opy_, bstack1l1lll1_opy_ (u"ࠬ࡯࡮ࡥࡧࡻࠫᶛ"): str(multiprocessing.current_process().name)}
        if bstack1l1lll1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡥࡥࡳࡴࡲࡶࡤࡲࡩࡴࡶࠪᶜ") not in multiprocessing.current_process().__dict__.keys():
            multiprocessing.current_process().bstack_error_list = []
        multiprocessing.current_process().bstack_error_list.append(bstack11lll1111_opy_)
  except Exception as e:
      logger.warn(bstack1l1lll1_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡷࡹࡵࡲࡦࠢࡳࡽࡹ࡫ࡳࡵࠢࡩࡹࡳࡴࡥ࡭ࠢࡧࡥࡹࡧ࠺ࠡࡽࢀࠦᶝ").format(e))
def bstack111l1111ll_opy_(error_message, test_name, index, logger):
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack1l1lll1_opy_ (u"ࠨࡨ࡬ࡰࡪࡲ࡯ࡤ࡭ࠣࡲࡴࡺࠠࡢࡸࡤ࡭ࡱࡧࡢ࡭ࡧ࠯ࠤࡺࡹࡩ࡯ࡩࠣࡦࡦࡹࡩࡤࠢࡩ࡭ࡱ࡫ࠠࡰࡲࡨࡶࡦࡺࡩࡰࡰࡶࠫᶞ"))
    try:
      bstack1111ll111l1_opy_ = []
      bstack11lll1111_opy_ = {bstack1l1lll1_opy_ (u"ࠩࡱࡥࡲ࡫ࠧᶟ"): test_name, bstack1l1lll1_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩᶠ"): error_message, bstack1l1lll1_opy_ (u"ࠫ࡮ࡴࡤࡦࡺࠪᶡ"): index}
      bstack111l1l111l1_opy_ = os.path.join(tempfile.gettempdir(), bstack1l1lll1_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࡣࡪࡸࡲࡰࡴࡢࡰ࡮ࡹࡴ࠯࡬ࡶࡳࡳ࠭ᶢ"))
      if os.path.exists(bstack111l1l111l1_opy_):
          with open(bstack111l1l111l1_opy_) as f:
              bstack1111ll111l1_opy_ = json.load(f)
      bstack1111ll111l1_opy_.append(bstack11lll1111_opy_)
      with open(bstack111l1l111l1_opy_, bstack1l1lll1_opy_ (u"࠭ࡷࠨᶣ")) as f:
          json.dump(bstack1111ll111l1_opy_, f)
    except Exception as e:
      logger.warn(bstack1l1lll1_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡷࡹࡵࡲࡦࠢࡵࡳࡧࡵࡴࠡࡨࡸࡲࡳ࡫࡬ࠡࡦࡤࡸࡦࡀࠠࡼࡿࠥᶤ").format(e))
    return
  bstack1111ll111l1_opy_ = []
  bstack11lll1111_opy_ = {bstack1l1lll1_opy_ (u"ࠨࡰࡤࡱࡪ࠭ᶥ"): test_name, bstack1l1lll1_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨᶦ"): error_message, bstack1l1lll1_opy_ (u"ࠪ࡭ࡳࡪࡥࡹࠩᶧ"): index}
  bstack111l1l111l1_opy_ = os.path.join(tempfile.gettempdir(), bstack1l1lll1_opy_ (u"ࠫࡷࡵࡢࡰࡶࡢࡩࡷࡸ࡯ࡳࡡ࡯࡭ࡸࡺ࠮࡫ࡵࡲࡲࠬᶨ"))
  lock_file = bstack111l1l111l1_opy_ + bstack1l1lll1_opy_ (u"ࠬ࠴࡬ࡰࡥ࡮ࠫᶩ")
  try:
    with FileLock(lock_file, timeout=10):
      if os.path.exists(bstack111l1l111l1_opy_):
          with open(bstack111l1l111l1_opy_, bstack1l1lll1_opy_ (u"࠭ࡲࠨᶪ")) as f:
              content = f.read().strip()
              if content:
                  bstack1111ll111l1_opy_ = json.load(open(bstack111l1l111l1_opy_))
      bstack1111ll111l1_opy_.append(bstack11lll1111_opy_)
      with open(bstack111l1l111l1_opy_, bstack1l1lll1_opy_ (u"ࠧࡸࠩᶫ")) as f:
          json.dump(bstack1111ll111l1_opy_, f)
  except Exception as e:
    logger.warn(bstack1l1lll1_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡸࡺ࡯ࡳࡧࠣࡶࡴࡨ࡯ࡵࠢࡩࡹࡳࡴࡥ࡭ࠢࡧࡥࡹࡧࠠࡸ࡫ࡷ࡬ࠥ࡬ࡩ࡭ࡧࠣࡰࡴࡩ࡫ࡪࡰࡪ࠾ࠥࢁࡽࠣᶬ").format(e))
def bstack1l1ll11ll_opy_(bstack1111l1l11_opy_, name, logger):
  try:
    bstack11lll1111_opy_ = {bstack1l1lll1_opy_ (u"ࠩࡱࡥࡲ࡫ࠧᶭ"): name, bstack1l1lll1_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩᶮ"): bstack1111l1l11_opy_, bstack1l1lll1_opy_ (u"ࠫ࡮ࡴࡤࡦࡺࠪᶯ"): str(threading.current_thread()._name)}
    return bstack11lll1111_opy_
  except Exception as e:
    logger.warn(bstack1l1lll1_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡵࡷࡳࡷ࡫ࠠࡣࡧ࡫ࡥࡻ࡫ࠠࡧࡷࡱࡲࡪࡲࠠࡥࡣࡷࡥ࠿ࠦࡻࡾࠤᶰ").format(e))
  return
def bstack1111llllll1_opy_():
    return platform.system() == bstack1l1lll1_opy_ (u"࠭ࡗࡪࡰࡧࡳࡼࡹࠧᶱ")
def bstack1l111l1111_opy_(bstack1111ll1l11l_opy_, config, logger):
    bstack111ll111111_opy_ = {}
    try:
        return {key: config[key] for key in config if bstack1111ll1l11l_opy_.match(key)}
    except Exception as e:
        logger.debug(bstack1l1lll1_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡪ࡮ࡲࡴࡦࡴࠣࡧࡴࡴࡦࡪࡩࠣ࡯ࡪࡿࡳࠡࡤࡼࠤࡷ࡫ࡧࡦࡺࠣࡱࡦࡺࡣࡩ࠼ࠣࡿࢂࠨᶲ").format(e))
    return bstack111ll111111_opy_
def bstack11l1ll111l1_opy_(bstack111l111111l_opy_, bstack111l1l11ll1_opy_):
    bstack111l1ll1l1l_opy_ = version.parse(bstack111l111111l_opy_)
    bstack1111l1l1ll1_opy_ = version.parse(bstack111l1l11ll1_opy_)
    if bstack111l1ll1l1l_opy_ > bstack1111l1l1ll1_opy_:
        return 1
    elif bstack111l1ll1l1l_opy_ < bstack1111l1l1ll1_opy_:
        return -1
    else:
        return 0
def bstack1l11111l_opy_():
    return datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None)
def bstack1111l1l1l11_opy_(timestamp):
    return datetime.datetime.fromtimestamp(timestamp, datetime.timezone.utc).replace(tzinfo=None)
def bstack1111lllll11_opy_(framework):
    from browserstack_sdk._version import __version__
    return str(framework) + str(__version__)
def bstack111l111lll_opy_(options, framework, config, bstack1ll11ll11l_opy_={}):
    if options is None:
        return
    if getattr(options, bstack1l1lll1_opy_ (u"ࠨࡩࡨࡸࠬᶳ"), None):
        caps = options
    else:
        caps = options.to_capabilities()
    bstack1l1l1l11ll_opy_ = caps.get(bstack1l1lll1_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪᶴ"))
    bstack1111l11llll_opy_ = True
    bstack1111l1l11l_opy_ = os.environ[bstack1l1lll1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨᶵ")]
    bstack1l111lll1ll_opy_ = config.get(bstack1l1lll1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫᶶ"), False)
    if bstack1l111lll1ll_opy_:
        bstack1l1l111l111_opy_ = config.get(bstack1l1lll1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷࠬᶷ"), {})
        bstack1l1l111l111_opy_[bstack1l1lll1_opy_ (u"࠭ࡡࡶࡶ࡫ࡘࡴࡱࡥ࡯ࠩᶸ")] = os.getenv(bstack1l1lll1_opy_ (u"ࠧࡃࡕࡢࡅ࠶࠷࡙ࡠࡌ࡚ࡘࠬᶹ"))
        bstack1111l1ll1l1_opy_ = json.loads(os.getenv(bstack1l1lll1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡤࡇࡃࡄࡇࡖࡗࡎࡈࡉࡍࡋࡗ࡝ࡤࡉࡏࡏࡈࡌࡋ࡚ࡘࡁࡕࡋࡒࡒࡤ࡟ࡍࡍࠩᶺ"), bstack1l1lll1_opy_ (u"ࠩࡾࢁࠬᶻ"))).get(bstack1l1lll1_opy_ (u"ࠪࡷࡨࡧ࡮࡯ࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫᶼ"))
    if bstack1111lll1l1l_opy_(caps.get(bstack1l1lll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡹࡸ࡫ࡗ࠴ࡅࠪᶽ"))) or bstack1111lll1l1l_opy_(caps.get(bstack1l1lll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡺࡹࡥࡠࡹ࠶ࡧࠬᶾ"))):
        bstack1111l11llll_opy_ = False
    if bstack1111lll1l1_opy_({bstack1l1lll1_opy_ (u"ࠨࡵࡴࡧ࡚࠷ࡈࠨᶿ"): bstack1111l11llll_opy_}):
        bstack1l1l1l11ll_opy_ = bstack1l1l1l11ll_opy_ or {}
        bstack1l1l1l11ll_opy_[bstack1l1lll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࡙ࡄࡌࠩ᷀")] = bstack1111lllll11_opy_(framework)
        bstack1l1l1l11ll_opy_[bstack1l1lll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠪ᷁")] = bstack1llll1111ll_opy_()
        bstack1l1l1l11ll_opy_[bstack1l1lll1_opy_ (u"ࠩࡷࡩࡸࡺࡨࡶࡤࡅࡹ࡮ࡲࡤࡖࡷ࡬ࡨ᷂ࠬ")] = bstack1111l1l11l_opy_
        bstack1l1l1l11ll_opy_[bstack1l1lll1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡒࡵࡳࡩࡻࡣࡵࡏࡤࡴࠬ᷃")] = bstack1ll11ll11l_opy_
        if bstack1l111lll1ll_opy_:
            bstack1l1l1l11ll_opy_[bstack1l1lll1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ᷄")] = bstack1l111lll1ll_opy_
            bstack1l1l1l11ll_opy_[bstack1l1lll1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷࠬ᷅")] = bstack1l1l111l111_opy_
            bstack1l1l1l11ll_opy_[bstack1l1lll1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭᷆")][bstack1l1lll1_opy_ (u"ࠧࡴࡥࡤࡲࡳ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨ᷇")] = bstack1111l1ll1l1_opy_
        if getattr(options, bstack1l1lll1_opy_ (u"ࠨࡵࡨࡸࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡺࠩ᷈"), None):
            options.set_capability(bstack1l1lll1_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪ᷉"), bstack1l1l1l11ll_opy_)
        else:
            options[bstack1l1lll1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶ᷊ࠫ")] = bstack1l1l1l11ll_opy_
    else:
        if getattr(options, bstack1l1lll1_opy_ (u"ࠫࡸ࡫ࡴࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷࡽࠬ᷋"), None):
            options.set_capability(bstack1l1lll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡖࡈࡐ࠭᷌"), bstack1111lllll11_opy_(framework))
            options.set_capability(bstack1l1lll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠧ᷍"), bstack1llll1111ll_opy_())
            options.set_capability(bstack1l1lll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡴࡦࡵࡷ࡬ࡺࡨࡂࡶ࡫࡯ࡨ࡚ࡻࡩࡥ᷎ࠩ"), bstack1111l1l11l_opy_)
            options.set_capability(bstack1l1lll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡣࡷ࡬ࡰࡩࡖࡲࡰࡦࡸࡧࡹࡓࡡࡱ᷏ࠩ"), bstack1ll11ll11l_opy_)
            if bstack1l111lll1ll_opy_:
                options.set_capability(bstack1l1lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨ᷐"), bstack1l111lll1ll_opy_)
                options.set_capability(bstack1l1lll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩ᷑"), bstack1l1l111l111_opy_)
                options.set_capability(bstack1l1lll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵ࠱ࡷࡨࡧ࡮࡯ࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫ᷒"), bstack1111l1ll1l1_opy_)
        else:
            options[bstack1l1lll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡖࡈࡐ࠭ᷓ")] = bstack1111lllll11_opy_(framework)
            options[bstack1l1lll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠧᷔ")] = bstack1llll1111ll_opy_()
            options[bstack1l1lll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡴࡦࡵࡷ࡬ࡺࡨࡂࡶ࡫࡯ࡨ࡚ࡻࡩࡥࠩᷕ")] = bstack1111l1l11l_opy_
            options[bstack1l1lll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡣࡷ࡬ࡰࡩࡖࡲࡰࡦࡸࡧࡹࡓࡡࡱࠩᷖ")] = bstack1ll11ll11l_opy_
            if bstack1l111lll1ll_opy_:
                options[bstack1l1lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨᷗ")] = bstack1l111lll1ll_opy_
                options[bstack1l1lll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩᷘ")] = bstack1l1l111l111_opy_
                options[bstack1l1lll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪᷙ")][bstack1l1lll1_opy_ (u"ࠬࡹࡣࡢࡰࡱࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ᷚ")] = bstack1111l1ll1l1_opy_
    return options
def bstack1111ll11lll_opy_(ws_endpoint, framework):
    bstack1ll11ll11l_opy_ = bstack1111111l_opy_.get_property(bstack1l1lll1_opy_ (u"ࠨࡐࡍࡃ࡜࡛ࡗࡏࡇࡉࡖࡢࡔࡗࡕࡄࡖࡅࡗࡣࡒࡇࡐࠣᷛ"))
    if ws_endpoint and len(ws_endpoint.split(bstack1l1lll1_opy_ (u"ࠧࡤࡣࡳࡷࡂ࠭ᷜ"))) > 1:
        ws_url = ws_endpoint.split(bstack1l1lll1_opy_ (u"ࠨࡥࡤࡴࡸࡃࠧᷝ"))[0]
        if bstack1l1lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱࠬᷞ") in ws_url:
            from browserstack_sdk._version import __version__
            bstack1111lll111l_opy_ = json.loads(urllib.parse.unquote(ws_endpoint.split(bstack1l1lll1_opy_ (u"ࠪࡧࡦࡶࡳ࠾ࠩᷟ"))[1]))
            bstack1111lll111l_opy_ = bstack1111lll111l_opy_ or {}
            bstack1111l1l11l_opy_ = os.environ[bstack1l1lll1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩᷠ")]
            bstack1111lll111l_opy_[bstack1l1lll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡖࡈࡐ࠭ᷡ")] = str(framework) + str(__version__)
            bstack1111lll111l_opy_[bstack1l1lll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠧᷢ")] = bstack1llll1111ll_opy_()
            bstack1111lll111l_opy_[bstack1l1lll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡴࡦࡵࡷ࡬ࡺࡨࡂࡶ࡫࡯ࡨ࡚ࡻࡩࡥࠩᷣ")] = bstack1111l1l11l_opy_
            bstack1111lll111l_opy_[bstack1l1lll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡣࡷ࡬ࡰࡩࡖࡲࡰࡦࡸࡧࡹࡓࡡࡱࠩᷤ")] = bstack1ll11ll11l_opy_
            ws_endpoint = ws_endpoint.split(bstack1l1lll1_opy_ (u"ࠩࡦࡥࡵࡹ࠽ࠨᷥ"))[0] + bstack1l1lll1_opy_ (u"ࠪࡧࡦࡶࡳ࠾ࠩᷦ") + urllib.parse.quote(json.dumps(bstack1111lll111l_opy_))
    return ws_endpoint
def bstack1111ll111l_opy_():
    global bstack1l11llllll_opy_
    from playwright._impl._browser_type import BrowserType
    bstack1l11llllll_opy_ = BrowserType.connect
    return bstack1l11llllll_opy_
def bstack111l11llll_opy_(framework_name):
    global bstack1l1ll111l1_opy_
    bstack1l1ll111l1_opy_ = framework_name
    return framework_name
def bstack11l1ll1lll_opy_(self, *args, **kwargs):
    global bstack1l11llllll_opy_
    try:
        global bstack1l1ll111l1_opy_
        if bstack1l1lll1_opy_ (u"ࠫࡼࡹࡅ࡯ࡦࡳࡳ࡮ࡴࡴࠨᷧ") in kwargs:
            kwargs[bstack1l1lll1_opy_ (u"ࠬࡽࡳࡆࡰࡧࡴࡴ࡯࡮ࡵࠩᷨ")] = bstack1111ll11lll_opy_(
                kwargs.get(bstack1l1lll1_opy_ (u"࠭ࡷࡴࡇࡱࡨࡵࡵࡩ࡯ࡶࠪᷩ"), None),
                bstack1l1ll111l1_opy_
            )
    except Exception as e:
        logger.error(bstack1l1lll1_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡷࡩࡧࡱࠤࡵࡸ࡯ࡤࡧࡶࡷ࡮ࡴࡧࠡࡕࡇࡏࠥࡩࡡࡱࡵ࠽ࠤࢀࢃࠢᷪ").format(str(e)))
    return bstack1l11llllll_opy_(self, *args, **kwargs)
def bstack111l111ll1l_opy_(bstack1111ll1llll_opy_, proxies):
    proxy_settings = {}
    try:
        if not proxies:
            proxies = bstack11l1l11ll_opy_(bstack1111ll1llll_opy_, bstack1l1lll1_opy_ (u"ࠣࠤᷫ"))
        if proxies and proxies.get(bstack1l1lll1_opy_ (u"ࠤ࡫ࡸࡹࡶࡳࠣᷬ")):
            parsed_url = urlparse(proxies.get(bstack1l1lll1_opy_ (u"ࠥ࡬ࡹࡺࡰࡴࠤᷭ")))
            if parsed_url and parsed_url.hostname: proxy_settings[bstack1l1lll1_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡋࡳࡸࡺࠧᷮ")] = str(parsed_url.hostname)
            if parsed_url and parsed_url.port: proxy_settings[bstack1l1lll1_opy_ (u"ࠬࡶࡲࡰࡺࡼࡔࡴࡸࡴࠨᷯ")] = str(parsed_url.port)
            if parsed_url and parsed_url.username: proxy_settings[bstack1l1lll1_opy_ (u"࠭ࡰࡳࡱࡻࡽ࡚ࡹࡥࡳࠩᷰ")] = str(parsed_url.username)
            if parsed_url and parsed_url.password: proxy_settings[bstack1l1lll1_opy_ (u"ࠧࡱࡴࡲࡼࡾࡖࡡࡴࡵࠪᷱ")] = str(parsed_url.password)
        return proxy_settings
    except:
        return proxy_settings
def bstack11l11l11l1_opy_(bstack1111ll1llll_opy_):
    bstack111l1l1ll11_opy_ = {
        bstack11l1l1ll111_opy_[bstack111l11llll1_opy_]: bstack1111ll1llll_opy_[bstack111l11llll1_opy_]
        for bstack111l11llll1_opy_ in bstack1111ll1llll_opy_
        if bstack111l11llll1_opy_ in bstack11l1l1ll111_opy_
    }
    bstack111l1l1ll11_opy_[bstack1l1lll1_opy_ (u"ࠣࡲࡵࡳࡽࡿࡓࡦࡶࡷ࡭ࡳ࡭ࡳࠣᷲ")] = bstack111l111ll1l_opy_(bstack1111ll1llll_opy_, bstack1111111l_opy_.get_property(bstack1l1lll1_opy_ (u"ࠤࡳࡶࡴࡾࡹࡔࡧࡷࡸ࡮ࡴࡧࡴࠤᷳ")))
    bstack111l11l11l1_opy_ = [element.lower() for element in bstack11l1l1ll1ll_opy_]
    bstack111l111ll11_opy_(bstack111l1l1ll11_opy_, bstack111l11l11l1_opy_)
    return bstack111l1l1ll11_opy_
def bstack111l111ll11_opy_(d, keys):
    for key in list(d.keys()):
        if key.lower() in keys:
            d[key] = bstack1l1lll1_opy_ (u"ࠥ࠮࠯࠰ࠪࠣᷴ")
    for value in d.values():
        if isinstance(value, dict):
            bstack111l111ll11_opy_(value, keys)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    bstack111l111ll11_opy_(item, keys)
def bstack1ll1l1lllll_opy_():
    bstack1111lllllll_opy_ = [os.environ.get(bstack1l1lll1_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡊࡎࡒࡅࡔࡡࡇࡍࡗࠨ᷵")), os.path.join(os.path.expanduser(bstack1l1lll1_opy_ (u"ࠧࢄࠢ᷶")), bstack1l1lll1_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ᷷࠭")), os.path.join(bstack1l1lll1_opy_ (u"ࠧ࠰ࡶࡰࡴ᷸ࠬ"), bstack1l1lll1_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨ᷹"))]
    for path in bstack1111lllllll_opy_:
        if path is None:
            continue
        try:
            if os.path.exists(path):
                logger.debug(bstack1l1lll1_opy_ (u"ࠤࡉ࡭ࡱ࡫ࠠࠨࠤ᷺") + str(path) + bstack1l1lll1_opy_ (u"ࠥࠫࠥ࡫ࡸࡪࡵࡷࡷ࠳ࠨ᷻"))
                if not os.access(path, os.W_OK):
                    logger.debug(bstack1l1lll1_opy_ (u"ࠦࡌ࡯ࡶࡪࡰࡪࠤࡵ࡫ࡲ࡮࡫ࡶࡷ࡮ࡵ࡮ࡴࠢࡩࡳࡷࠦࠧࠣ᷼") + str(path) + bstack1l1lll1_opy_ (u"᷽ࠧ࠭ࠢ"))
                    os.chmod(path, 0o777)
                else:
                    logger.debug(bstack1l1lll1_opy_ (u"ࠨࡆࡪ࡮ࡨࠤࠬࠨ᷾") + str(path) + bstack1l1lll1_opy_ (u"ࠢࠨࠢࡤࡰࡷ࡫ࡡࡥࡻࠣ࡬ࡦࡹࠠࡵࡪࡨࠤࡷ࡫ࡱࡶ࡫ࡵࡩࡩࠦࡰࡦࡴࡰ࡭ࡸࡹࡩࡰࡰࡶ࠲᷿ࠧ"))
            else:
                logger.debug(bstack1l1lll1_opy_ (u"ࠣࡅࡵࡩࡦࡺࡩ࡯ࡩࠣࡪ࡮ࡲࡥࠡࠩࠥḀ") + str(path) + bstack1l1lll1_opy_ (u"ࠤࠪࠤࡼ࡯ࡴࡩࠢࡺࡶ࡮ࡺࡥࠡࡲࡨࡶࡲ࡯ࡳࡴ࡫ࡲࡲ࠳ࠨḁ"))
                os.makedirs(path, exist_ok=True)
                os.chmod(path, 0o777)
            logger.debug(bstack1l1lll1_opy_ (u"ࠥࡓࡵ࡫ࡲࡢࡶ࡬ࡳࡳࠦࡳࡶࡥࡦࡩࡪࡪࡥࡥࠢࡩࡳࡷࠦࠧࠣḂ") + str(path) + bstack1l1lll1_opy_ (u"ࠦࠬ࠴ࠢḃ"))
            return path
        except Exception as e:
            logger.debug(bstack1l1lll1_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡵࡨࡸࠥࡻࡰࠡࡨ࡬ࡰࡪࠦࠧࡼࡲࡤࡸ࡭ࢃࠧ࠻ࠢࠥḄ") + str(e) + bstack1l1lll1_opy_ (u"ࠨࠢḅ"))
    logger.debug(bstack1l1lll1_opy_ (u"ࠢࡂ࡮࡯ࠤࡵࡧࡴࡩࡵࠣࡪࡦ࡯࡬ࡦࡦ࠱ࠦḆ"))
    return None
@measure(event_name=EVENTS.bstack11l1l11l11l_opy_, stage=STAGE.bstack1111llll1l_opy_)
def bstack1l1ll11l111_opy_(binary_path, bstack1l1l11lll11_opy_, bs_config):
    logger.debug(bstack1l1lll1_opy_ (u"ࠣࡅࡸࡶࡷ࡫࡮ࡵࠢࡆࡐࡎࠦࡐࡢࡶ࡫ࠤ࡫ࡵࡵ࡯ࡦ࠽ࠤࢀࢃࠢḇ").format(binary_path))
    bstack1111ll11l11_opy_ = bstack1l1lll1_opy_ (u"ࠩࠪḈ")
    bstack111l11111l1_opy_ = {
        bstack1l1lll1_opy_ (u"ࠪࡷࡩࡱ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨḉ"): __version__,
        bstack1l1lll1_opy_ (u"ࠦࡴࡹࠢḊ"): platform.system(),
        bstack1l1lll1_opy_ (u"ࠧࡵࡳࡠࡣࡵࡧ࡭ࠨḋ"): platform.machine(),
        bstack1l1lll1_opy_ (u"ࠨࡣ࡭࡫ࡢࡺࡪࡸࡳࡪࡱࡱࠦḌ"): bstack1l1lll1_opy_ (u"ࠧ࠱ࠩḍ"),
        bstack1l1lll1_opy_ (u"ࠣࡵࡧ࡯ࡤࡲࡡ࡯ࡩࡸࡥ࡬࡫ࠢḎ"): bstack1l1lll1_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯ࠩḏ")
    }
    bstack111l111l1ll_opy_(bstack111l11111l1_opy_)
    try:
        if binary_path:
            bstack111l11111l1_opy_[bstack1l1lll1_opy_ (u"ࠪࡧࡱ࡯࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨḐ")] = subprocess.check_output([binary_path, bstack1l1lll1_opy_ (u"ࠦࡻ࡫ࡲࡴ࡫ࡲࡲࠧḑ")]).strip().decode(bstack1l1lll1_opy_ (u"ࠬࡻࡴࡧ࠯࠻ࠫḒ"))
        response = requests.request(
            bstack1l1lll1_opy_ (u"࠭ࡇࡆࡖࠪḓ"),
            url=bstack1l111l11l_opy_(bstack11l1l1111l1_opy_),
            headers=None,
            auth=(bs_config[bstack1l1lll1_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩḔ")], bs_config[bstack1l1lll1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫḕ")]),
            json=None,
            params=bstack111l11111l1_opy_
        )
        data = response.json()
        if response.status_code == 200 and bstack1l1lll1_opy_ (u"ࠩࡸࡶࡱ࠭Ḗ") in data.keys() and bstack1l1lll1_opy_ (u"ࠪࡹࡵࡪࡡࡵࡧࡧࡣࡨࡲࡩࡠࡸࡨࡶࡸ࡯࡯࡯ࠩḗ") in data.keys():
            logger.debug(bstack1l1lll1_opy_ (u"ࠦࡓ࡫ࡥࡥࠢࡷࡳࠥࡻࡰࡥࡣࡷࡩࠥࡨࡩ࡯ࡣࡵࡽ࠱ࠦࡣࡶࡴࡵࡩࡳࡺࠠࡣ࡫ࡱࡥࡷࡿࠠࡷࡧࡵࡷ࡮ࡵ࡮࠻ࠢࡾࢁࠧḘ").format(bstack111l11111l1_opy_[bstack1l1lll1_opy_ (u"ࠬࡩ࡬ࡪࡡࡹࡩࡷࡹࡩࡰࡰࠪḙ")]))
            if bstack1l1lll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡈࡉࡏࡃࡕ࡝ࡤ࡛ࡒࡍࠩḚ") in os.environ:
                logger.debug(bstack1l1lll1_opy_ (u"ࠢࡔ࡭࡬ࡴࡵ࡯࡮ࡨࠢࡥ࡭ࡳࡧࡲࡺࠢࡧࡳࡼࡴ࡬ࡰࡣࡧࠤࡦࡹࠠࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡂࡊࡐࡄࡖ࡞ࡥࡕࡓࡎࠣ࡭ࡸࠦࡳࡦࡶࠥḛ"))
                data[bstack1l1lll1_opy_ (u"ࠨࡷࡵࡰࠬḜ")] = os.environ[bstack1l1lll1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡄࡌࡒࡆࡘ࡙ࡠࡗࡕࡐࠬḝ")]
            bstack111l1l1l1l1_opy_ = bstack111l1l11lll_opy_(data[bstack1l1lll1_opy_ (u"ࠪࡹࡷࡲࠧḞ")], bstack1l1l11lll11_opy_)
            bstack1111ll11l11_opy_ = os.path.join(bstack1l1l11lll11_opy_, bstack111l1l1l1l1_opy_)
            os.chmod(bstack1111ll11l11_opy_, 0o777) # bstack1111l1lll1l_opy_ permission
            return bstack1111ll11l11_opy_
    except Exception as e:
        logger.debug(bstack1l1lll1_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡻ࡭࡯࡬ࡦࠢࡧࡳࡼࡴ࡬ࡰࡣࡧ࡭ࡳ࡭ࠠ࡯ࡧࡺࠤࡘࡊࡋࠡࡽࢀࠦḟ").format(e))
    return binary_path
def bstack111l111l1ll_opy_(bstack111l11111l1_opy_):
    try:
        if bstack1l1lll1_opy_ (u"ࠬࡲࡩ࡯ࡷࡻࠫḠ") not in bstack111l11111l1_opy_[bstack1l1lll1_opy_ (u"࠭࡯ࡴࠩḡ")].lower():
            return
        if os.path.exists(bstack1l1lll1_opy_ (u"ࠢ࠰ࡧࡷࡧ࠴ࡵࡳ࠮ࡴࡨࡰࡪࡧࡳࡦࠤḢ")):
            with open(bstack1l1lll1_opy_ (u"ࠣ࠱ࡨࡸࡨ࠵࡯ࡴ࠯ࡵࡩࡱ࡫ࡡࡴࡧࠥḣ"), bstack1l1lll1_opy_ (u"ࠤࡵࠦḤ")) as f:
                bstack111l11lll1l_opy_ = {}
                for line in f:
                    if bstack1l1lll1_opy_ (u"ࠥࡁࠧḥ") in line:
                        key, value = line.rstrip().split(bstack1l1lll1_opy_ (u"ࠦࡂࠨḦ"), 1)
                        bstack111l11lll1l_opy_[key] = value.strip(bstack1l1lll1_opy_ (u"ࠬࠨ࡜ࠨࠩḧ"))
                bstack111l11111l1_opy_[bstack1l1lll1_opy_ (u"࠭ࡤࡪࡵࡷࡶࡴ࠭Ḩ")] = bstack111l11lll1l_opy_.get(bstack1l1lll1_opy_ (u"ࠢࡊࡆࠥḩ"), bstack1l1lll1_opy_ (u"ࠣࠤḪ"))
        elif os.path.exists(bstack1l1lll1_opy_ (u"ࠤ࠲ࡩࡹࡩ࠯ࡢ࡮ࡳ࡭ࡳ࡫࠭ࡳࡧ࡯ࡩࡦࡹࡥࠣḫ")):
            bstack111l11111l1_opy_[bstack1l1lll1_opy_ (u"ࠪࡨ࡮ࡹࡴࡳࡱࠪḬ")] = bstack1l1lll1_opy_ (u"ࠫࡦࡲࡰࡪࡰࡨࠫḭ")
    except Exception as e:
        logger.debug(bstack1l1lll1_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡩࡨࡸࠥࡪࡩࡴࡶࡵࡳࠥࡵࡦࠡ࡮࡬ࡲࡺࡾࠢḮ") + e)
@measure(event_name=EVENTS.bstack11l11lll1l1_opy_, stage=STAGE.bstack1111llll1l_opy_)
def bstack111l1l11lll_opy_(bstack111l1111l11_opy_, bstack1111l1l11l1_opy_):
    logger.debug(bstack1l1lll1_opy_ (u"ࠨࡄࡰࡹࡱࡰࡴࡧࡤࡪࡰࡪࠤࡘࡊࡋࠡࡤ࡬ࡲࡦࡸࡹࠡࡨࡵࡳࡲࡀࠠࠣḯ") + str(bstack111l1111l11_opy_) + bstack1l1lll1_opy_ (u"ࠢࠣḰ"))
    zip_path = os.path.join(bstack1111l1l11l1_opy_, bstack1l1lll1_opy_ (u"ࠣࡦࡲࡻࡳࡲ࡯ࡢࡦࡨࡨࡤ࡬ࡩ࡭ࡧ࠱ࡾ࡮ࡶࠢḱ"))
    bstack111l1l1l1l1_opy_ = bstack1l1lll1_opy_ (u"ࠩࠪḲ")
    with requests.get(bstack111l1111l11_opy_, stream=True) as response:
        response.raise_for_status()
        with open(zip_path, bstack1l1lll1_opy_ (u"ࠥࡻࡧࠨḳ")) as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
        logger.debug(bstack1l1lll1_opy_ (u"ࠦࡋ࡯࡬ࡦࠢࡧࡳࡼࡴ࡬ࡰࡣࡧࡩࡩࠦࡳࡶࡥࡦࡩࡸࡹࡦࡶ࡮࡯ࡽ࠳ࠨḴ"))
    with zipfile.ZipFile(zip_path, bstack1l1lll1_opy_ (u"ࠬࡸࠧḵ")) as zip_ref:
        bstack1111llll11l_opy_ = zip_ref.namelist()
        if len(bstack1111llll11l_opy_) > 0:
            bstack111l1l1l1l1_opy_ = bstack1111llll11l_opy_[0] # bstack1111lll1ll1_opy_ bstack11l1l1ll1l1_opy_ will be bstack111l1ll11ll_opy_ 1 file i.e. the binary in the zip
        zip_ref.extractall(bstack1111l1l11l1_opy_)
        logger.debug(bstack1l1lll1_opy_ (u"ࠨࡆࡪ࡮ࡨࡷࠥࡹࡵࡤࡥࡨࡷࡸ࡬ࡵ࡭࡮ࡼࠤࡪࡾࡴࡳࡣࡦࡸࡪࡪࠠࡵࡱࠣࠫࠧḶ") + str(bstack1111l1l11l1_opy_) + bstack1l1lll1_opy_ (u"ࠢࠨࠤḷ"))
    os.remove(zip_path)
    return bstack111l1l1l1l1_opy_
def get_cli_dir():
    bstack1111ll1ll1l_opy_ = bstack1ll1l1lllll_opy_()
    if bstack1111ll1ll1l_opy_:
        bstack1l1l11lll11_opy_ = os.path.join(bstack1111ll1ll1l_opy_, bstack1l1lll1_opy_ (u"ࠣࡥ࡯࡭ࠧḸ"))
        if not os.path.exists(bstack1l1l11lll11_opy_):
            os.makedirs(bstack1l1l11lll11_opy_, mode=0o777, exist_ok=True)
        return bstack1l1l11lll11_opy_
    else:
        raise FileNotFoundError(bstack1l1lll1_opy_ (u"ࠤࡑࡳࠥࡽࡲࡪࡶࡤࡦࡱ࡫ࠠࡥ࡫ࡵࡩࡨࡺ࡯ࡳࡻࠣࡥࡻࡧࡩ࡭ࡣࡥࡰࡪࠦࡦࡰࡴࠣࡸ࡭࡫ࠠࡔࡆࡎࠤࡧ࡯࡮ࡢࡴࡼ࠲ࠧḹ"))
def bstack1l11ll1ll11_opy_(bstack1l1l11lll11_opy_):
    bstack1l1lll1_opy_ (u"ࠥࠦࠧࡍࡥࡵࠢࡷ࡬ࡪࠦࡰࡢࡶ࡫ࠤ࡫ࡵࡲࠡࡶ࡫ࡩࠥࡈࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࠤࡘࡊࡋࠡࡤ࡬ࡲࡦࡸࡹࠡ࡫ࡱࠤࡦࠦࡷࡳ࡫ࡷࡥࡧࡲࡥࠡࡦ࡬ࡶࡪࡩࡴࡰࡴࡼ࠲ࠧࠨࠢḺ")
    bstack1111l1llll1_opy_ = [
        os.path.join(bstack1l1l11lll11_opy_, f)
        for f in os.listdir(bstack1l1l11lll11_opy_)
        if os.path.isfile(os.path.join(bstack1l1l11lll11_opy_, f)) and f.startswith(bstack1l1lll1_opy_ (u"ࠦࡧ࡯࡮ࡢࡴࡼ࠱ࠧḻ"))
    ]
    if len(bstack1111l1llll1_opy_) > 0:
        return max(bstack1111l1llll1_opy_, key=os.path.getmtime) # get bstack111l1l1l1ll_opy_ binary
    return bstack1l1lll1_opy_ (u"ࠧࠨḼ")
def bstack1111ll1l111_opy_():
  from selenium import webdriver
  return version.parse(webdriver.__version__)
def bstack1l1111ll111_opy_(d, u):
  for k, v in u.items():
    if isinstance(v, collections.abc.Mapping):
      d[k] = bstack1l1111ll111_opy_(d.get(k, {}), v)
    else:
      if isinstance(v, list):
        d[k] = d.get(k, []) + v
      else:
        d[k] = v
  return d
def bstack11l11ll11l_opy_(data, keys, default=None):
    bstack1l1lll1_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࡓࡢࡨࡨࡰࡾࠦࡧࡦࡶࠣࡥࠥࡴࡥࡴࡶࡨࡨࠥࡼࡡ࡭ࡷࡨࠤ࡫ࡸ࡯࡮ࠢࡤࠤࡩ࡯ࡣࡵ࡫ࡲࡲࡦࡸࡹࠡࡱࡵࠤࡱ࡯ࡳࡵ࠰ࠍࠤࠥࠦࠠ࠻ࡲࡤࡶࡦࡳࠠࡥࡣࡷࡥ࠿ࠦࡔࡩࡧࠣࡨ࡮ࡩࡴࡪࡱࡱࡥࡷࡿࠠࡰࡴࠣࡰ࡮ࡹࡴࠡࡶࡲࠤࡹࡸࡡࡷࡧࡵࡷࡪ࠴ࠊࠡࠢࠣࠤ࠿ࡶࡡࡳࡣࡰࠤࡰ࡫ࡹࡴ࠼ࠣࡅࠥࡲࡩࡴࡶࠣࡳ࡫ࠦ࡫ࡦࡻࡶ࠳࡮ࡴࡤࡪࡥࡨࡷࠥࡸࡥࡱࡴࡨࡷࡪࡴࡴࡪࡰࡪࠤࡹ࡮ࡥࠡࡲࡤࡸ࡭࠴ࠊࠡࠢࠣࠤ࠿ࡶࡡࡳࡣࡰࠤࡩ࡫ࡦࡢࡷ࡯ࡸ࠿ࠦࡖࡢ࡮ࡸࡩࠥࡺ࡯ࠡࡴࡨࡸࡺࡸ࡮ࠡ࡫ࡩࠤࡹ࡮ࡥࠡࡲࡤࡸ࡭ࠦࡤࡰࡧࡶࠤࡳࡵࡴࠡࡧࡻ࡭ࡸࡺ࠮ࠋࠢࠣࠤࠥࡀࡲࡦࡶࡸࡶࡳࡀࠠࡕࡪࡨࠤࡻࡧ࡬ࡶࡧࠣࡥࡹࠦࡴࡩࡧࠣࡲࡪࡹࡴࡦࡦࠣࡴࡦࡺࡨ࠭ࠢࡲࡶࠥࡪࡥࡧࡣࡸࡰࡹࠦࡩࡧࠢࡱࡳࡹࠦࡦࡰࡷࡱࡨ࠳ࠐࠠࠡࠢࠣࠦࠧࠨḽ")
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