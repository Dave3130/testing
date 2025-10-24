# coding: UTF-8
import sys
bstack1lll1_opy_ = sys.version_info [0] == 2
bstack11l11_opy_ = 2048
bstack1_opy_ = 7
def bstack1l1_opy_ (bstack1llllll_opy_):
    global bstack1l11111_opy_
    bstack1l111l_opy_ = ord (bstack1llllll_opy_ [-1])
    bstack11l1ll1_opy_ = bstack1llllll_opy_ [:-1]
    bstack11l1l1l_opy_ = bstack1l111l_opy_ % len (bstack11l1ll1_opy_)
    bstack11111l1_opy_ = bstack11l1ll1_opy_ [:bstack11l1l1l_opy_] + bstack11l1ll1_opy_ [bstack11l1l1l_opy_:]
    if bstack1lll1_opy_:
        bstack1lllll1_opy_ = unicode () .join ([unichr (ord (char) - bstack11l11_opy_ - (bstack1l1ll11_opy_ + bstack1l111l_opy_) % bstack1_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11111l1_opy_)])
    else:
        bstack1lllll1_opy_ = str () .join ([chr (ord (char) - bstack11l11_opy_ - (bstack1l1ll11_opy_ + bstack1l111l_opy_) % bstack1_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11111l1_opy_)])
    return eval (bstack1lllll1_opy_)
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
from bstack_utils.constants import (bstack1111l1l11_opy_, bstack11l1ll11l1_opy_, bstack1lll11l111_opy_,
                                    bstack11l1l11l11l_opy_, bstack11l11llllll_opy_, bstack11l11l1llll_opy_, bstack11l1l1l1l1l_opy_)
from bstack_utils.measure import measure
from bstack_utils.messages import bstack111lllll11_opy_, bstack11ll1l1ll1_opy_
from bstack_utils.proxy import bstack1111ll1lll_opy_, bstack1l1l11lll1_opy_
from bstack_utils.constants import *
from bstack_utils import bstack1ll1111l1_opy_
from bstack_utils.bstack11l11l111l_opy_ import bstack11ll1ll1ll_opy_
from browserstack_sdk._version import __version__
bstack11l11111_opy_ = Config.bstack1111ll1l_opy_()
logger = bstack1ll1111l1_opy_.get_logger(__name__, bstack1ll1111l1_opy_.bstack1l1l111l1ll_opy_())
def bstack111l1ll1ll1_opy_(config):
    return config[bstack1l1_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧᯢ")]
def bstack111l11l1111_opy_(config):
    return config[bstack1l1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩᯣ")]
def bstack1l11lll1l1_opy_():
    try:
        import playwright
        return True
    except ImportError:
        return False
def bstack111l1llll11_opy_(obj):
    values = []
    bstack1111lll111l_opy_ = re.compile(bstack1l1_opy_ (u"ࡲࠣࡠࡆ࡙ࡘ࡚ࡏࡎࡡࡗࡅࡌࡥ࡜ࡥ࠭ࠧࠦᯤ"), re.I)
    for key in obj.keys():
        if bstack1111lll111l_opy_.match(key):
            values.append(obj[key])
    return values
def bstack1111l1l1111_opy_(config):
    tags = []
    tags.extend(bstack111l1llll11_opy_(os.environ))
    tags.extend(bstack111l1llll11_opy_(config))
    return tags
def bstack111l1l1ll11_opy_(markers):
    tags = []
    for marker in markers:
        tags.append(marker.name)
    return tags
def bstack111l1l11l11_opy_(bstack1111ll1111l_opy_):
    if not bstack1111ll1111l_opy_:
        return bstack1l1_opy_ (u"ࠨࠩᯥ")
    return bstack1l1_opy_ (u"ࠤࡾࢁࠥ࠮ࡻࡾ᯦ࠫࠥ").format(bstack1111ll1111l_opy_.name, bstack1111ll1111l_opy_.email)
def bstack111l1ll1l11_opy_():
    try:
        repo = git.Repo(search_parent_directories=True)
        bstack111l1ll1lll_opy_ = repo.common_dir
        info = {
            bstack1l1_opy_ (u"ࠥࡷ࡭ࡧࠢᯧ"): repo.head.commit.hexsha,
            bstack1l1_opy_ (u"ࠦࡸ࡮࡯ࡳࡶࡢࡷ࡭ࡧࠢᯨ"): repo.git.rev_parse(repo.head.commit, short=True),
            bstack1l1_opy_ (u"ࠧࡨࡲࡢࡰࡦ࡬ࠧᯩ"): repo.active_branch.name,
            bstack1l1_opy_ (u"ࠨࡴࡢࡩࠥᯪ"): repo.git.describe(all=True, tags=True, exact_match=True),
            bstack1l1_opy_ (u"ࠢࡤࡱࡰࡱ࡮ࡺࡴࡦࡴࠥᯫ"): bstack111l1l11l11_opy_(repo.head.commit.committer),
            bstack1l1_opy_ (u"ࠣࡥࡲࡱࡲ࡯ࡴࡵࡧࡵࡣࡩࡧࡴࡦࠤᯬ"): repo.head.commit.committed_datetime.isoformat(),
            bstack1l1_opy_ (u"ࠤࡤࡹࡹ࡮࡯ࡳࠤᯭ"): bstack111l1l11l11_opy_(repo.head.commit.author),
            bstack1l1_opy_ (u"ࠥࡥࡺࡺࡨࡰࡴࡢࡨࡦࡺࡥࠣᯮ"): repo.head.commit.authored_datetime.isoformat(),
            bstack1l1_opy_ (u"ࠦࡨࡵ࡭࡮࡫ࡷࡣࡲ࡫ࡳࡴࡣࡪࡩࠧᯯ"): repo.head.commit.message,
            bstack1l1_opy_ (u"ࠧࡸ࡯ࡰࡶࠥᯰ"): repo.git.rev_parse(bstack1l1_opy_ (u"ࠨ࠭࠮ࡵ࡫ࡳࡼ࠳ࡴࡰࡲ࡯ࡩࡻ࡫࡬ࠣᯱ")),
            bstack1l1_opy_ (u"ࠢࡤࡱࡰࡱࡴࡴ࡟ࡨ࡫ࡷࡣࡩ࡯ࡲ᯲ࠣ"): bstack111l1ll1lll_opy_,
            bstack1l1_opy_ (u"ࠣࡹࡲࡶࡰࡺࡲࡦࡧࡢ࡫࡮ࡺ࡟ࡥ࡫ࡵ᯳ࠦ"): subprocess.check_output([bstack1l1_opy_ (u"ࠤࡪ࡭ࡹࠨ᯴"), bstack1l1_opy_ (u"ࠥࡶࡪࡼ࠭ࡱࡣࡵࡷࡪࠨ᯵"), bstack1l1_opy_ (u"ࠦ࠲࠳ࡧࡪࡶ࠰ࡧࡴࡳ࡭ࡰࡰ࠰ࡨ࡮ࡸࠢ᯶")]).strip().decode(
                bstack1l1_opy_ (u"ࠬࡻࡴࡧ࠯࠻ࠫ᯷")),
            bstack1l1_opy_ (u"ࠨ࡬ࡢࡵࡷࡣࡹࡧࡧࠣ᯸"): repo.git.describe(tags=True, abbrev=0, always=True),
            bstack1l1_opy_ (u"ࠢࡤࡱࡰࡱ࡮ࡺࡳࡠࡵ࡬ࡲࡨ࡫࡟࡭ࡣࡶࡸࡤࡺࡡࡨࠤ᯹"): repo.git.rev_list(
                bstack1l1_opy_ (u"ࠣࡽࢀ࠲࠳ࢁࡽࠣ᯺").format(repo.head.commit, repo.git.describe(tags=True, abbrev=0, always=True)), count=True)
        }
        remotes = repo.remotes
        bstack111l1111111_opy_ = []
        for remote in remotes:
            bstack111l1l1l111_opy_ = {
                bstack1l1_opy_ (u"ࠤࡱࡥࡲ࡫ࠢ᯻"): remote.name,
                bstack1l1_opy_ (u"ࠥࡹࡷࡲࠢ᯼"): remote.url,
            }
            bstack111l1111111_opy_.append(bstack111l1l1l111_opy_)
        bstack111l1l1lll1_opy_ = {
            bstack1l1_opy_ (u"ࠦࡳࡧ࡭ࡦࠤ᯽"): bstack1l1_opy_ (u"ࠧ࡭ࡩࡵࠤ᯾"),
            **info,
            bstack1l1_opy_ (u"ࠨࡲࡦ࡯ࡲࡸࡪࡹࠢ᯿"): bstack111l1111111_opy_
        }
        bstack111l1l1lll1_opy_ = bstack1111llll11l_opy_(bstack111l1l1lll1_opy_)
        return bstack111l1l1lll1_opy_
    except git.InvalidGitRepositoryError:
        return {}
    except Exception as err:
        print(bstack1l1_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡰࡰࡲࡸࡰࡦࡺࡩ࡯ࡩࠣࡋ࡮ࡺࠠ࡮ࡧࡷࡥࡩࡧࡴࡢࠢࡺ࡭ࡹ࡮ࠠࡦࡴࡵࡳࡷࡀࠠࡼࡿࠥᰀ").format(err))
        return {}
def bstack11lll1111l1_opy_(bstack111l1l1llll_opy_=None):
    bstack1l1_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࡉࡨࡸࠥ࡭ࡩࡵࠢࡰࡩࡹࡧࡤࡢࡶࡤࠤࡸࡶࡥࡤ࡫ࡩ࡭ࡨࡧ࡬࡭ࡻࠣࡪࡴࡸ࡭ࡢࡶࡷࡩࡩࠦࡦࡰࡴࠣࡅࡎࠦࡳࡦ࡮ࡨࡧࡹ࡯࡯࡯ࠢࡸࡷࡪࠦࡣࡢࡵࡨࡷࠥ࡬࡯ࡳࠢࡨࡥࡨ࡮ࠠࡧࡱ࡯ࡨࡪࡸࠠࡪࡰࠣࡸ࡭࡫ࠠ࡭࡫ࡶࡸ࠳ࠐࠠࠡࠢࠣࡅࡷ࡭ࡳ࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࡪࡴࡲࡤࡦࡴࡶࠤ࠭ࡲࡩࡴࡶ࠯ࠤࡴࡶࡴࡪࡱࡱࡥࡱ࠯࠺ࠡࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠ࠮ࠢࡑࡳࡳ࡫࠺ࠡࡏࡲࡲࡴ࠳ࡲࡦࡲࡲࠤࡦࡶࡰࡳࡱࡤࡧ࡭࠲ࠠࡶࡵࡨࡷࠥࡩࡵࡳࡴࡨࡲࡹࠦࡤࡪࡴࡨࡧࡹࡵࡲࡺࠢ࡞ࡳࡸ࠴ࡧࡦࡶࡦࡻࡩ࠮ࠩ࡞ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠ࠮ࠢࡈࡱࡵࡺࡹࠡ࡮࡬ࡷࡹ࡛ࠦ࡞࠼ࠣࡑࡺࡲࡴࡪ࠯ࡵࡩࡵࡵࠠࡢࡲࡳࡶࡴࡧࡣࡩࠢࡺ࡭ࡹ࡮ࠠ࡯ࡱࠣࡷࡴࡻࡲࡤࡧࡶࠤࡨࡵ࡮ࡧ࡫ࡪࡹࡷ࡫ࡤ࠭ࠢࡵࡩࡹࡻࡲ࡯ࡵࠣ࡟ࡢࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࠲ࠦࡌࡪࡵࡷࠤࡴ࡬ࠠࡱࡣࡷ࡬ࡸࡀࠠࡎࡷ࡯ࡸ࡮࠳ࡲࡦࡲࡲࠤࡦࡶࡰࡳࡱࡤࡧ࡭ࠦࡷࡪࡶ࡫ࠤࡸࡶࡥࡤ࡫ࡩ࡭ࡨࠦࡦࡰ࡮ࡧࡩࡷࡹࠠࡵࡱࠣࡥࡳࡧ࡬ࡺࡼࡨࠎࠥࠦࠠࠡࡔࡨࡸࡺࡸ࡮ࡴ࠼ࠍࠤࠥࠦࠠࠡࠢࠣࠤࡱ࡯ࡳࡵ࠼ࠣࡐ࡮ࡹࡴࠡࡱࡩࠤࡩ࡯ࡣࡵࡵ࠯ࠤࡪࡧࡣࡩࠢࡦࡳࡳࡺࡡࡪࡰ࡬ࡲ࡬ࠦࡧࡪࡶࠣࡱࡪࡺࡡࡥࡣࡷࡥࠥ࡬࡯ࡳࠢࡤࠤ࡫ࡵ࡬ࡥࡧࡵ࠲ࠏࠦࠠࠡࠢࠥࠦࠧᰁ")
    if bstack111l1l1llll_opy_ is None:
        bstack111l1l1llll_opy_ = [os.getcwd()]
    elif isinstance(bstack111l1l1llll_opy_, list) and len(bstack111l1l1llll_opy_) == 0:
        return []
    results = []
    for folder in bstack111l1l1llll_opy_:
        try:
            repo = git.Repo(folder, search_parent_directories=True)
            result = {
                bstack1l1_opy_ (u"ࠤࡳࡶࡎࡪࠢᰂ"): bstack1l1_opy_ (u"ࠥࠦᰃ"),
                bstack1l1_opy_ (u"ࠦ࡫࡯࡬ࡦࡵࡆ࡬ࡦࡴࡧࡦࡦࠥᰄ"): [],
                bstack1l1_opy_ (u"ࠧࡧࡵࡵࡪࡲࡶࡸࠨᰅ"): [],
                bstack1l1_opy_ (u"ࠨࡰࡳࡆࡤࡸࡪࠨᰆ"): bstack1l1_opy_ (u"ࠢࠣᰇ"),
                bstack1l1_opy_ (u"ࠣࡥࡲࡱࡲ࡯ࡴࡎࡧࡶࡷࡦ࡭ࡥࡴࠤᰈ"): [],
                bstack1l1_opy_ (u"ࠤࡳࡶ࡙࡯ࡴ࡭ࡧࠥᰉ"): bstack1l1_opy_ (u"ࠥࠦᰊ"),
                bstack1l1_opy_ (u"ࠦࡵࡸࡄࡦࡵࡦࡶ࡮ࡶࡴࡪࡱࡱࠦᰋ"): bstack1l1_opy_ (u"ࠧࠨᰌ"),
                bstack1l1_opy_ (u"ࠨࡰࡳࡔࡤࡻࡉ࡯ࡦࡧࠤᰍ"): bstack1l1_opy_ (u"ࠢࠣᰎ")
            }
            bstack1111l1l11ll_opy_ = repo.active_branch.name
            bstack1111lllll1l_opy_ = repo.head.commit
            result[bstack1l1_opy_ (u"ࠣࡲࡵࡍࡩࠨᰏ")] = bstack1111lllll1l_opy_.hexsha
            bstack1111l11l11l_opy_ = _1111l1ll111_opy_(repo)
            logger.debug(bstack1l1_opy_ (u"ࠤࡅࡥࡸ࡫ࠠࡣࡴࡤࡲࡨ࡮ࠠࡧࡱࡵࠤࡨࡵ࡭ࡱࡣࡵ࡭ࡸࡵ࡮࠻ࠢࠥᰐ") + str(bstack1111l11l11l_opy_) + bstack1l1_opy_ (u"ࠥࠦᰑ"))
            if bstack1111l11l11l_opy_:
                try:
                    bstack1111l1lll11_opy_ = repo.git.diff(bstack1l1_opy_ (u"ࠦ࠲࠳࡮ࡢ࡯ࡨ࠱ࡴࡴ࡬ࡺࠤᰒ"), bstack1lll1llll11_opy_ (u"ࠧࢁࡢࡢࡵࡨࡣࡧࡸࡡ࡯ࡥ࡫ࢁ࠳࠴࠮ࡼࡥࡸࡶࡷ࡫࡮ࡵࡡࡥࡶࡦࡴࡣࡩࡿࠥᰓ")).split(bstack1l1_opy_ (u"࠭࡜࡯ࠩᰔ"))
                    logger.debug(bstack1l1_opy_ (u"ࠢࡄࡪࡤࡲ࡬࡫ࡤࠡࡨ࡬ࡰࡪࡹࠠࡣࡧࡷࡻࡪ࡫࡮ࠡࡽࡥࡥࡸ࡫࡟ࡣࡴࡤࡲࡨ࡮ࡽࠡࡣࡱࡨࠥࢁࡣࡶࡴࡵࡩࡳࡺ࡟ࡣࡴࡤࡲࡨ࡮ࡽ࠻ࠢࠥᰕ") + str(bstack1111l1lll11_opy_) + bstack1l1_opy_ (u"ࠣࠤᰖ"))
                    result[bstack1l1_opy_ (u"ࠤࡩ࡭ࡱ࡫ࡳࡄࡪࡤࡲ࡬࡫ࡤࠣᰗ")] = [f.strip() for f in bstack1111l1lll11_opy_ if f.strip()]
                    commits = list(repo.iter_commits(bstack1lll1llll11_opy_ (u"ࠥࡿࡧࡧࡳࡦࡡࡥࡶࡦࡴࡣࡩࡿ࠱࠲ࢀࡩࡵࡳࡴࡨࡲࡹࡥࡢࡳࡣࡱࡧ࡭ࢃࠢᰘ")))
                except Exception:
                    logger.debug(bstack1l1_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡨࡧࡷࠤࡨ࡮ࡡ࡯ࡩࡨࡨࠥ࡬ࡩ࡭ࡧࡶࠤ࡫ࡸ࡯࡮ࠢࡥࡶࡦࡴࡣࡩࠢࡦࡳࡲࡶࡡࡳ࡫ࡶࡳࡳ࠴ࠠࡇࡣ࡯ࡰ࡮ࡴࡧࠡࡤࡤࡧࡰࠦࡴࡰࠢࡵࡩࡨ࡫࡮ࡵࠢࡦࡳࡲࡳࡩࡵࡵ࠱ࠦᰙ"))
                    commits = list(repo.iter_commits(max_count=10))
                    if commits:
                        result[bstack1l1_opy_ (u"ࠧ࡬ࡩ࡭ࡧࡶࡇ࡭ࡧ࡮ࡨࡧࡧࠦᰚ")] = _111l111111l_opy_(commits[:5])
            else:
                commits = list(repo.iter_commits(max_count=10))
                if commits:
                    result[bstack1l1_opy_ (u"ࠨࡦࡪ࡮ࡨࡷࡈ࡮ࡡ࡯ࡩࡨࡨࠧᰛ")] = _111l111111l_opy_(commits[:5])
            bstack1111ll11ll1_opy_ = set()
            bstack111l11llll1_opy_ = []
            for commit in commits:
                logger.debug(bstack1l1_opy_ (u"ࠢࡑࡴࡲࡧࡪࡹࡳࡪࡰࡪࠤࡨࡵ࡭࡮࡫ࡷ࠾ࠥࠨᰜ") + str(commit.message) + bstack1l1_opy_ (u"ࠣࠤᰝ"))
                bstack111l11l1l11_opy_ = commit.author.name if commit.author else bstack1l1_opy_ (u"ࠤࡘࡲࡰࡴ࡯ࡸࡰࠥᰞ")
                bstack1111ll11ll1_opy_.add(bstack111l11l1l11_opy_)
                bstack111l11llll1_opy_.append({
                    bstack1l1_opy_ (u"ࠥࡱࡪࡹࡳࡢࡩࡨࠦᰟ"): commit.message.strip(),
                    bstack1l1_opy_ (u"ࠦࡺࡹࡥࡳࠤᰠ"): bstack111l11l1l11_opy_
                })
            result[bstack1l1_opy_ (u"ࠧࡧࡵࡵࡪࡲࡶࡸࠨᰡ")] = list(bstack1111ll11ll1_opy_)
            result[bstack1l1_opy_ (u"ࠨࡣࡰ࡯ࡰ࡭ࡹࡓࡥࡴࡵࡤ࡫ࡪࡹࠢᰢ")] = bstack111l11llll1_opy_
            result[bstack1l1_opy_ (u"ࠢࡱࡴࡇࡥࡹ࡫ࠢᰣ")] = bstack1111lllll1l_opy_.committed_datetime.strftime(bstack1l1_opy_ (u"ࠣࠧ࡜࠱ࠪࡳ࠭ࠦࡦࠥᰤ"))
            if (not result[bstack1l1_opy_ (u"ࠤࡳࡶ࡙࡯ࡴ࡭ࡧࠥᰥ")] or result[bstack1l1_opy_ (u"ࠥࡴࡷ࡚ࡩࡵ࡮ࡨࠦᰦ")].strip() == bstack1l1_opy_ (u"ࠦࠧᰧ")) and bstack1111lllll1l_opy_.message:
                bstack111l1ll1111_opy_ = bstack1111lllll1l_opy_.message.strip().splitlines()
                result[bstack1l1_opy_ (u"ࠧࡶࡲࡕ࡫ࡷࡰࡪࠨᰨ")] = bstack111l1ll1111_opy_[0] if bstack111l1ll1111_opy_ else bstack1l1_opy_ (u"ࠨࠢᰩ")
                if len(bstack111l1ll1111_opy_) > 2:
                    result[bstack1l1_opy_ (u"ࠢࡱࡴࡇࡩࡸࡩࡲࡪࡲࡷ࡭ࡴࡴࠢᰪ")] = bstack1l1_opy_ (u"ࠨ࡞ࡱࠫᰫ").join(bstack111l1ll1111_opy_[2:]).strip()
            results.append(result)
        except Exception as err:
            logger.error(bstack1l1_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡲࡲࡴࡺࡲࡡࡵ࡫ࡱ࡫ࠥࡍࡩࡵࠢࡰࡩࡹࡧࡤࡢࡶࡤࠤ࡫ࡵࡲࠡࡃࡌࠤࡸ࡫࡬ࡦࡥࡷ࡭ࡴࡴࠠࠩࡨࡲࡰࡩ࡫ࡲ࠻ࠢࡾࢁ࠮ࡀࠠࡼࡿࠣ࠱ࠥࢁࡽࠣᰬ").format(
                folder,
                type(err).__name__,
                str(err)
            ))
            logger.error(bstack1l1_opy_ (u"ࠥࡊࡺࡲ࡬ࠡࡶࡵࡥࡨ࡫ࡢࡢࡥ࡮࠾ࠥࢁࡽࠣᰭ").format(traceback.format_exc()))
    filtered_results = [
        result
        for result in results
        if _111l11ll1l1_opy_(result)
    ]
    return filtered_results
def _111l11ll1l1_opy_(result):
    bstack1l1_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࡍ࡫࡬ࡱࡧࡵࠤࡹࡵࠠࡤࡪࡨࡧࡰࠦࡩࡧࠢࡤࠤ࡬࡯ࡴࠡ࡯ࡨࡸࡦࡪࡡࡵࡣࠣࡶࡪࡹࡵ࡭ࡶࠣ࡭ࡸࠦࡶࡢ࡮࡬ࡨࠥ࠮࡮ࡰࡰ࠰ࡩࡲࡶࡴࡺࠢࡩ࡭ࡱ࡫ࡳࡄࡪࡤࡲ࡬࡫ࡤࠡࡣࡱࡨࠥࡧࡵࡵࡪࡲࡶࡸ࠯࠮ࠋࠢࠣࠤࠥࠨࠢࠣᰮ")
    return (
        isinstance(result.get(bstack1l1_opy_ (u"ࠧ࡬ࡩ࡭ࡧࡶࡇ࡭ࡧ࡮ࡨࡧࡧࠦᰯ"), None), list)
        and len(result[bstack1l1_opy_ (u"ࠨࡦࡪ࡮ࡨࡷࡈ࡮ࡡ࡯ࡩࡨࡨࠧᰰ")]) > 0
        and isinstance(result.get(bstack1l1_opy_ (u"ࠢࡢࡷࡷ࡬ࡴࡸࡳࠣᰱ"), None), list)
        and len(result[bstack1l1_opy_ (u"ࠣࡣࡸࡸ࡭ࡵࡲࡴࠤᰲ")]) > 0
    )
def _1111l1ll111_opy_(repo):
    bstack1l1_opy_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࡗࡶࡾࠦࡴࡰࠢࡧࡩࡹ࡫ࡲ࡮࡫ࡱࡩࠥࡺࡨࡦࠢࡥࡥࡸ࡫ࠠࡣࡴࡤࡲࡨ࡮ࠠࡧࡱࡵࠤࡹ࡮ࡥࠡࡩ࡬ࡺࡪࡴࠠࡳࡧࡳࡳࠥࡽࡩࡵࡪࡲࡹࡹࠦࡨࡢࡴࡧࡧࡴࡪࡥࡥࠢࡱࡥࡲ࡫ࡳࠡࡣࡱࡨࠥࡽ࡯ࡳ࡭ࠣࡻ࡮ࡺࡨࠡࡣ࡯ࡰࠥ࡜ࡃࡔࠢࡳࡶࡴࡼࡩࡥࡧࡵࡷ࠳ࠐࠠࠡࠢࠣࡖࡪࡺࡵࡳࡰࡶࠤࡹ࡮ࡥࠡࡦࡨࡪࡦࡻ࡬ࡵࠢࡥࡶࡦࡴࡣࡩࠢ࡬ࡪࠥࡶ࡯ࡴࡵ࡬ࡦࡱ࡫ࠬࠡࡧ࡯ࡷࡪࠦࡎࡰࡰࡨ࠲ࠏࠦࠠࠡࠢࠥࠦࠧᰳ")
    try:
        try:
            origin = repo.remotes.origin
            bstack111l11111ll_opy_ = origin.refs[bstack1l1_opy_ (u"ࠪࡌࡊࡇࡄࠨᰴ")]
            target = bstack111l11111ll_opy_.reference.name
            if target.startswith(bstack1l1_opy_ (u"ࠫࡴࡸࡩࡨ࡫ࡱ࠳ࠬᰵ")):
                return target
        except Exception:
            pass
        if repo.remotes and repo.remotes.origin.refs:
            for ref in repo.remotes.origin.refs:
                if ref.name.startswith(bstack1l1_opy_ (u"ࠬࡵࡲࡪࡩ࡬ࡲ࠴࠭ᰶ")):
                    return ref.name
        if repo.heads:
            return repo.heads[0].name
    except Exception:
        pass
    return None
def _111l111111l_opy_(commits):
    bstack1l1_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࡇࡦࡶࠣࡰ࡮ࡹࡴࠡࡱࡩࠤࡨ࡮ࡡ࡯ࡩࡨࡨࠥ࡬ࡩ࡭ࡧࡶࠤ࡫ࡸ࡯࡮ࠢࡤࠤࡱ࡯ࡳࡵࠢࡲࡪࠥࡩ࡯࡮࡯࡬ࡸࡸ࠴ࠊࠡࠢࠣࠤࠧࠨ᰷ࠢ")
    bstack1111l1lll11_opy_ = set()
    try:
        for commit in commits:
            if commit.parents:
                for parent in commit.parents:
                    diff = commit.diff(parent)
                    for bstack111l111ll1l_opy_ in diff:
                        if bstack111l111ll1l_opy_.a_path:
                            bstack1111l1lll11_opy_.add(bstack111l111ll1l_opy_.a_path)
                        if bstack111l111ll1l_opy_.b_path:
                            bstack1111l1lll11_opy_.add(bstack111l111ll1l_opy_.b_path)
    except Exception:
        pass
    return list(bstack1111l1lll11_opy_)
def bstack1111llll11l_opy_(bstack111l1l1lll1_opy_):
    bstack111l111llll_opy_ = bstack111l1l1111l_opy_(bstack111l1l1lll1_opy_)
    if bstack111l111llll_opy_ and bstack111l111llll_opy_ > bstack11l1l11l11l_opy_:
        bstack1111lllll11_opy_ = bstack111l111llll_opy_ - bstack11l1l11l11l_opy_
        bstack111l111l1l1_opy_ = bstack111l111l111_opy_(bstack111l1l1lll1_opy_[bstack1l1_opy_ (u"ࠢࡤࡱࡰࡱ࡮ࡺ࡟࡮ࡧࡶࡷࡦ࡭ࡥࠣ᰸")], bstack1111lllll11_opy_)
        bstack111l1l1lll1_opy_[bstack1l1_opy_ (u"ࠣࡥࡲࡱࡲ࡯ࡴࡠ࡯ࡨࡷࡸࡧࡧࡦࠤ᰹")] = bstack111l111l1l1_opy_
        logger.info(bstack1l1_opy_ (u"ࠤࡗ࡬ࡪࠦࡣࡰ࡯ࡰ࡭ࡹࠦࡨࡢࡵࠣࡦࡪ࡫࡮ࠡࡶࡵࡹࡳࡩࡡࡵࡧࡧ࠲࡙ࠥࡩࡻࡧࠣࡳ࡫ࠦࡣࡰ࡯ࡰ࡭ࡹࠦࡡࡧࡶࡨࡶࠥࡺࡲࡶࡰࡦࡥࡹ࡯࡯࡯ࠢ࡬ࡷࠥࢁࡽࠡࡍࡅࠦ᰺")
                    .format(bstack111l1l1111l_opy_(bstack111l1l1lll1_opy_) / 1024))
    return bstack111l1l1lll1_opy_
def bstack111l1l1111l_opy_(json_data):
    try:
        if json_data:
            bstack1111l1lll1l_opy_ = json.dumps(json_data)
            bstack1111ll111ll_opy_ = sys.getsizeof(bstack1111l1lll1l_opy_)
            return bstack1111ll111ll_opy_
    except Exception as e:
        logger.debug(bstack1l1_opy_ (u"ࠥࡗࡴࡳࡥࡵࡪ࡬ࡲ࡬ࠦࡷࡦࡰࡷࠤࡼࡸ࡯࡯ࡩࠣࡻ࡭࡯࡬ࡦࠢࡦࡥࡱࡩࡵ࡭ࡣࡷ࡭ࡳ࡭ࠠࡴ࡫ࡽࡩࠥࡵࡦࠡࡌࡖࡓࡓࠦ࡯ࡣ࡬ࡨࡧࡹࡀࠠࡼࡿࠥ᰻").format(e))
    return -1
def bstack111l111l111_opy_(field, bstack1111lll1l1l_opy_):
    try:
        bstack1111ll1llll_opy_ = len(bytes(bstack11l11llllll_opy_, bstack1l1_opy_ (u"ࠫࡺࡺࡦ࠮࠺ࠪ᰼")))
        bstack1111l11llll_opy_ = bytes(field, bstack1l1_opy_ (u"ࠬࡻࡴࡧ࠯࠻ࠫ᰽"))
        bstack1111llll1l1_opy_ = len(bstack1111l11llll_opy_)
        bstack111l111l11l_opy_ = ceil(bstack1111llll1l1_opy_ - bstack1111lll1l1l_opy_ - bstack1111ll1llll_opy_)
        if bstack111l111l11l_opy_ > 0:
            bstack1111l11ll1l_opy_ = bstack1111l11llll_opy_[:bstack111l111l11l_opy_].decode(bstack1l1_opy_ (u"࠭ࡵࡵࡨ࠰࠼ࠬ᰾"), errors=bstack1l1_opy_ (u"ࠧࡪࡩࡱࡳࡷ࡫ࠧ᰿")) + bstack11l11llllll_opy_
            return bstack1111l11ll1l_opy_
    except Exception as e:
        logger.debug(bstack1l1_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡸࡪ࡬ࡰࡪࠦࡴࡳࡷࡱࡧࡦࡺࡩ࡯ࡩࠣࡪ࡮࡫࡬ࡥ࠮ࠣࡲࡴࡺࡨࡪࡰࡪࠤࡼࡧࡳࠡࡶࡵࡹࡳࡩࡡࡵࡧࡧࠤ࡭࡫ࡲࡦ࠼ࠣࡿࢂࠨ᱀").format(e))
    return field
def bstack1ll11llll_opy_():
    env = os.environ
    if (bstack1l1_opy_ (u"ࠤࡍࡉࡓࡑࡉࡏࡕࡢ࡙ࡗࡒࠢ᱁") in env and len(env[bstack1l1_opy_ (u"ࠥࡎࡊࡔࡋࡊࡐࡖࡣ࡚ࡘࡌࠣ᱂")]) > 0) or (
            bstack1l1_opy_ (u"ࠦࡏࡋࡎࡌࡋࡑࡗࡤࡎࡏࡎࡇࠥ᱃") in env and len(env[bstack1l1_opy_ (u"ࠧࡐࡅࡏࡍࡌࡒࡘࡥࡈࡐࡏࡈࠦ᱄")]) > 0):
        return {
            bstack1l1_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦ᱅"): bstack1l1_opy_ (u"ࠢࡋࡧࡱ࡯࡮ࡴࡳࠣ᱆"),
            bstack1l1_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦ᱇"): env.get(bstack1l1_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡠࡗࡕࡐࠧ᱈")),
            bstack1l1_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧ᱉"): env.get(bstack1l1_opy_ (u"ࠦࡏࡕࡂࡠࡐࡄࡑࡊࠨ᱊")),
            bstack1l1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦ᱋"): env.get(bstack1l1_opy_ (u"ࠨࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࠧ᱌"))
        }
    if env.get(bstack1l1_opy_ (u"ࠢࡄࡋࠥᱍ")) == bstack1l1_opy_ (u"ࠣࡶࡵࡹࡪࠨᱎ") and bstack1ll1111ll1_opy_(env.get(bstack1l1_opy_ (u"ࠤࡆࡍࡗࡉࡌࡆࡅࡌࠦᱏ"))):
        return {
            bstack1l1_opy_ (u"ࠥࡲࡦࡳࡥࠣ᱐"): bstack1l1_opy_ (u"ࠦࡈ࡯ࡲࡤ࡮ࡨࡇࡎࠨ᱑"),
            bstack1l1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣ᱒"): env.get(bstack1l1_opy_ (u"ࠨࡃࡊࡔࡆࡐࡊࡥࡂࡖࡋࡏࡈࡤ࡛ࡒࡍࠤ᱓")),
            bstack1l1_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤ᱔"): env.get(bstack1l1_opy_ (u"ࠣࡅࡌࡖࡈࡒࡅࡠࡌࡒࡆࠧ᱕")),
            bstack1l1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣ᱖"): env.get(bstack1l1_opy_ (u"ࠥࡇࡎࡘࡃࡍࡇࡢࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࠨ᱗"))
        }
    if env.get(bstack1l1_opy_ (u"ࠦࡈࡏࠢ᱘")) == bstack1l1_opy_ (u"ࠧࡺࡲࡶࡧࠥ᱙") and bstack1ll1111ll1_opy_(env.get(bstack1l1_opy_ (u"ࠨࡔࡓࡃ࡙ࡍࡘࠨᱚ"))):
        return {
            bstack1l1_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᱛ"): bstack1l1_opy_ (u"ࠣࡖࡵࡥࡻ࡯ࡳࠡࡅࡌࠦᱜ"),
            bstack1l1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᱝ"): env.get(bstack1l1_opy_ (u"ࠥࡘࡗࡇࡖࡊࡕࡢࡆ࡚ࡏࡌࡅࡡ࡚ࡉࡇࡥࡕࡓࡎࠥᱞ")),
            bstack1l1_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᱟ"): env.get(bstack1l1_opy_ (u"࡚ࠧࡒࡂࡘࡌࡗࡤࡐࡏࡃࡡࡑࡅࡒࡋࠢᱠ")),
            bstack1l1_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᱡ"): env.get(bstack1l1_opy_ (u"ࠢࡕࡔࡄ࡚ࡎ࡙࡟ࡃࡗࡌࡐࡉࡥࡎࡖࡏࡅࡉࡗࠨᱢ"))
        }
    if env.get(bstack1l1_opy_ (u"ࠣࡅࡌࠦᱣ")) == bstack1l1_opy_ (u"ࠤࡷࡶࡺ࡫ࠢᱤ") and env.get(bstack1l1_opy_ (u"ࠥࡇࡎࡥࡎࡂࡏࡈࠦᱥ")) == bstack1l1_opy_ (u"ࠦࡨࡵࡤࡦࡵ࡫࡭ࡵࠨᱦ"):
        return {
            bstack1l1_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᱧ"): bstack1l1_opy_ (u"ࠨࡃࡰࡦࡨࡷ࡭࡯ࡰࠣᱨ"),
            bstack1l1_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᱩ"): None,
            bstack1l1_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᱪ"): None,
            bstack1l1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᱫ"): None
        }
    if env.get(bstack1l1_opy_ (u"ࠥࡆࡎ࡚ࡂࡖࡅࡎࡉ࡙ࡥࡂࡓࡃࡑࡇࡍࠨᱬ")) and env.get(bstack1l1_opy_ (u"ࠦࡇࡏࡔࡃࡗࡆࡏࡊ࡚࡟ࡄࡑࡐࡑࡎ࡚ࠢᱭ")):
        return {
            bstack1l1_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᱮ"): bstack1l1_opy_ (u"ࠨࡂࡪࡶࡥࡹࡨࡱࡥࡵࠤᱯ"),
            bstack1l1_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᱰ"): env.get(bstack1l1_opy_ (u"ࠣࡄࡌࡘࡇ࡛ࡃࡌࡇࡗࡣࡌࡏࡔࡠࡊࡗࡘࡕࡥࡏࡓࡋࡊࡍࡓࠨᱱ")),
            bstack1l1_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᱲ"): None,
            bstack1l1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤᱳ"): env.get(bstack1l1_opy_ (u"ࠦࡇࡏࡔࡃࡗࡆࡏࡊ࡚࡟ࡃࡗࡌࡐࡉࡥࡎࡖࡏࡅࡉࡗࠨᱴ"))
        }
    if env.get(bstack1l1_opy_ (u"ࠧࡉࡉࠣᱵ")) == bstack1l1_opy_ (u"ࠨࡴࡳࡷࡨࠦᱶ") and bstack1ll1111ll1_opy_(env.get(bstack1l1_opy_ (u"ࠢࡅࡔࡒࡒࡊࠨᱷ"))):
        return {
            bstack1l1_opy_ (u"ࠣࡰࡤࡱࡪࠨᱸ"): bstack1l1_opy_ (u"ࠤࡇࡶࡴࡴࡥࠣᱹ"),
            bstack1l1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᱺ"): env.get(bstack1l1_opy_ (u"ࠦࡉࡘࡏࡏࡇࡢࡆ࡚ࡏࡌࡅࡡࡏࡍࡓࡑࠢᱻ")),
            bstack1l1_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᱼ"): None,
            bstack1l1_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᱽ"): env.get(bstack1l1_opy_ (u"ࠢࡅࡔࡒࡒࡊࡥࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࠧ᱾"))
        }
    if env.get(bstack1l1_opy_ (u"ࠣࡅࡌࠦ᱿")) == bstack1l1_opy_ (u"ࠤࡷࡶࡺ࡫ࠢᲀ") and bstack1ll1111ll1_opy_(env.get(bstack1l1_opy_ (u"ࠥࡗࡊࡓࡁࡑࡊࡒࡖࡊࠨᲁ"))):
        return {
            bstack1l1_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᲂ"): bstack1l1_opy_ (u"࡙ࠧࡥ࡮ࡣࡳ࡬ࡴࡸࡥࠣᲃ"),
            bstack1l1_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᲄ"): env.get(bstack1l1_opy_ (u"ࠢࡔࡇࡐࡅࡕࡎࡏࡓࡇࡢࡓࡗࡍࡁࡏࡋ࡝ࡅ࡙ࡏࡏࡏࡡࡘࡖࡑࠨᲅ")),
            bstack1l1_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᲆ"): env.get(bstack1l1_opy_ (u"ࠤࡖࡉࡒࡇࡐࡉࡑࡕࡉࡤࡐࡏࡃࡡࡑࡅࡒࡋࠢᲇ")),
            bstack1l1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤᲈ"): env.get(bstack1l1_opy_ (u"ࠦࡘࡋࡍࡂࡒࡋࡓࡗࡋ࡟ࡋࡑࡅࡣࡎࡊࠢᲉ"))
        }
    if env.get(bstack1l1_opy_ (u"ࠧࡉࡉࠣᲊ")) == bstack1l1_opy_ (u"ࠨࡴࡳࡷࡨࠦ᲋") and bstack1ll1111ll1_opy_(env.get(bstack1l1_opy_ (u"ࠢࡈࡋࡗࡐࡆࡈ࡟ࡄࡋࠥ᲌"))):
        return {
            bstack1l1_opy_ (u"ࠣࡰࡤࡱࡪࠨ᲍"): bstack1l1_opy_ (u"ࠤࡊ࡭ࡹࡒࡡࡣࠤ᲎"),
            bstack1l1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨ᲏"): env.get(bstack1l1_opy_ (u"ࠦࡈࡏ࡟ࡋࡑࡅࡣ࡚ࡘࡌࠣᲐ")),
            bstack1l1_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᲑ"): env.get(bstack1l1_opy_ (u"ࠨࡃࡊࡡࡍࡓࡇࡥࡎࡂࡏࡈࠦᲒ")),
            bstack1l1_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᲓ"): env.get(bstack1l1_opy_ (u"ࠣࡅࡌࡣࡏࡕࡂࡠࡋࡇࠦᲔ"))
        }
    if env.get(bstack1l1_opy_ (u"ࠤࡆࡍࠧᲕ")) == bstack1l1_opy_ (u"ࠥࡸࡷࡻࡥࠣᲖ") and bstack1ll1111ll1_opy_(env.get(bstack1l1_opy_ (u"ࠦࡇ࡛ࡉࡍࡆࡎࡍ࡙ࡋࠢᲗ"))):
        return {
            bstack1l1_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᲘ"): bstack1l1_opy_ (u"ࠨࡂࡶ࡫࡯ࡨࡰ࡯ࡴࡦࠤᲙ"),
            bstack1l1_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᲚ"): env.get(bstack1l1_opy_ (u"ࠣࡄࡘࡍࡑࡊࡋࡊࡖࡈࡣࡇ࡛ࡉࡍࡆࡢ࡙ࡗࡒࠢᲛ")),
            bstack1l1_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᲜ"): env.get(bstack1l1_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡍࡌࡘࡊࡥࡌࡂࡄࡈࡐࠧᲝ")) or env.get(bstack1l1_opy_ (u"ࠦࡇ࡛ࡉࡍࡆࡎࡍ࡙ࡋ࡟ࡑࡋࡓࡉࡑࡏࡎࡆࡡࡑࡅࡒࡋࠢᲞ")),
            bstack1l1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᲟ"): env.get(bstack1l1_opy_ (u"ࠨࡂࡖࡋࡏࡈࡐࡏࡔࡆࡡࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࡇࡋࡒࠣᲠ"))
        }
    if bstack1ll1111ll1_opy_(env.get(bstack1l1_opy_ (u"ࠢࡕࡈࡢࡆ࡚ࡏࡌࡅࠤᲡ"))):
        return {
            bstack1l1_opy_ (u"ࠣࡰࡤࡱࡪࠨᲢ"): bstack1l1_opy_ (u"ࠤ࡙࡭ࡸࡻࡡ࡭ࠢࡖࡸࡺࡪࡩࡰࠢࡗࡩࡦࡳࠠࡔࡧࡵࡺ࡮ࡩࡥࡴࠤᲣ"),
            bstack1l1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᲤ"): bstack1l1_opy_ (u"ࠦࢀࢃࡻࡾࠤᲥ").format(env.get(bstack1l1_opy_ (u"࡙࡙ࠬࡔࡖࡈࡑࡤ࡚ࡅࡂࡏࡉࡓ࡚ࡔࡄࡂࡖࡌࡓࡓ࡙ࡅࡓࡘࡈࡖ࡚ࡘࡉࠨᲦ")), env.get(bstack1l1_opy_ (u"࠭ࡓ࡚ࡕࡗࡉࡒࡥࡔࡆࡃࡐࡔࡗࡕࡊࡆࡅࡗࡍࡉ࠭Ყ"))),
            bstack1l1_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᲨ"): env.get(bstack1l1_opy_ (u"ࠣࡕ࡜ࡗ࡙ࡋࡍࡠࡆࡈࡊࡎࡔࡉࡕࡋࡒࡒࡎࡊࠢᲩ")),
            bstack1l1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᲪ"): env.get(bstack1l1_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡡࡅ࡙ࡎࡒࡄࡊࡆࠥᲫ"))
        }
    if bstack1ll1111ll1_opy_(env.get(bstack1l1_opy_ (u"ࠦࡆࡖࡐࡗࡇ࡜ࡓࡗࠨᲬ"))):
        return {
            bstack1l1_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᲭ"): bstack1l1_opy_ (u"ࠨࡁࡱࡲࡹࡩࡾࡵࡲࠣᲮ"),
            bstack1l1_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᲯ"): bstack1l1_opy_ (u"ࠣࡽࢀ࠳ࡵࡸ࡯࡫ࡧࡦࡸ࠴ࢁࡽ࠰ࡽࢀ࠳ࡧࡻࡩ࡭ࡦࡶ࠳ࢀࢃࠢᲰ").format(env.get(bstack1l1_opy_ (u"ࠩࡄࡔࡕ࡜ࡅ࡚ࡑࡕࡣ࡚ࡘࡌࠨᲱ")), env.get(bstack1l1_opy_ (u"ࠪࡅࡕࡖࡖࡆ࡛ࡒࡖࡤࡇࡃࡄࡑࡘࡒ࡙ࡥࡎࡂࡏࡈࠫᲲ")), env.get(bstack1l1_opy_ (u"ࠫࡆࡖࡐࡗࡇ࡜ࡓࡗࡥࡐࡓࡑࡍࡉࡈ࡚࡟ࡔࡎࡘࡋࠬᲳ")), env.get(bstack1l1_opy_ (u"ࠬࡇࡐࡑࡘࡈ࡝ࡔࡘ࡟ࡃࡗࡌࡐࡉࡥࡉࡅࠩᲴ"))),
            bstack1l1_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᲵ"): env.get(bstack1l1_opy_ (u"ࠢࡂࡒࡓ࡚ࡊ࡟ࡏࡓࡡࡍࡓࡇࡥࡎࡂࡏࡈࠦᲶ")),
            bstack1l1_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᲷ"): env.get(bstack1l1_opy_ (u"ࠤࡄࡔࡕ࡜ࡅ࡚ࡑࡕࡣࡇ࡛ࡉࡍࡆࡢࡒ࡚ࡓࡂࡆࡔࠥᲸ"))
        }
    if env.get(bstack1l1_opy_ (u"ࠥࡅ࡟࡛ࡒࡆࡡࡋࡘ࡙ࡖ࡟ࡖࡕࡈࡖࡤࡇࡇࡆࡐࡗࠦᲹ")) and env.get(bstack1l1_opy_ (u"࡙ࠦࡌ࡟ࡃࡗࡌࡐࡉࠨᲺ")):
        return {
            bstack1l1_opy_ (u"ࠧࡴࡡ࡮ࡧࠥ᲻"): bstack1l1_opy_ (u"ࠨࡁࡻࡷࡵࡩࠥࡉࡉࠣ᲼"),
            bstack1l1_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᲽ"): bstack1l1_opy_ (u"ࠣࡽࢀࡿࢂ࠵࡟ࡣࡷ࡬ࡰࡩ࠵ࡲࡦࡵࡸࡰࡹࡹ࠿ࡣࡷ࡬ࡰࡩࡏࡤ࠾ࡽࢀࠦᲾ").format(env.get(bstack1l1_opy_ (u"ࠩࡖ࡝ࡘ࡚ࡅࡎࡡࡗࡉࡆࡓࡆࡐࡗࡑࡈࡆ࡚ࡉࡐࡐࡖࡉࡗ࡜ࡅࡓࡗࡕࡍࠬᲿ")), env.get(bstack1l1_opy_ (u"ࠪࡗ࡞࡙ࡔࡆࡏࡢࡘࡊࡇࡍࡑࡔࡒࡎࡊࡉࡔࠨ᳀")), env.get(bstack1l1_opy_ (u"ࠫࡇ࡛ࡉࡍࡆࡢࡆ࡚ࡏࡌࡅࡋࡇࠫ᳁"))),
            bstack1l1_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢ᳂"): env.get(bstack1l1_opy_ (u"ࠨࡂࡖࡋࡏࡈࡤࡈࡕࡊࡎࡇࡍࡉࠨ᳃")),
            bstack1l1_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨ᳄"): env.get(bstack1l1_opy_ (u"ࠣࡄࡘࡍࡑࡊ࡟ࡃࡗࡌࡐࡉࡏࡄࠣ᳅"))
        }
    if any([env.get(bstack1l1_opy_ (u"ࠤࡆࡓࡉࡋࡂࡖࡋࡏࡈࡤࡈࡕࡊࡎࡇࡣࡎࡊࠢ᳆")), env.get(bstack1l1_opy_ (u"ࠥࡇࡔࡊࡅࡃࡗࡌࡐࡉࡥࡒࡆࡕࡒࡐ࡛ࡋࡄࡠࡕࡒ࡙ࡗࡉࡅࡠࡘࡈࡖࡘࡏࡏࡏࠤ᳇")), env.get(bstack1l1_opy_ (u"ࠦࡈࡕࡄࡆࡄࡘࡍࡑࡊ࡟ࡔࡑࡘࡖࡈࡋ࡟ࡗࡇࡕࡗࡎࡕࡎࠣ᳈"))]):
        return {
            bstack1l1_opy_ (u"ࠧࡴࡡ࡮ࡧࠥ᳉"): bstack1l1_opy_ (u"ࠨࡁࡘࡕࠣࡇࡴࡪࡥࡃࡷ࡬ࡰࡩࠨ᳊"),
            bstack1l1_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥ᳋"): env.get(bstack1l1_opy_ (u"ࠣࡅࡒࡈࡊࡈࡕࡊࡎࡇࡣࡕ࡛ࡂࡍࡋࡆࡣࡇ࡛ࡉࡍࡆࡢ࡙ࡗࡒࠢ᳌")),
            bstack1l1_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦ᳍"): env.get(bstack1l1_opy_ (u"ࠥࡇࡔࡊࡅࡃࡗࡌࡐࡉࡥࡂࡖࡋࡏࡈࡤࡏࡄࠣ᳎")),
            bstack1l1_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥ᳏"): env.get(bstack1l1_opy_ (u"ࠧࡉࡏࡅࡇࡅ࡙ࡎࡒࡄࡠࡄࡘࡍࡑࡊ࡟ࡊࡆࠥ᳐"))
        }
    if env.get(bstack1l1_opy_ (u"ࠨࡢࡢ࡯ࡥࡳࡴࡥࡢࡶ࡫࡯ࡨࡓࡻ࡭ࡣࡧࡵࠦ᳑")):
        return {
            bstack1l1_opy_ (u"ࠢ࡯ࡣࡰࡩࠧ᳒"): bstack1l1_opy_ (u"ࠣࡄࡤࡱࡧࡵ࡯ࠣ᳓"),
            bstack1l1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰ᳔ࠧ"): env.get(bstack1l1_opy_ (u"ࠥࡦࡦࡳࡢࡰࡱࡢࡦࡺ࡯࡬ࡥࡔࡨࡷࡺࡲࡴࡴࡗࡵࡰ᳕ࠧ")),
            bstack1l1_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨ᳖"): env.get(bstack1l1_opy_ (u"ࠧࡨࡡ࡮ࡤࡲࡳࡤࡹࡨࡰࡴࡷࡎࡴࡨࡎࡢ࡯ࡨ᳗ࠦ")),
            bstack1l1_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶ᳘ࠧ"): env.get(bstack1l1_opy_ (u"ࠢࡣࡣࡰࡦࡴࡵ࡟ࡣࡷ࡬ࡰࡩࡔࡵ࡮ࡤࡨࡶ᳙ࠧ"))
        }
    if env.get(bstack1l1_opy_ (u"࡙ࠣࡈࡖࡈࡑࡅࡓࠤ᳚")) or env.get(bstack1l1_opy_ (u"ࠤ࡚ࡉࡗࡉࡋࡆࡔࡢࡑࡆࡏࡎࡠࡒࡌࡔࡊࡒࡉࡏࡇࡢࡗ࡙ࡇࡒࡕࡇࡇࠦ᳛")):
        return {
            bstack1l1_opy_ (u"ࠥࡲࡦࡳࡥ᳜ࠣ"): bstack1l1_opy_ (u"ࠦ࡜࡫ࡲࡤ࡭ࡨࡶ᳝ࠧ"),
            bstack1l1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬᳞ࠣ"): env.get(bstack1l1_opy_ (u"ࠨࡗࡆࡔࡆࡏࡊࡘ࡟ࡃࡗࡌࡐࡉࡥࡕࡓࡎ᳟ࠥ")),
            bstack1l1_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤ᳠"): bstack1l1_opy_ (u"ࠣࡏࡤ࡭ࡳࠦࡐࡪࡲࡨࡰ࡮ࡴࡥࠣ᳡") if env.get(bstack1l1_opy_ (u"ࠤ࡚ࡉࡗࡉࡋࡆࡔࡢࡑࡆࡏࡎࡠࡒࡌࡔࡊࡒࡉࡏࡇࡢࡗ࡙ࡇࡒࡕࡇࡇ᳢ࠦ")) else None,
            bstack1l1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤ᳣"): env.get(bstack1l1_opy_ (u"ࠦ࡜ࡋࡒࡄࡍࡈࡖࡤࡍࡉࡕࡡࡆࡓࡒࡓࡉࡕࠤ᳤"))
        }
    if any([env.get(bstack1l1_opy_ (u"ࠧࡍࡃࡑࡡࡓࡖࡔࡐࡅࡄࡖ᳥ࠥ")), env.get(bstack1l1_opy_ (u"ࠨࡇࡄࡎࡒ࡙ࡉࡥࡐࡓࡑࡍࡉࡈ᳦࡚ࠢ")), env.get(bstack1l1_opy_ (u"ࠢࡈࡑࡒࡋࡑࡋ࡟ࡄࡎࡒ࡙ࡉࡥࡐࡓࡑࡍࡉࡈ᳧࡚ࠢ"))]):
        return {
            bstack1l1_opy_ (u"ࠣࡰࡤࡱࡪࠨ᳨"): bstack1l1_opy_ (u"ࠤࡊࡳࡴ࡭࡬ࡦࠢࡆࡰࡴࡻࡤࠣᳩ"),
            bstack1l1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᳪ"): None,
            bstack1l1_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᳫ"): env.get(bstack1l1_opy_ (u"ࠧࡖࡒࡐࡌࡈࡇ࡙ࡥࡉࡅࠤᳬ")),
            bstack1l1_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶ᳭ࠧ"): env.get(bstack1l1_opy_ (u"ࠢࡃࡗࡌࡐࡉࡥࡉࡅࠤᳮ"))
        }
    if env.get(bstack1l1_opy_ (u"ࠣࡕࡋࡍࡕࡖࡁࡃࡎࡈࠦᳯ")):
        return {
            bstack1l1_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᳰ"): bstack1l1_opy_ (u"ࠥࡗ࡭࡯ࡰࡱࡣࡥࡰࡪࠨᳱ"),
            bstack1l1_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᳲ"): env.get(bstack1l1_opy_ (u"࡙ࠧࡈࡊࡒࡓࡅࡇࡒࡅࡠࡄࡘࡍࡑࡊ࡟ࡖࡔࡏࠦᳳ")),
            bstack1l1_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣ᳴"): bstack1l1_opy_ (u"ࠢࡋࡱࡥࠤࠨࢁࡽࠣᳵ").format(env.get(bstack1l1_opy_ (u"ࠨࡕࡋࡍࡕࡖࡁࡃࡎࡈࡣࡏࡕࡂࡠࡋࡇࠫᳶ"))) if env.get(bstack1l1_opy_ (u"ࠤࡖࡌࡎࡖࡐࡂࡄࡏࡉࡤࡐࡏࡃࡡࡌࡈࠧ᳷")) else None,
            bstack1l1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤ᳸"): env.get(bstack1l1_opy_ (u"ࠦࡘࡎࡉࡑࡒࡄࡆࡑࡋ࡟ࡃࡗࡌࡐࡉࡥࡎࡖࡏࡅࡉࡗࠨ᳹"))
        }
    if bstack1ll1111ll1_opy_(env.get(bstack1l1_opy_ (u"ࠧࡔࡅࡕࡎࡌࡊ࡞ࠨᳺ"))):
        return {
            bstack1l1_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦ᳻"): bstack1l1_opy_ (u"ࠢࡏࡧࡷࡰ࡮࡬ࡹࠣ᳼"),
            bstack1l1_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦ᳽"): env.get(bstack1l1_opy_ (u"ࠤࡇࡉࡕࡒࡏ࡚ࡡࡘࡖࡑࠨ᳾")),
            bstack1l1_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧ᳿"): env.get(bstack1l1_opy_ (u"ࠦࡘࡏࡔࡆࡡࡑࡅࡒࡋࠢᴀ")),
            bstack1l1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᴁ"): env.get(bstack1l1_opy_ (u"ࠨࡂࡖࡋࡏࡈࡤࡏࡄࠣᴂ"))
        }
    if bstack1ll1111ll1_opy_(env.get(bstack1l1_opy_ (u"ࠢࡈࡋࡗࡌ࡚ࡈ࡟ࡂࡅࡗࡍࡔࡔࡓࠣᴃ"))):
        return {
            bstack1l1_opy_ (u"ࠣࡰࡤࡱࡪࠨᴄ"): bstack1l1_opy_ (u"ࠤࡊ࡭ࡹࡎࡵࡣࠢࡄࡧࡹ࡯࡯࡯ࡵࠥᴅ"),
            bstack1l1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᴆ"): bstack1l1_opy_ (u"ࠦࢀࢃ࠯ࡼࡿ࠲ࡥࡨࡺࡩࡰࡰࡶ࠳ࡷࡻ࡮ࡴ࠱ࡾࢁࠧᴇ").format(env.get(bstack1l1_opy_ (u"ࠬࡍࡉࡕࡊࡘࡆࡤ࡙ࡅࡓࡘࡈࡖࡤ࡛ࡒࡍࠩᴈ")), env.get(bstack1l1_opy_ (u"࠭ࡇࡊࡖࡋ࡙ࡇࡥࡒࡆࡒࡒࡗࡎ࡚ࡏࡓ࡛ࠪᴉ")), env.get(bstack1l1_opy_ (u"ࠧࡈࡋࡗࡌ࡚ࡈ࡟ࡓࡗࡑࡣࡎࡊࠧᴊ"))),
            bstack1l1_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᴋ"): env.get(bstack1l1_opy_ (u"ࠤࡊࡍ࡙ࡎࡕࡃࡡ࡚ࡓࡗࡑࡆࡍࡑ࡚ࠦᴌ")),
            bstack1l1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤᴍ"): env.get(bstack1l1_opy_ (u"ࠦࡌࡏࡔࡉࡗࡅࡣࡗ࡛ࡎࡠࡋࡇࠦᴎ"))
        }
    if env.get(bstack1l1_opy_ (u"ࠧࡉࡉࠣᴏ")) == bstack1l1_opy_ (u"ࠨࡴࡳࡷࡨࠦᴐ") and env.get(bstack1l1_opy_ (u"ࠢࡗࡇࡕࡇࡊࡒࠢᴑ")) == bstack1l1_opy_ (u"ࠣ࠳ࠥᴒ"):
        return {
            bstack1l1_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᴓ"): bstack1l1_opy_ (u"࡚ࠥࡪࡸࡣࡦ࡮ࠥᴔ"),
            bstack1l1_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᴕ"): bstack1l1_opy_ (u"ࠧ࡮ࡴࡵࡲ࠽࠳࠴ࢁࡽࠣᴖ").format(env.get(bstack1l1_opy_ (u"࠭ࡖࡆࡔࡆࡉࡑࡥࡕࡓࡎࠪᴗ"))),
            bstack1l1_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᴘ"): None,
            bstack1l1_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᴙ"): None,
        }
    if env.get(bstack1l1_opy_ (u"ࠤࡗࡉࡆࡓࡃࡊࡖ࡜ࡣ࡛ࡋࡒࡔࡋࡒࡒࠧᴚ")):
        return {
            bstack1l1_opy_ (u"ࠥࡲࡦࡳࡥࠣᴛ"): bstack1l1_opy_ (u"࡙ࠦ࡫ࡡ࡮ࡥ࡬ࡸࡾࠨᴜ"),
            bstack1l1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣᴝ"): None,
            bstack1l1_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᴞ"): env.get(bstack1l1_opy_ (u"ࠢࡕࡇࡄࡑࡈࡏࡔ࡚ࡡࡓࡖࡔࡐࡅࡄࡖࡢࡒࡆࡓࡅࠣᴟ")),
            bstack1l1_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᴠ"): env.get(bstack1l1_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࡇࡋࡒࠣᴡ"))
        }
    if any([env.get(bstack1l1_opy_ (u"ࠥࡇࡔࡔࡃࡐࡗࡕࡗࡊࠨᴢ")), env.get(bstack1l1_opy_ (u"ࠦࡈࡕࡎࡄࡑࡘࡖࡘࡋ࡟ࡖࡔࡏࠦᴣ")), env.get(bstack1l1_opy_ (u"ࠧࡉࡏࡏࡅࡒ࡙ࡗ࡙ࡅࡠࡗࡖࡉࡗࡔࡁࡎࡇࠥᴤ")), env.get(bstack1l1_opy_ (u"ࠨࡃࡐࡐࡆࡓ࡚ࡘࡓࡆࡡࡗࡉࡆࡓࠢᴥ"))]):
        return {
            bstack1l1_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᴦ"): bstack1l1_opy_ (u"ࠣࡅࡲࡲࡨࡵࡵࡳࡵࡨࠦᴧ"),
            bstack1l1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᴨ"): None,
            bstack1l1_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᴩ"): env.get(bstack1l1_opy_ (u"ࠦࡇ࡛ࡉࡍࡆࡢࡎࡔࡈ࡟ࡏࡃࡐࡉࠧᴪ")) or None,
            bstack1l1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᴫ"): env.get(bstack1l1_opy_ (u"ࠨࡂࡖࡋࡏࡈࡤࡏࡄࠣᴬ"), 0)
        }
    if env.get(bstack1l1_opy_ (u"ࠢࡈࡑࡢࡎࡔࡈ࡟ࡏࡃࡐࡉࠧᴭ")):
        return {
            bstack1l1_opy_ (u"ࠣࡰࡤࡱࡪࠨᴮ"): bstack1l1_opy_ (u"ࠤࡊࡳࡈࡊࠢᴯ"),
            bstack1l1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᴰ"): None,
            bstack1l1_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᴱ"): env.get(bstack1l1_opy_ (u"ࠧࡍࡏࡠࡌࡒࡆࡤࡔࡁࡎࡇࠥᴲ")),
            bstack1l1_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᴳ"): env.get(bstack1l1_opy_ (u"ࠢࡈࡑࡢࡔࡎࡖࡅࡍࡋࡑࡉࡤࡉࡏࡖࡐࡗࡉࡗࠨᴴ"))
        }
    if env.get(bstack1l1_opy_ (u"ࠣࡅࡉࡣࡇ࡛ࡉࡍࡆࡢࡍࡉࠨᴵ")):
        return {
            bstack1l1_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᴶ"): bstack1l1_opy_ (u"ࠥࡇࡴࡪࡥࡇࡴࡨࡷ࡭ࠨᴷ"),
            bstack1l1_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᴸ"): env.get(bstack1l1_opy_ (u"ࠧࡉࡆࡠࡄࡘࡍࡑࡊ࡟ࡖࡔࡏࠦᴹ")),
            bstack1l1_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᴺ"): env.get(bstack1l1_opy_ (u"ࠢࡄࡈࡢࡔࡎࡖࡅࡍࡋࡑࡉࡤࡔࡁࡎࡇࠥᴻ")),
            bstack1l1_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᴼ"): env.get(bstack1l1_opy_ (u"ࠤࡆࡊࡤࡈࡕࡊࡎࡇࡣࡎࡊࠢᴽ"))
        }
    return {bstack1l1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤᴾ"): None}
def get_host_info():
    return {
        bstack1l1_opy_ (u"ࠦ࡭ࡵࡳࡵࡰࡤࡱࡪࠨᴿ"): platform.node(),
        bstack1l1_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳࠢᵀ"): platform.system(),
        bstack1l1_opy_ (u"ࠨࡴࡺࡲࡨࠦᵁ"): platform.machine(),
        bstack1l1_opy_ (u"ࠢࡷࡧࡵࡷ࡮ࡵ࡮ࠣᵂ"): platform.version(),
        bstack1l1_opy_ (u"ࠣࡣࡵࡧ࡭ࠨᵃ"): platform.architecture()[0]
    }
def bstack1l111l11ll_opy_():
    try:
        import selenium
        return True
    except ImportError:
        return False
def bstack1111lll1ll1_opy_():
    if bstack11l11111_opy_.get_property(bstack1l1_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡡࡶࡩࡸࡹࡩࡰࡰࠪᵄ")):
        return bstack1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩᵅ")
    return bstack1l1_opy_ (u"ࠫࡺࡴ࡫࡯ࡱࡺࡲࡤ࡭ࡲࡪࡦࠪᵆ")
def bstack1111l1ll1l1_opy_(driver):
    info = {
        bstack1l1_opy_ (u"ࠬࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠫᵇ"): driver.capabilities,
        bstack1l1_opy_ (u"࠭ࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡪࡦࠪᵈ"): driver.session_id,
        bstack1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࠨᵉ"): driver.capabilities.get(bstack1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭ᵊ"), None),
        bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡢࡺࡪࡸࡳࡪࡱࡱࠫᵋ"): driver.capabilities.get(bstack1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫᵌ"), None),
        bstack1l1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲ࠭ᵍ"): driver.capabilities.get(bstack1l1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡎࡢ࡯ࡨࠫᵎ"), None),
        bstack1l1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡠࡸࡨࡶࡸ࡯࡯࡯ࠩᵏ"):driver.capabilities.get(bstack1l1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡘࡨࡶࡸ࡯࡯࡯ࠩᵐ"), None),
    }
    if bstack1111lll1ll1_opy_() == bstack1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧᵑ"):
        if bstack11ll11111_opy_():
            info[bstack1l1_opy_ (u"ࠩࡳࡶࡴࡪࡵࡤࡶࠪᵒ")] = bstack1l1_opy_ (u"ࠪࡥࡵࡶ࠭ࡢࡷࡷࡳࡲࡧࡴࡦࠩᵓ")
        elif driver.capabilities.get(bstack1l1_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬᵔ"), {}).get(bstack1l1_opy_ (u"ࠬࡺࡵࡳࡤࡲࡷࡨࡧ࡬ࡦࠩᵕ"), False):
            info[bstack1l1_opy_ (u"࠭ࡰࡳࡱࡧࡹࡨࡺࠧᵖ")] = bstack1l1_opy_ (u"ࠧࡵࡷࡵࡦࡴࡹࡣࡢ࡮ࡨࠫᵗ")
        else:
            info[bstack1l1_opy_ (u"ࠨࡲࡵࡳࡩࡻࡣࡵࠩᵘ")] = bstack1l1_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶࡨࠫᵙ")
    return info
def bstack11ll11111_opy_():
    if bstack11l11111_opy_.get_property(bstack1l1_opy_ (u"ࠪࡥࡵࡶ࡟ࡢࡷࡷࡳࡲࡧࡴࡦࠩᵚ")):
        return True
    if bstack1ll1111ll1_opy_(os.environ.get(bstack1l1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡍࡘࡥࡁࡑࡒࡢࡅ࡚࡚ࡏࡎࡃࡗࡉࠬᵛ"), None)):
        return True
    return False
def bstack1lll1l1l11_opy_(bstack1111ll1l1l1_opy_, url, data, config):
    headers = config.get(bstack1l1_opy_ (u"ࠬ࡮ࡥࡢࡦࡨࡶࡸ࠭ᵜ"), None)
    proxies = bstack1111ll1lll_opy_(config, url)
    auth = config.get(bstack1l1_opy_ (u"࠭ࡡࡶࡶ࡫ࠫᵝ"), None)
    response = requests.request(
            bstack1111ll1l1l1_opy_,
            url=url,
            headers=headers,
            auth=auth,
            json=data,
            proxies=proxies
        )
    return response
def bstack11l1l1ll1_opy_(bstack11l11111ll_opy_, size):
    bstack1ll1llll11_opy_ = []
    while len(bstack11l11111ll_opy_) > size:
        bstack1111llll1_opy_ = bstack11l11111ll_opy_[:size]
        bstack1ll1llll11_opy_.append(bstack1111llll1_opy_)
        bstack11l11111ll_opy_ = bstack11l11111ll_opy_[size:]
    bstack1ll1llll11_opy_.append(bstack11l11111ll_opy_)
    return bstack1ll1llll11_opy_
def bstack111l1ll1l1l_opy_(message, bstack111l1ll11ll_opy_=False):
    os.write(1, bytes(message, bstack1l1_opy_ (u"ࠧࡶࡶࡩ࠱࠽࠭ᵞ")))
    os.write(1, bytes(bstack1l1_opy_ (u"ࠨ࡞ࡱࠫᵟ"), bstack1l1_opy_ (u"ࠩࡸࡸ࡫࠳࠸ࠨᵠ")))
    if bstack111l1ll11ll_opy_:
        with open(bstack1l1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠰ࡳ࠶࠷ࡹ࠮ࠩᵡ") + os.environ[bstack1l1_opy_ (u"ࠫࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡄࡘࡍࡑࡊ࡟ࡉࡃࡖࡌࡊࡊ࡟ࡊࡆࠪᵢ")] + bstack1l1_opy_ (u"ࠬ࠴࡬ࡰࡩࠪᵣ"), bstack1l1_opy_ (u"࠭ࡡࠨᵤ")) as f:
            f.write(message + bstack1l1_opy_ (u"ࠧ࡝ࡰࠪᵥ"))
def bstack1lll1ll111l_opy_():
    return os.environ[bstack1l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡂࡗࡗࡓࡒࡇࡔࡊࡑࡑࠫᵦ")].lower() == bstack1l1_opy_ (u"ࠩࡷࡶࡺ࡫ࠧᵧ")
def bstack1l1ll11l_opy_():
    return bstack1llll1ll_opy_().replace(tzinfo=None).isoformat() + bstack1l1_opy_ (u"ࠪ࡞ࠬᵨ")
def bstack1111llll1ll_opy_(start, finish):
    return (datetime.datetime.fromisoformat(finish.rstrip(bstack1l1_opy_ (u"ࠫ࡟࠭ᵩ"))) - datetime.datetime.fromisoformat(start.rstrip(bstack1l1_opy_ (u"ࠬࡠࠧᵪ")))).total_seconds() * 1000
def bstack1111ll1l11l_opy_(timestamp):
    return bstack111l1l11l1l_opy_(timestamp).isoformat() + bstack1l1_opy_ (u"࡚࠭ࠨᵫ")
def bstack1111ll1l111_opy_(bstack1111l1l111l_opy_):
    date_format = bstack1l1_opy_ (u"࡛ࠧࠦࠨࡱࠪࡪࠠࠦࡊ࠽ࠩࡒࡀࠥࡔ࠰ࠨࡪࠬᵬ")
    bstack1111lll1111_opy_ = datetime.datetime.strptime(bstack1111l1l111l_opy_, date_format)
    return bstack1111lll1111_opy_.isoformat() + bstack1l1_opy_ (u"ࠨ࡜ࠪᵭ")
def bstack111l1l11ll1_opy_(outcome):
    _, exception, _ = outcome.excinfo or (None, None, None)
    if exception:
        return bstack1l1_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩᵮ")
    else:
        return bstack1l1_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪᵯ")
def bstack1ll1111ll1_opy_(val):
    if val is None:
        return False
    return val.__str__().lower() == bstack1l1_opy_ (u"ࠫࡹࡸࡵࡦࠩᵰ")
def bstack111l111l1ll_opy_(val):
    return val.__str__().lower() == bstack1l1_opy_ (u"ࠬ࡬ࡡ࡭ࡵࡨࠫᵱ")
def error_handler(bstack1111l1l1l11_opy_=Exception, class_method=False, default_value=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except bstack1111l1l1l11_opy_ as e:
                print(bstack1l1_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠠࡼࡿࠣ࠱ࡃࠦࡻࡾ࠼ࠣࡿࢂࠨᵲ").format(func.__name__, bstack1111l1l1l11_opy_.__name__, str(e)))
                return default_value
        return wrapper
    def bstack1111ll1ll1l_opy_(bstack1111l1l1l1l_opy_):
        def wrapped(cls, *args, **kwargs):
            try:
                return bstack1111l1l1l1l_opy_(cls, *args, **kwargs)
            except bstack1111l1l1l11_opy_ as e:
                print(bstack1l1_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠡࡽࢀࠤ࠲ࡄࠠࡼࡿ࠽ࠤࢀࢃࠢᵳ").format(bstack1111l1l1l1l_opy_.__name__, bstack1111l1l1l11_opy_.__name__, str(e)))
                return default_value
        return wrapped
    if class_method:
        return bstack1111ll1ll1l_opy_
    else:
        return decorator
def bstack1lllllll11_opy_(bstack11111l11_opy_):
    if os.getenv(bstack1l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡂࡗࡗࡓࡒࡇࡔࡊࡑࡑࠫᵴ")) is not None:
        return bstack1ll1111ll1_opy_(os.getenv(bstack1l1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡃࡘࡘࡔࡓࡁࡕࡋࡒࡒࠬᵵ")))
    if bstack1l1_opy_ (u"ࠪࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠧᵶ") in bstack11111l11_opy_ and bstack111l111l1ll_opy_(bstack11111l11_opy_[bstack1l1_opy_ (u"ࠫࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠨᵷ")]):
        return False
    if bstack1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠧᵸ") in bstack11111l11_opy_ and bstack111l111l1ll_opy_(bstack11111l11_opy_[bstack1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠨᵹ")]):
        return False
    return True
def bstack1l11l11ll_opy_():
    try:
        from pytest_bdd import reporting
        bstack111l11l1l1l_opy_ = os.environ.get(bstack1l1_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡕࡔࡇࡕࡣࡋࡘࡁࡎࡇ࡚ࡓࡗࡑࠢᵺ"), None)
        return bstack111l11l1l1l_opy_ is None or bstack111l11l1l1l_opy_ == bstack1l1_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠧᵻ")
    except Exception as e:
        return False
def bstack1lllll11l1_opy_(hub_url, CONFIG):
    if bstack11llll111_opy_() <= version.parse(bstack1l1_opy_ (u"ࠩ࠶࠲࠶࠹࠮࠱ࠩᵼ")):
        if hub_url:
            return bstack1l1_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻࠱࠲ࠦᵽ") + hub_url + bstack1l1_opy_ (u"ࠦ࠿࠾࠰࠰ࡹࡧ࠳࡭ࡻࡢࠣᵾ")
        return bstack11l1ll11l1_opy_
    if hub_url:
        return bstack1l1_opy_ (u"ࠧ࡮ࡴࡵࡲࡶ࠾࠴࠵ࠢᵿ") + hub_url + bstack1l1_opy_ (u"ࠨ࠯ࡸࡦ࠲࡬ࡺࡨࠢᶀ")
    return bstack1lll11l111_opy_
def bstack111l1l1l1l1_opy_():
    return isinstance(os.getenv(bstack1l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐ࡚ࡖࡈࡗ࡙ࡥࡐࡍࡗࡊࡍࡓ࠭ᶁ")), str)
def bstack1lll1ll11l_opy_(url):
    return urlparse(url).hostname
def bstack1l1l1l1l11_opy_(hostname):
    for bstack1l11ll111l_opy_ in bstack1111l1l11_opy_:
        regex = re.compile(bstack1l11ll111l_opy_)
        if regex.match(hostname):
            return True
    return False
def bstack11ll111l11l_opy_(bstack1111l11l1l1_opy_, file_name, logger):
    bstack1l1ll1ll1l_opy_ = os.path.join(os.path.expanduser(bstack1l1_opy_ (u"ࠨࢀࠪᶂ")), bstack1111l11l1l1_opy_)
    try:
        if not os.path.exists(bstack1l1ll1ll1l_opy_):
            os.makedirs(bstack1l1ll1ll1l_opy_)
        file_path = os.path.join(os.path.expanduser(bstack1l1_opy_ (u"ࠩࢁࠫᶃ")), bstack1111l11l1l1_opy_, file_name)
        if not os.path.isfile(file_path):
            with open(file_path, bstack1l1_opy_ (u"ࠪࡻࠬᶄ")):
                pass
            with open(file_path, bstack1l1_opy_ (u"ࠦࡼ࠱ࠢᶅ")) as outfile:
                json.dump({}, outfile)
        return file_path
    except Exception as e:
        logger.debug(bstack111lllll11_opy_.format(str(e)))
def bstack11ll111l1l1_opy_(file_name, key, value, logger):
    file_path = bstack11ll111l11l_opy_(bstack1l1_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬᶆ"), file_name, logger)
    if file_path != None:
        if os.path.exists(file_path):
            bstack11l11ll1l1_opy_ = json.load(open(file_path, bstack1l1_opy_ (u"࠭ࡲࡣࠩᶇ")))
        else:
            bstack11l11ll1l1_opy_ = {}
        bstack11l11ll1l1_opy_[key] = value
        with open(file_path, bstack1l1_opy_ (u"ࠢࡸ࠭ࠥᶈ")) as outfile:
            json.dump(bstack11l11ll1l1_opy_, outfile)
def bstack11l1ll1111_opy_(file_name, logger):
    file_path = bstack11ll111l11l_opy_(bstack1l1_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨᶉ"), file_name, logger)
    bstack11l11ll1l1_opy_ = {}
    if file_path != None and os.path.exists(file_path):
        with open(file_path, bstack1l1_opy_ (u"ࠩࡵࠫᶊ")) as bstack11llll1l1l_opy_:
            bstack11l11ll1l1_opy_ = json.load(bstack11llll1l1l_opy_)
    return bstack11l11ll1l1_opy_
def bstack1ll1l1l111_opy_(file_path, logger):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
    except Exception as e:
        logger.debug(bstack1l1_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡪࡥ࡭ࡧࡷ࡭ࡳ࡭ࠠࡧ࡫࡯ࡩ࠿ࠦࠧᶋ") + file_path + bstack1l1_opy_ (u"ࠫࠥ࠭ᶌ") + str(e))
def bstack11llll111_opy_():
    from selenium import webdriver
    return version.parse(webdriver.__version__)
class Notset:
    def __repr__(self):
        return bstack1l1_opy_ (u"ࠧࡂࡎࡐࡖࡖࡉ࡙ࡄࠢᶍ")
def bstack1l1ll1l11l_opy_(config):
    if bstack1l1_opy_ (u"࠭ࡩࡴࡒ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠬᶎ") in config:
        del (config[bstack1l1_opy_ (u"ࠧࡪࡵࡓࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹ࠭ᶏ")])
        return False
    if bstack11llll111_opy_() < version.parse(bstack1l1_opy_ (u"ࠨ࠵࠱࠸࠳࠶ࠧᶐ")):
        return False
    if bstack11llll111_opy_() >= version.parse(bstack1l1_opy_ (u"ࠩ࠷࠲࠶࠴࠵ࠨᶑ")):
        return True
    if bstack1l1_opy_ (u"ࠪࡹࡸ࡫ࡗ࠴ࡅࠪᶒ") in config and config[bstack1l1_opy_ (u"ࠫࡺࡹࡥࡘ࠵ࡆࠫᶓ")] is False:
        return False
    else:
        return True
def bstack1l1l1l1ll1_opy_(args_list, bstack1111l1ll11l_opy_):
    index = -1
    for value in bstack1111l1ll11l_opy_:
        try:
            index = args_list.index(value)
            return index
        except Exception as e:
            return index
    return index
def bstack111l1lll1l1_opy_(a, b):
  for k, v in b.items():
    if isinstance(v, dict) and k in a and isinstance(a[k], dict):
        bstack111l1lll1l1_opy_(a[k], v)
    else:
        a[k] = v
class Result:
    def __init__(self, result=None, duration=None, exception=None, bstack1llll111_opy_=None):
        self.result = result
        self.duration = duration
        self.exception = exception
        self.exception_type = type(self.exception).__name__ if exception else None
        self.bstack1llll111_opy_ = bstack1llll111_opy_
    @classmethod
    def passed(cls):
        return Result(result=bstack1l1_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬᶔ"))
    @classmethod
    def failed(cls, exception=None):
        return Result(result=bstack1l1_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ᶕ"), exception=exception)
    def bstack111111l111_opy_(self):
        if self.result != bstack1l1_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧᶖ"):
            return None
        if isinstance(self.exception_type, str) and bstack1l1_opy_ (u"ࠣࡃࡶࡷࡪࡸࡴࡪࡱࡱࠦᶗ") in self.exception_type:
            return bstack1l1_opy_ (u"ࠤࡄࡷࡸ࡫ࡲࡵ࡫ࡲࡲࡊࡸࡲࡰࡴࠥᶘ")
        return bstack1l1_opy_ (u"࡙ࠥࡳ࡮ࡡ࡯ࡦ࡯ࡩࡩࡋࡲࡳࡱࡵࠦᶙ")
    def bstack111l11111l1_opy_(self):
        if self.result != bstack1l1_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫᶚ"):
            return None
        if self.bstack1llll111_opy_:
            return self.bstack1llll111_opy_
        return bstack1111ll11111_opy_(self.exception)
def bstack1111ll11111_opy_(exc):
    return [traceback.format_exception(exc)]
def bstack111l11lll1l_opy_(message):
    if isinstance(message, str):
        return not bool(message and message.strip())
    return True
def bstack11lll111_opy_(object, key, default_value):
    if not object or not object.__dict__:
        return default_value
    if key in object.__dict__.keys():
        return object.__dict__.get(key)
    return default_value
def bstack1l1l1l11l1_opy_(config, logger):
    try:
        import playwright
        bstack111l11ll111_opy_ = playwright.__file__
        bstack111l11l1lll_opy_ = os.path.split(bstack111l11ll111_opy_)
        bstack111l11l111l_opy_ = bstack111l11l1lll_opy_[0] + bstack1l1_opy_ (u"ࠬ࠵ࡤࡳ࡫ࡹࡩࡷ࠵ࡰࡢࡥ࡮ࡥ࡬࡫࠯࡭࡫ࡥ࠳ࡨࡲࡩ࠰ࡥ࡯࡭࠳ࡰࡳࠨᶛ")
        os.environ[bstack1l1_opy_ (u"࠭ࡇࡍࡑࡅࡅࡑࡥࡁࡈࡇࡑࡘࡤࡎࡔࡕࡒࡢࡔࡗࡕࡘ࡚ࠩᶜ")] = bstack1l1l11lll1_opy_(config)
        with open(bstack111l11l111l_opy_, bstack1l1_opy_ (u"ࠧࡳࠩᶝ")) as f:
            file_content = f.read()
            bstack1111l1l1lll_opy_ = bstack1l1_opy_ (u"ࠨࡩ࡯ࡳࡧࡧ࡬࠮ࡣࡪࡩࡳࡺࠧᶞ")
            bstack111l11l1ll1_opy_ = file_content.find(bstack1111l1l1lll_opy_)
            if bstack111l11l1ll1_opy_ == -1:
              process = subprocess.Popen(bstack1l1_opy_ (u"ࠤࡱࡴࡲࠦࡩ࡯ࡵࡷࡥࡱࡲࠠࡨ࡮ࡲࡦࡦࡲ࠭ࡢࡩࡨࡲࡹࠨᶟ"), shell=True, cwd=bstack111l11l1lll_opy_[0])
              process.wait()
              bstack111l1l1l11l_opy_ = bstack1l1_opy_ (u"ࠪࠦࡺࡹࡥࠡࡵࡷࡶ࡮ࡩࡴࠣ࠽ࠪᶠ")
              bstack1111l11l1ll_opy_ = bstack1l1_opy_ (u"ࠦࠧࠨࠠ࡝ࠤࡸࡷࡪࠦࡳࡵࡴ࡬ࡧࡹࡢࠢ࠼ࠢࡦࡳࡳࡹࡴࠡࡽࠣࡦࡴࡵࡴࡴࡶࡵࡥࡵࠦࡽࠡ࠿ࠣࡶࡪࡷࡵࡪࡴࡨࠬࠬ࡭࡬ࡰࡤࡤࡰ࠲ࡧࡧࡦࡰࡷࠫ࠮ࡁࠠࡪࡨࠣࠬࡵࡸ࡯ࡤࡧࡶࡷ࠳࡫࡮ࡷ࠰ࡊࡐࡔࡈࡁࡍࡡࡄࡋࡊࡔࡔࡠࡊࡗࡘࡕࡥࡐࡓࡑ࡛࡝࠮ࠦࡢࡰࡱࡷࡷࡹࡸࡡࡱࠪࠬ࠿ࠥࠨࠢࠣᶡ")
              bstack111l1111lll_opy_ = file_content.replace(bstack111l1l1l11l_opy_, bstack1111l11l1ll_opy_)
              with open(bstack111l11l111l_opy_, bstack1l1_opy_ (u"ࠬࡽࠧᶢ")) as f:
                f.write(bstack111l1111lll_opy_)
    except Exception as e:
        logger.error(bstack11ll1l1ll1_opy_.format(str(e)))
def bstack1l1111l11l_opy_():
  try:
    bstack1111l1l11l1_opy_ = os.path.join(tempfile.gettempdir(), bstack1l1_opy_ (u"࠭࡯ࡱࡶ࡬ࡱࡦࡲ࡟ࡩࡷࡥࡣࡺࡸ࡬࠯࡬ࡶࡳࡳ࠭ᶣ"))
    bstack111l1ll11l1_opy_ = []
    if os.path.exists(bstack1111l1l11l1_opy_):
      with open(bstack1111l1l11l1_opy_) as f:
        bstack111l1ll11l1_opy_ = json.load(f)
      os.remove(bstack1111l1l11l1_opy_)
    return bstack111l1ll11l1_opy_
  except:
    pass
  return []
def bstack1l1l111l1l_opy_(bstack11111lllll_opy_):
  try:
    bstack111l1ll11l1_opy_ = []
    bstack1111l1l11l1_opy_ = os.path.join(tempfile.gettempdir(), bstack1l1_opy_ (u"ࠧࡰࡲࡷ࡭ࡲࡧ࡬ࡠࡪࡸࡦࡤࡻࡲ࡭࠰࡭ࡷࡴࡴࠧᶤ"))
    if os.path.exists(bstack1111l1l11l1_opy_):
      with open(bstack1111l1l11l1_opy_) as f:
        bstack111l1ll11l1_opy_ = json.load(f)
    bstack111l1ll11l1_opy_.append(bstack11111lllll_opy_)
    with open(bstack1111l1l11l1_opy_, bstack1l1_opy_ (u"ࠨࡹࠪᶥ")) as f:
        json.dump(bstack111l1ll11l1_opy_, f)
  except:
    pass
def bstack1111llllll_opy_(logger, bstack111l1111ll1_opy_ = False):
  try:
    test_name = os.environ.get(bstack1l1_opy_ (u"ࠩࡓ࡝࡙ࡋࡓࡕࡡࡗࡉࡘ࡚࡟ࡏࡃࡐࡉࠬᶦ"), bstack1l1_opy_ (u"ࠪࠫᶧ"))
    if test_name == bstack1l1_opy_ (u"ࠫࠬᶨ"):
        test_name = threading.current_thread().__dict__.get(bstack1l1_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࡇࡪࡤࡠࡶࡨࡷࡹࡥ࡮ࡢ࡯ࡨࠫᶩ"), bstack1l1_opy_ (u"࠭ࠧᶪ"))
    bstack111l11ll1ll_opy_ = bstack1l1_opy_ (u"ࠧ࠭ࠢࠪᶫ").join(threading.current_thread().bstackTestErrorMessages)
    if bstack111l1111ll1_opy_:
        bstack11111l1l1_opy_ = os.environ.get(bstack1l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡎࡄࡘࡋࡕࡒࡎࡡࡌࡒࡉࡋࡘࠨᶬ"), bstack1l1_opy_ (u"ࠩ࠳ࠫᶭ"))
        bstack1l11111ll1_opy_ = {bstack1l1_opy_ (u"ࠪࡲࡦࡳࡥࠨᶮ"): test_name, bstack1l1_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪᶯ"): bstack111l11ll1ll_opy_, bstack1l1_opy_ (u"ࠬ࡯࡮ࡥࡧࡻࠫᶰ"): bstack11111l1l1_opy_}
        bstack1111lll11ll_opy_ = []
        bstack1111llll111_opy_ = os.path.join(tempfile.gettempdir(), bstack1l1_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹࡥࡰࡱࡲࡢࡩࡷࡸ࡯ࡳࡡ࡯࡭ࡸࡺ࠮࡫ࡵࡲࡲࠬᶱ"))
        if os.path.exists(bstack1111llll111_opy_):
            with open(bstack1111llll111_opy_) as f:
                bstack1111lll11ll_opy_ = json.load(f)
        bstack1111lll11ll_opy_.append(bstack1l11111ll1_opy_)
        with open(bstack1111llll111_opy_, bstack1l1_opy_ (u"ࠧࡸࠩᶲ")) as f:
            json.dump(bstack1111lll11ll_opy_, f)
    else:
        bstack1l11111ll1_opy_ = {bstack1l1_opy_ (u"ࠨࡰࡤࡱࡪ࠭ᶳ"): test_name, bstack1l1_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨᶴ"): bstack111l11ll1ll_opy_, bstack1l1_opy_ (u"ࠪ࡭ࡳࡪࡥࡹࠩᶵ"): str(multiprocessing.current_process().name)}
        if bstack1l1_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡣࡪࡸࡲࡰࡴࡢࡰ࡮ࡹࡴࠨᶶ") not in multiprocessing.current_process().__dict__.keys():
            multiprocessing.current_process().bstack_error_list = []
        multiprocessing.current_process().bstack_error_list.append(bstack1l11111ll1_opy_)
  except Exception as e:
      logger.warn(bstack1l1_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡵࡷࡳࡷ࡫ࠠࡱࡻࡷࡩࡸࡺࠠࡧࡷࡱࡲࡪࡲࠠࡥࡣࡷࡥ࠿ࠦࡻࡾࠤᶷ").format(e))
def bstack1ll1ll1l1l_opy_(error_message, test_name, index, logger):
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack1l1_opy_ (u"࠭ࡦࡪ࡮ࡨࡰࡴࡩ࡫ࠡࡰࡲࡸࠥࡧࡶࡢ࡫࡯ࡥࡧࡲࡥ࠭ࠢࡸࡷ࡮ࡴࡧࠡࡤࡤࡷ࡮ࡩࠠࡧ࡫࡯ࡩࠥࡵࡰࡦࡴࡤࡸ࡮ࡵ࡮ࡴࠩᶸ"))
    try:
      bstack1111llllll1_opy_ = []
      bstack1l11111ll1_opy_ = {bstack1l1_opy_ (u"ࠧ࡯ࡣࡰࡩࠬᶹ"): test_name, bstack1l1_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧᶺ"): error_message, bstack1l1_opy_ (u"ࠩ࡬ࡲࡩ࡫ࡸࠨᶻ"): index}
      bstack1111lllllll_opy_ = os.path.join(tempfile.gettempdir(), bstack1l1_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࡡࡨࡶࡷࡵࡲࡠ࡮࡬ࡷࡹ࠴ࡪࡴࡱࡱࠫᶼ"))
      if os.path.exists(bstack1111lllllll_opy_):
          with open(bstack1111lllllll_opy_) as f:
              bstack1111llllll1_opy_ = json.load(f)
      bstack1111llllll1_opy_.append(bstack1l11111ll1_opy_)
      with open(bstack1111lllllll_opy_, bstack1l1_opy_ (u"ࠫࡼ࠭ᶽ")) as f:
          json.dump(bstack1111llllll1_opy_, f)
    except Exception as e:
      logger.warn(bstack1l1_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡵࡷࡳࡷ࡫ࠠࡳࡱࡥࡳࡹࠦࡦࡶࡰࡱࡩࡱࠦࡤࡢࡶࡤ࠾ࠥࢁࡽࠣᶾ").format(e))
    return
  bstack1111llllll1_opy_ = []
  bstack1l11111ll1_opy_ = {bstack1l1_opy_ (u"࠭࡮ࡢ࡯ࡨࠫᶿ"): test_name, bstack1l1_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭᷀"): error_message, bstack1l1_opy_ (u"ࠨ࡫ࡱࡨࡪࡾࠧ᷁"): index}
  bstack1111lllllll_opy_ = os.path.join(tempfile.gettempdir(), bstack1l1_opy_ (u"ࠩࡵࡳࡧࡵࡴࡠࡧࡵࡶࡴࡸ࡟࡭࡫ࡶࡸ࠳ࡰࡳࡰࡰ᷂ࠪ"))
  lock_file = bstack1111lllllll_opy_ + bstack1l1_opy_ (u"ࠪ࠲ࡱࡵࡣ࡬ࠩ᷃")
  try:
    with FileLock(lock_file, timeout=10):
      if os.path.exists(bstack1111lllllll_opy_):
          with open(bstack1111lllllll_opy_, bstack1l1_opy_ (u"ࠫࡷ࠭᷄")) as f:
              content = f.read().strip()
              if content:
                  bstack1111llllll1_opy_ = json.load(open(bstack1111lllllll_opy_))
      bstack1111llllll1_opy_.append(bstack1l11111ll1_opy_)
      with open(bstack1111lllllll_opy_, bstack1l1_opy_ (u"ࠬࡽࠧ᷅")) as f:
          json.dump(bstack1111llllll1_opy_, f)
  except Exception as e:
    logger.warn(bstack1l1_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡶࡸࡴࡸࡥࠡࡴࡲࡦࡴࡺࠠࡧࡷࡱࡲࡪࡲࠠࡥࡣࡷࡥࠥࡽࡩࡵࡪࠣࡪ࡮ࡲࡥࠡ࡮ࡲࡧࡰ࡯࡮ࡨ࠼ࠣࡿࢂࠨ᷆").format(e))
def bstack11l1ll11l_opy_(bstack1111lll11_opy_, name, logger):
  try:
    bstack1l11111ll1_opy_ = {bstack1l1_opy_ (u"ࠧ࡯ࡣࡰࡩࠬ᷇"): name, bstack1l1_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧ᷈"): bstack1111lll11_opy_, bstack1l1_opy_ (u"ࠩ࡬ࡲࡩ࡫ࡸࠨ᷉"): str(threading.current_thread()._name)}
    return bstack1l11111ll1_opy_
  except Exception as e:
    logger.warn(bstack1l1_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡳࡵࡱࡵࡩࠥࡨࡥࡩࡣࡹࡩࠥ࡬ࡵ࡯ࡰࡨࡰࠥࡪࡡࡵࡣ࠽ࠤࢀࢃ᷊ࠢ").format(e))
  return
def bstack111l11lll11_opy_():
    return platform.system() == bstack1l1_opy_ (u"ࠫ࡜࡯࡮ࡥࡱࡺࡷࠬ᷋")
def bstack111ll1111l_opy_(bstack111l11l11ll_opy_, config, logger):
    bstack1111ll1l1ll_opy_ = {}
    try:
        return {key: config[key] for key in config if bstack111l11l11ll_opy_.match(key)}
    except Exception as e:
        logger.debug(bstack1l1_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡨ࡬ࡰࡹ࡫ࡲࠡࡥࡲࡲ࡫࡯ࡧࠡ࡭ࡨࡽࡸࠦࡢࡺࠢࡵࡩ࡬࡫ࡸࠡ࡯ࡤࡸࡨ࡮࠺ࠡࡽࢀࠦ᷌").format(e))
    return bstack1111ll1l1ll_opy_
def bstack11l1ll11l1l_opy_(bstack1111l11ll11_opy_, bstack111l1111l1l_opy_):
    bstack111l1lll11l_opy_ = version.parse(bstack1111l11ll11_opy_)
    bstack1111lll1l11_opy_ = version.parse(bstack111l1111l1l_opy_)
    if bstack111l1lll11l_opy_ > bstack1111lll1l11_opy_:
        return 1
    elif bstack111l1lll11l_opy_ < bstack1111lll1l11_opy_:
        return -1
    else:
        return 0
def bstack1llll1ll_opy_():
    return datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None)
def bstack111l1l11l1l_opy_(timestamp):
    return datetime.datetime.fromtimestamp(timestamp, datetime.timezone.utc).replace(tzinfo=None)
def bstack111l1l1ll1l_opy_(framework):
    from browserstack_sdk._version import __version__
    return str(framework) + str(__version__)
def bstack1l11111lll_opy_(options, framework, config, bstack11lllllll_opy_={}):
    if options is None:
        return
    if getattr(options, bstack1l1_opy_ (u"࠭ࡧࡦࡶࠪ᷍"), None):
        caps = options
    else:
        caps = options.to_capabilities()
    bstack1l1lllll1_opy_ = caps.get(bstack1l1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨ᷎"))
    bstack1111lll1lll_opy_ = True
    bstack11111ll11l_opy_ = os.environ[bstack1l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ᷏࠭")]
    bstack1l1111ll1ll_opy_ = config.get(bstack1l1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺ᷐ࠩ"), False)
    if bstack1l1111ll1ll_opy_:
        bstack1l1l1l1l11l_opy_ = config.get(bstack1l1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪ᷑"), {})
        bstack1l1l1l1l11l_opy_[bstack1l1_opy_ (u"ࠫࡦࡻࡴࡩࡖࡲ࡯ࡪࡴࠧ᷒")] = os.getenv(bstack1l1_opy_ (u"ࠬࡈࡓࡠࡃ࠴࠵࡞ࡥࡊࡘࡖࠪᷓ"))
        bstack111l1111l11_opy_ = json.loads(os.getenv(bstack1l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡢࡅࡈࡉࡅࡔࡕࡌࡆࡎࡒࡉࡕ࡛ࡢࡇࡔࡔࡆࡊࡉࡘࡖࡆ࡚ࡉࡐࡐࡢ࡝ࡒࡒࠧᷔ"), bstack1l1_opy_ (u"ࠧࡼࡿࠪᷕ"))).get(bstack1l1_opy_ (u"ࠨࡵࡦࡥࡳࡴࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩᷖ"))
    if bstack111l111l1ll_opy_(caps.get(bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡷࡶࡩ࡜࠹ࡃࠨᷗ"))) or bstack111l111l1ll_opy_(caps.get(bstack1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡸࡷࡪࡥࡷ࠴ࡥࠪᷘ"))):
        bstack1111lll1lll_opy_ = False
    if bstack1l1ll1l11l_opy_({bstack1l1_opy_ (u"ࠦࡺࡹࡥࡘ࠵ࡆࠦᷙ"): bstack1111lll1lll_opy_}):
        bstack1l1lllll1_opy_ = bstack1l1lllll1_opy_ or {}
        bstack1l1lllll1_opy_[bstack1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡗࡉࡑࠧᷚ")] = bstack111l1l1ll1l_opy_(framework)
        bstack1l1lllll1_opy_[bstack1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠨᷛ")] = bstack1lll1ll111l_opy_()
        bstack1l1lllll1_opy_[bstack1l1_opy_ (u"ࠧࡵࡧࡶࡸ࡭ࡻࡢࡃࡷ࡬ࡰࡩ࡛ࡵࡪࡦࠪᷜ")] = bstack11111ll11l_opy_
        bstack1l1lllll1_opy_[bstack1l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡐࡳࡱࡧࡹࡨࡺࡍࡢࡲࠪᷝ")] = bstack11lllllll_opy_
        if bstack1l1111ll1ll_opy_:
            bstack1l1lllll1_opy_[bstack1l1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩᷞ")] = bstack1l1111ll1ll_opy_
            bstack1l1lllll1_opy_[bstack1l1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪᷟ")] = bstack1l1l1l1l11l_opy_
            bstack1l1lllll1_opy_[bstack1l1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫᷠ")][bstack1l1_opy_ (u"ࠬࡹࡣࡢࡰࡱࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ᷡ")] = bstack111l1111l11_opy_
        if getattr(options, bstack1l1_opy_ (u"࠭ࡳࡦࡶࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹࡿࠧᷢ"), None):
            options.set_capability(bstack1l1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨᷣ"), bstack1l1lllll1_opy_)
        else:
            options[bstack1l1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩᷤ")] = bstack1l1lllll1_opy_
    else:
        if getattr(options, bstack1l1_opy_ (u"ࠩࡶࡩࡹࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵࡻࠪᷥ"), None):
            options.set_capability(bstack1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡔࡆࡎࠫᷦ"), bstack111l1l1ll1l_opy_(framework))
            options.set_capability(bstack1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬᷧ"), bstack1lll1ll111l_opy_())
            options.set_capability(bstack1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡹ࡫ࡳࡵࡪࡸࡦࡇࡻࡩ࡭ࡦࡘࡹ࡮ࡪࠧᷨ"), bstack11111ll11l_opy_)
            options.set_capability(bstack1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡨࡵࡪ࡮ࡧࡔࡷࡵࡤࡶࡥࡷࡑࡦࡶࠧᷩ"), bstack11lllllll_opy_)
            if bstack1l1111ll1ll_opy_:
                options.set_capability(bstack1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭ᷪ"), bstack1l1111ll1ll_opy_)
                options.set_capability(bstack1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧᷫ"), bstack1l1l1l1l11l_opy_)
                options.set_capability(bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳ࠯ࡵࡦࡥࡳࡴࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩᷬ"), bstack111l1111l11_opy_)
        else:
            options[bstack1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡔࡆࡎࠫᷭ")] = bstack111l1l1ll1l_opy_(framework)
            options[bstack1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬᷮ")] = bstack1lll1ll111l_opy_()
            options[bstack1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡹ࡫ࡳࡵࡪࡸࡦࡇࡻࡩ࡭ࡦࡘࡹ࡮ࡪࠧᷯ")] = bstack11111ll11l_opy_
            options[bstack1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡨࡵࡪ࡮ࡧࡔࡷࡵࡤࡶࡥࡷࡑࡦࡶࠧᷰ")] = bstack11lllllll_opy_
            if bstack1l1111ll1ll_opy_:
                options[bstack1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭ᷱ")] = bstack1l1111ll1ll_opy_
                options[bstack1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧᷲ")] = bstack1l1l1l1l11l_opy_
                options[bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨᷳ")][bstack1l1_opy_ (u"ࠪࡷࡨࡧ࡮࡯ࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫᷴ")] = bstack111l1111l11_opy_
    return options
def bstack1111lll11l1_opy_(ws_endpoint, framework):
    bstack11lllllll_opy_ = bstack11l11111_opy_.get_property(bstack1l1_opy_ (u"ࠦࡕࡒࡁ࡚࡙ࡕࡍࡌࡎࡔࡠࡒࡕࡓࡉ࡛ࡃࡕࡡࡐࡅࡕࠨ᷵"))
    if ws_endpoint and len(ws_endpoint.split(bstack1l1_opy_ (u"ࠬࡩࡡࡱࡵࡀࠫ᷶"))) > 1:
        ws_url = ws_endpoint.split(bstack1l1_opy_ (u"࠭ࡣࡢࡲࡶࡁ᷷ࠬ"))[0]
        if bstack1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯᷸ࠪ") in ws_url:
            from browserstack_sdk._version import __version__
            bstack1111l1lllll_opy_ = json.loads(urllib.parse.unquote(ws_endpoint.split(bstack1l1_opy_ (u"ࠨࡥࡤࡴࡸࡃ᷹ࠧ"))[1]))
            bstack1111l1lllll_opy_ = bstack1111l1lllll_opy_ or {}
            bstack11111ll11l_opy_ = os.environ[bstack1l1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊ᷺ࠧ")]
            bstack1111l1lllll_opy_[bstack1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡔࡆࡎࠫ᷻")] = str(framework) + str(__version__)
            bstack1111l1lllll_opy_[bstack1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬ᷼")] = bstack1lll1ll111l_opy_()
            bstack1111l1lllll_opy_[bstack1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡹ࡫ࡳࡵࡪࡸࡦࡇࡻࡩ࡭ࡦࡘࡹ࡮ࡪ᷽ࠧ")] = bstack11111ll11l_opy_
            bstack1111l1lllll_opy_[bstack1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡨࡵࡪ࡮ࡧࡔࡷࡵࡤࡶࡥࡷࡑࡦࡶࠧ᷾")] = bstack11lllllll_opy_
            ws_endpoint = ws_endpoint.split(bstack1l1_opy_ (u"ࠧࡤࡣࡳࡷࡂ᷿࠭"))[0] + bstack1l1_opy_ (u"ࠨࡥࡤࡴࡸࡃࠧḀ") + urllib.parse.quote(json.dumps(bstack1111l1lllll_opy_))
    return ws_endpoint
def bstack1ll111llll_opy_():
    global bstack1l1llll111_opy_
    from playwright._impl._browser_type import BrowserType
    bstack1l1llll111_opy_ = BrowserType.connect
    return bstack1l1llll111_opy_
def bstack1ll11l111l_opy_(framework_name):
    global bstack1l1l11l11l_opy_
    bstack1l1l11l11l_opy_ = framework_name
    return framework_name
def bstack1ll1ll1ll1_opy_(self, *args, **kwargs):
    global bstack1l1llll111_opy_
    try:
        global bstack1l1l11l11l_opy_
        if bstack1l1_opy_ (u"ࠩࡺࡷࡊࡴࡤࡱࡱ࡬ࡲࡹ࠭ḁ") in kwargs:
            kwargs[bstack1l1_opy_ (u"ࠪࡻࡸࡋ࡮ࡥࡲࡲ࡭ࡳࡺࠧḂ")] = bstack1111lll11l1_opy_(
                kwargs.get(bstack1l1_opy_ (u"ࠫࡼࡹࡅ࡯ࡦࡳࡳ࡮ࡴࡴࠨḃ"), None),
                bstack1l1l11l11l_opy_
            )
    except Exception as e:
        logger.error(bstack1l1_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡥ࡯ࠢࡳࡶࡴࡩࡥࡴࡵ࡬ࡲ࡬ࠦࡓࡅࡍࠣࡧࡦࡶࡳ࠻ࠢࡾࢁࠧḄ").format(str(e)))
    return bstack1l1llll111_opy_(self, *args, **kwargs)
def bstack111l1l1l1ll_opy_(bstack1111ll11lll_opy_, proxies):
    proxy_settings = {}
    try:
        if not proxies:
            proxies = bstack1111ll1lll_opy_(bstack1111ll11lll_opy_, bstack1l1_opy_ (u"ࠨࠢḅ"))
        if proxies and proxies.get(bstack1l1_opy_ (u"ࠢࡩࡶࡷࡴࡸࠨḆ")):
            parsed_url = urlparse(proxies.get(bstack1l1_opy_ (u"ࠣࡪࡷࡸࡵࡹࠢḇ")))
            if parsed_url and parsed_url.hostname: proxy_settings[bstack1l1_opy_ (u"ࠩࡳࡶࡴࡾࡹࡉࡱࡶࡸࠬḈ")] = str(parsed_url.hostname)
            if parsed_url and parsed_url.port: proxy_settings[bstack1l1_opy_ (u"ࠪࡴࡷࡵࡸࡺࡒࡲࡶࡹ࠭ḉ")] = str(parsed_url.port)
            if parsed_url and parsed_url.username: proxy_settings[bstack1l1_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡘࡷࡪࡸࠧḊ")] = str(parsed_url.username)
            if parsed_url and parsed_url.password: proxy_settings[bstack1l1_opy_ (u"ࠬࡶࡲࡰࡺࡼࡔࡦࡹࡳࠨḋ")] = str(parsed_url.password)
        return proxy_settings
    except:
        return proxy_settings
def bstack111l1l1l11_opy_(bstack1111ll11lll_opy_):
    bstack1111ll111l1_opy_ = {
        bstack11l1l1l1l1l_opy_[bstack1111l1l1ll1_opy_]: bstack1111ll11lll_opy_[bstack1111l1l1ll1_opy_]
        for bstack1111l1l1ll1_opy_ in bstack1111ll11lll_opy_
        if bstack1111l1l1ll1_opy_ in bstack11l1l1l1l1l_opy_
    }
    bstack1111ll111l1_opy_[bstack1l1_opy_ (u"ࠨࡰࡳࡱࡻࡽࡘ࡫ࡴࡵ࡫ࡱ࡫ࡸࠨḌ")] = bstack111l1l1l1ll_opy_(bstack1111ll11lll_opy_, bstack11l11111_opy_.get_property(bstack1l1_opy_ (u"ࠢࡱࡴࡲࡼࡾ࡙ࡥࡵࡶ࡬ࡲ࡬ࡹࠢḍ")))
    bstack111l111lll1_opy_ = [element.lower() for element in bstack11l11l1llll_opy_]
    bstack111l11lllll_opy_(bstack1111ll111l1_opy_, bstack111l111lll1_opy_)
    return bstack1111ll111l1_opy_
def bstack111l11lllll_opy_(d, keys):
    for key in list(d.keys()):
        if key.lower() in keys:
            d[key] = bstack1l1_opy_ (u"ࠣࠬ࠭࠮࠯ࠨḎ")
    for value in d.values():
        if isinstance(value, dict):
            bstack111l11lllll_opy_(value, keys)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    bstack111l11lllll_opy_(item, keys)
def bstack1l1llll1111_opy_():
    bstack111l11l11l1_opy_ = [os.environ.get(bstack1l1_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡈࡌࡐࡊ࡙࡟ࡅࡋࡕࠦḏ")), os.path.join(os.path.expanduser(bstack1l1_opy_ (u"ࠥࢂࠧḐ")), bstack1l1_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫḑ")), os.path.join(bstack1l1_opy_ (u"ࠬ࠵ࡴ࡮ࡲࠪḒ"), bstack1l1_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ḓ"))]
    for path in bstack111l11l11l1_opy_:
        if path is None:
            continue
        try:
            if os.path.exists(path):
                logger.debug(bstack1l1_opy_ (u"ࠢࡇ࡫࡯ࡩࠥ࠭ࠢḔ") + str(path) + bstack1l1_opy_ (u"ࠣࠩࠣࡩࡽ࡯ࡳࡵࡵ࠱ࠦḕ"))
                if not os.access(path, os.W_OK):
                    logger.debug(bstack1l1_opy_ (u"ࠤࡊ࡭ࡻ࡯࡮ࡨࠢࡳࡩࡷࡳࡩࡴࡵ࡬ࡳࡳࡹࠠࡧࡱࡵࠤࠬࠨḖ") + str(path) + bstack1l1_opy_ (u"ࠥࠫࠧḗ"))
                    os.chmod(path, 0o777)
                else:
                    logger.debug(bstack1l1_opy_ (u"ࠦࡋ࡯࡬ࡦࠢࠪࠦḘ") + str(path) + bstack1l1_opy_ (u"ࠧ࠭ࠠࡢ࡮ࡵࡩࡦࡪࡹࠡࡪࡤࡷࠥࡺࡨࡦࠢࡵࡩࡶࡻࡩࡳࡧࡧࠤࡵ࡫ࡲ࡮࡫ࡶࡷ࡮ࡵ࡮ࡴ࠰ࠥḙ"))
            else:
                logger.debug(bstack1l1_opy_ (u"ࠨࡃࡳࡧࡤࡸ࡮ࡴࡧࠡࡨ࡬ࡰࡪࠦࠧࠣḚ") + str(path) + bstack1l1_opy_ (u"ࠢࠨࠢࡺ࡭ࡹ࡮ࠠࡸࡴ࡬ࡸࡪࠦࡰࡦࡴࡰ࡭ࡸࡹࡩࡰࡰ࠱ࠦḛ"))
                os.makedirs(path, exist_ok=True)
                os.chmod(path, 0o777)
            logger.debug(bstack1l1_opy_ (u"ࠣࡑࡳࡩࡷࡧࡴࡪࡱࡱࠤࡸࡻࡣࡤࡧࡨࡨࡪࡪࠠࡧࡱࡵࠤࠬࠨḜ") + str(path) + bstack1l1_opy_ (u"ࠤࠪ࠲ࠧḝ"))
            return path
        except Exception as e:
            logger.debug(bstack1l1_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡳࡦࡶࠣࡹࡵࠦࡦࡪ࡮ࡨࠤࠬࢁࡰࡢࡶ࡫ࢁࠬࡀࠠࠣḞ") + str(e) + bstack1l1_opy_ (u"ࠦࠧḟ"))
    logger.debug(bstack1l1_opy_ (u"ࠧࡇ࡬࡭ࠢࡳࡥࡹ࡮ࡳࠡࡨࡤ࡭ࡱ࡫ࡤ࠯ࠤḠ"))
    return None
@measure(event_name=EVENTS.bstack11l1l1111l1_opy_, stage=STAGE.bstack1lllll1l1l_opy_)
def bstack1l1l11111l1_opy_(binary_path, bstack1l1l1ll1l11_opy_, bs_config):
    logger.debug(bstack1l1_opy_ (u"ࠨࡃࡶࡴࡵࡩࡳࡺࠠࡄࡎࡌࠤࡕࡧࡴࡩࠢࡩࡳࡺࡴࡤ࠻ࠢࡾࢁࠧḡ").format(binary_path))
    bstack111l1l111ll_opy_ = bstack1l1_opy_ (u"ࠧࠨḢ")
    bstack1111l11lll1_opy_ = {
        bstack1l1_opy_ (u"ࠨࡵࡧ࡯ࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭ḣ"): __version__,
        bstack1l1_opy_ (u"ࠤࡲࡷࠧḤ"): platform.system(),
        bstack1l1_opy_ (u"ࠥࡳࡸࡥࡡࡳࡥ࡫ࠦḥ"): platform.machine(),
        bstack1l1_opy_ (u"ࠦࡨࡲࡩࡠࡸࡨࡶࡸ࡯࡯࡯ࠤḦ"): bstack1l1_opy_ (u"ࠬ࠶ࠧḧ"),
        bstack1l1_opy_ (u"ࠨࡳࡥ࡭ࡢࡰࡦࡴࡧࡶࡣࡪࡩࠧḨ"): bstack1l1_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧḩ")
    }
    bstack1111ll11l11_opy_(bstack1111l11lll1_opy_)
    try:
        if binary_path:
            bstack1111l11lll1_opy_[bstack1l1_opy_ (u"ࠨࡥ࡯࡭ࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭Ḫ")] = subprocess.check_output([binary_path, bstack1l1_opy_ (u"ࠤࡹࡩࡷࡹࡩࡰࡰࠥḫ")]).strip().decode(bstack1l1_opy_ (u"ࠪࡹࡹ࡬࠭࠹ࠩḬ"))
        response = requests.request(
            bstack1l1_opy_ (u"ࠫࡌࡋࡔࠨḭ"),
            url=bstack11ll1ll1ll_opy_(bstack11l11llll1l_opy_),
            headers=None,
            auth=(bs_config[bstack1l1_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧḮ")], bs_config[bstack1l1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩḯ")]),
            json=None,
            params=bstack1111l11lll1_opy_
        )
        data = response.json()
        if response.status_code == 200 and bstack1l1_opy_ (u"ࠧࡶࡴ࡯ࠫḰ") in data.keys() and bstack1l1_opy_ (u"ࠨࡷࡳࡨࡦࡺࡥࡥࡡࡦࡰ࡮ࡥࡶࡦࡴࡶ࡭ࡴࡴࠧḱ") in data.keys():
            logger.debug(bstack1l1_opy_ (u"ࠤࡑࡩࡪࡪࠠࡵࡱࠣࡹࡵࡪࡡࡵࡧࠣࡦ࡮ࡴࡡࡳࡻ࠯ࠤࡨࡻࡲࡳࡧࡱࡸࠥࡨࡩ࡯ࡣࡵࡽࠥࡼࡥࡳࡵ࡬ࡳࡳࡀࠠࡼࡿࠥḲ").format(bstack1111l11lll1_opy_[bstack1l1_opy_ (u"ࠪࡧࡱ࡯࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨḳ")]))
            if bstack1l1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡆࡎࡔࡁࡓ࡛ࡢ࡙ࡗࡒࠧḴ") in os.environ:
                logger.debug(bstack1l1_opy_ (u"࡙ࠧ࡫ࡪࡲࡳ࡭ࡳ࡭ࠠࡣ࡫ࡱࡥࡷࡿࠠࡥࡱࡺࡲࡱࡵࡡࡥࠢࡤࡷࠥࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡇࡏࡎࡂࡔ࡜ࡣ࡚ࡘࡌࠡ࡫ࡶࠤࡸ࡫ࡴࠣḵ"))
                data[bstack1l1_opy_ (u"࠭ࡵࡳ࡮ࠪḶ")] = os.environ[bstack1l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡂࡊࡐࡄࡖ࡞ࡥࡕࡓࡎࠪḷ")]
            bstack111l1l111l1_opy_ = bstack111l11ll11l_opy_(data[bstack1l1_opy_ (u"ࠨࡷࡵࡰࠬḸ")], bstack1l1l1ll1l11_opy_)
            bstack111l1l111ll_opy_ = os.path.join(bstack1l1l1ll1l11_opy_, bstack111l1l111l1_opy_)
            os.chmod(bstack111l1l111ll_opy_, 0o777) # bstack1111ll1lll1_opy_ permission
            return bstack111l1l111ll_opy_
    except Exception as e:
        logger.debug(bstack1l1_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡹ࡫࡭ࡱ࡫ࠠࡥࡱࡺࡲࡱࡵࡡࡥ࡫ࡱ࡫ࠥࡴࡥࡸࠢࡖࡈࡐࠦࡻࡾࠤḹ").format(e))
    return binary_path
def bstack1111ll11l11_opy_(bstack1111l11lll1_opy_):
    try:
        if bstack1l1_opy_ (u"ࠪࡰ࡮ࡴࡵࡹࠩḺ") not in bstack1111l11lll1_opy_[bstack1l1_opy_ (u"ࠫࡴࡹࠧḻ")].lower():
            return
        if os.path.exists(bstack1l1_opy_ (u"ࠧ࠵ࡥࡵࡥ࠲ࡳࡸ࠳ࡲࡦ࡮ࡨࡥࡸ࡫ࠢḼ")):
            with open(bstack1l1_opy_ (u"ࠨ࠯ࡦࡶࡦ࠳ࡴࡹ࠭ࡳࡧ࡯ࡩࡦࡹࡥࠣḽ"), bstack1l1_opy_ (u"ࠢࡳࠤḾ")) as f:
                bstack1111ll11l1l_opy_ = {}
                for line in f:
                    if bstack1l1_opy_ (u"ࠣ࠿ࠥḿ") in line:
                        key, value = line.rstrip().split(bstack1l1_opy_ (u"ࠤࡀࠦṀ"), 1)
                        bstack1111ll11l1l_opy_[key] = value.strip(bstack1l1_opy_ (u"ࠪࠦࡡ࠭ࠧṁ"))
                bstack1111l11lll1_opy_[bstack1l1_opy_ (u"ࠫࡩ࡯ࡳࡵࡴࡲࠫṂ")] = bstack1111ll11l1l_opy_.get(bstack1l1_opy_ (u"ࠧࡏࡄࠣṃ"), bstack1l1_opy_ (u"ࠨࠢṄ"))
        elif os.path.exists(bstack1l1_opy_ (u"ࠢ࠰ࡧࡷࡧ࠴ࡧ࡬ࡱ࡫ࡱࡩ࠲ࡸࡥ࡭ࡧࡤࡷࡪࠨṅ")):
            bstack1111l11lll1_opy_[bstack1l1_opy_ (u"ࠨࡦ࡬ࡷࡹࡸ࡯ࠨṆ")] = bstack1l1_opy_ (u"ࠩࡤࡰࡵ࡯࡮ࡦࠩṇ")
    except Exception as e:
        logger.debug(bstack1l1_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡧࡦࡶࠣࡨ࡮ࡹࡴࡳࡱࠣࡳ࡫ࠦ࡬ࡪࡰࡸࡼࠧṈ") + e)
@measure(event_name=EVENTS.bstack11l11ll1ll1_opy_, stage=STAGE.bstack1lllll1l1l_opy_)
def bstack111l11ll11l_opy_(bstack1111l1llll1_opy_, bstack111l1l11111_opy_):
    logger.debug(bstack1l1_opy_ (u"ࠦࡉࡵࡷ࡯࡮ࡲࡥࡩ࡯࡮ࡨࠢࡖࡈࡐࠦࡢࡪࡰࡤࡶࡾࠦࡦࡳࡱࡰ࠾ࠥࠨṉ") + str(bstack1111l1llll1_opy_) + bstack1l1_opy_ (u"ࠧࠨṊ"))
    zip_path = os.path.join(bstack111l1l11111_opy_, bstack1l1_opy_ (u"ࠨࡤࡰࡹࡱࡰࡴࡧࡤࡦࡦࡢࡪ࡮ࡲࡥ࠯ࡼ࡬ࡴࠧṋ"))
    bstack111l1l111l1_opy_ = bstack1l1_opy_ (u"ࠧࠨṌ")
    with requests.get(bstack1111l1llll1_opy_, stream=True) as response:
        response.raise_for_status()
        with open(zip_path, bstack1l1_opy_ (u"ࠣࡹࡥࠦṍ")) as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
        logger.debug(bstack1l1_opy_ (u"ࠤࡉ࡭ࡱ࡫ࠠࡥࡱࡺࡲࡱࡵࡡࡥࡧࡧࠤࡸࡻࡣࡤࡧࡶࡷ࡫ࡻ࡬࡭ࡻ࠱ࠦṎ"))
    with zipfile.ZipFile(zip_path, bstack1l1_opy_ (u"ࠪࡶࠬṏ")) as zip_ref:
        bstack111l1lll1ll_opy_ = zip_ref.namelist()
        if len(bstack111l1lll1ll_opy_) > 0:
            bstack111l1l111l1_opy_ = bstack111l1lll1ll_opy_[0] # bstack1111l1ll1ll_opy_ bstack11l1l1l1ll1_opy_ will be bstack111l1lll111_opy_ 1 file i.e. the binary in the zip
        zip_ref.extractall(bstack111l1l11111_opy_)
        logger.debug(bstack1l1_opy_ (u"ࠦࡋ࡯࡬ࡦࡵࠣࡷࡺࡩࡣࡦࡵࡶࡪࡺࡲ࡬ࡺࠢࡨࡼࡹࡸࡡࡤࡶࡨࡨࠥࡺ࡯ࠡࠩࠥṐ") + str(bstack111l1l11111_opy_) + bstack1l1_opy_ (u"ࠧ࠭ࠢṑ"))
    os.remove(zip_path)
    return bstack111l1l111l1_opy_
def get_cli_dir():
    bstack1111ll1ll11_opy_ = bstack1l1llll1111_opy_()
    if bstack1111ll1ll11_opy_:
        bstack1l1l1ll1l11_opy_ = os.path.join(bstack1111ll1ll11_opy_, bstack1l1_opy_ (u"ࠨࡣ࡭࡫ࠥṒ"))
        if not os.path.exists(bstack1l1l1ll1l11_opy_):
            os.makedirs(bstack1l1l1ll1l11_opy_, mode=0o777, exist_ok=True)
        return bstack1l1l1ll1l11_opy_
    else:
        raise FileNotFoundError(bstack1l1_opy_ (u"ࠢࡏࡱࠣࡻࡷ࡯ࡴࡢࡤ࡯ࡩࠥࡪࡩࡳࡧࡦࡸࡴࡸࡹࠡࡣࡹࡥ࡮ࡲࡡࡣ࡮ࡨࠤ࡫ࡵࡲࠡࡶ࡫ࡩ࡙ࠥࡄࡌࠢࡥ࡭ࡳࡧࡲࡺ࠰ࠥṓ"))
def bstack1l1l1ll1lll_opy_(bstack1l1l1ll1l11_opy_):
    bstack1l1_opy_ (u"ࠣࠤࠥࡋࡪࡺࠠࡵࡪࡨࠤࡵࡧࡴࡩࠢࡩࡳࡷࠦࡴࡩࡧࠣࡆࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࠢࡖࡈࡐࠦࡢࡪࡰࡤࡶࡾࠦࡩ࡯ࠢࡤࠤࡼࡸࡩࡵࡣࡥࡰࡪࠦࡤࡪࡴࡨࡧࡹࡵࡲࡺ࠰ࠥࠦࠧṔ")
    bstack111l111ll11_opy_ = [
        os.path.join(bstack1l1l1ll1l11_opy_, f)
        for f in os.listdir(bstack1l1l1ll1l11_opy_)
        if os.path.isfile(os.path.join(bstack1l1l1ll1l11_opy_, f)) and f.startswith(bstack1l1_opy_ (u"ࠤࡥ࡭ࡳࡧࡲࡺ࠯ࠥṕ"))
    ]
    if len(bstack111l111ll11_opy_) > 0:
        return max(bstack111l111ll11_opy_, key=os.path.getmtime) # get bstack111l1l11lll_opy_ binary
    return bstack1l1_opy_ (u"ࠥࠦṖ")
def bstack111l1ll111l_opy_():
  from selenium import webdriver
  return version.parse(webdriver.__version__)
def bstack1l1111l11l1_opy_(d, u):
  for k, v in u.items():
    if isinstance(v, collections.abc.Mapping):
      d[k] = bstack1l1111l11l1_opy_(d.get(k, {}), v)
    else:
      if isinstance(v, list):
        d[k] = d.get(k, []) + v
      else:
        d[k] = v
  return d
def bstack11ll11llll_opy_(data, keys, default=None):
    bstack1l1_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࡘࡧࡦࡦ࡮ࡼࠤ࡬࡫ࡴࠡࡣࠣࡲࡪࡹࡴࡦࡦࠣࡺࡦࡲࡵࡦࠢࡩࡶࡴࡳࠠࡢࠢࡧ࡭ࡨࡺࡩࡰࡰࡤࡶࡾࠦ࡯ࡳࠢ࡯࡭ࡸࡺ࠮ࠋࠢࠣࠤࠥࡀࡰࡢࡴࡤࡱࠥࡪࡡࡵࡣ࠽ࠤ࡙࡮ࡥࠡࡦ࡬ࡧࡹ࡯࡯࡯ࡣࡵࡽࠥࡵࡲࠡ࡮࡬ࡷࡹࠦࡴࡰࠢࡷࡶࡦࡼࡥࡳࡵࡨ࠲ࠏࠦࠠࠡࠢ࠽ࡴࡦࡸࡡ࡮ࠢ࡮ࡩࡾࡹ࠺ࠡࡃࠣࡰ࡮ࡹࡴࠡࡱࡩࠤࡰ࡫ࡹࡴ࠱࡬ࡲࡩ࡯ࡣࡦࡵࠣࡶࡪࡶࡲࡦࡵࡨࡲࡹ࡯࡮ࡨࠢࡷ࡬ࡪࠦࡰࡢࡶ࡫࠲ࠏࠦࠠࠡࠢ࠽ࡴࡦࡸࡡ࡮ࠢࡧࡩ࡫ࡧࡵ࡭ࡶ࠽ࠤ࡛ࡧ࡬ࡶࡧࠣࡸࡴࠦࡲࡦࡶࡸࡶࡳࠦࡩࡧࠢࡷ࡬ࡪࠦࡰࡢࡶ࡫ࠤࡩࡵࡥࡴࠢࡱࡳࡹࠦࡥࡹ࡫ࡶࡸ࠳ࠐࠠࠡࠢࠣ࠾ࡷ࡫ࡴࡶࡴࡱ࠾࡚ࠥࡨࡦࠢࡹࡥࡱࡻࡥࠡࡣࡷࠤࡹ࡮ࡥࠡࡰࡨࡷࡹ࡫ࡤࠡࡲࡤࡸ࡭࠲ࠠࡰࡴࠣࡨࡪ࡬ࡡࡶ࡮ࡷࠤ࡮࡬ࠠ࡯ࡱࡷࠤ࡫ࡵࡵ࡯ࡦ࠱ࠎࠥࠦࠠࠡࠤࠥࠦṗ")
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