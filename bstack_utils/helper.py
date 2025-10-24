# coding: UTF-8
import sys
bstack1lllll1_opy_ = sys.version_info [0] == 2
bstack11lll1l_opy_ = 2048
bstack1lll1l_opy_ = 7
def bstack11l11l1_opy_ (bstack111l1ll_opy_):
    global bstack1ll1l_opy_
    bstack1l1l1ll_opy_ = ord (bstack111l1ll_opy_ [-1])
    bstack1l11l_opy_ = bstack111l1ll_opy_ [:-1]
    bstack1lllll1l_opy_ = bstack1l1l1ll_opy_ % len (bstack1l11l_opy_)
    bstack11ll1l1_opy_ = bstack1l11l_opy_ [:bstack1lllll1l_opy_] + bstack1l11l_opy_ [bstack1lllll1l_opy_:]
    if bstack1lllll1_opy_:
        bstack1lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11lll1l_opy_ - (bstack1l1ll11_opy_ + bstack1l1l1ll_opy_) % bstack1lll1l_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11ll1l1_opy_)])
    else:
        bstack1lll_opy_ = str () .join ([chr (ord (char) - bstack11lll1l_opy_ - (bstack1l1ll11_opy_ + bstack1l1l1ll_opy_) % bstack1lll1l_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11ll1l1_opy_)])
    return eval (bstack1lll_opy_)
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
from bstack_utils.constants import (bstack1111l1111l_opy_, bstack111lll111_opy_, bstack11ll11ll11_opy_,
                                    bstack11l11l1lll1_opy_, bstack11l1l11l1l1_opy_, bstack11l11lll111_opy_, bstack11l1l11lll1_opy_)
from bstack_utils.measure import measure
from bstack_utils.messages import bstack1111l1llll_opy_, bstack11lll1111l_opy_
from bstack_utils.proxy import bstack11l1ll111_opy_, bstack1lllll11l1_opy_
from bstack_utils.constants import *
from bstack_utils import bstack11111l1l1_opy_
from bstack_utils.bstack11lllll1l_opy_ import bstack1l111111l1_opy_
from browserstack_sdk._version import __version__
bstack11111111_opy_ = Config.bstack1llll1ll1_opy_()
logger = bstack11111l1l1_opy_.get_logger(__name__, bstack11111l1l1_opy_.bstack1l11lll11ll_opy_())
def bstack1111ll11111_opy_(config):
    return config[bstack11l11l1_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧᯢ")]
def bstack1111ll1l111_opy_(config):
    return config[bstack11l11l1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩᯣ")]
def bstack1l1l11111l_opy_():
    try:
        import playwright
        return True
    except ImportError:
        return False
def bstack111l111llll_opy_(obj):
    values = []
    bstack1111l1l1lll_opy_ = re.compile(bstack11l11l1_opy_ (u"ࡲࠣࡠࡆ࡙ࡘ࡚ࡏࡎࡡࡗࡅࡌࡥ࡜ࡥ࠭ࠧࠦᯤ"), re.I)
    for key in obj.keys():
        if bstack1111l1l1lll_opy_.match(key):
            values.append(obj[key])
    return values
def bstack1111lll11l1_opy_(config):
    tags = []
    tags.extend(bstack111l111llll_opy_(os.environ))
    tags.extend(bstack111l111llll_opy_(config))
    return tags
def bstack1111llllll1_opy_(markers):
    tags = []
    for marker in markers:
        tags.append(marker.name)
    return tags
def bstack111l11lll1l_opy_(bstack1111l11llll_opy_):
    if not bstack1111l11llll_opy_:
        return bstack11l11l1_opy_ (u"ࠨࠩᯥ")
    return bstack11l11l1_opy_ (u"ࠤࡾࢁࠥ࠮ࡻࡾ᯦ࠫࠥ").format(bstack1111l11llll_opy_.name, bstack1111l11llll_opy_.email)
def bstack1111l11ll11_opy_():
    try:
        repo = git.Repo(search_parent_directories=True)
        bstack1111lllll11_opy_ = repo.common_dir
        info = {
            bstack11l11l1_opy_ (u"ࠥࡷ࡭ࡧࠢᯧ"): repo.head.commit.hexsha,
            bstack11l11l1_opy_ (u"ࠦࡸ࡮࡯ࡳࡶࡢࡷ࡭ࡧࠢᯨ"): repo.git.rev_parse(repo.head.commit, short=True),
            bstack11l11l1_opy_ (u"ࠧࡨࡲࡢࡰࡦ࡬ࠧᯩ"): repo.active_branch.name,
            bstack11l11l1_opy_ (u"ࠨࡴࡢࡩࠥᯪ"): repo.git.describe(all=True, tags=True, exact_match=True),
            bstack11l11l1_opy_ (u"ࠢࡤࡱࡰࡱ࡮ࡺࡴࡦࡴࠥᯫ"): bstack111l11lll1l_opy_(repo.head.commit.committer),
            bstack11l11l1_opy_ (u"ࠣࡥࡲࡱࡲ࡯ࡴࡵࡧࡵࡣࡩࡧࡴࡦࠤᯬ"): repo.head.commit.committed_datetime.isoformat(),
            bstack11l11l1_opy_ (u"ࠤࡤࡹࡹ࡮࡯ࡳࠤᯭ"): bstack111l11lll1l_opy_(repo.head.commit.author),
            bstack11l11l1_opy_ (u"ࠥࡥࡺࡺࡨࡰࡴࡢࡨࡦࡺࡥࠣᯮ"): repo.head.commit.authored_datetime.isoformat(),
            bstack11l11l1_opy_ (u"ࠦࡨࡵ࡭࡮࡫ࡷࡣࡲ࡫ࡳࡴࡣࡪࡩࠧᯯ"): repo.head.commit.message,
            bstack11l11l1_opy_ (u"ࠧࡸ࡯ࡰࡶࠥᯰ"): repo.git.rev_parse(bstack11l11l1_opy_ (u"ࠨ࠭࠮ࡵ࡫ࡳࡼ࠳ࡴࡰࡲ࡯ࡩࡻ࡫࡬ࠣᯱ")),
            bstack11l11l1_opy_ (u"ࠢࡤࡱࡰࡱࡴࡴ࡟ࡨ࡫ࡷࡣࡩ࡯ࡲ᯲ࠣ"): bstack1111lllll11_opy_,
            bstack11l11l1_opy_ (u"ࠣࡹࡲࡶࡰࡺࡲࡦࡧࡢ࡫࡮ࡺ࡟ࡥ࡫ࡵ᯳ࠦ"): subprocess.check_output([bstack11l11l1_opy_ (u"ࠤࡪ࡭ࡹࠨ᯴"), bstack11l11l1_opy_ (u"ࠥࡶࡪࡼ࠭ࡱࡣࡵࡷࡪࠨ᯵"), bstack11l11l1_opy_ (u"ࠦ࠲࠳ࡧࡪࡶ࠰ࡧࡴࡳ࡭ࡰࡰ࠰ࡨ࡮ࡸࠢ᯶")]).strip().decode(
                bstack11l11l1_opy_ (u"ࠬࡻࡴࡧ࠯࠻ࠫ᯷")),
            bstack11l11l1_opy_ (u"ࠨ࡬ࡢࡵࡷࡣࡹࡧࡧࠣ᯸"): repo.git.describe(tags=True, abbrev=0, always=True),
            bstack11l11l1_opy_ (u"ࠢࡤࡱࡰࡱ࡮ࡺࡳࡠࡵ࡬ࡲࡨ࡫࡟࡭ࡣࡶࡸࡤࡺࡡࡨࠤ᯹"): repo.git.rev_list(
                bstack11l11l1_opy_ (u"ࠣࡽࢀ࠲࠳ࢁࡽࠣ᯺").format(repo.head.commit, repo.git.describe(tags=True, abbrev=0, always=True)), count=True)
        }
        remotes = repo.remotes
        bstack1111lll1lll_opy_ = []
        for remote in remotes:
            bstack1111lll111l_opy_ = {
                bstack11l11l1_opy_ (u"ࠤࡱࡥࡲ࡫ࠢ᯻"): remote.name,
                bstack11l11l1_opy_ (u"ࠥࡹࡷࡲࠢ᯼"): remote.url,
            }
            bstack1111lll1lll_opy_.append(bstack1111lll111l_opy_)
        bstack1111lll1111_opy_ = {
            bstack11l11l1_opy_ (u"ࠦࡳࡧ࡭ࡦࠤ᯽"): bstack11l11l1_opy_ (u"ࠧ࡭ࡩࡵࠤ᯾"),
            **info,
            bstack11l11l1_opy_ (u"ࠨࡲࡦ࡯ࡲࡸࡪࡹࠢ᯿"): bstack1111lll1lll_opy_
        }
        bstack1111lll1111_opy_ = bstack111l1l1llll_opy_(bstack1111lll1111_opy_)
        return bstack1111lll1111_opy_
    except git.InvalidGitRepositoryError:
        return {}
    except Exception as err:
        print(bstack11l11l1_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡰࡰࡲࡸࡰࡦࡺࡩ࡯ࡩࠣࡋ࡮ࡺࠠ࡮ࡧࡷࡥࡩࡧࡴࡢࠢࡺ࡭ࡹ࡮ࠠࡦࡴࡵࡳࡷࡀࠠࡼࡿࠥᰀ").format(err))
        return {}
def bstack11ll1l1l1ll_opy_(bstack1111ll11l11_opy_=None):
    bstack11l11l1_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࡉࡨࡸࠥ࡭ࡩࡵࠢࡰࡩࡹࡧࡤࡢࡶࡤࠤࡸࡶࡥࡤ࡫ࡩ࡭ࡨࡧ࡬࡭ࡻࠣࡪࡴࡸ࡭ࡢࡶࡷࡩࡩࠦࡦࡰࡴࠣࡅࡎࠦࡳࡦ࡮ࡨࡧࡹ࡯࡯࡯ࠢࡸࡷࡪࠦࡣࡢࡵࡨࡷࠥ࡬࡯ࡳࠢࡨࡥࡨ࡮ࠠࡧࡱ࡯ࡨࡪࡸࠠࡪࡰࠣࡸ࡭࡫ࠠ࡭࡫ࡶࡸ࠳ࠐࠠࠡࠢࠣࡅࡷ࡭ࡳ࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࡪࡴࡲࡤࡦࡴࡶࠤ࠭ࡲࡩࡴࡶ࠯ࠤࡴࡶࡴࡪࡱࡱࡥࡱ࠯࠺ࠡࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠ࠮ࠢࡑࡳࡳ࡫࠺ࠡࡏࡲࡲࡴ࠳ࡲࡦࡲࡲࠤࡦࡶࡰࡳࡱࡤࡧ࡭࠲ࠠࡶࡵࡨࡷࠥࡩࡵࡳࡴࡨࡲࡹࠦࡤࡪࡴࡨࡧࡹࡵࡲࡺࠢ࡞ࡳࡸ࠴ࡧࡦࡶࡦࡻࡩ࠮ࠩ࡞ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠ࠮ࠢࡈࡱࡵࡺࡹࠡ࡮࡬ࡷࡹ࡛ࠦ࡞࠼ࠣࡑࡺࡲࡴࡪ࠯ࡵࡩࡵࡵࠠࡢࡲࡳࡶࡴࡧࡣࡩࠢࡺ࡭ࡹ࡮ࠠ࡯ࡱࠣࡷࡴࡻࡲࡤࡧࡶࠤࡨࡵ࡮ࡧ࡫ࡪࡹࡷ࡫ࡤ࠭ࠢࡵࡩࡹࡻࡲ࡯ࡵࠣ࡟ࡢࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࠲ࠦࡌࡪࡵࡷࠤࡴ࡬ࠠࡱࡣࡷ࡬ࡸࡀࠠࡎࡷ࡯ࡸ࡮࠳ࡲࡦࡲࡲࠤࡦࡶࡰࡳࡱࡤࡧ࡭ࠦࡷࡪࡶ࡫ࠤࡸࡶࡥࡤ࡫ࡩ࡭ࡨࠦࡦࡰ࡮ࡧࡩࡷࡹࠠࡵࡱࠣࡥࡳࡧ࡬ࡺࡼࡨࠎࠥࠦࠠࠡࡔࡨࡸࡺࡸ࡮ࡴ࠼ࠍࠤࠥࠦࠠࠡࠢࠣࠤࡱ࡯ࡳࡵ࠼ࠣࡐ࡮ࡹࡴࠡࡱࡩࠤࡩ࡯ࡣࡵࡵ࠯ࠤࡪࡧࡣࡩࠢࡦࡳࡳࡺࡡࡪࡰ࡬ࡲ࡬ࠦࡧࡪࡶࠣࡱࡪࡺࡡࡥࡣࡷࡥࠥ࡬࡯ࡳࠢࡤࠤ࡫ࡵ࡬ࡥࡧࡵ࠲ࠏࠦࠠࠡࠢࠥࠦࠧᰁ")
    if bstack1111ll11l11_opy_ is None:
        bstack1111ll11l11_opy_ = [os.getcwd()]
    elif isinstance(bstack1111ll11l11_opy_, list) and len(bstack1111ll11l11_opy_) == 0:
        return []
    results = []
    for folder in bstack1111ll11l11_opy_:
        try:
            repo = git.Repo(folder, search_parent_directories=True)
            result = {
                bstack11l11l1_opy_ (u"ࠤࡳࡶࡎࡪࠢᰂ"): bstack11l11l1_opy_ (u"ࠥࠦᰃ"),
                bstack11l11l1_opy_ (u"ࠦ࡫࡯࡬ࡦࡵࡆ࡬ࡦࡴࡧࡦࡦࠥᰄ"): [],
                bstack11l11l1_opy_ (u"ࠧࡧࡵࡵࡪࡲࡶࡸࠨᰅ"): [],
                bstack11l11l1_opy_ (u"ࠨࡰࡳࡆࡤࡸࡪࠨᰆ"): bstack11l11l1_opy_ (u"ࠢࠣᰇ"),
                bstack11l11l1_opy_ (u"ࠣࡥࡲࡱࡲ࡯ࡴࡎࡧࡶࡷࡦ࡭ࡥࡴࠤᰈ"): [],
                bstack11l11l1_opy_ (u"ࠤࡳࡶ࡙࡯ࡴ࡭ࡧࠥᰉ"): bstack11l11l1_opy_ (u"ࠥࠦᰊ"),
                bstack11l11l1_opy_ (u"ࠦࡵࡸࡄࡦࡵࡦࡶ࡮ࡶࡴࡪࡱࡱࠦᰋ"): bstack11l11l1_opy_ (u"ࠧࠨᰌ"),
                bstack11l11l1_opy_ (u"ࠨࡰࡳࡔࡤࡻࡉ࡯ࡦࡧࠤᰍ"): bstack11l11l1_opy_ (u"ࠢࠣᰎ")
            }
            bstack1111l1l11l1_opy_ = repo.active_branch.name
            bstack111l111111l_opy_ = repo.head.commit
            result[bstack11l11l1_opy_ (u"ࠣࡲࡵࡍࡩࠨᰏ")] = bstack111l111111l_opy_.hexsha
            bstack111l1l11l1l_opy_ = _111l1ll11l1_opy_(repo)
            logger.debug(bstack11l11l1_opy_ (u"ࠤࡅࡥࡸ࡫ࠠࡣࡴࡤࡲࡨ࡮ࠠࡧࡱࡵࠤࡨࡵ࡭ࡱࡣࡵ࡭ࡸࡵ࡮࠻ࠢࠥᰐ") + str(bstack111l1l11l1l_opy_) + bstack11l11l1_opy_ (u"ࠥࠦᰑ"))
            if bstack111l1l11l1l_opy_:
                try:
                    bstack1111l1ll111_opy_ = repo.git.diff(bstack11l11l1_opy_ (u"ࠦ࠲࠳࡮ࡢ࡯ࡨ࠱ࡴࡴ࡬ࡺࠤᰒ"), bstack1llll11l1ll_opy_ (u"ࠧࢁࡢࡢࡵࡨࡣࡧࡸࡡ࡯ࡥ࡫ࢁ࠳࠴࠮ࡼࡥࡸࡶࡷ࡫࡮ࡵࡡࡥࡶࡦࡴࡣࡩࡿࠥᰓ")).split(bstack11l11l1_opy_ (u"࠭࡜࡯ࠩᰔ"))
                    logger.debug(bstack11l11l1_opy_ (u"ࠢࡄࡪࡤࡲ࡬࡫ࡤࠡࡨ࡬ࡰࡪࡹࠠࡣࡧࡷࡻࡪ࡫࡮ࠡࡽࡥࡥࡸ࡫࡟ࡣࡴࡤࡲࡨ࡮ࡽࠡࡣࡱࡨࠥࢁࡣࡶࡴࡵࡩࡳࡺ࡟ࡣࡴࡤࡲࡨ࡮ࡽ࠻ࠢࠥᰕ") + str(bstack1111l1ll111_opy_) + bstack11l11l1_opy_ (u"ࠣࠤᰖ"))
                    result[bstack11l11l1_opy_ (u"ࠤࡩ࡭ࡱ࡫ࡳࡄࡪࡤࡲ࡬࡫ࡤࠣᰗ")] = [f.strip() for f in bstack1111l1ll111_opy_ if f.strip()]
                    commits = list(repo.iter_commits(bstack1llll11l1ll_opy_ (u"ࠥࡿࡧࡧࡳࡦࡡࡥࡶࡦࡴࡣࡩࡿ࠱࠲ࢀࡩࡵࡳࡴࡨࡲࡹࡥࡢࡳࡣࡱࡧ࡭ࢃࠢᰘ")))
                except Exception:
                    logger.debug(bstack11l11l1_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡨࡧࡷࠤࡨ࡮ࡡ࡯ࡩࡨࡨࠥ࡬ࡩ࡭ࡧࡶࠤ࡫ࡸ࡯࡮ࠢࡥࡶࡦࡴࡣࡩࠢࡦࡳࡲࡶࡡࡳ࡫ࡶࡳࡳ࠴ࠠࡇࡣ࡯ࡰ࡮ࡴࡧࠡࡤࡤࡧࡰࠦࡴࡰࠢࡵࡩࡨ࡫࡮ࡵࠢࡦࡳࡲࡳࡩࡵࡵ࠱ࠦᰙ"))
                    commits = list(repo.iter_commits(max_count=10))
                    if commits:
                        result[bstack11l11l1_opy_ (u"ࠧ࡬ࡩ࡭ࡧࡶࡇ࡭ࡧ࡮ࡨࡧࡧࠦᰚ")] = _111l11lll11_opy_(commits[:5])
            else:
                commits = list(repo.iter_commits(max_count=10))
                if commits:
                    result[bstack11l11l1_opy_ (u"ࠨࡦࡪ࡮ࡨࡷࡈ࡮ࡡ࡯ࡩࡨࡨࠧᰛ")] = _111l11lll11_opy_(commits[:5])
            bstack111l1lll1ll_opy_ = set()
            bstack111l1l1l111_opy_ = []
            for commit in commits:
                logger.debug(bstack11l11l1_opy_ (u"ࠢࡑࡴࡲࡧࡪࡹࡳࡪࡰࡪࠤࡨࡵ࡭࡮࡫ࡷ࠾ࠥࠨᰜ") + str(commit.message) + bstack11l11l1_opy_ (u"ࠣࠤᰝ"))
                bstack1111ll11lll_opy_ = commit.author.name if commit.author else bstack11l11l1_opy_ (u"ࠤࡘࡲࡰࡴ࡯ࡸࡰࠥᰞ")
                bstack111l1lll1ll_opy_.add(bstack1111ll11lll_opy_)
                bstack111l1l1l111_opy_.append({
                    bstack11l11l1_opy_ (u"ࠥࡱࡪࡹࡳࡢࡩࡨࠦᰟ"): commit.message.strip(),
                    bstack11l11l1_opy_ (u"ࠦࡺࡹࡥࡳࠤᰠ"): bstack1111ll11lll_opy_
                })
            result[bstack11l11l1_opy_ (u"ࠧࡧࡵࡵࡪࡲࡶࡸࠨᰡ")] = list(bstack111l1lll1ll_opy_)
            result[bstack11l11l1_opy_ (u"ࠨࡣࡰ࡯ࡰ࡭ࡹࡓࡥࡴࡵࡤ࡫ࡪࡹࠢᰢ")] = bstack111l1l1l111_opy_
            result[bstack11l11l1_opy_ (u"ࠢࡱࡴࡇࡥࡹ࡫ࠢᰣ")] = bstack111l111111l_opy_.committed_datetime.strftime(bstack11l11l1_opy_ (u"ࠣࠧ࡜࠱ࠪࡳ࠭ࠦࡦࠥᰤ"))
            if (not result[bstack11l11l1_opy_ (u"ࠤࡳࡶ࡙࡯ࡴ࡭ࡧࠥᰥ")] or result[bstack11l11l1_opy_ (u"ࠥࡴࡷ࡚ࡩࡵ࡮ࡨࠦᰦ")].strip() == bstack11l11l1_opy_ (u"ࠦࠧᰧ")) and bstack111l111111l_opy_.message:
                bstack111l1l111l1_opy_ = bstack111l111111l_opy_.message.strip().splitlines()
                result[bstack11l11l1_opy_ (u"ࠧࡶࡲࡕ࡫ࡷࡰࡪࠨᰨ")] = bstack111l1l111l1_opy_[0] if bstack111l1l111l1_opy_ else bstack11l11l1_opy_ (u"ࠨࠢᰩ")
                if len(bstack111l1l111l1_opy_) > 2:
                    result[bstack11l11l1_opy_ (u"ࠢࡱࡴࡇࡩࡸࡩࡲࡪࡲࡷ࡭ࡴࡴࠢᰪ")] = bstack11l11l1_opy_ (u"ࠨ࡞ࡱࠫᰫ").join(bstack111l1l111l1_opy_[2:]).strip()
            results.append(result)
        except Exception as err:
            logger.error(bstack11l11l1_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡲࡲࡴࡺࡲࡡࡵ࡫ࡱ࡫ࠥࡍࡩࡵࠢࡰࡩࡹࡧࡤࡢࡶࡤࠤ࡫ࡵࡲࠡࡃࡌࠤࡸ࡫࡬ࡦࡥࡷ࡭ࡴࡴࠠࠩࡨࡲࡰࡩ࡫ࡲ࠻ࠢࡾࢁ࠮ࡀࠠࡼࡿࠥᰬ").format(folder, str(err)))
    filtered_results = [
        result
        for result in results
        if _1111l1l1ll1_opy_(result)
    ]
    return filtered_results
def _1111l1l1ll1_opy_(result):
    bstack11l11l1_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࡌࡪࡲࡰࡦࡴࠣࡸࡴࠦࡣࡩࡧࡦ࡯ࠥ࡯ࡦࠡࡣࠣ࡫࡮ࡺࠠ࡮ࡧࡷࡥࡩࡧࡴࡢࠢࡵࡩࡸࡻ࡬ࡵࠢ࡬ࡷࠥࡼࡡ࡭࡫ࡧࠤ࠭ࡴ࡯࡯࠯ࡨࡱࡵࡺࡹࠡࡨ࡬ࡰࡪࡹࡃࡩࡣࡱ࡫ࡪࡪࠠࡢࡰࡧࠤࡦࡻࡴࡩࡱࡵࡷ࠮࠴ࠊࠡࠢࠣࠤࠧࠨࠢᰭ")
    return (
        isinstance(result.get(bstack11l11l1_opy_ (u"ࠦ࡫࡯࡬ࡦࡵࡆ࡬ࡦࡴࡧࡦࡦࠥᰮ"), None), list)
        and len(result[bstack11l11l1_opy_ (u"ࠧ࡬ࡩ࡭ࡧࡶࡇ࡭ࡧ࡮ࡨࡧࡧࠦᰯ")]) > 0
        and isinstance(result.get(bstack11l11l1_opy_ (u"ࠨࡡࡶࡶ࡫ࡳࡷࡹࠢᰰ"), None), list)
        and len(result[bstack11l11l1_opy_ (u"ࠢࡢࡷࡷ࡬ࡴࡸࡳࠣᰱ")]) > 0
    )
def _111l1ll11l1_opy_(repo):
    bstack11l11l1_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࡖࡵࡽࠥࡺ࡯ࠡࡦࡨࡸࡪࡸ࡭ࡪࡰࡨࠤࡹ࡮ࡥࠡࡤࡤࡷࡪࠦࡢࡳࡣࡱࡧ࡭ࠦࡦࡰࡴࠣࡸ࡭࡫ࠠࡨ࡫ࡹࡩࡳࠦࡲࡦࡲࡲࠤࡼ࡯ࡴࡩࡱࡸࡸࠥ࡮ࡡࡳࡦࡦࡳࡩ࡫ࡤࠡࡰࡤࡱࡪࡹࠠࡢࡰࡧࠤࡼࡵࡲ࡬ࠢࡺ࡭ࡹ࡮ࠠࡢ࡮࡯ࠤ࡛ࡉࡓࠡࡲࡵࡳࡻ࡯ࡤࡦࡴࡶ࠲ࠏࠦࠠࠡࠢࡕࡩࡹࡻࡲ࡯ࡵࠣࡸ࡭࡫ࠠࡥࡧࡩࡥࡺࡲࡴࠡࡤࡵࡥࡳࡩࡨࠡ࡫ࡩࠤࡵࡵࡳࡴ࡫ࡥࡰࡪ࠲ࠠࡦ࡮ࡶࡩࠥࡔ࡯࡯ࡧ࠱ࠎࠥࠦࠠࠡࠤࠥࠦᰲ")
    try:
        try:
            origin = repo.remotes.origin
            bstack111l1111ll1_opy_ = origin.refs[bstack11l11l1_opy_ (u"ࠩࡋࡉࡆࡊࠧᰳ")]
            target = bstack111l1111ll1_opy_.reference.name
            if target.startswith(bstack11l11l1_opy_ (u"ࠪࡳࡷ࡯ࡧࡪࡰ࠲ࠫᰴ")):
                return target
        except Exception:
            pass
        if repo.remotes and repo.remotes.origin.refs:
            for ref in repo.remotes.origin.refs:
                if ref.name.startswith(bstack11l11l1_opy_ (u"ࠫࡴࡸࡩࡨ࡫ࡱ࠳ࠬᰵ")):
                    return ref.name
        if repo.heads:
            return repo.heads[0].name
    except Exception:
        pass
    return None
def _111l11lll11_opy_(commits):
    bstack11l11l1_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࡍࡥࡵࠢ࡯࡭ࡸࡺࠠࡰࡨࠣࡧ࡭ࡧ࡮ࡨࡧࡧࠤ࡫࡯࡬ࡦࡵࠣࡪࡷࡵ࡭ࠡࡣࠣࡰ࡮ࡹࡴࠡࡱࡩࠤࡨࡵ࡭࡮࡫ࡷࡷ࠳ࠐࠠࠡࠢࠣࠦࠧࠨᰶ")
    bstack1111l1ll111_opy_ = set()
    try:
        for commit in commits:
            if commit.parents:
                for parent in commit.parents:
                    diff = commit.diff(parent)
                    for bstack111l1l1l11l_opy_ in diff:
                        if bstack111l1l1l11l_opy_.a_path:
                            bstack1111l1ll111_opy_.add(bstack111l1l1l11l_opy_.a_path)
                        if bstack111l1l1l11l_opy_.b_path:
                            bstack1111l1ll111_opy_.add(bstack111l1l1l11l_opy_.b_path)
    except Exception:
        pass
    return list(bstack1111l1ll111_opy_)
def bstack111l1l1llll_opy_(bstack1111lll1111_opy_):
    bstack111l11lllll_opy_ = bstack1111llll1ll_opy_(bstack1111lll1111_opy_)
    if bstack111l11lllll_opy_ and bstack111l11lllll_opy_ > bstack11l11l1lll1_opy_:
        bstack111l1l1l1l1_opy_ = bstack111l11lllll_opy_ - bstack11l11l1lll1_opy_
        bstack1111llll1l1_opy_ = bstack111l111ll11_opy_(bstack1111lll1111_opy_[bstack11l11l1_opy_ (u"ࠨࡣࡰ࡯ࡰ࡭ࡹࡥ࡭ࡦࡵࡶࡥ࡬࡫᰷ࠢ")], bstack111l1l1l1l1_opy_)
        bstack1111lll1111_opy_[bstack11l11l1_opy_ (u"ࠢࡤࡱࡰࡱ࡮ࡺ࡟࡮ࡧࡶࡷࡦ࡭ࡥࠣ᰸")] = bstack1111llll1l1_opy_
        logger.info(bstack11l11l1_opy_ (u"ࠣࡖ࡫ࡩࠥࡩ࡯࡮࡯࡬ࡸࠥ࡮ࡡࡴࠢࡥࡩࡪࡴࠠࡵࡴࡸࡲࡨࡧࡴࡦࡦ࠱ࠤࡘ࡯ࡺࡦࠢࡲࡪࠥࡩ࡯࡮࡯࡬ࡸࠥࡧࡦࡵࡧࡵࠤࡹࡸࡵ࡯ࡥࡤࡸ࡮ࡵ࡮ࠡ࡫ࡶࠤࢀࢃࠠࡌࡄࠥ᰹")
                    .format(bstack1111llll1ll_opy_(bstack1111lll1111_opy_) / 1024))
    return bstack1111lll1111_opy_
def bstack1111llll1ll_opy_(json_data):
    try:
        if json_data:
            bstack111l1l11111_opy_ = json.dumps(json_data)
            bstack111l1ll1ll1_opy_ = sys.getsizeof(bstack111l1l11111_opy_)
            return bstack111l1ll1ll1_opy_
    except Exception as e:
        logger.debug(bstack11l11l1_opy_ (u"ࠤࡖࡳࡲ࡫ࡴࡩ࡫ࡱ࡫ࠥࡽࡥ࡯ࡶࠣࡻࡷࡵ࡮ࡨࠢࡺ࡬࡮ࡲࡥࠡࡥࡤࡰࡨࡻ࡬ࡢࡶ࡬ࡲ࡬ࠦࡳࡪࡼࡨࠤࡴ࡬ࠠࡋࡕࡒࡒࠥࡵࡢ࡫ࡧࡦࡸ࠿ࠦࡻࡾࠤ᰺").format(e))
    return -1
def bstack111l111ll11_opy_(field, bstack1111ll1l11l_opy_):
    try:
        bstack111l11ll1l1_opy_ = len(bytes(bstack11l1l11l1l1_opy_, bstack11l11l1_opy_ (u"ࠪࡹࡹ࡬࠭࠹ࠩ᰻")))
        bstack111l1ll1l1l_opy_ = bytes(field, bstack11l11l1_opy_ (u"ࠫࡺࡺࡦ࠮࠺ࠪ᰼"))
        bstack1111l11ll1l_opy_ = len(bstack111l1ll1l1l_opy_)
        bstack1111ll11ll1_opy_ = ceil(bstack1111l11ll1l_opy_ - bstack1111ll1l11l_opy_ - bstack111l11ll1l1_opy_)
        if bstack1111ll11ll1_opy_ > 0:
            bstack111l1lll1l1_opy_ = bstack111l1ll1l1l_opy_[:bstack1111ll11ll1_opy_].decode(bstack11l11l1_opy_ (u"ࠬࡻࡴࡧ࠯࠻ࠫ᰽"), errors=bstack11l11l1_opy_ (u"࠭ࡩࡨࡰࡲࡶࡪ࠭᰾")) + bstack11l1l11l1l1_opy_
            return bstack111l1lll1l1_opy_
    except Exception as e:
        logger.debug(bstack11l11l1_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡷࡩ࡫࡯ࡩࠥࡺࡲࡶࡰࡦࡥࡹ࡯࡮ࡨࠢࡩ࡭ࡪࡲࡤ࠭ࠢࡱࡳࡹ࡮ࡩ࡯ࡩࠣࡻࡦࡹࠠࡵࡴࡸࡲࡨࡧࡴࡦࡦࠣ࡬ࡪࡸࡥ࠻ࠢࡾࢁࠧ᰿").format(e))
    return field
def bstack11lll11l1_opy_():
    env = os.environ
    if (bstack11l11l1_opy_ (u"ࠣࡌࡈࡒࡐࡏࡎࡔࡡࡘࡖࡑࠨ᱀") in env and len(env[bstack11l11l1_opy_ (u"ࠤࡍࡉࡓࡑࡉࡏࡕࡢ࡙ࡗࡒࠢ᱁")]) > 0) or (
            bstack11l11l1_opy_ (u"ࠥࡎࡊࡔࡋࡊࡐࡖࡣࡍࡕࡍࡆࠤ᱂") in env and len(env[bstack11l11l1_opy_ (u"ࠦࡏࡋࡎࡌࡋࡑࡗࡤࡎࡏࡎࡇࠥ᱃")]) > 0):
        return {
            bstack11l11l1_opy_ (u"ࠧࡴࡡ࡮ࡧࠥ᱄"): bstack11l11l1_opy_ (u"ࠨࡊࡦࡰ࡮࡭ࡳࡹࠢ᱅"),
            bstack11l11l1_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥ᱆"): env.get(bstack11l11l1_opy_ (u"ࠣࡄࡘࡍࡑࡊ࡟ࡖࡔࡏࠦ᱇")),
            bstack11l11l1_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦ᱈"): env.get(bstack11l11l1_opy_ (u"ࠥࡎࡔࡈ࡟ࡏࡃࡐࡉࠧ᱉")),
            bstack11l11l1_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥ᱊"): env.get(bstack11l11l1_opy_ (u"ࠧࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࡃࡇࡕࠦ᱋"))
        }
    if env.get(bstack11l11l1_opy_ (u"ࠨࡃࡊࠤ᱌")) == bstack11l11l1_opy_ (u"ࠢࡵࡴࡸࡩࠧᱍ") and bstack111lll11l1_opy_(env.get(bstack11l11l1_opy_ (u"ࠣࡅࡌࡖࡈࡒࡅࡄࡋࠥᱎ"))):
        return {
            bstack11l11l1_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᱏ"): bstack11l11l1_opy_ (u"ࠥࡇ࡮ࡸࡣ࡭ࡧࡆࡍࠧ᱐"),
            bstack11l11l1_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢ᱑"): env.get(bstack11l11l1_opy_ (u"ࠧࡉࡉࡓࡅࡏࡉࡤࡈࡕࡊࡎࡇࡣ࡚ࡘࡌࠣ᱒")),
            bstack11l11l1_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣ᱓"): env.get(bstack11l11l1_opy_ (u"ࠢࡄࡋࡕࡇࡑࡋ࡟ࡋࡑࡅࠦ᱔")),
            bstack11l11l1_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢ᱕"): env.get(bstack11l11l1_opy_ (u"ࠤࡆࡍࡗࡉࡌࡆࡡࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࠧ᱖"))
        }
    if env.get(bstack11l11l1_opy_ (u"ࠥࡇࡎࠨ᱗")) == bstack11l11l1_opy_ (u"ࠦࡹࡸࡵࡦࠤ᱘") and bstack111lll11l1_opy_(env.get(bstack11l11l1_opy_ (u"࡚ࠧࡒࡂࡘࡌࡗࠧ᱙"))):
        return {
            bstack11l11l1_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᱚ"): bstack11l11l1_opy_ (u"ࠢࡕࡴࡤࡺ࡮ࡹࠠࡄࡋࠥᱛ"),
            bstack11l11l1_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᱜ"): env.get(bstack11l11l1_opy_ (u"ࠤࡗࡖࡆ࡜ࡉࡔࡡࡅ࡙ࡎࡒࡄࡠ࡙ࡈࡆࡤ࡛ࡒࡍࠤᱝ")),
            bstack11l11l1_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᱞ"): env.get(bstack11l11l1_opy_ (u"࡙ࠦࡘࡁࡗࡋࡖࡣࡏࡕࡂࡠࡐࡄࡑࡊࠨᱟ")),
            bstack11l11l1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᱠ"): env.get(bstack11l11l1_opy_ (u"ࠨࡔࡓࡃ࡙ࡍࡘࡥࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࠧᱡ"))
        }
    if env.get(bstack11l11l1_opy_ (u"ࠢࡄࡋࠥᱢ")) == bstack11l11l1_opy_ (u"ࠣࡶࡵࡹࡪࠨᱣ") and env.get(bstack11l11l1_opy_ (u"ࠤࡆࡍࡤࡔࡁࡎࡇࠥᱤ")) == bstack11l11l1_opy_ (u"ࠥࡧࡴࡪࡥࡴࡪ࡬ࡴࠧᱥ"):
        return {
            bstack11l11l1_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᱦ"): bstack11l11l1_opy_ (u"ࠧࡉ࡯ࡥࡧࡶ࡬࡮ࡶࠢᱧ"),
            bstack11l11l1_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᱨ"): None,
            bstack11l11l1_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᱩ"): None,
            bstack11l11l1_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᱪ"): None
        }
    if env.get(bstack11l11l1_opy_ (u"ࠤࡅࡍ࡙ࡈࡕࡄࡍࡈࡘࡤࡈࡒࡂࡐࡆࡌࠧᱫ")) and env.get(bstack11l11l1_opy_ (u"ࠥࡆࡎ࡚ࡂࡖࡅࡎࡉ࡙ࡥࡃࡐࡏࡐࡍ࡙ࠨᱬ")):
        return {
            bstack11l11l1_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᱭ"): bstack11l11l1_opy_ (u"ࠧࡈࡩࡵࡤࡸࡧࡰ࡫ࡴࠣᱮ"),
            bstack11l11l1_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᱯ"): env.get(bstack11l11l1_opy_ (u"ࠢࡃࡋࡗࡆ࡚ࡉࡋࡆࡖࡢࡋࡎ࡚࡟ࡉࡖࡗࡔࡤࡕࡒࡊࡉࡌࡒࠧᱰ")),
            bstack11l11l1_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᱱ"): None,
            bstack11l11l1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᱲ"): env.get(bstack11l11l1_opy_ (u"ࠥࡆࡎ࡚ࡂࡖࡅࡎࡉ࡙ࡥࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࠧᱳ"))
        }
    if env.get(bstack11l11l1_opy_ (u"ࠦࡈࡏࠢᱴ")) == bstack11l11l1_opy_ (u"ࠧࡺࡲࡶࡧࠥᱵ") and bstack111lll11l1_opy_(env.get(bstack11l11l1_opy_ (u"ࠨࡄࡓࡑࡑࡉࠧᱶ"))):
        return {
            bstack11l11l1_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᱷ"): bstack11l11l1_opy_ (u"ࠣࡆࡵࡳࡳ࡫ࠢᱸ"),
            bstack11l11l1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᱹ"): env.get(bstack11l11l1_opy_ (u"ࠥࡈࡗࡕࡎࡆࡡࡅ࡙ࡎࡒࡄࡠࡎࡌࡒࡐࠨᱺ")),
            bstack11l11l1_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᱻ"): None,
            bstack11l11l1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᱼ"): env.get(bstack11l11l1_opy_ (u"ࠨࡄࡓࡑࡑࡉࡤࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࡃࡇࡕࠦᱽ"))
        }
    if env.get(bstack11l11l1_opy_ (u"ࠢࡄࡋࠥ᱾")) == bstack11l11l1_opy_ (u"ࠣࡶࡵࡹࡪࠨ᱿") and bstack111lll11l1_opy_(env.get(bstack11l11l1_opy_ (u"ࠤࡖࡉࡒࡇࡐࡉࡑࡕࡉࠧᲀ"))):
        return {
            bstack11l11l1_opy_ (u"ࠥࡲࡦࡳࡥࠣᲁ"): bstack11l11l1_opy_ (u"ࠦࡘ࡫࡭ࡢࡲ࡫ࡳࡷ࡫ࠢᲂ"),
            bstack11l11l1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣᲃ"): env.get(bstack11l11l1_opy_ (u"ࠨࡓࡆࡏࡄࡔࡍࡕࡒࡆࡡࡒࡖࡌࡇࡎࡊ࡜ࡄࡘࡎࡕࡎࡠࡗࡕࡐࠧᲄ")),
            bstack11l11l1_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᲅ"): env.get(bstack11l11l1_opy_ (u"ࠣࡕࡈࡑࡆࡖࡈࡐࡔࡈࡣࡏࡕࡂࡠࡐࡄࡑࡊࠨᲆ")),
            bstack11l11l1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᲇ"): env.get(bstack11l11l1_opy_ (u"ࠥࡗࡊࡓࡁࡑࡊࡒࡖࡊࡥࡊࡐࡄࡢࡍࡉࠨᲈ"))
        }
    if env.get(bstack11l11l1_opy_ (u"ࠦࡈࡏࠢᲉ")) == bstack11l11l1_opy_ (u"ࠧࡺࡲࡶࡧࠥᲊ") and bstack111lll11l1_opy_(env.get(bstack11l11l1_opy_ (u"ࠨࡇࡊࡖࡏࡅࡇࡥࡃࡊࠤ᲋"))):
        return {
            bstack11l11l1_opy_ (u"ࠢ࡯ࡣࡰࡩࠧ᲌"): bstack11l11l1_opy_ (u"ࠣࡉ࡬ࡸࡑࡧࡢࠣ᲍"),
            bstack11l11l1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧ᲎"): env.get(bstack11l11l1_opy_ (u"ࠥࡇࡎࡥࡊࡐࡄࡢ࡙ࡗࡒࠢ᲏")),
            bstack11l11l1_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᲐ"): env.get(bstack11l11l1_opy_ (u"ࠧࡉࡉࡠࡌࡒࡆࡤࡔࡁࡎࡇࠥᲑ")),
            bstack11l11l1_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᲒ"): env.get(bstack11l11l1_opy_ (u"ࠢࡄࡋࡢࡎࡔࡈ࡟ࡊࡆࠥᲓ"))
        }
    if env.get(bstack11l11l1_opy_ (u"ࠣࡅࡌࠦᲔ")) == bstack11l11l1_opy_ (u"ࠤࡷࡶࡺ࡫ࠢᲕ") and bstack111lll11l1_opy_(env.get(bstack11l11l1_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡍࡌࡘࡊࠨᲖ"))):
        return {
            bstack11l11l1_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᲗ"): bstack11l11l1_opy_ (u"ࠧࡈࡵࡪ࡮ࡧ࡯࡮ࡺࡥࠣᲘ"),
            bstack11l11l1_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᲙ"): env.get(bstack11l11l1_opy_ (u"ࠢࡃࡗࡌࡐࡉࡑࡉࡕࡇࡢࡆ࡚ࡏࡌࡅࡡࡘࡖࡑࠨᲚ")),
            bstack11l11l1_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᲛ"): env.get(bstack11l11l1_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡌࡋࡗࡉࡤࡒࡁࡃࡇࡏࠦᲜ")) or env.get(bstack11l11l1_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡍࡌࡘࡊࡥࡐࡊࡒࡈࡐࡎࡔࡅࡠࡐࡄࡑࡊࠨᲝ")),
            bstack11l11l1_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᲞ"): env.get(bstack11l11l1_opy_ (u"ࠧࡈࡕࡊࡎࡇࡏࡎ࡚ࡅࡠࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘࠢᲟ"))
        }
    if bstack111lll11l1_opy_(env.get(bstack11l11l1_opy_ (u"ࠨࡔࡇࡡࡅ࡙ࡎࡒࡄࠣᲠ"))):
        return {
            bstack11l11l1_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᲡ"): bstack11l11l1_opy_ (u"ࠣࡘ࡬ࡷࡺࡧ࡬ࠡࡕࡷࡹࡩ࡯࡯ࠡࡖࡨࡥࡲࠦࡓࡦࡴࡹ࡭ࡨ࡫ࡳࠣᲢ"),
            bstack11l11l1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᲣ"): bstack11l11l1_opy_ (u"ࠥࡿࢂࢁࡽࠣᲤ").format(env.get(bstack11l11l1_opy_ (u"ࠫࡘ࡟ࡓࡕࡇࡐࡣ࡙ࡋࡁࡎࡈࡒ࡙ࡓࡊࡁࡕࡋࡒࡒࡘࡋࡒࡗࡇࡕ࡙ࡗࡏࠧᲥ")), env.get(bstack11l11l1_opy_ (u"࡙࡙ࠬࡔࡖࡈࡑࡤ࡚ࡅࡂࡏࡓࡖࡔࡐࡅࡄࡖࡌࡈࠬᲦ"))),
            bstack11l11l1_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᲧ"): env.get(bstack11l11l1_opy_ (u"ࠢࡔ࡛ࡖࡘࡊࡓ࡟ࡅࡇࡉࡍࡓࡏࡔࡊࡑࡑࡍࡉࠨᲨ")),
            bstack11l11l1_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᲩ"): env.get(bstack11l11l1_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡠࡄࡘࡍࡑࡊࡉࡅࠤᲪ"))
        }
    if bstack111lll11l1_opy_(env.get(bstack11l11l1_opy_ (u"ࠥࡅࡕࡖࡖࡆ࡛ࡒࡖࠧᲫ"))):
        return {
            bstack11l11l1_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᲬ"): bstack11l11l1_opy_ (u"ࠧࡇࡰࡱࡸࡨࡽࡴࡸࠢᲭ"),
            bstack11l11l1_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᲮ"): bstack11l11l1_opy_ (u"ࠢࡼࡿ࠲ࡴࡷࡵࡪࡦࡥࡷ࠳ࢀࢃ࠯ࡼࡿ࠲ࡦࡺ࡯࡬ࡥࡵ࠲ࡿࢂࠨᲯ").format(env.get(bstack11l11l1_opy_ (u"ࠨࡃࡓࡔ࡛ࡋ࡙ࡐࡔࡢ࡙ࡗࡒࠧᲰ")), env.get(bstack11l11l1_opy_ (u"ࠩࡄࡔࡕ࡜ࡅ࡚ࡑࡕࡣࡆࡉࡃࡐࡗࡑࡘࡤࡔࡁࡎࡇࠪᲱ")), env.get(bstack11l11l1_opy_ (u"ࠪࡅࡕࡖࡖࡆ࡛ࡒࡖࡤࡖࡒࡐࡌࡈࡇ࡙ࡥࡓࡍࡗࡊࠫᲲ")), env.get(bstack11l11l1_opy_ (u"ࠫࡆࡖࡐࡗࡇ࡜ࡓࡗࡥࡂࡖࡋࡏࡈࡤࡏࡄࠨᲳ"))),
            bstack11l11l1_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᲴ"): env.get(bstack11l11l1_opy_ (u"ࠨࡁࡑࡒ࡙ࡉ࡞ࡕࡒࡠࡌࡒࡆࡤࡔࡁࡎࡇࠥᲵ")),
            bstack11l11l1_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᲶ"): env.get(bstack11l11l1_opy_ (u"ࠣࡃࡓࡔ࡛ࡋ࡙ࡐࡔࡢࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࡈࡅࡓࠤᲷ"))
        }
    if env.get(bstack11l11l1_opy_ (u"ࠤࡄ࡞࡚ࡘࡅࡠࡊࡗࡘࡕࡥࡕࡔࡇࡕࡣࡆࡍࡅࡏࡖࠥᲸ")) and env.get(bstack11l11l1_opy_ (u"ࠥࡘࡋࡥࡂࡖࡋࡏࡈࠧᲹ")):
        return {
            bstack11l11l1_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᲺ"): bstack11l11l1_opy_ (u"ࠧࡇࡺࡶࡴࡨࠤࡈࡏࠢ᲻"),
            bstack11l11l1_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤ᲼"): bstack11l11l1_opy_ (u"ࠢࡼࡿࡾࢁ࠴ࡥࡢࡶ࡫࡯ࡨ࠴ࡸࡥࡴࡷ࡯ࡸࡸࡅࡢࡶ࡫࡯ࡨࡎࡪ࠽ࡼࡿࠥᲽ").format(env.get(bstack11l11l1_opy_ (u"ࠨࡕ࡜ࡗ࡙ࡋࡍࡠࡖࡈࡅࡒࡌࡏࡖࡐࡇࡅ࡙ࡏࡏࡏࡕࡈࡖ࡛ࡋࡒࡖࡔࡌࠫᲾ")), env.get(bstack11l11l1_opy_ (u"ࠩࡖ࡝ࡘ࡚ࡅࡎࡡࡗࡉࡆࡓࡐࡓࡑࡍࡉࡈ࡚ࠧᲿ")), env.get(bstack11l11l1_opy_ (u"ࠪࡆ࡚ࡏࡌࡅࡡࡅ࡙ࡎࡒࡄࡊࡆࠪ᳀"))),
            bstack11l11l1_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨ᳁"): env.get(bstack11l11l1_opy_ (u"ࠧࡈࡕࡊࡎࡇࡣࡇ࡛ࡉࡍࡆࡌࡈࠧ᳂")),
            bstack11l11l1_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧ᳃"): env.get(bstack11l11l1_opy_ (u"ࠢࡃࡗࡌࡐࡉࡥࡂࡖࡋࡏࡈࡎࡊࠢ᳄"))
        }
    if any([env.get(bstack11l11l1_opy_ (u"ࠣࡅࡒࡈࡊࡈࡕࡊࡎࡇࡣࡇ࡛ࡉࡍࡆࡢࡍࡉࠨ᳅")), env.get(bstack11l11l1_opy_ (u"ࠤࡆࡓࡉࡋࡂࡖࡋࡏࡈࡤࡘࡅࡔࡑࡏ࡚ࡊࡊ࡟ࡔࡑࡘࡖࡈࡋ࡟ࡗࡇࡕࡗࡎࡕࡎࠣ᳆")), env.get(bstack11l11l1_opy_ (u"ࠥࡇࡔࡊࡅࡃࡗࡌࡐࡉࡥࡓࡐࡗࡕࡇࡊࡥࡖࡆࡔࡖࡍࡔࡔࠢ᳇"))]):
        return {
            bstack11l11l1_opy_ (u"ࠦࡳࡧ࡭ࡦࠤ᳈"): bstack11l11l1_opy_ (u"ࠧࡇࡗࡔࠢࡆࡳࡩ࡫ࡂࡶ࡫࡯ࡨࠧ᳉"),
            bstack11l11l1_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤ᳊"): env.get(bstack11l11l1_opy_ (u"ࠢࡄࡑࡇࡉࡇ࡛ࡉࡍࡆࡢࡔ࡚ࡈࡌࡊࡅࡢࡆ࡚ࡏࡌࡅࡡࡘࡖࡑࠨ᳋")),
            bstack11l11l1_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥ᳌"): env.get(bstack11l11l1_opy_ (u"ࠤࡆࡓࡉࡋࡂࡖࡋࡏࡈࡤࡈࡕࡊࡎࡇࡣࡎࡊࠢ᳍")),
            bstack11l11l1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤ᳎"): env.get(bstack11l11l1_opy_ (u"ࠦࡈࡕࡄࡆࡄࡘࡍࡑࡊ࡟ࡃࡗࡌࡐࡉࡥࡉࡅࠤ᳏"))
        }
    if env.get(bstack11l11l1_opy_ (u"ࠧࡨࡡ࡮ࡤࡲࡳࡤࡨࡵࡪ࡮ࡧࡒࡺࡳࡢࡦࡴࠥ᳐")):
        return {
            bstack11l11l1_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦ᳑"): bstack11l11l1_opy_ (u"ࠢࡃࡣࡰࡦࡴࡵࠢ᳒"),
            bstack11l11l1_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦ᳓"): env.get(bstack11l11l1_opy_ (u"ࠤࡥࡥࡲࡨ࡯ࡰࡡࡥࡹ࡮ࡲࡤࡓࡧࡶࡹࡱࡺࡳࡖࡴ࡯᳔ࠦ")),
            bstack11l11l1_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩ᳕ࠧ"): env.get(bstack11l11l1_opy_ (u"ࠦࡧࡧ࡭ࡣࡱࡲࡣࡸ࡮࡯ࡳࡶࡍࡳࡧࡔࡡ࡮ࡧ᳖ࠥ")),
            bstack11l11l1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵ᳗ࠦ"): env.get(bstack11l11l1_opy_ (u"ࠨࡢࡢ࡯ࡥࡳࡴࡥࡢࡶ࡫࡯ࡨࡓࡻ࡭ࡣࡧࡵ᳘ࠦ"))
        }
    if env.get(bstack11l11l1_opy_ (u"ࠢࡘࡇࡕࡇࡐࡋࡒ᳙ࠣ")) or env.get(bstack11l11l1_opy_ (u"࡙ࠣࡈࡖࡈࡑࡅࡓࡡࡐࡅࡎࡔ࡟ࡑࡋࡓࡉࡑࡏࡎࡆࡡࡖࡘࡆࡘࡔࡆࡆࠥ᳚")):
        return {
            bstack11l11l1_opy_ (u"ࠤࡱࡥࡲ࡫ࠢ᳛"): bstack11l11l1_opy_ (u"࡛ࠥࡪࡸࡣ࡬ࡧࡵ᳜ࠦ"),
            bstack11l11l1_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲ᳝ࠢ"): env.get(bstack11l11l1_opy_ (u"ࠧ࡝ࡅࡓࡅࡎࡉࡗࡥࡂࡖࡋࡏࡈࡤ࡛ࡒࡍࠤ᳞")),
            bstack11l11l1_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥ᳟ࠣ"): bstack11l11l1_opy_ (u"ࠢࡎࡣ࡬ࡲࠥࡖࡩࡱࡧ࡯࡭ࡳ࡫ࠢ᳠") if env.get(bstack11l11l1_opy_ (u"࡙ࠣࡈࡖࡈࡑࡅࡓࡡࡐࡅࡎࡔ࡟ࡑࡋࡓࡉࡑࡏࡎࡆࡡࡖࡘࡆࡘࡔࡆࡆࠥ᳡")) else None,
            bstack11l11l1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲ᳢ࠣ"): env.get(bstack11l11l1_opy_ (u"࡛ࠥࡊࡘࡃࡌࡇࡕࡣࡌࡏࡔࡠࡅࡒࡑࡒࡏࡔ᳣ࠣ"))
        }
    if any([env.get(bstack11l11l1_opy_ (u"ࠦࡌࡉࡐࡠࡒࡕࡓࡏࡋࡃࡕࠤ᳤")), env.get(bstack11l11l1_opy_ (u"ࠧࡍࡃࡍࡑࡘࡈࡤࡖࡒࡐࡌࡈࡇ࡙ࠨ᳥")), env.get(bstack11l11l1_opy_ (u"ࠨࡇࡐࡑࡊࡐࡊࡥࡃࡍࡑࡘࡈࡤࡖࡒࡐࡌࡈࡇ࡙ࠨ᳦"))]):
        return {
            bstack11l11l1_opy_ (u"ࠢ࡯ࡣࡰࡩ᳧ࠧ"): bstack11l11l1_opy_ (u"ࠣࡉࡲࡳ࡬ࡲࡥࠡࡅ࡯ࡳࡺࡪ᳨ࠢ"),
            bstack11l11l1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᳩ"): None,
            bstack11l11l1_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᳪ"): env.get(bstack11l11l1_opy_ (u"ࠦࡕࡘࡏࡋࡇࡆࡘࡤࡏࡄࠣᳫ")),
            bstack11l11l1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᳬ"): env.get(bstack11l11l1_opy_ (u"ࠨࡂࡖࡋࡏࡈࡤࡏࡄ᳭ࠣ"))
        }
    if env.get(bstack11l11l1_opy_ (u"ࠢࡔࡊࡌࡔࡕࡇࡂࡍࡇࠥᳮ")):
        return {
            bstack11l11l1_opy_ (u"ࠣࡰࡤࡱࡪࠨᳯ"): bstack11l11l1_opy_ (u"ࠤࡖ࡬࡮ࡶࡰࡢࡤ࡯ࡩࠧᳰ"),
            bstack11l11l1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᳱ"): env.get(bstack11l11l1_opy_ (u"ࠦࡘࡎࡉࡑࡒࡄࡆࡑࡋ࡟ࡃࡗࡌࡐࡉࡥࡕࡓࡎࠥᳲ")),
            bstack11l11l1_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᳳ"): bstack11l11l1_opy_ (u"ࠨࡊࡰࡤࠣࠧࢀࢃࠢ᳴").format(env.get(bstack11l11l1_opy_ (u"ࠧࡔࡊࡌࡔࡕࡇࡂࡍࡇࡢࡎࡔࡈ࡟ࡊࡆࠪᳵ"))) if env.get(bstack11l11l1_opy_ (u"ࠣࡕࡋࡍࡕࡖࡁࡃࡎࡈࡣࡏࡕࡂࡠࡋࡇࠦᳶ")) else None,
            bstack11l11l1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣ᳷"): env.get(bstack11l11l1_opy_ (u"ࠥࡗࡍࡏࡐࡑࡃࡅࡐࡊࡥࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࠧ᳸"))
        }
    if bstack111lll11l1_opy_(env.get(bstack11l11l1_opy_ (u"ࠦࡓࡋࡔࡍࡋࡉ࡝ࠧ᳹"))):
        return {
            bstack11l11l1_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᳺ"): bstack11l11l1_opy_ (u"ࠨࡎࡦࡶ࡯࡭࡫ࡿࠢ᳻"),
            bstack11l11l1_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥ᳼"): env.get(bstack11l11l1_opy_ (u"ࠣࡆࡈࡔࡑࡕ࡙ࡠࡗࡕࡐࠧ᳽")),
            bstack11l11l1_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦ᳾"): env.get(bstack11l11l1_opy_ (u"ࠥࡗࡎ࡚ࡅࡠࡐࡄࡑࡊࠨ᳿")),
            bstack11l11l1_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᴀ"): env.get(bstack11l11l1_opy_ (u"ࠧࡈࡕࡊࡎࡇࡣࡎࡊࠢᴁ"))
        }
    if bstack111lll11l1_opy_(env.get(bstack11l11l1_opy_ (u"ࠨࡇࡊࡖࡋ࡙ࡇࡥࡁࡄࡖࡌࡓࡓ࡙ࠢᴂ"))):
        return {
            bstack11l11l1_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᴃ"): bstack11l11l1_opy_ (u"ࠣࡉ࡬ࡸࡍࡻࡢࠡࡃࡦࡸ࡮ࡵ࡮ࡴࠤᴄ"),
            bstack11l11l1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᴅ"): bstack11l11l1_opy_ (u"ࠥࡿࢂ࠵ࡻࡾ࠱ࡤࡧࡹ࡯࡯࡯ࡵ࠲ࡶࡺࡴࡳ࠰ࡽࢀࠦᴆ").format(env.get(bstack11l11l1_opy_ (u"ࠫࡌࡏࡔࡉࡗࡅࡣࡘࡋࡒࡗࡇࡕࡣ࡚ࡘࡌࠨᴇ")), env.get(bstack11l11l1_opy_ (u"ࠬࡍࡉࡕࡊࡘࡆࡤࡘࡅࡑࡑࡖࡍ࡙ࡕࡒ࡚ࠩᴈ")), env.get(bstack11l11l1_opy_ (u"࠭ࡇࡊࡖࡋ࡙ࡇࡥࡒࡖࡐࡢࡍࡉ࠭ᴉ"))),
            bstack11l11l1_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᴊ"): env.get(bstack11l11l1_opy_ (u"ࠣࡉࡌࡘࡍ࡛ࡂࡠ࡙ࡒࡖࡐࡌࡌࡐ࡙ࠥᴋ")),
            bstack11l11l1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᴌ"): env.get(bstack11l11l1_opy_ (u"ࠥࡋࡎ࡚ࡈࡖࡄࡢࡖ࡚ࡔ࡟ࡊࡆࠥᴍ"))
        }
    if env.get(bstack11l11l1_opy_ (u"ࠦࡈࡏࠢᴎ")) == bstack11l11l1_opy_ (u"ࠧࡺࡲࡶࡧࠥᴏ") and env.get(bstack11l11l1_opy_ (u"ࠨࡖࡆࡔࡆࡉࡑࠨᴐ")) == bstack11l11l1_opy_ (u"ࠢ࠲ࠤᴑ"):
        return {
            bstack11l11l1_opy_ (u"ࠣࡰࡤࡱࡪࠨᴒ"): bstack11l11l1_opy_ (u"ࠤ࡙ࡩࡷࡩࡥ࡭ࠤᴓ"),
            bstack11l11l1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᴔ"): bstack11l11l1_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼࠲࠳ࢀࢃࠢᴕ").format(env.get(bstack11l11l1_opy_ (u"ࠬ࡜ࡅࡓࡅࡈࡐࡤ࡛ࡒࡍࠩᴖ"))),
            bstack11l11l1_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᴗ"): None,
            bstack11l11l1_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᴘ"): None,
        }
    if env.get(bstack11l11l1_opy_ (u"ࠣࡖࡈࡅࡒࡉࡉࡕ࡛ࡢ࡚ࡊࡘࡓࡊࡑࡑࠦᴙ")):
        return {
            bstack11l11l1_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᴚ"): bstack11l11l1_opy_ (u"ࠥࡘࡪࡧ࡭ࡤ࡫ࡷࡽࠧᴛ"),
            bstack11l11l1_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᴜ"): None,
            bstack11l11l1_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᴝ"): env.get(bstack11l11l1_opy_ (u"ࠨࡔࡆࡃࡐࡇࡎ࡚࡙ࡠࡒࡕࡓࡏࡋࡃࡕࡡࡑࡅࡒࡋࠢᴞ")),
            bstack11l11l1_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᴟ"): env.get(bstack11l11l1_opy_ (u"ࠣࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘࠢᴠ"))
        }
    if any([env.get(bstack11l11l1_opy_ (u"ࠤࡆࡓࡓࡉࡏࡖࡔࡖࡉࠧᴡ")), env.get(bstack11l11l1_opy_ (u"ࠥࡇࡔࡔࡃࡐࡗࡕࡗࡊࡥࡕࡓࡎࠥᴢ")), env.get(bstack11l11l1_opy_ (u"ࠦࡈࡕࡎࡄࡑࡘࡖࡘࡋ࡟ࡖࡕࡈࡖࡓࡇࡍࡆࠤᴣ")), env.get(bstack11l11l1_opy_ (u"ࠧࡉࡏࡏࡅࡒ࡙ࡗ࡙ࡅࡠࡖࡈࡅࡒࠨᴤ"))]):
        return {
            bstack11l11l1_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᴥ"): bstack11l11l1_opy_ (u"ࠢࡄࡱࡱࡧࡴࡻࡲࡴࡧࠥᴦ"),
            bstack11l11l1_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᴧ"): None,
            bstack11l11l1_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᴨ"): env.get(bstack11l11l1_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡡࡍࡓࡇࡥࡎࡂࡏࡈࠦᴩ")) or None,
            bstack11l11l1_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᴪ"): env.get(bstack11l11l1_opy_ (u"ࠧࡈࡕࡊࡎࡇࡣࡎࡊࠢᴫ"), 0)
        }
    if env.get(bstack11l11l1_opy_ (u"ࠨࡇࡐࡡࡍࡓࡇࡥࡎࡂࡏࡈࠦᴬ")):
        return {
            bstack11l11l1_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᴭ"): bstack11l11l1_opy_ (u"ࠣࡉࡲࡇࡉࠨᴮ"),
            bstack11l11l1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᴯ"): None,
            bstack11l11l1_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᴰ"): env.get(bstack11l11l1_opy_ (u"ࠦࡌࡕ࡟ࡋࡑࡅࡣࡓࡇࡍࡆࠤᴱ")),
            bstack11l11l1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᴲ"): env.get(bstack11l11l1_opy_ (u"ࠨࡇࡐࡡࡓࡍࡕࡋࡌࡊࡐࡈࡣࡈࡕࡕࡏࡖࡈࡖࠧᴳ"))
        }
    if env.get(bstack11l11l1_opy_ (u"ࠢࡄࡈࡢࡆ࡚ࡏࡌࡅࡡࡌࡈࠧᴴ")):
        return {
            bstack11l11l1_opy_ (u"ࠣࡰࡤࡱࡪࠨᴵ"): bstack11l11l1_opy_ (u"ࠤࡆࡳࡩ࡫ࡆࡳࡧࡶ࡬ࠧᴶ"),
            bstack11l11l1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᴷ"): env.get(bstack11l11l1_opy_ (u"ࠦࡈࡌ࡟ࡃࡗࡌࡐࡉࡥࡕࡓࡎࠥᴸ")),
            bstack11l11l1_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᴹ"): env.get(bstack11l11l1_opy_ (u"ࠨࡃࡇࡡࡓࡍࡕࡋࡌࡊࡐࡈࡣࡓࡇࡍࡆࠤᴺ")),
            bstack11l11l1_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᴻ"): env.get(bstack11l11l1_opy_ (u"ࠣࡅࡉࡣࡇ࡛ࡉࡍࡆࡢࡍࡉࠨᴼ"))
        }
    return {bstack11l11l1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᴽ"): None}
def get_host_info():
    return {
        bstack11l11l1_opy_ (u"ࠥ࡬ࡴࡹࡴ࡯ࡣࡰࡩࠧᴾ"): platform.node(),
        bstack11l11l1_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲࠨᴿ"): platform.system(),
        bstack11l11l1_opy_ (u"ࠧࡺࡹࡱࡧࠥᵀ"): platform.machine(),
        bstack11l11l1_opy_ (u"ࠨࡶࡦࡴࡶ࡭ࡴࡴࠢᵁ"): platform.version(),
        bstack11l11l1_opy_ (u"ࠢࡢࡴࡦ࡬ࠧᵂ"): platform.architecture()[0]
    }
def bstack1lll1l1l1l_opy_():
    try:
        import selenium
        return True
    except ImportError:
        return False
def bstack111l11ll11l_opy_():
    if bstack11111111_opy_.get_property(bstack11l11l1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠࡵࡨࡷࡸ࡯࡯࡯ࠩᵃ")):
        return bstack11l11l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨᵄ")
    return bstack11l11l1_opy_ (u"ࠪࡹࡳࡱ࡮ࡰࡹࡱࡣ࡬ࡸࡩࡥࠩᵅ")
def bstack111l1l11lll_opy_(driver):
    info = {
        bstack11l11l1_opy_ (u"ࠫࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠪᵆ"): driver.capabilities,
        bstack11l11l1_opy_ (u"ࠬࡹࡥࡴࡵ࡬ࡳࡳࡥࡩࡥࠩᵇ"): driver.session_id,
        bstack11l11l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࠧᵈ"): driver.capabilities.get(bstack11l11l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬᵉ"), None),
        bstack11l11l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡡࡹࡩࡷࡹࡩࡰࡰࠪᵊ"): driver.capabilities.get(bstack11l11l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪᵋ"), None),
        bstack11l11l1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࠬᵌ"): driver.capabilities.get(bstack11l11l1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡔࡡ࡮ࡧࠪᵍ"), None),
        bstack11l11l1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨᵎ"):driver.capabilities.get(bstack11l11l1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠨᵏ"), None),
    }
    if bstack111l11ll11l_opy_() == bstack11l11l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ᵐ"):
        if bstack11llll11ll_opy_():
            info[bstack11l11l1_opy_ (u"ࠨࡲࡵࡳࡩࡻࡣࡵࠩᵑ")] = bstack11l11l1_opy_ (u"ࠩࡤࡴࡵ࠳ࡡࡶࡶࡲࡱࡦࡺࡥࠨᵒ")
        elif driver.capabilities.get(bstack11l11l1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫᵓ"), {}).get(bstack11l11l1_opy_ (u"ࠫࡹࡻࡲࡣࡱࡶࡧࡦࡲࡥࠨᵔ"), False):
            info[bstack11l11l1_opy_ (u"ࠬࡶࡲࡰࡦࡸࡧࡹ࠭ᵕ")] = bstack11l11l1_opy_ (u"࠭ࡴࡶࡴࡥࡳࡸࡩࡡ࡭ࡧࠪᵖ")
        else:
            info[bstack11l11l1_opy_ (u"ࠧࡱࡴࡲࡨࡺࡩࡴࠨᵗ")] = bstack11l11l1_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵࡧࠪᵘ")
    return info
def bstack11llll11ll_opy_():
    if bstack11111111_opy_.get_property(bstack11l11l1_opy_ (u"ࠩࡤࡴࡵࡥࡡࡶࡶࡲࡱࡦࡺࡥࠨᵙ")):
        return True
    if bstack111lll11l1_opy_(os.environ.get(bstack11l11l1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡌࡗࡤࡇࡐࡑࡡࡄ࡙࡙ࡕࡍࡂࡖࡈࠫᵚ"), None)):
        return True
    return False
def bstack1ll1l1l11l_opy_(bstack111l1l1ll11_opy_, url, data, config):
    headers = config.get(bstack11l11l1_opy_ (u"ࠫ࡭࡫ࡡࡥࡧࡵࡷࠬᵛ"), None)
    proxies = bstack11l1ll111_opy_(config, url)
    auth = config.get(bstack11l11l1_opy_ (u"ࠬࡧࡵࡵࡪࠪᵜ"), None)
    response = requests.request(
            bstack111l1l1ll11_opy_,
            url=url,
            headers=headers,
            auth=auth,
            json=data,
            proxies=proxies
        )
    return response
def bstack1l11111111_opy_(bstack11llll1l1l_opy_, size):
    bstack1l111l1ll_opy_ = []
    while len(bstack11llll1l1l_opy_) > size:
        bstack1111lll1l1_opy_ = bstack11llll1l1l_opy_[:size]
        bstack1l111l1ll_opy_.append(bstack1111lll1l1_opy_)
        bstack11llll1l1l_opy_ = bstack11llll1l1l_opy_[size:]
    bstack1l111l1ll_opy_.append(bstack11llll1l1l_opy_)
    return bstack1l111l1ll_opy_
def bstack1111llll11l_opy_(message, bstack111l11111ll_opy_=False):
    os.write(1, bytes(message, bstack11l11l1_opy_ (u"࠭ࡵࡵࡨ࠰࠼ࠬᵝ")))
    os.write(1, bytes(bstack11l11l1_opy_ (u"ࠧ࡝ࡰࠪᵞ"), bstack11l11l1_opy_ (u"ࠨࡷࡷࡪ࠲࠾ࠧᵟ")))
    if bstack111l11111ll_opy_:
        with open(bstack11l11l1_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠯ࡲ࠵࠶ࡿ࠭ࠨᵠ") + os.environ[bstack11l11l1_opy_ (u"ࠪࡆࡘࡥࡔࡆࡕࡗࡓࡕ࡙࡟ࡃࡗࡌࡐࡉࡥࡈࡂࡕࡋࡉࡉࡥࡉࡅࠩᵡ")] + bstack11l11l1_opy_ (u"ࠫ࠳ࡲ࡯ࡨࠩᵢ"), bstack11l11l1_opy_ (u"ࠬࡧࠧᵣ")) as f:
            f.write(message + bstack11l11l1_opy_ (u"࠭࡜࡯ࠩᵤ"))
def bstack1lll1l1111l_opy_():
    return os.environ[bstack11l11l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡁࡖࡖࡒࡑࡆ࡚ࡉࡐࡐࠪᵥ")].lower() == bstack11l11l1_opy_ (u"ࠨࡶࡵࡹࡪ࠭ᵦ")
def bstack1l11ll1l_opy_():
    return bstack1l1l1ll1_opy_().replace(tzinfo=None).isoformat() + bstack11l11l1_opy_ (u"ࠩ࡝ࠫᵧ")
def bstack1111lllllll_opy_(start, finish):
    return (datetime.datetime.fromisoformat(finish.rstrip(bstack11l11l1_opy_ (u"ࠪ࡞ࠬᵨ"))) - datetime.datetime.fromisoformat(start.rstrip(bstack11l11l1_opy_ (u"ࠫ࡟࠭ᵩ")))).total_seconds() * 1000
def bstack111l11l1ll1_opy_(timestamp):
    return bstack111l11l111l_opy_(timestamp).isoformat() + bstack11l11l1_opy_ (u"ࠬࡠࠧᵪ")
def bstack1111ll1llll_opy_(bstack111l11ll1ll_opy_):
    date_format = bstack11l11l1_opy_ (u"࡚࠭ࠥࠧࡰࠩࡩࠦࠥࡉ࠼ࠨࡑ࠿ࠫࡓ࠯ࠧࡩࠫᵫ")
    bstack111l11l1lll_opy_ = datetime.datetime.strptime(bstack111l11ll1ll_opy_, date_format)
    return bstack111l11l1lll_opy_.isoformat() + bstack11l11l1_opy_ (u"࡛ࠧࠩᵬ")
def bstack1111l1ll1l1_opy_(outcome):
    _, exception, _ = outcome.excinfo or (None, None, None)
    if exception:
        return bstack11l11l1_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨᵭ")
    else:
        return bstack11l11l1_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩᵮ")
def bstack111lll11l1_opy_(val):
    if val is None:
        return False
    return val.__str__().lower() == bstack11l11l1_opy_ (u"ࠪࡸࡷࡻࡥࠨᵯ")
def bstack111l111l1l1_opy_(val):
    return val.__str__().lower() == bstack11l11l1_opy_ (u"ࠫ࡫ࡧ࡬ࡴࡧࠪᵰ")
def error_handler(bstack1111ll11l1l_opy_=Exception, class_method=False, default_value=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except bstack1111ll11l1l_opy_ as e:
                print(bstack11l11l1_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࠦࡻࡾࠢ࠰ࡂࠥࢁࡽ࠻ࠢࡾࢁࠧᵱ").format(func.__name__, bstack1111ll11l1l_opy_.__name__, str(e)))
                return default_value
        return wrapper
    def bstack1111l11lll1_opy_(bstack1111l11l11l_opy_):
        def wrapped(cls, *args, **kwargs):
            try:
                return bstack1111l11l11l_opy_(cls, *args, **kwargs)
            except bstack1111ll11l1l_opy_ as e:
                print(bstack11l11l1_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠠࡼࡿࠣ࠱ࡃࠦࡻࡾ࠼ࠣࡿࢂࠨᵲ").format(bstack1111l11l11l_opy_.__name__, bstack1111ll11l1l_opy_.__name__, str(e)))
                return default_value
        return wrapped
    if class_method:
        return bstack1111l11lll1_opy_
    else:
        return decorator
def bstack1ll11lll11_opy_(bstack1111l111_opy_):
    if os.getenv(bstack11l11l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡁࡖࡖࡒࡑࡆ࡚ࡉࡐࡐࠪᵳ")) is not None:
        return bstack111lll11l1_opy_(os.getenv(bstack11l11l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡂࡗࡗࡓࡒࡇࡔࡊࡑࡑࠫᵴ")))
    if bstack11l11l1_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳ࠭ᵵ") in bstack1111l111_opy_ and bstack111l111l1l1_opy_(bstack1111l111_opy_[bstack11l11l1_opy_ (u"ࠪࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠧᵶ")]):
        return False
    if bstack11l11l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳ࠭ᵷ") in bstack1111l111_opy_ and bstack111l111l1l1_opy_(bstack1111l111_opy_[bstack11l11l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠧᵸ")]):
        return False
    return True
def bstack11l1llllll_opy_():
    try:
        from pytest_bdd import reporting
        bstack111l111ll1l_opy_ = os.environ.get(bstack11l11l1_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡛ࡓࡆࡔࡢࡊࡗࡇࡍࡆ࡙ࡒࡖࡐࠨᵹ"), None)
        return bstack111l111ll1l_opy_ is None or bstack111l111ll1l_opy_ == bstack11l11l1_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠦᵺ")
    except Exception as e:
        return False
def bstack11ll1ll1ll_opy_(hub_url, CONFIG):
    if bstack11l1ll1l11_opy_() <= version.parse(bstack11l11l1_opy_ (u"ࠨ࠵࠱࠵࠸࠴࠰ࠨᵻ")):
        if hub_url:
            return bstack11l11l1_opy_ (u"ࠤ࡫ࡸࡹࡶ࠺࠰࠱ࠥᵼ") + hub_url + bstack11l11l1_opy_ (u"ࠥ࠾࠽࠶࠯ࡸࡦ࠲࡬ࡺࡨࠢᵽ")
        return bstack111lll111_opy_
    if hub_url:
        return bstack11l11l1_opy_ (u"ࠦ࡭ࡺࡴࡱࡵ࠽࠳࠴ࠨᵾ") + hub_url + bstack11l11l1_opy_ (u"ࠧ࠵ࡷࡥ࠱࡫ࡹࡧࠨᵿ")
    return bstack11ll11ll11_opy_
def bstack1111lll11ll_opy_():
    return isinstance(os.getenv(bstack11l11l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖ࡙ࡕࡇࡖࡘࡤࡖࡌࡖࡉࡌࡒࠬᶀ")), str)
def bstack11llllll11_opy_(url):
    return urlparse(url).hostname
def bstack11l1l1l111_opy_(hostname):
    for bstack1ll1llll1l_opy_ in bstack1111l1111l_opy_:
        regex = re.compile(bstack1ll1llll1l_opy_)
        if regex.match(hostname):
            return True
    return False
def bstack11ll1111ll1_opy_(bstack111l1ll111l_opy_, file_name, logger):
    bstack1l11l1111_opy_ = os.path.join(os.path.expanduser(bstack11l11l1_opy_ (u"ࠧࡿࠩᶁ")), bstack111l1ll111l_opy_)
    try:
        if not os.path.exists(bstack1l11l1111_opy_):
            os.makedirs(bstack1l11l1111_opy_)
        file_path = os.path.join(os.path.expanduser(bstack11l11l1_opy_ (u"ࠨࢀࠪᶂ")), bstack111l1ll111l_opy_, file_name)
        if not os.path.isfile(file_path):
            with open(file_path, bstack11l11l1_opy_ (u"ࠩࡺࠫᶃ")):
                pass
            with open(file_path, bstack11l11l1_opy_ (u"ࠥࡻ࠰ࠨᶄ")) as outfile:
                json.dump({}, outfile)
        return file_path
    except Exception as e:
        logger.debug(bstack1111l1llll_opy_.format(str(e)))
def bstack11ll1111l1l_opy_(file_name, key, value, logger):
    file_path = bstack11ll1111ll1_opy_(bstack11l11l1_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫᶅ"), file_name, logger)
    if file_path != None:
        if os.path.exists(file_path):
            bstack1l111l111_opy_ = json.load(open(file_path, bstack11l11l1_opy_ (u"ࠬࡸࡢࠨᶆ")))
        else:
            bstack1l111l111_opy_ = {}
        bstack1l111l111_opy_[key] = value
        with open(file_path, bstack11l11l1_opy_ (u"ࠨࡷࠬࠤᶇ")) as outfile:
            json.dump(bstack1l111l111_opy_, outfile)
def bstack1111l11l1l_opy_(file_name, logger):
    file_path = bstack11ll1111ll1_opy_(bstack11l11l1_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧᶈ"), file_name, logger)
    bstack1l111l111_opy_ = {}
    if file_path != None and os.path.exists(file_path):
        with open(file_path, bstack11l11l1_opy_ (u"ࠨࡴࠪᶉ")) as bstack11l111l11l_opy_:
            bstack1l111l111_opy_ = json.load(bstack11l111l11l_opy_)
    return bstack1l111l111_opy_
def bstack11111111l_opy_(file_path, logger):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
    except Exception as e:
        logger.debug(bstack11l11l1_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡩ࡫࡬ࡦࡶ࡬ࡲ࡬ࠦࡦࡪ࡮ࡨ࠾ࠥ࠭ᶊ") + file_path + bstack11l11l1_opy_ (u"ࠪࠤࠬᶋ") + str(e))
def bstack11l1ll1l11_opy_():
    from selenium import webdriver
    return version.parse(webdriver.__version__)
class Notset:
    def __repr__(self):
        return bstack11l11l1_opy_ (u"ࠦࡁࡔࡏࡕࡕࡈࡘࡃࠨᶌ")
def bstack1l1l1111ll_opy_(config):
    if bstack11l11l1_opy_ (u"ࠬ࡯ࡳࡑ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠫᶍ") in config:
        del (config[bstack11l11l1_opy_ (u"࠭ࡩࡴࡒ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠬᶎ")])
        return False
    if bstack11l1ll1l11_opy_() < version.parse(bstack11l11l1_opy_ (u"ࠧ࠴࠰࠷࠲࠵࠭ᶏ")):
        return False
    if bstack11l1ll1l11_opy_() >= version.parse(bstack11l11l1_opy_ (u"ࠨ࠶࠱࠵࠳࠻ࠧᶐ")):
        return True
    if bstack11l11l1_opy_ (u"ࠩࡸࡷࡪ࡝࠳ࡄࠩᶑ") in config and config[bstack11l11l1_opy_ (u"ࠪࡹࡸ࡫ࡗ࠴ࡅࠪᶒ")] is False:
        return False
    else:
        return True
def bstack1l1l11l11_opy_(args_list, bstack1111l1llll1_opy_):
    index = -1
    for value in bstack1111l1llll1_opy_:
        try:
            index = args_list.index(value)
            return index
        except Exception as e:
            return index
    return index
def bstack111l1111111_opy_(a, b):
  for k, v in b.items():
    if isinstance(v, dict) and k in a and isinstance(a[k], dict):
        bstack111l1111111_opy_(a[k], v)
    else:
        a[k] = v
class Result:
    def __init__(self, result=None, duration=None, exception=None, bstack1ll1l11l_opy_=None):
        self.result = result
        self.duration = duration
        self.exception = exception
        self.exception_type = type(self.exception).__name__ if exception else None
        self.bstack1ll1l11l_opy_ = bstack1ll1l11l_opy_
    @classmethod
    def passed(cls):
        return Result(result=bstack11l11l1_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫᶓ"))
    @classmethod
    def failed(cls, exception=None):
        return Result(result=bstack11l11l1_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬᶔ"), exception=exception)
    def bstack111111l1ll_opy_(self):
        if self.result != bstack11l11l1_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ᶕ"):
            return None
        if isinstance(self.exception_type, str) and bstack11l11l1_opy_ (u"ࠢࡂࡵࡶࡩࡷࡺࡩࡰࡰࠥᶖ") in self.exception_type:
            return bstack11l11l1_opy_ (u"ࠣࡃࡶࡷࡪࡸࡴࡪࡱࡱࡉࡷࡸ࡯ࡳࠤᶗ")
        return bstack11l11l1_opy_ (u"ࠤࡘࡲ࡭ࡧ࡮ࡥ࡮ࡨࡨࡊࡸࡲࡰࡴࠥᶘ")
    def bstack111l1ll1l11_opy_(self):
        if self.result != bstack11l11l1_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪᶙ"):
            return None
        if self.bstack1ll1l11l_opy_:
            return self.bstack1ll1l11l_opy_
        return bstack1111l1l11ll_opy_(self.exception)
def bstack1111l1l11ll_opy_(exc):
    return [traceback.format_exception(exc)]
def bstack111l11ll111_opy_(message):
    if isinstance(message, str):
        return not bool(message and message.strip())
    return True
def bstack1ll11l1l_opy_(object, key, default_value):
    if not object or not object.__dict__:
        return default_value
    if key in object.__dict__.keys():
        return object.__dict__.get(key)
    return default_value
def bstack1lll1l1111_opy_(config, logger):
    try:
        import playwright
        bstack1111l1l1l1l_opy_ = playwright.__file__
        bstack111l1ll11ll_opy_ = os.path.split(bstack1111l1l1l1l_opy_)
        bstack111l1lll11l_opy_ = bstack111l1ll11ll_opy_[0] + bstack11l11l1_opy_ (u"ࠫ࠴ࡪࡲࡪࡸࡨࡶ࠴ࡶࡡࡤ࡭ࡤ࡫ࡪ࠵࡬ࡪࡤ࠲ࡧࡱ࡯࠯ࡤ࡮࡬࠲࡯ࡹࠧᶚ")
        os.environ[bstack11l11l1_opy_ (u"ࠬࡍࡌࡐࡄࡄࡐࡤࡇࡇࡆࡐࡗࡣࡍ࡚ࡔࡑࡡࡓࡖࡔ࡞࡙ࠨᶛ")] = bstack1lllll11l1_opy_(config)
        with open(bstack111l1lll11l_opy_, bstack11l11l1_opy_ (u"࠭ࡲࠨᶜ")) as f:
            file_content = f.read()
            bstack111l11111l1_opy_ = bstack11l11l1_opy_ (u"ࠧࡨ࡮ࡲࡦࡦࡲ࠭ࡢࡩࡨࡲࡹ࠭ᶝ")
            bstack1111l1ll1ll_opy_ = file_content.find(bstack111l11111l1_opy_)
            if bstack1111l1ll1ll_opy_ == -1:
              process = subprocess.Popen(bstack11l11l1_opy_ (u"ࠣࡰࡳࡱࠥ࡯࡮ࡴࡶࡤࡰࡱࠦࡧ࡭ࡱࡥࡥࡱ࠳ࡡࡨࡧࡱࡸࠧᶞ"), shell=True, cwd=bstack111l1ll11ll_opy_[0])
              process.wait()
              bstack111l11l1l11_opy_ = bstack11l11l1_opy_ (u"ࠩࠥࡹࡸ࡫ࠠࡴࡶࡵ࡭ࡨࡺࠢ࠼ࠩᶟ")
              bstack111l1l1lll1_opy_ = bstack11l11l1_opy_ (u"ࠥࠦࠧࠦ࡜ࠣࡷࡶࡩࠥࡹࡴࡳ࡫ࡦࡸࡡࠨ࠻ࠡࡥࡲࡲࡸࡺࠠࡼࠢࡥࡳࡴࡺࡳࡵࡴࡤࡴࠥࢃࠠ࠾ࠢࡵࡩࡶࡻࡩࡳࡧࠫࠫ࡬ࡲ࡯ࡣࡣ࡯࠱ࡦ࡭ࡥ࡯ࡶࠪ࠭ࡀࠦࡩࡧࠢࠫࡴࡷࡵࡣࡦࡵࡶ࠲ࡪࡴࡶ࠯ࡉࡏࡓࡇࡇࡌࡠࡃࡊࡉࡓ࡚࡟ࡉࡖࡗࡔࡤࡖࡒࡐ࡚࡜࠭ࠥࡨ࡯ࡰࡶࡶࡸࡷࡧࡰࠩࠫ࠾ࠤࠧࠨࠢᶠ")
              bstack1111ll1111l_opy_ = file_content.replace(bstack111l11l1l11_opy_, bstack111l1l1lll1_opy_)
              with open(bstack111l1lll11l_opy_, bstack11l11l1_opy_ (u"ࠫࡼ࠭ᶡ")) as f:
                f.write(bstack1111ll1111l_opy_)
    except Exception as e:
        logger.error(bstack11lll1111l_opy_.format(str(e)))
def bstack1l1ll1l11_opy_():
  try:
    bstack111l11l11ll_opy_ = os.path.join(tempfile.gettempdir(), bstack11l11l1_opy_ (u"ࠬࡵࡰࡵ࡫ࡰࡥࡱࡥࡨࡶࡤࡢࡹࡷࡲ࠮࡫ࡵࡲࡲࠬᶢ"))
    bstack1111ll1l1ll_opy_ = []
    if os.path.exists(bstack111l11l11ll_opy_):
      with open(bstack111l11l11ll_opy_) as f:
        bstack1111ll1l1ll_opy_ = json.load(f)
      os.remove(bstack111l11l11ll_opy_)
    return bstack1111ll1l1ll_opy_
  except:
    pass
  return []
def bstack1l1l1lllll_opy_(bstack1lllll1111_opy_):
  try:
    bstack1111ll1l1ll_opy_ = []
    bstack111l11l11ll_opy_ = os.path.join(tempfile.gettempdir(), bstack11l11l1_opy_ (u"࠭࡯ࡱࡶ࡬ࡱࡦࡲ࡟ࡩࡷࡥࡣࡺࡸ࡬࠯࡬ࡶࡳࡳ࠭ᶣ"))
    if os.path.exists(bstack111l11l11ll_opy_):
      with open(bstack111l11l11ll_opy_) as f:
        bstack1111ll1l1ll_opy_ = json.load(f)
    bstack1111ll1l1ll_opy_.append(bstack1lllll1111_opy_)
    with open(bstack111l11l11ll_opy_, bstack11l11l1_opy_ (u"ࠧࡸࠩᶤ")) as f:
        json.dump(bstack1111ll1l1ll_opy_, f)
  except:
    pass
def bstack111ll1111_opy_(logger, bstack1111ll111ll_opy_ = False):
  try:
    test_name = os.environ.get(bstack11l11l1_opy_ (u"ࠨࡒ࡜ࡘࡊ࡙ࡔࡠࡖࡈࡗ࡙ࡥࡎࡂࡏࡈࠫᶥ"), bstack11l11l1_opy_ (u"ࠩࠪᶦ"))
    if test_name == bstack11l11l1_opy_ (u"ࠪࠫᶧ"):
        test_name = threading.current_thread().__dict__.get(bstack11l11l1_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࡆࡩࡪ࡟ࡵࡧࡶࡸࡤࡴࡡ࡮ࡧࠪᶨ"), bstack11l11l1_opy_ (u"ࠬ࠭ᶩ"))
    bstack111l1l1111l_opy_ = bstack11l11l1_opy_ (u"࠭ࠬࠡࠩᶪ").join(threading.current_thread().bstackTestErrorMessages)
    if bstack1111ll111ll_opy_:
        bstack111111ll11_opy_ = os.environ.get(bstack11l11l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡋࡑࡈࡊ࡞ࠧᶫ"), bstack11l11l1_opy_ (u"ࠨ࠲ࠪᶬ"))
        bstack1lll1l11l1_opy_ = {bstack11l11l1_opy_ (u"ࠩࡱࡥࡲ࡫ࠧᶭ"): test_name, bstack11l11l1_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩᶮ"): bstack111l1l1111l_opy_, bstack11l11l1_opy_ (u"ࠫ࡮ࡴࡤࡦࡺࠪᶯ"): bstack111111ll11_opy_}
        bstack111l11llll1_opy_ = []
        bstack111l1111l1l_opy_ = os.path.join(tempfile.gettempdir(), bstack11l11l1_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࡤࡶࡰࡱࡡࡨࡶࡷࡵࡲࡠ࡮࡬ࡷࡹ࠴ࡪࡴࡱࡱࠫᶰ"))
        if os.path.exists(bstack111l1111l1l_opy_):
            with open(bstack111l1111l1l_opy_) as f:
                bstack111l11llll1_opy_ = json.load(f)
        bstack111l11llll1_opy_.append(bstack1lll1l11l1_opy_)
        with open(bstack111l1111l1l_opy_, bstack11l11l1_opy_ (u"࠭ࡷࠨᶱ")) as f:
            json.dump(bstack111l11llll1_opy_, f)
    else:
        bstack1lll1l11l1_opy_ = {bstack11l11l1_opy_ (u"ࠧ࡯ࡣࡰࡩࠬᶲ"): test_name, bstack11l11l1_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧᶳ"): bstack111l1l1111l_opy_, bstack11l11l1_opy_ (u"ࠩ࡬ࡲࡩ࡫ࡸࠨᶴ"): str(multiprocessing.current_process().name)}
        if bstack11l11l1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡢࡩࡷࡸ࡯ࡳࡡ࡯࡭ࡸࡺࠧᶵ") not in multiprocessing.current_process().__dict__.keys():
            multiprocessing.current_process().bstack_error_list = []
        multiprocessing.current_process().bstack_error_list.append(bstack1lll1l11l1_opy_)
  except Exception as e:
      logger.warn(bstack11l11l1_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡴࡶࡲࡶࡪࠦࡰࡺࡶࡨࡷࡹࠦࡦࡶࡰࡱࡩࡱࠦࡤࡢࡶࡤ࠾ࠥࢁࡽࠣᶶ").format(e))
def bstack11l1l1l11_opy_(error_message, test_name, index, logger):
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack11l11l1_opy_ (u"ࠬ࡬ࡩ࡭ࡧ࡯ࡳࡨࡱࠠ࡯ࡱࡷࠤࡦࡼࡡࡪ࡮ࡤࡦࡱ࡫ࠬࠡࡷࡶ࡭ࡳ࡭ࠠࡣࡣࡶ࡭ࡨࠦࡦࡪ࡮ࡨࠤࡴࡶࡥࡳࡣࡷ࡭ࡴࡴࡳࠨᶷ"))
    try:
      bstack111l11l1l1l_opy_ = []
      bstack1lll1l11l1_opy_ = {bstack11l11l1_opy_ (u"࠭࡮ࡢ࡯ࡨࠫᶸ"): test_name, bstack11l11l1_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭ᶹ"): error_message, bstack11l11l1_opy_ (u"ࠨ࡫ࡱࡨࡪࡾࠧᶺ"): index}
      bstack1111l1lll1l_opy_ = os.path.join(tempfile.gettempdir(), bstack11l11l1_opy_ (u"ࠩࡵࡳࡧࡵࡴࡠࡧࡵࡶࡴࡸ࡟࡭࡫ࡶࡸ࠳ࡰࡳࡰࡰࠪᶻ"))
      if os.path.exists(bstack1111l1lll1l_opy_):
          with open(bstack1111l1lll1l_opy_) as f:
              bstack111l11l1l1l_opy_ = json.load(f)
      bstack111l11l1l1l_opy_.append(bstack1lll1l11l1_opy_)
      with open(bstack1111l1lll1l_opy_, bstack11l11l1_opy_ (u"ࠪࡻࠬᶼ")) as f:
          json.dump(bstack111l11l1l1l_opy_, f)
    except Exception as e:
      logger.warn(bstack11l11l1_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡴࡶࡲࡶࡪࠦࡲࡰࡤࡲࡸࠥ࡬ࡵ࡯ࡰࡨࡰࠥࡪࡡࡵࡣ࠽ࠤࢀࢃࠢᶽ").format(e))
    return
  bstack111l11l1l1l_opy_ = []
  bstack1lll1l11l1_opy_ = {bstack11l11l1_opy_ (u"ࠬࡴࡡ࡮ࡧࠪᶾ"): test_name, bstack11l11l1_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬᶿ"): error_message, bstack11l11l1_opy_ (u"ࠧࡪࡰࡧࡩࡽ࠭᷀"): index}
  bstack1111l1lll1l_opy_ = os.path.join(tempfile.gettempdir(), bstack11l11l1_opy_ (u"ࠨࡴࡲࡦࡴࡺ࡟ࡦࡴࡵࡳࡷࡥ࡬ࡪࡵࡷ࠲࡯ࡹ࡯࡯ࠩ᷁"))
  lock_file = bstack1111l1lll1l_opy_ + bstack11l11l1_opy_ (u"ࠩ࠱ࡰࡴࡩ࡫ࠨ᷂")
  try:
    with FileLock(lock_file, timeout=10):
      if os.path.exists(bstack1111l1lll1l_opy_):
          with open(bstack1111l1lll1l_opy_, bstack11l11l1_opy_ (u"ࠪࡶࠬ᷃")) as f:
              content = f.read().strip()
              if content:
                  bstack111l11l1l1l_opy_ = json.load(open(bstack1111l1lll1l_opy_))
      bstack111l11l1l1l_opy_.append(bstack1lll1l11l1_opy_)
      with open(bstack1111l1lll1l_opy_, bstack11l11l1_opy_ (u"ࠫࡼ࠭᷄")) as f:
          json.dump(bstack111l11l1l1l_opy_, f)
  except Exception as e:
    logger.warn(bstack11l11l1_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡵࡷࡳࡷ࡫ࠠࡳࡱࡥࡳࡹࠦࡦࡶࡰࡱࡩࡱࠦࡤࡢࡶࡤࠤࡼ࡯ࡴࡩࠢࡩ࡭ࡱ࡫ࠠ࡭ࡱࡦ࡯࡮ࡴࡧ࠻ࠢࡾࢁࠧ᷅").format(e))
def bstack11l11l1111_opy_(bstack1l1l11l111_opy_, name, logger):
  try:
    bstack1lll1l11l1_opy_ = {bstack11l11l1_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ᷆"): name, bstack11l11l1_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭᷇"): bstack1l1l11l111_opy_, bstack11l11l1_opy_ (u"ࠨ࡫ࡱࡨࡪࡾࠧ᷈"): str(threading.current_thread()._name)}
    return bstack1lll1l11l1_opy_
  except Exception as e:
    logger.warn(bstack11l11l1_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡹࡴࡰࡴࡨࠤࡧ࡫ࡨࡢࡸࡨࠤ࡫ࡻ࡮࡯ࡧ࡯ࠤࡩࡧࡴࡢ࠼ࠣࡿࢂࠨ᷉").format(e))
  return
def bstack1111l1lllll_opy_():
    return platform.system() == bstack11l11l1_opy_ (u"࡛ࠪ࡮ࡴࡤࡰࡹࡶ᷊ࠫ")
def bstack1l1l11l1ll_opy_(bstack111l1l11ll1_opy_, config, logger):
    bstack111l1ll1111_opy_ = {}
    try:
        return {key: config[key] for key in config if bstack111l1l11ll1_opy_.match(key)}
    except Exception as e:
        logger.debug(bstack11l11l1_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡧ࡫࡯ࡸࡪࡸࠠࡤࡱࡱࡪ࡮࡭ࠠ࡬ࡧࡼࡷࠥࡨࡹࠡࡴࡨ࡫ࡪࡾࠠ࡮ࡣࡷࡧ࡭ࡀࠠࡼࡿࠥ᷋").format(e))
    return bstack111l1ll1111_opy_
def bstack11l1l1l1lll_opy_(bstack111l1l1l1ll_opy_, bstack1111llll111_opy_):
    bstack111l1l1ll1l_opy_ = version.parse(bstack111l1l1l1ll_opy_)
    bstack1111lll1l1l_opy_ = version.parse(bstack1111llll111_opy_)
    if bstack111l1l1ll1l_opy_ > bstack1111lll1l1l_opy_:
        return 1
    elif bstack111l1l1ll1l_opy_ < bstack1111lll1l1l_opy_:
        return -1
    else:
        return 0
def bstack1l1l1ll1_opy_():
    return datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None)
def bstack111l11l111l_opy_(timestamp):
    return datetime.datetime.fromtimestamp(timestamp, datetime.timezone.utc).replace(tzinfo=None)
def bstack1111ll1l1l1_opy_(framework):
    from browserstack_sdk._version import __version__
    return str(framework) + str(__version__)
def bstack1llll111l1_opy_(options, framework, config, bstack111ll11ll1_opy_={}):
    if options is None:
        return
    if getattr(options, bstack11l11l1_opy_ (u"ࠬ࡭ࡥࡵࠩ᷌"), None):
        caps = options
    else:
        caps = options.to_capabilities()
    bstack1ll1ll11l_opy_ = caps.get(bstack11l11l1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧ᷍"))
    bstack1111l11l1l1_opy_ = True
    bstack111l111111_opy_ = os.environ[bstack11l11l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈ᷎ࠬ")]
    bstack1l111ll11ll_opy_ = config.get(bstack11l11l1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨ᷏"), False)
    if bstack1l111ll11ll_opy_:
        bstack1l11lllll1l_opy_ = config.get(bstack11l11l1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴ᷐ࠩ"), {})
        bstack1l11lllll1l_opy_[bstack11l11l1_opy_ (u"ࠪࡥࡺࡺࡨࡕࡱ࡮ࡩࡳ࠭᷑")] = os.getenv(bstack11l11l1_opy_ (u"ࠫࡇ࡙࡟ࡂ࠳࠴࡝ࡤࡐࡗࡕࠩ᷒"))
        bstack111l111l11l_opy_ = json.loads(os.getenv(bstack11l11l1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡡࡄࡇࡈࡋࡓࡔࡋࡅࡍࡑࡏࡔ࡚ࡡࡆࡓࡓࡌࡉࡈࡗࡕࡅ࡙ࡏࡏࡏࡡ࡜ࡑࡑ࠭ᷓ"), bstack11l11l1_opy_ (u"࠭ࡻࡾࠩᷔ"))).get(bstack11l11l1_opy_ (u"ࠧࡴࡥࡤࡲࡳ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨᷕ"))
    if bstack111l111l1l1_opy_(caps.get(bstack11l11l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡶࡵࡨ࡛࠸ࡉࠧᷖ"))) or bstack111l111l1l1_opy_(caps.get(bstack11l11l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡷࡶࡩࡤࡽ࠳ࡤࠩᷗ"))):
        bstack1111l11l1l1_opy_ = False
    if bstack1l1l1111ll_opy_({bstack11l11l1_opy_ (u"ࠥࡹࡸ࡫ࡗ࠴ࡅࠥᷘ"): bstack1111l11l1l1_opy_}):
        bstack1ll1ll11l_opy_ = bstack1ll1ll11l_opy_ or {}
        bstack1ll1ll11l_opy_[bstack11l11l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡖࡈࡐ࠭ᷙ")] = bstack1111ll1l1l1_opy_(framework)
        bstack1ll1ll11l_opy_[bstack11l11l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠧᷚ")] = bstack1lll1l1111l_opy_()
        bstack1ll1ll11l_opy_[bstack11l11l1_opy_ (u"࠭ࡴࡦࡵࡷ࡬ࡺࡨࡂࡶ࡫࡯ࡨ࡚ࡻࡩࡥࠩᷛ")] = bstack111l111111_opy_
        bstack1ll1ll11l_opy_[bstack11l11l1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡖࡲࡰࡦࡸࡧࡹࡓࡡࡱࠩᷜ")] = bstack111ll11ll1_opy_
        if bstack1l111ll11ll_opy_:
            bstack1ll1ll11l_opy_[bstack11l11l1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨᷝ")] = bstack1l111ll11ll_opy_
            bstack1ll1ll11l_opy_[bstack11l11l1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩᷞ")] = bstack1l11lllll1l_opy_
            bstack1ll1ll11l_opy_[bstack11l11l1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪᷟ")][bstack11l11l1_opy_ (u"ࠫࡸࡩࡡ࡯ࡰࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬᷠ")] = bstack111l111l11l_opy_
        if getattr(options, bstack11l11l1_opy_ (u"ࠬࡹࡥࡵࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸࡾ࠭ᷡ"), None):
            options.set_capability(bstack11l11l1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧᷢ"), bstack1ll1ll11l_opy_)
        else:
            options[bstack11l11l1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨᷣ")] = bstack1ll1ll11l_opy_
    else:
        if getattr(options, bstack11l11l1_opy_ (u"ࠨࡵࡨࡸࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡺࠩᷤ"), None):
            options.set_capability(bstack11l11l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡓࡅࡍࠪᷥ"), bstack1111ll1l1l1_opy_(framework))
            options.set_capability(bstack11l11l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫᷦ"), bstack1lll1l1111l_opy_())
            options.set_capability(bstack11l11l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡸࡪࡹࡴࡩࡷࡥࡆࡺ࡯࡬ࡥࡗࡸ࡭ࡩ࠭ᷧ"), bstack111l111111_opy_)
            options.set_capability(bstack11l11l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡧࡻࡩ࡭ࡦࡓࡶࡴࡪࡵࡤࡶࡐࡥࡵ࠭ᷨ"), bstack111ll11ll1_opy_)
            if bstack1l111ll11ll_opy_:
                options.set_capability(bstack11l11l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬᷩ"), bstack1l111ll11ll_opy_)
                options.set_capability(bstack11l11l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭ᷪ"), bstack1l11lllll1l_opy_)
                options.set_capability(bstack11l11l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹ࠮ࡴࡥࡤࡲࡳ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨᷫ"), bstack111l111l11l_opy_)
        else:
            options[bstack11l11l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡓࡅࡍࠪᷬ")] = bstack1111ll1l1l1_opy_(framework)
            options[bstack11l11l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫᷭ")] = bstack1lll1l1111l_opy_()
            options[bstack11l11l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡸࡪࡹࡴࡩࡷࡥࡆࡺ࡯࡬ࡥࡗࡸ࡭ࡩ࠭ᷮ")] = bstack111l111111_opy_
            options[bstack11l11l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡧࡻࡩ࡭ࡦࡓࡶࡴࡪࡵࡤࡶࡐࡥࡵ࠭ᷯ")] = bstack111ll11ll1_opy_
            if bstack1l111ll11ll_opy_:
                options[bstack11l11l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬᷰ")] = bstack1l111ll11ll_opy_
                options[bstack11l11l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭ᷱ")] = bstack1l11lllll1l_opy_
                options[bstack11l11l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧᷲ")][bstack11l11l1_opy_ (u"ࠩࡶࡧࡦࡴ࡮ࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪᷳ")] = bstack111l111l11l_opy_
    return options
def bstack111l1ll1lll_opy_(ws_endpoint, framework):
    bstack111ll11ll1_opy_ = bstack11111111_opy_.get_property(bstack11l11l1_opy_ (u"ࠥࡔࡑࡇ࡙ࡘࡔࡌࡋࡍ࡚࡟ࡑࡔࡒࡈ࡚ࡉࡔࡠࡏࡄࡔࠧᷴ"))
    if ws_endpoint and len(ws_endpoint.split(bstack11l11l1_opy_ (u"ࠫࡨࡧࡰࡴ࠿ࠪ᷵"))) > 1:
        ws_url = ws_endpoint.split(bstack11l11l1_opy_ (u"ࠬࡩࡡࡱࡵࡀࠫ᷶"))[0]
        if bstack11l11l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮᷷ࠩ") in ws_url:
            from browserstack_sdk._version import __version__
            bstack111l11l1111_opy_ = json.loads(urllib.parse.unquote(ws_endpoint.split(bstack11l11l1_opy_ (u"ࠧࡤࡣࡳࡷࡂ᷸࠭"))[1]))
            bstack111l11l1111_opy_ = bstack111l11l1111_opy_ or {}
            bstack111l111111_opy_ = os.environ[bstack11l11l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ᷹࠭")]
            bstack111l11l1111_opy_[bstack11l11l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡓࡅࡍ᷺ࠪ")] = str(framework) + str(__version__)
            bstack111l11l1111_opy_[bstack11l11l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫ᷻")] = bstack1lll1l1111l_opy_()
            bstack111l11l1111_opy_[bstack11l11l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡸࡪࡹࡴࡩࡷࡥࡆࡺ࡯࡬ࡥࡗࡸ࡭ࡩ࠭᷼")] = bstack111l111111_opy_
            bstack111l11l1111_opy_[bstack11l11l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡧࡻࡩ࡭ࡦࡓࡶࡴࡪࡵࡤࡶࡐࡥࡵ᷽࠭")] = bstack111ll11ll1_opy_
            ws_endpoint = ws_endpoint.split(bstack11l11l1_opy_ (u"࠭ࡣࡢࡲࡶࡁࠬ᷾"))[0] + bstack11l11l1_opy_ (u"ࠧࡤࡣࡳࡷࡂ᷿࠭") + urllib.parse.quote(json.dumps(bstack111l11l1111_opy_))
    return ws_endpoint
def bstack1l1111ll11_opy_():
    global bstack11ll1l111_opy_
    from playwright._impl._browser_type import BrowserType
    bstack11ll1l111_opy_ = BrowserType.connect
    return bstack11ll1l111_opy_
def bstack1ll1l1ll11_opy_(framework_name):
    global bstack11111ll1l_opy_
    bstack11111ll1l_opy_ = framework_name
    return framework_name
def bstack1lll1l1lll_opy_(self, *args, **kwargs):
    global bstack11ll1l111_opy_
    try:
        global bstack11111ll1l_opy_
        if bstack11l11l1_opy_ (u"ࠨࡹࡶࡉࡳࡪࡰࡰ࡫ࡱࡸࠬḀ") in kwargs:
            kwargs[bstack11l11l1_opy_ (u"ࠩࡺࡷࡊࡴࡤࡱࡱ࡬ࡲࡹ࠭ḁ")] = bstack111l1ll1lll_opy_(
                kwargs.get(bstack11l11l1_opy_ (u"ࠪࡻࡸࡋ࡮ࡥࡲࡲ࡭ࡳࡺࠧḂ"), None),
                bstack11111ll1l_opy_
            )
    except Exception as e:
        logger.error(bstack11l11l1_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡻ࡭࡫࡮ࠡࡲࡵࡳࡨ࡫ࡳࡴ࡫ࡱ࡫࡙ࠥࡄࡌࠢࡦࡥࡵࡹ࠺ࠡࡽࢀࠦḃ").format(str(e)))
    return bstack11ll1l111_opy_(self, *args, **kwargs)
def bstack111l111l111_opy_(bstack111l1l11l11_opy_, proxies):
    proxy_settings = {}
    try:
        if not proxies:
            proxies = bstack11l1ll111_opy_(bstack111l1l11l11_opy_, bstack11l11l1_opy_ (u"ࠧࠨḄ"))
        if proxies and proxies.get(bstack11l11l1_opy_ (u"ࠨࡨࡵࡶࡳࡷࠧḅ")):
            parsed_url = urlparse(proxies.get(bstack11l11l1_opy_ (u"ࠢࡩࡶࡷࡴࡸࠨḆ")))
            if parsed_url and parsed_url.hostname: proxy_settings[bstack11l11l1_opy_ (u"ࠨࡲࡵࡳࡽࡿࡈࡰࡵࡷࠫḇ")] = str(parsed_url.hostname)
            if parsed_url and parsed_url.port: proxy_settings[bstack11l11l1_opy_ (u"ࠩࡳࡶࡴࡾࡹࡑࡱࡵࡸࠬḈ")] = str(parsed_url.port)
            if parsed_url and parsed_url.username: proxy_settings[bstack11l11l1_opy_ (u"ࠪࡴࡷࡵࡸࡺࡗࡶࡩࡷ࠭ḉ")] = str(parsed_url.username)
            if parsed_url and parsed_url.password: proxy_settings[bstack11l11l1_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡓࡥࡸࡹࠧḊ")] = str(parsed_url.password)
        return proxy_settings
    except:
        return proxy_settings
def bstack1ll11lll1l_opy_(bstack111l1l11l11_opy_):
    bstack1111l1l111l_opy_ = {
        bstack11l1l11lll1_opy_[bstack1111l1ll11l_opy_]: bstack111l1l11l11_opy_[bstack1111l1ll11l_opy_]
        for bstack1111l1ll11l_opy_ in bstack111l1l11l11_opy_
        if bstack1111l1ll11l_opy_ in bstack11l1l11lll1_opy_
    }
    bstack1111l1l111l_opy_[bstack11l11l1_opy_ (u"ࠧࡶࡲࡰࡺࡼࡗࡪࡺࡴࡪࡰࡪࡷࠧḋ")] = bstack111l111l111_opy_(bstack111l1l11l11_opy_, bstack11111111_opy_.get_property(bstack11l11l1_opy_ (u"ࠨࡰࡳࡱࡻࡽࡘ࡫ࡴࡵ࡫ࡱ࡫ࡸࠨḌ")))
    bstack1111ll1ll11_opy_ = [element.lower() for element in bstack11l11lll111_opy_]
    bstack111l111lll1_opy_(bstack1111l1l111l_opy_, bstack1111ll1ll11_opy_)
    return bstack1111l1l111l_opy_
def bstack111l111lll1_opy_(d, keys):
    for key in list(d.keys()):
        if key.lower() in keys:
            d[key] = bstack11l11l1_opy_ (u"ࠢࠫࠬ࠭࠮ࠧḍ")
    for value in d.values():
        if isinstance(value, dict):
            bstack111l111lll1_opy_(value, keys)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    bstack111l111lll1_opy_(item, keys)
def bstack1ll11ll1lll_opy_():
    bstack1111l1l1111_opy_ = [os.environ.get(bstack11l11l1_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡇࡋࡏࡉࡘࡥࡄࡊࡔࠥḎ")), os.path.join(os.path.expanduser(bstack11l11l1_opy_ (u"ࠤࢁࠦḏ")), bstack11l11l1_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪḐ")), os.path.join(bstack11l11l1_opy_ (u"ࠫ࠴ࡺ࡭ࡱࠩḑ"), bstack11l11l1_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬḒ"))]
    for path in bstack1111l1l1111_opy_:
        if path is None:
            continue
        try:
            if os.path.exists(path):
                logger.debug(bstack11l11l1_opy_ (u"ࠨࡆࡪ࡮ࡨࠤࠬࠨḓ") + str(path) + bstack11l11l1_opy_ (u"ࠢࠨࠢࡨࡼ࡮ࡹࡴࡴ࠰ࠥḔ"))
                if not os.access(path, os.W_OK):
                    logger.debug(bstack11l11l1_opy_ (u"ࠣࡉ࡬ࡺ࡮ࡴࡧࠡࡲࡨࡶࡲ࡯ࡳࡴ࡫ࡲࡲࡸࠦࡦࡰࡴࠣࠫࠧḕ") + str(path) + bstack11l11l1_opy_ (u"ࠤࠪࠦḖ"))
                    os.chmod(path, 0o777)
                else:
                    logger.debug(bstack11l11l1_opy_ (u"ࠥࡊ࡮ࡲࡥࠡࠩࠥḗ") + str(path) + bstack11l11l1_opy_ (u"ࠦࠬࠦࡡ࡭ࡴࡨࡥࡩࡿࠠࡩࡣࡶࠤࡹ࡮ࡥࠡࡴࡨࡵࡺ࡯ࡲࡦࡦࠣࡴࡪࡸ࡭ࡪࡵࡶ࡭ࡴࡴࡳ࠯ࠤḘ"))
            else:
                logger.debug(bstack11l11l1_opy_ (u"ࠧࡉࡲࡦࡣࡷ࡭ࡳ࡭ࠠࡧ࡫࡯ࡩࠥ࠭ࠢḙ") + str(path) + bstack11l11l1_opy_ (u"ࠨࠧࠡࡹ࡬ࡸ࡭ࠦࡷࡳ࡫ࡷࡩࠥࡶࡥࡳ࡯࡬ࡷࡸ࡯࡯࡯࠰ࠥḚ"))
                os.makedirs(path, exist_ok=True)
                os.chmod(path, 0o777)
            logger.debug(bstack11l11l1_opy_ (u"ࠢࡐࡲࡨࡶࡦࡺࡩࡰࡰࠣࡷࡺࡩࡣࡦࡧࡧࡩࡩࠦࡦࡰࡴࠣࠫࠧḛ") + str(path) + bstack11l11l1_opy_ (u"ࠣࠩ࠱ࠦḜ"))
            return path
        except Exception as e:
            logger.debug(bstack11l11l1_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡹࡥࡵࠢࡸࡴࠥ࡬ࡩ࡭ࡧࠣࠫࢀࡶࡡࡵࡪࢀࠫ࠿ࠦࠢḝ") + str(e) + bstack11l11l1_opy_ (u"ࠥࠦḞ"))
    logger.debug(bstack11l11l1_opy_ (u"ࠦࡆࡲ࡬ࠡࡲࡤࡸ࡭ࡹࠠࡧࡣ࡬ࡰࡪࡪ࠮ࠣḟ"))
    return None
@measure(event_name=EVENTS.bstack11l1l1l1l1l_opy_, stage=STAGE.bstack1ll1lllll_opy_)
def bstack1l11ll1ll1l_opy_(binary_path, bstack1l1l1l1l1ll_opy_, bs_config):
    logger.debug(bstack11l11l1_opy_ (u"ࠧࡉࡵࡳࡴࡨࡲࡹࠦࡃࡍࡋࠣࡔࡦࡺࡨࠡࡨࡲࡹࡳࡪ࠺ࠡࡽࢀࠦḠ").format(binary_path))
    bstack1111ll1lll1_opy_ = bstack11l11l1_opy_ (u"࠭ࠧḡ")
    bstack111l1111l11_opy_ = {
        bstack11l11l1_opy_ (u"ࠧࡴࡦ࡮ࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬḢ"): __version__,
        bstack11l11l1_opy_ (u"ࠣࡱࡶࠦḣ"): platform.system(),
        bstack11l11l1_opy_ (u"ࠤࡲࡷࡤࡧࡲࡤࡪࠥḤ"): platform.machine(),
        bstack11l11l1_opy_ (u"ࠥࡧࡱ࡯࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠣḥ"): bstack11l11l1_opy_ (u"ࠫ࠵࠭Ḧ"),
        bstack11l11l1_opy_ (u"ࠧࡹࡤ࡬ࡡ࡯ࡥࡳ࡭ࡵࡢࡩࡨࠦḧ"): bstack11l11l1_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭Ḩ")
    }
    bstack1111l11l1ll_opy_(bstack111l1111l11_opy_)
    try:
        if binary_path:
            bstack111l1111l11_opy_[bstack11l11l1_opy_ (u"ࠧࡤ࡮࡬ࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬḩ")] = subprocess.check_output([binary_path, bstack11l11l1_opy_ (u"ࠣࡸࡨࡶࡸ࡯࡯࡯ࠤḪ")]).strip().decode(bstack11l11l1_opy_ (u"ࠩࡸࡸ࡫࠳࠸ࠨḫ"))
        response = requests.request(
            bstack11l11l1_opy_ (u"ࠪࡋࡊ࡚ࠧḬ"),
            url=bstack1l111111l1_opy_(bstack11l1l1l11l1_opy_),
            headers=None,
            auth=(bs_config[bstack11l11l1_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭ḭ")], bs_config[bstack11l11l1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨḮ")]),
            json=None,
            params=bstack111l1111l11_opy_
        )
        data = response.json()
        if response.status_code == 200 and bstack11l11l1_opy_ (u"࠭ࡵࡳ࡮ࠪḯ") in data.keys() and bstack11l11l1_opy_ (u"ࠧࡶࡲࡧࡥࡹ࡫ࡤࡠࡥ࡯࡭ࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭Ḱ") in data.keys():
            logger.debug(bstack11l11l1_opy_ (u"ࠣࡐࡨࡩࡩࠦࡴࡰࠢࡸࡴࡩࡧࡴࡦࠢࡥ࡭ࡳࡧࡲࡺ࠮ࠣࡧࡺࡸࡲࡦࡰࡷࠤࡧ࡯࡮ࡢࡴࡼࠤࡻ࡫ࡲࡴ࡫ࡲࡲ࠿ࠦࡻࡾࠤḱ").format(bstack111l1111l11_opy_[bstack11l11l1_opy_ (u"ࠩࡦࡰ࡮ࡥࡶࡦࡴࡶ࡭ࡴࡴࠧḲ")]))
            if bstack11l11l1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡅࡍࡓࡇࡒ࡚ࡡࡘࡖࡑ࠭ḳ") in os.environ:
                logger.debug(bstack11l11l1_opy_ (u"ࠦࡘࡱࡩࡱࡲ࡬ࡲ࡬ࠦࡢࡪࡰࡤࡶࡾࠦࡤࡰࡹࡱࡰࡴࡧࡤࠡࡣࡶࠤࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡆࡎࡔࡁࡓ࡛ࡢ࡙ࡗࡒࠠࡪࡵࠣࡷࡪࡺࠢḴ"))
                data[bstack11l11l1_opy_ (u"ࠬࡻࡲ࡭ࠩḵ")] = os.environ[bstack11l11l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡈࡉࡏࡃࡕ࡝ࡤ࡛ࡒࡍࠩḶ")]
            bstack111l1llll11_opy_ = bstack111l1lll111_opy_(data[bstack11l11l1_opy_ (u"ࠧࡶࡴ࡯ࠫḷ")], bstack1l1l1l1l1ll_opy_)
            bstack1111ll1lll1_opy_ = os.path.join(bstack1l1l1l1l1ll_opy_, bstack111l1llll11_opy_)
            os.chmod(bstack1111ll1lll1_opy_, 0o777) # bstack1111lll1l11_opy_ permission
            return bstack1111ll1lll1_opy_
    except Exception as e:
        logger.debug(bstack11l11l1_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡸࡪ࡬ࡰࡪࠦࡤࡰࡹࡱࡰࡴࡧࡤࡪࡰࡪࠤࡳ࡫ࡷࠡࡕࡇࡏࠥࢁࡽࠣḸ").format(e))
    return binary_path
def bstack1111l11l1ll_opy_(bstack111l1111l11_opy_):
    try:
        if bstack11l11l1_opy_ (u"ࠩ࡯࡭ࡳࡻࡸࠨḹ") not in bstack111l1111l11_opy_[bstack11l11l1_opy_ (u"ࠪࡳࡸ࠭Ḻ")].lower():
            return
        if os.path.exists(bstack11l11l1_opy_ (u"ࠦ࠴࡫ࡴࡤ࠱ࡲࡷ࠲ࡸࡥ࡭ࡧࡤࡷࡪࠨḻ")):
            with open(bstack11l11l1_opy_ (u"ࠧ࠵ࡥࡵࡥ࠲ࡳࡸ࠳ࡲࡦ࡮ࡨࡥࡸ࡫ࠢḼ"), bstack11l11l1_opy_ (u"ࠨࡲࠣḽ")) as f:
                bstack111l1l111ll_opy_ = {}
                for line in f:
                    if bstack11l11l1_opy_ (u"ࠢ࠾ࠤḾ") in line:
                        key, value = line.rstrip().split(bstack11l11l1_opy_ (u"ࠣ࠿ࠥḿ"), 1)
                        bstack111l1l111ll_opy_[key] = value.strip(bstack11l11l1_opy_ (u"ࠩࠥࡠࠬ࠭Ṁ"))
                bstack111l1111l11_opy_[bstack11l11l1_opy_ (u"ࠪࡨ࡮ࡹࡴࡳࡱࠪṁ")] = bstack111l1l111ll_opy_.get(bstack11l11l1_opy_ (u"ࠦࡎࡊࠢṂ"), bstack11l11l1_opy_ (u"ࠧࠨṃ"))
        elif os.path.exists(bstack11l11l1_opy_ (u"ࠨ࠯ࡦࡶࡦ࠳ࡦࡲࡰࡪࡰࡨ࠱ࡷ࡫࡬ࡦࡣࡶࡩࠧṄ")):
            bstack111l1111l11_opy_[bstack11l11l1_opy_ (u"ࠧࡥ࡫ࡶࡸࡷࡵࠧṅ")] = bstack11l11l1_opy_ (u"ࠨࡣ࡯ࡴ࡮ࡴࡥࠨṆ")
    except Exception as e:
        logger.debug(bstack11l11l1_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥ࡭ࡥࡵࠢࡧ࡭ࡸࡺࡲࡰࠢࡲࡪࠥࡲࡩ࡯ࡷࡻࠦṇ") + e)
@measure(event_name=EVENTS.bstack11l1l1l111l_opy_, stage=STAGE.bstack1ll1lllll_opy_)
def bstack111l1lll111_opy_(bstack1111l1l1l11_opy_, bstack1111ll1ll1l_opy_):
    logger.debug(bstack11l11l1_opy_ (u"ࠥࡈࡴࡽ࡮࡭ࡱࡤࡨ࡮ࡴࡧࠡࡕࡇࡏࠥࡨࡩ࡯ࡣࡵࡽࠥ࡬ࡲࡰ࡯࠽ࠤࠧṈ") + str(bstack1111l1l1l11_opy_) + bstack11l11l1_opy_ (u"ࠦࠧṉ"))
    zip_path = os.path.join(bstack1111ll1ll1l_opy_, bstack11l11l1_opy_ (u"ࠧࡪ࡯ࡸࡰ࡯ࡳࡦࡪࡥࡥࡡࡩ࡭ࡱ࡫࠮ࡻ࡫ࡳࠦṊ"))
    bstack111l1llll11_opy_ = bstack11l11l1_opy_ (u"࠭ࠧṋ")
    with requests.get(bstack1111l1l1l11_opy_, stream=True) as response:
        response.raise_for_status()
        with open(zip_path, bstack11l11l1_opy_ (u"ࠢࡸࡤࠥṌ")) as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
        logger.debug(bstack11l11l1_opy_ (u"ࠣࡈ࡬ࡰࡪࠦࡤࡰࡹࡱࡰࡴࡧࡤࡦࡦࠣࡷࡺࡩࡣࡦࡵࡶࡪࡺࡲ࡬ࡺ࠰ࠥṍ"))
    with zipfile.ZipFile(zip_path, bstack11l11l1_opy_ (u"ࠩࡵࠫṎ")) as zip_ref:
        bstack1111lll1ll1_opy_ = zip_ref.namelist()
        if len(bstack1111lll1ll1_opy_) > 0:
            bstack111l1llll11_opy_ = bstack1111lll1ll1_opy_[0] # bstack111l11l11l1_opy_ bstack11l1l1111l1_opy_ will be bstack111l111l1ll_opy_ 1 file i.e. the binary in the zip
        zip_ref.extractall(bstack1111ll1ll1l_opy_)
        logger.debug(bstack11l11l1_opy_ (u"ࠥࡊ࡮ࡲࡥࡴࠢࡶࡹࡨࡩࡥࡴࡵࡩࡹࡱࡲࡹࠡࡧࡻࡸࡷࡧࡣࡵࡧࡧࠤࡹࡵࠠࠨࠤṏ") + str(bstack1111ll1ll1l_opy_) + bstack11l11l1_opy_ (u"ࠦࠬࠨṐ"))
    os.remove(zip_path)
    return bstack111l1llll11_opy_
def get_cli_dir():
    bstack1111ll111l1_opy_ = bstack1ll11ll1lll_opy_()
    if bstack1111ll111l1_opy_:
        bstack1l1l1l1l1ll_opy_ = os.path.join(bstack1111ll111l1_opy_, bstack11l11l1_opy_ (u"ࠧࡩ࡬ࡪࠤṑ"))
        if not os.path.exists(bstack1l1l1l1l1ll_opy_):
            os.makedirs(bstack1l1l1l1l1ll_opy_, mode=0o777, exist_ok=True)
        return bstack1l1l1l1l1ll_opy_
    else:
        raise FileNotFoundError(bstack11l11l1_opy_ (u"ࠨࡎࡰࠢࡺࡶ࡮ࡺࡡࡣ࡮ࡨࠤࡩ࡯ࡲࡦࡥࡷࡳࡷࡿࠠࡢࡸࡤ࡭ࡱࡧࡢ࡭ࡧࠣࡪࡴࡸࠠࡵࡪࡨࠤࡘࡊࡋࠡࡤ࡬ࡲࡦࡸࡹ࠯ࠤṒ"))
def bstack1l1l1ll1lll_opy_(bstack1l1l1l1l1ll_opy_):
    bstack11l11l1_opy_ (u"ࠢࠣࠤࡊࡩࡹࠦࡴࡩࡧࠣࡴࡦࡺࡨࠡࡨࡲࡶࠥࡺࡨࡦࠢࡅࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࠡࡕࡇࡏࠥࡨࡩ࡯ࡣࡵࡽࠥ࡯࡮ࠡࡣࠣࡻࡷ࡯ࡴࡢࡤ࡯ࡩࠥࡪࡩࡳࡧࡦࡸࡴࡸࡹ࠯ࠤࠥࠦṓ")
    bstack1111l1lll11_opy_ = [
        os.path.join(bstack1l1l1l1l1ll_opy_, f)
        for f in os.listdir(bstack1l1l1l1l1ll_opy_)
        if os.path.isfile(os.path.join(bstack1l1l1l1l1ll_opy_, f)) and f.startswith(bstack11l11l1_opy_ (u"ࠣࡤ࡬ࡲࡦࡸࡹ࠮ࠤṔ"))
    ]
    if len(bstack1111l1lll11_opy_) > 0:
        return max(bstack1111l1lll11_opy_, key=os.path.getmtime) # get bstack111l1111lll_opy_ binary
    return bstack11l11l1_opy_ (u"ࠤࠥṕ")
def bstack1111lllll1l_opy_():
  from selenium import webdriver
  return version.parse(webdriver.__version__)
def bstack1l111ll1l1l_opy_(d, u):
  for k, v in u.items():
    if isinstance(v, collections.abc.Mapping):
      d[k] = bstack1l111ll1l1l_opy_(d.get(k, {}), v)
    else:
      if isinstance(v, list):
        d[k] = d.get(k, []) + v
      else:
        d[k] = v
  return d
def bstack11l1lll1l_opy_(data, keys, default=None):
    bstack11l11l1_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࡗࡦ࡬ࡥ࡭ࡻࠣ࡫ࡪࡺࠠࡢࠢࡱࡩࡸࡺࡥࡥࠢࡹࡥࡱࡻࡥࠡࡨࡵࡳࡲࠦࡡࠡࡦ࡬ࡧࡹ࡯࡯࡯ࡣࡵࡽࠥࡵࡲࠡ࡮࡬ࡷࡹ࠴ࠊࠡࠢࠣࠤ࠿ࡶࡡࡳࡣࡰࠤࡩࡧࡴࡢ࠼ࠣࡘ࡭࡫ࠠࡥ࡫ࡦࡸ࡮ࡵ࡮ࡢࡴࡼࠤࡴࡸࠠ࡭࡫ࡶࡸࠥࡺ࡯ࠡࡶࡵࡥࡻ࡫ࡲࡴࡧ࠱ࠎࠥࠦࠠࠡ࠼ࡳࡥࡷࡧ࡭ࠡ࡭ࡨࡽࡸࡀࠠࡂࠢ࡯࡭ࡸࡺࠠࡰࡨࠣ࡯ࡪࡿࡳ࠰࡫ࡱࡨ࡮ࡩࡥࡴࠢࡵࡩࡵࡸࡥࡴࡧࡱࡸ࡮ࡴࡧࠡࡶ࡫ࡩࠥࡶࡡࡵࡪ࠱ࠎࠥࠦࠠࠡ࠼ࡳࡥࡷࡧ࡭ࠡࡦࡨࡪࡦࡻ࡬ࡵ࠼࡚ࠣࡦࡲࡵࡦࠢࡷࡳࠥࡸࡥࡵࡷࡵࡲࠥ࡯ࡦࠡࡶ࡫ࡩࠥࡶࡡࡵࡪࠣࡨࡴ࡫ࡳࠡࡰࡲࡸࠥ࡫ࡸࡪࡵࡷ࠲ࠏࠦࠠࠡࠢ࠽ࡶࡪࡺࡵࡳࡰ࠽ࠤ࡙࡮ࡥࠡࡸࡤࡰࡺ࡫ࠠࡢࡶࠣࡸ࡭࡫ࠠ࡯ࡧࡶࡸࡪࡪࠠࡱࡣࡷ࡬࠱ࠦ࡯ࡳࠢࡧࡩ࡫ࡧࡵ࡭ࡶࠣ࡭࡫ࠦ࡮ࡰࡶࠣࡪࡴࡻ࡮ࡥ࠰ࠍࠤࠥࠦࠠࠣࠤࠥṖ")
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