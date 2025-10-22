# coding: UTF-8
import sys
bstack111111l_opy_ = sys.version_info [0] == 2
bstack111lll_opy_ = 2048
bstack11ll111_opy_ = 7
def bstack11l1l11_opy_ (bstack1l11111_opy_):
    global bstack11l1ll1_opy_
    bstack1l1l111_opy_ = ord (bstack1l11111_opy_ [-1])
    bstack1lll11_opy_ = bstack1l11111_opy_ [:-1]
    bstack1ll11l_opy_ = bstack1l1l111_opy_ % len (bstack1lll11_opy_)
    bstack1ll1l_opy_ = bstack1lll11_opy_ [:bstack1ll11l_opy_] + bstack1lll11_opy_ [bstack1ll11l_opy_:]
    if bstack111111l_opy_:
        bstack1ll1_opy_ = unicode () .join ([unichr (ord (char) - bstack111lll_opy_ - (bstack1l1l1l_opy_ + bstack1l1l111_opy_) % bstack11ll111_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack1ll1l_opy_)])
    else:
        bstack1ll1_opy_ = str () .join ([chr (ord (char) - bstack111lll_opy_ - (bstack1l1l1l_opy_ + bstack1l1l111_opy_) % bstack11ll111_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack1ll1l_opy_)])
    return eval (bstack1ll1_opy_)
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
from bstack_utils.constants import (bstack11lll11l1_opy_, bstack11llll111l_opy_, bstack11l1lll11_opy_,
                                    bstack11l11ll11ll_opy_, bstack11l11llllll_opy_, bstack11l1l1111l1_opy_, bstack11l1l11l11l_opy_)
from bstack_utils.measure import measure
from bstack_utils.messages import bstack11l11ll11_opy_, bstack11lllll11_opy_
from bstack_utils.proxy import bstack11l11l1111_opy_, bstack1l1lllll1l_opy_
from bstack_utils.constants import *
from bstack_utils import bstack111l11ll1l_opy_
from bstack_utils.bstack11l1ll11ll_opy_ import bstack1l11l1111_opy_
from browserstack_sdk._version import __version__
bstack111ll1ll_opy_ = Config.bstack1llll1lll_opy_()
logger = bstack111l11ll1l_opy_.get_logger(__name__, bstack111l11ll1l_opy_.bstack1l1l1l11l11_opy_())
def bstack1111l1l1l1l_opy_(config):
    return config[bstack11l1l11_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬᯧ")]
def bstack1111ll11lll_opy_(config):
    return config[bstack11l1l11_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧᯨ")]
def bstack11l1l1lll1_opy_():
    try:
        import playwright
        return True
    except ImportError:
        return False
def bstack1111l1ll111_opy_(obj):
    values = []
    bstack1111l1lll1l_opy_ = re.compile(bstack11l1l11_opy_ (u"ࡷࠨ࡞ࡄࡗࡖࡘࡔࡓ࡟ࡕࡃࡊࡣࡡࡪࠫࠥࠤᯩ"), re.I)
    for key in obj.keys():
        if bstack1111l1lll1l_opy_.match(key):
            values.append(obj[key])
    return values
def bstack1111ll1l11l_opy_(config):
    tags = []
    tags.extend(bstack1111l1ll111_opy_(os.environ))
    tags.extend(bstack1111l1ll111_opy_(config))
    return tags
def bstack1111l11ll1l_opy_(markers):
    tags = []
    for marker in markers:
        tags.append(marker.name)
    return tags
def bstack1111ll1111l_opy_(bstack1111lll1l11_opy_):
    if not bstack1111lll1l11_opy_:
        return bstack11l1l11_opy_ (u"࠭ࠧᯪ")
    return bstack11l1l11_opy_ (u"ࠢࡼࡿࠣࠬࢀࢃࠩࠣᯫ").format(bstack1111lll1l11_opy_.name, bstack1111lll1l11_opy_.email)
def bstack111l11ll111_opy_():
    try:
        repo = git.Repo(search_parent_directories=True)
        bstack111l1ll11l1_opy_ = repo.common_dir
        info = {
            bstack11l1l11_opy_ (u"ࠣࡵ࡫ࡥࠧᯬ"): repo.head.commit.hexsha,
            bstack11l1l11_opy_ (u"ࠤࡶ࡬ࡴࡸࡴࡠࡵ࡫ࡥࠧᯭ"): repo.git.rev_parse(repo.head.commit, short=True),
            bstack11l1l11_opy_ (u"ࠥࡦࡷࡧ࡮ࡤࡪࠥᯮ"): repo.active_branch.name,
            bstack11l1l11_opy_ (u"ࠦࡹࡧࡧࠣᯯ"): repo.git.describe(all=True, tags=True, exact_match=True),
            bstack11l1l11_opy_ (u"ࠧࡩ࡯࡮࡯࡬ࡸࡹ࡫ࡲࠣᯰ"): bstack1111ll1111l_opy_(repo.head.commit.committer),
            bstack11l1l11_opy_ (u"ࠨࡣࡰ࡯ࡰ࡭ࡹࡺࡥࡳࡡࡧࡥࡹ࡫ࠢᯱ"): repo.head.commit.committed_datetime.isoformat(),
            bstack11l1l11_opy_ (u"ࠢࡢࡷࡷ࡬ࡴࡸ᯲ࠢ"): bstack1111ll1111l_opy_(repo.head.commit.author),
            bstack11l1l11_opy_ (u"ࠣࡣࡸࡸ࡭ࡵࡲࡠࡦࡤࡸࡪࠨ᯳"): repo.head.commit.authored_datetime.isoformat(),
            bstack11l1l11_opy_ (u"ࠤࡦࡳࡲࡳࡩࡵࡡࡰࡩࡸࡹࡡࡨࡧࠥ᯴"): repo.head.commit.message,
            bstack11l1l11_opy_ (u"ࠥࡶࡴࡵࡴࠣ᯵"): repo.git.rev_parse(bstack11l1l11_opy_ (u"ࠦ࠲࠳ࡳࡩࡱࡺ࠱ࡹࡵࡰ࡭ࡧࡹࡩࡱࠨ᯶")),
            bstack11l1l11_opy_ (u"ࠧࡩ࡯࡮࡯ࡲࡲࡤ࡭ࡩࡵࡡࡧ࡭ࡷࠨ᯷"): bstack111l1ll11l1_opy_,
            bstack11l1l11_opy_ (u"ࠨࡷࡰࡴ࡮ࡸࡷ࡫ࡥࡠࡩ࡬ࡸࡤࡪࡩࡳࠤ᯸"): subprocess.check_output([bstack11l1l11_opy_ (u"ࠢࡨ࡫ࡷࠦ᯹"), bstack11l1l11_opy_ (u"ࠣࡴࡨࡺ࠲ࡶࡡࡳࡵࡨࠦ᯺"), bstack11l1l11_opy_ (u"ࠤ࠰࠱࡬࡯ࡴ࠮ࡥࡲࡱࡲࡵ࡮࠮ࡦ࡬ࡶࠧ᯻")]).strip().decode(
                bstack11l1l11_opy_ (u"ࠪࡹࡹ࡬࠭࠹ࠩ᯼")),
            bstack11l1l11_opy_ (u"ࠦࡱࡧࡳࡵࡡࡷࡥ࡬ࠨ᯽"): repo.git.describe(tags=True, abbrev=0, always=True),
            bstack11l1l11_opy_ (u"ࠧࡩ࡯࡮࡯࡬ࡸࡸࡥࡳࡪࡰࡦࡩࡤࡲࡡࡴࡶࡢࡸࡦ࡭ࠢ᯾"): repo.git.rev_list(
                bstack11l1l11_opy_ (u"ࠨࡻࡾ࠰࠱ࡿࢂࠨ᯿").format(repo.head.commit, repo.git.describe(tags=True, abbrev=0, always=True)), count=True)
        }
        remotes = repo.remotes
        bstack1111ll11l11_opy_ = []
        for remote in remotes:
            bstack111l11l11ll_opy_ = {
                bstack11l1l11_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᰀ"): remote.name,
                bstack11l1l11_opy_ (u"ࠣࡷࡵࡰࠧᰁ"): remote.url,
            }
            bstack1111ll11l11_opy_.append(bstack111l11l11ll_opy_)
        bstack111l1ll1l1l_opy_ = {
            bstack11l1l11_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᰂ"): bstack11l1l11_opy_ (u"ࠥ࡫࡮ࡺࠢᰃ"),
            **info,
            bstack11l1l11_opy_ (u"ࠦࡷ࡫࡭ࡰࡶࡨࡷࠧᰄ"): bstack1111ll11l11_opy_
        }
        bstack111l1ll1l1l_opy_ = bstack111l1111111_opy_(bstack111l1ll1l1l_opy_)
        return bstack111l1ll1l1l_opy_
    except git.InvalidGitRepositoryError:
        return {}
    except Exception as err:
        print(bstack11l1l11_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡵࡵࡰࡶ࡮ࡤࡸ࡮ࡴࡧࠡࡉ࡬ࡸࠥࡳࡥࡵࡣࡧࡥࡹࡧࠠࡸ࡫ࡷ࡬ࠥ࡫ࡲࡳࡱࡵ࠾ࠥࢁࡽࠣᰅ").format(err))
        return {}
def bstack11ll1l1l111_opy_(bstack1111ll1lll1_opy_=None):
    bstack11l1l11_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࡇࡦࡶࠣ࡫࡮ࡺࠠ࡮ࡧࡷࡥࡩࡧࡴࡢࠢࡶࡴࡪࡩࡩࡧ࡫ࡦࡥࡱࡲࡹࠡࡨࡲࡶࡲࡧࡴࡵࡧࡧࠤ࡫ࡵࡲࠡࡃࡌࠤࡸ࡫࡬ࡦࡥࡷ࡭ࡴࡴࠠࡶࡵࡨࠤࡨࡧࡳࡦࡵࠣࡪࡴࡸࠠࡦࡣࡦ࡬ࠥ࡬࡯࡭ࡦࡨࡶࠥ࡯࡮ࠡࡶ࡫ࡩࠥࡲࡩࡴࡶ࠱ࠎࠥࠦࠠࠡࡃࡵ࡫ࡸࡀࠊࠡࠢࠣࠤࠥࠦࠠࠡࡨࡲࡰࡩ࡫ࡲࡴࠢࠫࡰ࡮ࡹࡴ࠭ࠢࡲࡴࡹ࡯࡯࡯ࡣ࡯࠭࠿ࠦࡌࡪࡵࡷࠤࡴ࡬ࠠࡧࡱ࡯ࡨࡪࡸࠠࡱࡣࡷ࡬ࡸࠦࡴࡰࠢࡨࡼࡹࡸࡡࡤࡶࠣ࡫࡮ࡺࠠ࡮ࡧࡷࡥࡩࡧࡴࡢࠢࡩࡶࡴࡳ࠮ࠡࡆࡨࡪࡦࡻ࡬ࡵࡵࠣࡸࡴ࡛ࠦࡰࡵ࠱࡫ࡪࡺࡣࡸࡦࠫ࠭ࡢ࠴ࠊࠡࠢࠣࠤࡗ࡫ࡴࡶࡴࡱࡷ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠ࡭࡫ࡶࡸ࠿ࠦࡌࡪࡵࡷࠤࡴ࡬ࠠࡥ࡫ࡦࡸࡸ࠲ࠠࡦࡣࡦ࡬ࠥࡩ࡯࡯ࡶࡤ࡭ࡳ࡯࡮ࡨࠢࡪ࡭ࡹࠦ࡭ࡦࡶࡤࡨࡦࡺࡡࠡࡨࡲࡶࠥࡧࠠࡧࡱ࡯ࡨࡪࡸ࠮ࠋࠢࠣࠤࠥࠨࠢࠣᰆ")
    if bstack1111ll1lll1_opy_ == None: # bstack111l11ll1ll_opy_ for bstack11ll1l11lll_opy_-repo
        bstack1111ll1lll1_opy_ = [os.getcwd()]
    results = []
    for folder in bstack1111ll1lll1_opy_:
        try:
            repo = git.Repo(folder, search_parent_directories=True)
            result = {
                bstack11l1l11_opy_ (u"ࠢࡱࡴࡌࡨࠧᰇ"): bstack11l1l11_opy_ (u"ࠣࠤᰈ"),
                bstack11l1l11_opy_ (u"ࠤࡩ࡭ࡱ࡫ࡳࡄࡪࡤࡲ࡬࡫ࡤࠣᰉ"): [],
                bstack11l1l11_opy_ (u"ࠥࡥࡺࡺࡨࡰࡴࡶࠦᰊ"): [],
                bstack11l1l11_opy_ (u"ࠦࡵࡸࡄࡢࡶࡨࠦᰋ"): bstack11l1l11_opy_ (u"ࠧࠨᰌ"),
                bstack11l1l11_opy_ (u"ࠨࡣࡰ࡯ࡰ࡭ࡹࡓࡥࡴࡵࡤ࡫ࡪࡹࠢᰍ"): [],
                bstack11l1l11_opy_ (u"ࠢࡱࡴࡗ࡭ࡹࡲࡥࠣᰎ"): bstack11l1l11_opy_ (u"ࠣࠤᰏ"),
                bstack11l1l11_opy_ (u"ࠤࡳࡶࡉ࡫ࡳࡤࡴ࡬ࡴࡹ࡯࡯࡯ࠤᰐ"): bstack11l1l11_opy_ (u"ࠥࠦᰑ"),
                bstack11l1l11_opy_ (u"ࠦࡵࡸࡒࡢࡹࡇ࡭࡫࡬ࠢᰒ"): bstack11l1l11_opy_ (u"ࠧࠨᰓ")
            }
            bstack1111llll111_opy_ = repo.active_branch.name
            bstack111l1l1l11l_opy_ = repo.head.commit
            result[bstack11l1l11_opy_ (u"ࠨࡰࡳࡋࡧࠦᰔ")] = bstack111l1l1l11l_opy_.hexsha
            bstack111l111ll11_opy_ = _111l1lll11l_opy_(repo)
            logger.debug(bstack11l1l11_opy_ (u"ࠢࡃࡣࡶࡩࠥࡨࡲࡢࡰࡦ࡬ࠥ࡬࡯ࡳࠢࡦࡳࡲࡶࡡࡳ࡫ࡶࡳࡳࡀࠠࠣᰕ") + str(bstack111l111ll11_opy_) + bstack11l1l11_opy_ (u"ࠣࠤᰖ"))
            if bstack111l111ll11_opy_:
                try:
                    bstack1111ll1ll11_opy_ = repo.git.diff(bstack11l1l11_opy_ (u"ࠤ࠰࠱ࡳࡧ࡭ࡦ࠯ࡲࡲࡱࡿࠢᰗ"), bstack1lll11ll111_opy_ (u"ࠥࡿࡧࡧࡳࡦࡡࡥࡶࡦࡴࡣࡩࡿ࠱࠲࠳ࢁࡣࡶࡴࡵࡩࡳࡺ࡟ࡣࡴࡤࡲࡨ࡮ࡽࠣᰘ")).split(bstack11l1l11_opy_ (u"ࠫࡡࡴࠧᰙ"))
                    logger.debug(bstack11l1l11_opy_ (u"ࠧࡉࡨࡢࡰࡪࡩࡩࠦࡦࡪ࡮ࡨࡷࠥࡨࡥࡵࡹࡨࡩࡳࠦࡻࡣࡣࡶࡩࡤࡨࡲࡢࡰࡦ࡬ࢂࠦࡡ࡯ࡦࠣࡿࡨࡻࡲࡳࡧࡱࡸࡤࡨࡲࡢࡰࡦ࡬ࢂࡀࠠࠣᰚ") + str(bstack1111ll1ll11_opy_) + bstack11l1l11_opy_ (u"ࠨࠢᰛ"))
                    result[bstack11l1l11_opy_ (u"ࠢࡧ࡫࡯ࡩࡸࡉࡨࡢࡰࡪࡩࡩࠨᰜ")] = [f.strip() for f in bstack1111ll1ll11_opy_ if f.strip()]
                    commits = list(repo.iter_commits(bstack1lll11ll111_opy_ (u"ࠣࡽࡥࡥࡸ࡫࡟ࡣࡴࡤࡲࡨ࡮ࡽ࠯࠰ࡾࡧࡺࡸࡲࡦࡰࡷࡣࡧࡸࡡ࡯ࡥ࡫ࢁࠧᰝ")))
                except Exception:
                    logger.debug(bstack11l1l11_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥ࡭ࡥࡵࠢࡦ࡬ࡦࡴࡧࡦࡦࠣࡪ࡮ࡲࡥࡴࠢࡩࡶࡴࡳࠠࡣࡴࡤࡲࡨ࡮ࠠࡤࡱࡰࡴࡦࡸࡩࡴࡱࡱ࠲ࠥࡌࡡ࡭࡮࡬ࡲ࡬ࠦࡢࡢࡥ࡮ࠤࡹࡵࠠࡳࡧࡦࡩࡳࡺࠠࡤࡱࡰࡱ࡮ࡺࡳ࠯ࠤᰞ"))
                    commits = list(repo.iter_commits(max_count=10))
                    if commits:
                        result[bstack11l1l11_opy_ (u"ࠥࡪ࡮ࡲࡥࡴࡅ࡫ࡥࡳ࡭ࡥࡥࠤᰟ")] = _111l1111l1l_opy_(commits[:5])
            else:
                commits = list(repo.iter_commits(max_count=10))
                if commits:
                    result[bstack11l1l11_opy_ (u"ࠦ࡫࡯࡬ࡦࡵࡆ࡬ࡦࡴࡧࡦࡦࠥᰠ")] = _111l1111l1l_opy_(commits[:5])
            bstack111l11l11l1_opy_ = set()
            bstack111l1ll1l11_opy_ = []
            for commit in commits:
                logger.debug(bstack11l1l11_opy_ (u"ࠧࡖࡲࡰࡥࡨࡷࡸ࡯࡮ࡨࠢࡦࡳࡲࡳࡩࡵ࠼ࠣࠦᰡ") + str(commit.message) + bstack11l1l11_opy_ (u"ࠨࠢᰢ"))
                bstack111l1l1ll1l_opy_ = commit.author.name if commit.author else bstack11l1l11_opy_ (u"ࠢࡖࡰ࡮ࡲࡴࡽ࡮ࠣᰣ")
                bstack111l11l11l1_opy_.add(bstack111l1l1ll1l_opy_)
                bstack111l1ll1l11_opy_.append({
                    bstack11l1l11_opy_ (u"ࠣ࡯ࡨࡷࡸࡧࡧࡦࠤᰤ"): commit.message.strip(),
                    bstack11l1l11_opy_ (u"ࠤࡸࡷࡪࡸࠢᰥ"): bstack111l1l1ll1l_opy_
                })
            result[bstack11l1l11_opy_ (u"ࠥࡥࡺࡺࡨࡰࡴࡶࠦᰦ")] = list(bstack111l11l11l1_opy_)
            result[bstack11l1l11_opy_ (u"ࠦࡨࡵ࡭࡮࡫ࡷࡑࡪࡹࡳࡢࡩࡨࡷࠧᰧ")] = bstack111l1ll1l11_opy_
            result[bstack11l1l11_opy_ (u"ࠧࡶࡲࡅࡣࡷࡩࠧᰨ")] = bstack111l1l1l11l_opy_.committed_datetime.strftime(bstack11l1l11_opy_ (u"ࠨ࡚ࠥ࠯ࠨࡱ࠲ࠫࡤࠣᰩ"))
            if (not result[bstack11l1l11_opy_ (u"ࠢࡱࡴࡗ࡭ࡹࡲࡥࠣᰪ")] or result[bstack11l1l11_opy_ (u"ࠣࡲࡵࡘ࡮ࡺ࡬ࡦࠤᰫ")].strip() == bstack11l1l11_opy_ (u"ࠤࠥᰬ")) and bstack111l1l1l11l_opy_.message:
                bstack111l1l11l11_opy_ = bstack111l1l1l11l_opy_.message.strip().splitlines()
                result[bstack11l1l11_opy_ (u"ࠥࡴࡷ࡚ࡩࡵ࡮ࡨࠦᰭ")] = bstack111l1l11l11_opy_[0] if bstack111l1l11l11_opy_ else bstack11l1l11_opy_ (u"ࠦࠧᰮ")
                if len(bstack111l1l11l11_opy_) > 2:
                    result[bstack11l1l11_opy_ (u"ࠧࡶࡲࡅࡧࡶࡧࡷ࡯ࡰࡵ࡫ࡲࡲࠧᰯ")] = bstack11l1l11_opy_ (u"࠭࡜࡯ࠩᰰ").join(bstack111l1l11l11_opy_[2:]).strip()
            results.append(result)
        except Exception as err:
            logger.error(bstack11l1l11_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡰࡰࡲࡸࡰࡦࡺࡩ࡯ࡩࠣࡋ࡮ࡺࠠ࡮ࡧࡷࡥࡩࡧࡴࡢࠢࡩࡳࡷࠦࡁࡊࠢࡶࡩࡱ࡫ࡣࡵ࡫ࡲࡲࠥ࠮ࡦࡰ࡮ࡧࡩࡷࡀࠠࡼࡨࡲࡰࡩ࡫ࡲࡾࠫ࠽ࠤࠧᰱ") + str(err) + bstack11l1l11_opy_ (u"ࠣࠤᰲ"))
    filtered_results = [
        result
        for result in results
        if _1111l1l1lll_opy_(result)
    ]
    return filtered_results
def _1111l1l1lll_opy_(result):
    bstack11l1l11_opy_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࡋࡩࡱࡶࡥࡳࠢࡷࡳࠥࡩࡨࡦࡥ࡮ࠤ࡮࡬ࠠࡢࠢࡪ࡭ࡹࠦ࡭ࡦࡶࡤࡨࡦࡺࡡࠡࡴࡨࡷࡺࡲࡴࠡ࡫ࡶࠤࡻࡧ࡬ࡪࡦࠣࠬࡳࡵ࡮࠮ࡧࡰࡴࡹࡿࠠࡧ࡫࡯ࡩࡸࡉࡨࡢࡰࡪࡩࡩࠦࡡ࡯ࡦࠣࡥࡺࡺࡨࡰࡴࡶ࠭࠳ࠐࠠࠡࠢࠣࠦࠧࠨᰳ")
    return (
        isinstance(result.get(bstack11l1l11_opy_ (u"ࠥࡪ࡮ࡲࡥࡴࡅ࡫ࡥࡳ࡭ࡥࡥࠤᰴ"), None), list)
        and len(result[bstack11l1l11_opy_ (u"ࠦ࡫࡯࡬ࡦࡵࡆ࡬ࡦࡴࡧࡦࡦࠥᰵ")]) > 0
        and isinstance(result.get(bstack11l1l11_opy_ (u"ࠧࡧࡵࡵࡪࡲࡶࡸࠨᰶ"), None), list)
        and len(result[bstack11l1l11_opy_ (u"ࠨࡡࡶࡶ࡫ࡳࡷࡹ᰷ࠢ")]) > 0
    )
def _111l1lll11l_opy_(repo):
    bstack11l1l11_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࡕࡴࡼࠤࡹࡵࠠࡥࡧࡷࡩࡷࡳࡩ࡯ࡧࠣࡸ࡭࡫ࠠࡣࡣࡶࡩࠥࡨࡲࡢࡰࡦ࡬ࠥ࡬࡯ࡳࠢࡷ࡬ࡪࠦࡧࡪࡸࡨࡲࠥࡸࡥࡱࡱࠣࡻ࡮ࡺࡨࡰࡷࡷࠤ࡭ࡧࡲࡥࡥࡲࡨࡪࡪࠠ࡯ࡣࡰࡩࡸࠦࡡ࡯ࡦࠣࡻࡴࡸ࡫ࠡࡹ࡬ࡸ࡭ࠦࡡ࡭࡮࡚ࠣࡈ࡙ࠠࡱࡴࡲࡺ࡮ࡪࡥࡳࡵ࠱ࠎࠥࠦࠠࠡࡔࡨࡸࡺࡸ࡮ࡴࠢࡷ࡬ࡪࠦࡤࡦࡨࡤࡹࡱࡺࠠࡣࡴࡤࡲࡨ࡮ࠠࡪࡨࠣࡴࡴࡹࡳࡪࡤ࡯ࡩ࠱ࠦࡥ࡭ࡵࡨࠤࡓࡵ࡮ࡦ࠰ࠍࠤࠥࠦࠠࠣࠤࠥ᰸")
    try:
        try:
            origin = repo.remotes.origin
            bstack111l11111ll_opy_ = origin.refs[bstack11l1l11_opy_ (u"ࠨࡊࡈࡅࡉ࠭᰹")]
            target = bstack111l11111ll_opy_.reference.name
            if target.startswith(bstack11l1l11_opy_ (u"ࠩࡲࡶ࡮࡭ࡩ࡯࠱ࠪ᰺")):
                return target
        except Exception:
            pass
        if repo.remotes and repo.remotes.origin.refs:
            for ref in repo.remotes.origin.refs:
                if ref.name.startswith(bstack11l1l11_opy_ (u"ࠪࡳࡷ࡯ࡧࡪࡰ࠲ࠫ᰻")):
                    return ref.name
        if repo.heads:
            return repo.heads[0].name
    except Exception:
        pass
    return None
def _111l1111l1l_opy_(commits):
    bstack11l1l11_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࡌ࡫ࡴࠡ࡮࡬ࡷࡹࠦ࡯ࡧࠢࡦ࡬ࡦࡴࡧࡦࡦࠣࡪ࡮ࡲࡥࡴࠢࡩࡶࡴࡳࠠࡢࠢ࡯࡭ࡸࡺࠠࡰࡨࠣࡧࡴࡳ࡭ࡪࡶࡶ࠲ࠏࠦࠠࠡࠢࠥࠦࠧ᰼")
    bstack1111ll1ll11_opy_ = set()
    try:
        for commit in commits:
            if commit.parents:
                for parent in commit.parents:
                    diff = commit.diff(parent)
                    for bstack1111l11l111_opy_ in diff:
                        if bstack1111l11l111_opy_.a_path:
                            bstack1111ll1ll11_opy_.add(bstack1111l11l111_opy_.a_path)
                        if bstack1111l11l111_opy_.b_path:
                            bstack1111ll1ll11_opy_.add(bstack1111l11l111_opy_.b_path)
    except Exception:
        pass
    return list(bstack1111ll1ll11_opy_)
def bstack111l1111111_opy_(bstack111l1ll1l1l_opy_):
    bstack1111ll11ll1_opy_ = bstack111l1ll111l_opy_(bstack111l1ll1l1l_opy_)
    if bstack1111ll11ll1_opy_ and bstack1111ll11ll1_opy_ > bstack11l11ll11ll_opy_:
        bstack111l1ll1ll1_opy_ = bstack1111ll11ll1_opy_ - bstack11l11ll11ll_opy_
        bstack111l111l1l1_opy_ = bstack111l111lll1_opy_(bstack111l1ll1l1l_opy_[bstack11l1l11_opy_ (u"ࠧࡩ࡯࡮࡯࡬ࡸࡤࡳࡥࡴࡵࡤ࡫ࡪࠨ᰽")], bstack111l1ll1ll1_opy_)
        bstack111l1ll1l1l_opy_[bstack11l1l11_opy_ (u"ࠨࡣࡰ࡯ࡰ࡭ࡹࡥ࡭ࡦࡵࡶࡥ࡬࡫ࠢ᰾")] = bstack111l111l1l1_opy_
        logger.info(bstack11l1l11_opy_ (u"ࠢࡕࡪࡨࠤࡨࡵ࡭࡮࡫ࡷࠤ࡭ࡧࡳࠡࡤࡨࡩࡳࠦࡴࡳࡷࡱࡧࡦࡺࡥࡥ࠰ࠣࡗ࡮ࢀࡥࠡࡱࡩࠤࡨࡵ࡭࡮࡫ࡷࠤࡦ࡬ࡴࡦࡴࠣࡸࡷࡻ࡮ࡤࡣࡷ࡭ࡴࡴࠠࡪࡵࠣࡿࢂࠦࡋࡃࠤ᰿")
                    .format(bstack111l1ll111l_opy_(bstack111l1ll1l1l_opy_) / 1024))
    return bstack111l1ll1l1l_opy_
def bstack111l1ll111l_opy_(json_data):
    try:
        if json_data:
            bstack111l1l1ll11_opy_ = json.dumps(json_data)
            bstack1111l111lll_opy_ = sys.getsizeof(bstack111l1l1ll11_opy_)
            return bstack1111l111lll_opy_
    except Exception as e:
        logger.debug(bstack11l1l11_opy_ (u"ࠣࡕࡲࡱࡪࡺࡨࡪࡰࡪࠤࡼ࡫࡮ࡵࠢࡺࡶࡴࡴࡧࠡࡹ࡫࡭ࡱ࡫ࠠࡤࡣ࡯ࡧࡺࡲࡡࡵ࡫ࡱ࡫ࠥࡹࡩࡻࡧࠣࡳ࡫ࠦࡊࡔࡑࡑࠤࡴࡨࡪࡦࡥࡷ࠾ࠥࢁࡽࠣ᱀").format(e))
    return -1
def bstack111l111lll1_opy_(field, bstack1111lll1l1l_opy_):
    try:
        bstack111l11ll1l1_opy_ = len(bytes(bstack11l11llllll_opy_, bstack11l1l11_opy_ (u"ࠩࡸࡸ࡫࠳࠸ࠨ᱁")))
        bstack1111l111l1l_opy_ = bytes(field, bstack11l1l11_opy_ (u"ࠪࡹࡹ࡬࠭࠹ࠩ᱂"))
        bstack1111l1l11ll_opy_ = len(bstack1111l111l1l_opy_)
        bstack1111l11l11l_opy_ = ceil(bstack1111l1l11ll_opy_ - bstack1111lll1l1l_opy_ - bstack111l11ll1l1_opy_)
        if bstack1111l11l11l_opy_ > 0:
            bstack111l11l1lll_opy_ = bstack1111l111l1l_opy_[:bstack1111l11l11l_opy_].decode(bstack11l1l11_opy_ (u"ࠫࡺࡺࡦ࠮࠺ࠪ᱃"), errors=bstack11l1l11_opy_ (u"ࠬ࡯ࡧ࡯ࡱࡵࡩࠬ᱄")) + bstack11l11llllll_opy_
            return bstack111l11l1lll_opy_
    except Exception as e:
        logger.debug(bstack11l1l11_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡽࡨࡪ࡮ࡨࠤࡹࡸࡵ࡯ࡥࡤࡸ࡮ࡴࡧࠡࡨ࡬ࡩࡱࡪࠬࠡࡰࡲࡸ࡭࡯࡮ࡨࠢࡺࡥࡸࠦࡴࡳࡷࡱࡧࡦࡺࡥࡥࠢ࡫ࡩࡷ࡫࠺ࠡࡽࢀࠦ᱅").format(e))
    return field
def bstack1l1l1l1l1_opy_():
    env = os.environ
    if (bstack11l1l11_opy_ (u"ࠢࡋࡇࡑࡏࡎࡔࡓࡠࡗࡕࡐࠧ᱆") in env and len(env[bstack11l1l11_opy_ (u"ࠣࡌࡈࡒࡐࡏࡎࡔࡡࡘࡖࡑࠨ᱇")]) > 0) or (
            bstack11l1l11_opy_ (u"ࠤࡍࡉࡓࡑࡉࡏࡕࡢࡌࡔࡓࡅࠣ᱈") in env and len(env[bstack11l1l11_opy_ (u"ࠥࡎࡊࡔࡋࡊࡐࡖࡣࡍࡕࡍࡆࠤ᱉")]) > 0):
        return {
            bstack11l1l11_opy_ (u"ࠦࡳࡧ࡭ࡦࠤ᱊"): bstack11l1l11_opy_ (u"ࠧࡐࡥ࡯࡭࡬ࡲࡸࠨ᱋"),
            bstack11l1l11_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤ᱌"): env.get(bstack11l1l11_opy_ (u"ࠢࡃࡗࡌࡐࡉࡥࡕࡓࡎࠥᱍ")),
            bstack11l1l11_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᱎ"): env.get(bstack11l1l11_opy_ (u"ࠤࡍࡓࡇࡥࡎࡂࡏࡈࠦᱏ")),
            bstack11l1l11_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤ᱐"): env.get(bstack11l1l11_opy_ (u"ࠦࡇ࡛ࡉࡍࡆࡢࡒ࡚ࡓࡂࡆࡔࠥ᱑"))
        }
    if env.get(bstack11l1l11_opy_ (u"ࠧࡉࡉࠣ᱒")) == bstack11l1l11_opy_ (u"ࠨࡴࡳࡷࡨࠦ᱓") and bstack1111ll111l_opy_(env.get(bstack11l1l11_opy_ (u"ࠢࡄࡋࡕࡇࡑࡋࡃࡊࠤ᱔"))):
        return {
            bstack11l1l11_opy_ (u"ࠣࡰࡤࡱࡪࠨ᱕"): bstack11l1l11_opy_ (u"ࠤࡆ࡭ࡷࡩ࡬ࡦࡅࡌࠦ᱖"),
            bstack11l1l11_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨ᱗"): env.get(bstack11l1l11_opy_ (u"ࠦࡈࡏࡒࡄࡎࡈࡣࡇ࡛ࡉࡍࡆࡢ࡙ࡗࡒࠢ᱘")),
            bstack11l1l11_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢ᱙"): env.get(bstack11l1l11_opy_ (u"ࠨࡃࡊࡔࡆࡐࡊࡥࡊࡐࡄࠥᱚ")),
            bstack11l1l11_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᱛ"): env.get(bstack11l1l11_opy_ (u"ࠣࡅࡌࡖࡈࡒࡅࡠࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࠦᱜ"))
        }
    if env.get(bstack11l1l11_opy_ (u"ࠤࡆࡍࠧᱝ")) == bstack11l1l11_opy_ (u"ࠥࡸࡷࡻࡥࠣᱞ") and bstack1111ll111l_opy_(env.get(bstack11l1l11_opy_ (u"࡙ࠦࡘࡁࡗࡋࡖࠦᱟ"))):
        return {
            bstack11l1l11_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᱠ"): bstack11l1l11_opy_ (u"ࠨࡔࡳࡣࡹ࡭ࡸࠦࡃࡊࠤᱡ"),
            bstack11l1l11_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᱢ"): env.get(bstack11l1l11_opy_ (u"ࠣࡖࡕࡅ࡛ࡏࡓࡠࡄࡘࡍࡑࡊ࡟ࡘࡇࡅࡣ࡚ࡘࡌࠣᱣ")),
            bstack11l1l11_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᱤ"): env.get(bstack11l1l11_opy_ (u"ࠥࡘࡗࡇࡖࡊࡕࡢࡎࡔࡈ࡟ࡏࡃࡐࡉࠧᱥ")),
            bstack11l1l11_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᱦ"): env.get(bstack11l1l11_opy_ (u"࡚ࠧࡒࡂࡘࡌࡗࡤࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࡃࡇࡕࠦᱧ"))
        }
    if env.get(bstack11l1l11_opy_ (u"ࠨࡃࡊࠤᱨ")) == bstack11l1l11_opy_ (u"ࠢࡵࡴࡸࡩࠧᱩ") and env.get(bstack11l1l11_opy_ (u"ࠣࡅࡌࡣࡓࡇࡍࡆࠤᱪ")) == bstack11l1l11_opy_ (u"ࠤࡦࡳࡩ࡫ࡳࡩ࡫ࡳࠦᱫ"):
        return {
            bstack11l1l11_opy_ (u"ࠥࡲࡦࡳࡥࠣᱬ"): bstack11l1l11_opy_ (u"ࠦࡈࡵࡤࡦࡵ࡫࡭ࡵࠨᱭ"),
            bstack11l1l11_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣᱮ"): None,
            bstack11l1l11_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᱯ"): None,
            bstack11l1l11_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᱰ"): None
        }
    if env.get(bstack11l1l11_opy_ (u"ࠣࡄࡌࡘࡇ࡛ࡃࡌࡇࡗࡣࡇࡘࡁࡏࡅࡋࠦᱱ")) and env.get(bstack11l1l11_opy_ (u"ࠤࡅࡍ࡙ࡈࡕࡄࡍࡈࡘࡤࡉࡏࡎࡏࡌࡘࠧᱲ")):
        return {
            bstack11l1l11_opy_ (u"ࠥࡲࡦࡳࡥࠣᱳ"): bstack11l1l11_opy_ (u"ࠦࡇ࡯ࡴࡣࡷࡦ࡯ࡪࡺࠢᱴ"),
            bstack11l1l11_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣᱵ"): env.get(bstack11l1l11_opy_ (u"ࠨࡂࡊࡖࡅ࡙ࡈࡑࡅࡕࡡࡊࡍ࡙ࡥࡈࡕࡖࡓࡣࡔࡘࡉࡈࡋࡑࠦᱶ")),
            bstack11l1l11_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᱷ"): None,
            bstack11l1l11_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᱸ"): env.get(bstack11l1l11_opy_ (u"ࠤࡅࡍ࡙ࡈࡕࡄࡍࡈࡘࡤࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࡃࡇࡕࠦᱹ"))
        }
    if env.get(bstack11l1l11_opy_ (u"ࠥࡇࡎࠨᱺ")) == bstack11l1l11_opy_ (u"ࠦࡹࡸࡵࡦࠤᱻ") and bstack1111ll111l_opy_(env.get(bstack11l1l11_opy_ (u"ࠧࡊࡒࡐࡐࡈࠦᱼ"))):
        return {
            bstack11l1l11_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᱽ"): bstack11l1l11_opy_ (u"ࠢࡅࡴࡲࡲࡪࠨ᱾"),
            bstack11l1l11_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦ᱿"): env.get(bstack11l1l11_opy_ (u"ࠤࡇࡖࡔࡔࡅࡠࡄࡘࡍࡑࡊ࡟ࡍࡋࡑࡏࠧᲀ")),
            bstack11l1l11_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᲁ"): None,
            bstack11l1l11_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᲂ"): env.get(bstack11l1l11_opy_ (u"ࠧࡊࡒࡐࡐࡈࡣࡇ࡛ࡉࡍࡆࡢࡒ࡚ࡓࡂࡆࡔࠥᲃ"))
        }
    if env.get(bstack11l1l11_opy_ (u"ࠨࡃࡊࠤᲄ")) == bstack11l1l11_opy_ (u"ࠢࡵࡴࡸࡩࠧᲅ") and bstack1111ll111l_opy_(env.get(bstack11l1l11_opy_ (u"ࠣࡕࡈࡑࡆࡖࡈࡐࡔࡈࠦᲆ"))):
        return {
            bstack11l1l11_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᲇ"): bstack11l1l11_opy_ (u"ࠥࡗࡪࡳࡡࡱࡪࡲࡶࡪࠨᲈ"),
            bstack11l1l11_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᲉ"): env.get(bstack11l1l11_opy_ (u"࡙ࠧࡅࡎࡃࡓࡌࡔࡘࡅࡠࡑࡕࡋࡆࡔࡉ࡛ࡃࡗࡍࡔࡔ࡟ࡖࡔࡏࠦᲊ")),
            bstack11l1l11_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣ᲋"): env.get(bstack11l1l11_opy_ (u"ࠢࡔࡇࡐࡅࡕࡎࡏࡓࡇࡢࡎࡔࡈ࡟ࡏࡃࡐࡉࠧ᲌")),
            bstack11l1l11_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢ᲍"): env.get(bstack11l1l11_opy_ (u"ࠤࡖࡉࡒࡇࡐࡉࡑࡕࡉࡤࡐࡏࡃࡡࡌࡈࠧ᲎"))
        }
    if env.get(bstack11l1l11_opy_ (u"ࠥࡇࡎࠨ᲏")) == bstack11l1l11_opy_ (u"ࠦࡹࡸࡵࡦࠤᲐ") and bstack1111ll111l_opy_(env.get(bstack11l1l11_opy_ (u"ࠧࡍࡉࡕࡎࡄࡆࡤࡉࡉࠣᲑ"))):
        return {
            bstack11l1l11_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᲒ"): bstack11l1l11_opy_ (u"ࠢࡈ࡫ࡷࡐࡦࡨࠢᲓ"),
            bstack11l1l11_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᲔ"): env.get(bstack11l1l11_opy_ (u"ࠤࡆࡍࡤࡐࡏࡃࡡࡘࡖࡑࠨᲕ")),
            bstack11l1l11_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᲖ"): env.get(bstack11l1l11_opy_ (u"ࠦࡈࡏ࡟ࡋࡑࡅࡣࡓࡇࡍࡆࠤᲗ")),
            bstack11l1l11_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᲘ"): env.get(bstack11l1l11_opy_ (u"ࠨࡃࡊࡡࡍࡓࡇࡥࡉࡅࠤᲙ"))
        }
    if env.get(bstack11l1l11_opy_ (u"ࠢࡄࡋࠥᲚ")) == bstack11l1l11_opy_ (u"ࠣࡶࡵࡹࡪࠨᲛ") and bstack1111ll111l_opy_(env.get(bstack11l1l11_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡌࡋࡗࡉࠧᲜ"))):
        return {
            bstack11l1l11_opy_ (u"ࠥࡲࡦࡳࡥࠣᲝ"): bstack11l1l11_opy_ (u"ࠦࡇࡻࡩ࡭ࡦ࡮࡭ࡹ࡫ࠢᲞ"),
            bstack11l1l11_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣᲟ"): env.get(bstack11l1l11_opy_ (u"ࠨࡂࡖࡋࡏࡈࡐࡏࡔࡆࡡࡅ࡙ࡎࡒࡄࡠࡗࡕࡐࠧᲠ")),
            bstack11l1l11_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᲡ"): env.get(bstack11l1l11_opy_ (u"ࠣࡄࡘࡍࡑࡊࡋࡊࡖࡈࡣࡑࡇࡂࡆࡎࠥᲢ")) or env.get(bstack11l1l11_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡌࡋࡗࡉࡤࡖࡉࡑࡇࡏࡍࡓࡋ࡟ࡏࡃࡐࡉࠧᲣ")),
            bstack11l1l11_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤᲤ"): env.get(bstack11l1l11_opy_ (u"ࠦࡇ࡛ࡉࡍࡆࡎࡍ࡙ࡋ࡟ࡃࡗࡌࡐࡉࡥࡎࡖࡏࡅࡉࡗࠨᲥ"))
        }
    if bstack1111ll111l_opy_(env.get(bstack11l1l11_opy_ (u"࡚ࠧࡆࡠࡄࡘࡍࡑࡊࠢᲦ"))):
        return {
            bstack11l1l11_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᲧ"): bstack11l1l11_opy_ (u"ࠢࡗ࡫ࡶࡹࡦࡲࠠࡔࡶࡸࡨ࡮ࡵࠠࡕࡧࡤࡱ࡙ࠥࡥࡳࡸ࡬ࡧࡪࡹࠢᲨ"),
            bstack11l1l11_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᲩ"): bstack11l1l11_opy_ (u"ࠤࡾࢁࢀࢃࠢᲪ").format(env.get(bstack11l1l11_opy_ (u"ࠪࡗ࡞࡙ࡔࡆࡏࡢࡘࡊࡇࡍࡇࡑࡘࡒࡉࡇࡔࡊࡑࡑࡗࡊࡘࡖࡆࡔࡘࡖࡎ࠭Ძ")), env.get(bstack11l1l11_opy_ (u"ࠫࡘ࡟ࡓࡕࡇࡐࡣ࡙ࡋࡁࡎࡒࡕࡓࡏࡋࡃࡕࡋࡇࠫᲬ"))),
            bstack11l1l11_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᲭ"): env.get(bstack11l1l11_opy_ (u"ࠨࡓ࡚ࡕࡗࡉࡒࡥࡄࡆࡈࡌࡒࡎ࡚ࡉࡐࡐࡌࡈࠧᲮ")),
            bstack11l1l11_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᲯ"): env.get(bstack11l1l11_opy_ (u"ࠣࡄࡘࡍࡑࡊ࡟ࡃࡗࡌࡐࡉࡏࡄࠣᲰ"))
        }
    if bstack1111ll111l_opy_(env.get(bstack11l1l11_opy_ (u"ࠤࡄࡔࡕ࡜ࡅ࡚ࡑࡕࠦᲱ"))):
        return {
            bstack11l1l11_opy_ (u"ࠥࡲࡦࡳࡥࠣᲲ"): bstack11l1l11_opy_ (u"ࠦࡆࡶࡰࡷࡧࡼࡳࡷࠨᲳ"),
            bstack11l1l11_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣᲴ"): bstack11l1l11_opy_ (u"ࠨࡻࡾ࠱ࡳࡶࡴࡰࡥࡤࡶ࠲ࡿࢂ࠵ࡻࡾ࠱ࡥࡹ࡮ࡲࡤࡴ࠱ࡾࢁࠧᲵ").format(env.get(bstack11l1l11_opy_ (u"ࠧࡂࡒࡓ࡚ࡊ࡟ࡏࡓࡡࡘࡖࡑ࠭Ჶ")), env.get(bstack11l1l11_opy_ (u"ࠨࡃࡓࡔ࡛ࡋ࡙ࡐࡔࡢࡅࡈࡉࡏࡖࡐࡗࡣࡓࡇࡍࡆࠩᲷ")), env.get(bstack11l1l11_opy_ (u"ࠩࡄࡔࡕ࡜ࡅ࡚ࡑࡕࡣࡕࡘࡏࡋࡇࡆࡘࡤ࡙ࡌࡖࡉࠪᲸ")), env.get(bstack11l1l11_opy_ (u"ࠪࡅࡕࡖࡖࡆ࡛ࡒࡖࡤࡈࡕࡊࡎࡇࡣࡎࡊࠧᲹ"))),
            bstack11l1l11_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᲺ"): env.get(bstack11l1l11_opy_ (u"ࠧࡇࡐࡑࡘࡈ࡝ࡔࡘ࡟ࡋࡑࡅࡣࡓࡇࡍࡆࠤ᲻")),
            bstack11l1l11_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧ᲼"): env.get(bstack11l1l11_opy_ (u"ࠢࡂࡒࡓ࡚ࡊ࡟ࡏࡓࡡࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࡇࡋࡒࠣᲽ"))
        }
    if env.get(bstack11l1l11_opy_ (u"ࠣࡃ࡝࡙ࡗࡋ࡟ࡉࡖࡗࡔࡤ࡛ࡓࡆࡔࡢࡅࡌࡋࡎࡕࠤᲾ")) and env.get(bstack11l1l11_opy_ (u"ࠤࡗࡊࡤࡈࡕࡊࡎࡇࠦᲿ")):
        return {
            bstack11l1l11_opy_ (u"ࠥࡲࡦࡳࡥࠣ᳀"): bstack11l1l11_opy_ (u"ࠦࡆࢀࡵࡳࡧࠣࡇࡎࠨ᳁"),
            bstack11l1l11_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣ᳂"): bstack11l1l11_opy_ (u"ࠨࡻࡾࡽࢀ࠳ࡤࡨࡵࡪ࡮ࡧ࠳ࡷ࡫ࡳࡶ࡮ࡷࡷࡄࡨࡵࡪ࡮ࡧࡍࡩࡃࡻࡾࠤ᳃").format(env.get(bstack11l1l11_opy_ (u"ࠧࡔ࡛ࡖࡘࡊࡓ࡟ࡕࡇࡄࡑࡋࡕࡕࡏࡆࡄࡘࡎࡕࡎࡔࡇࡕ࡚ࡊࡘࡕࡓࡋࠪ᳄")), env.get(bstack11l1l11_opy_ (u"ࠨࡕ࡜ࡗ࡙ࡋࡍࡠࡖࡈࡅࡒࡖࡒࡐࡌࡈࡇ࡙࠭᳅")), env.get(bstack11l1l11_opy_ (u"ࠩࡅ࡙ࡎࡒࡄࡠࡄࡘࡍࡑࡊࡉࡅࠩ᳆"))),
            bstack11l1l11_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧ᳇"): env.get(bstack11l1l11_opy_ (u"ࠦࡇ࡛ࡉࡍࡆࡢࡆ࡚ࡏࡌࡅࡋࡇࠦ᳈")),
            bstack11l1l11_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦ᳉"): env.get(bstack11l1l11_opy_ (u"ࠨࡂࡖࡋࡏࡈࡤࡈࡕࡊࡎࡇࡍࡉࠨ᳊"))
        }
    if any([env.get(bstack11l1l11_opy_ (u"ࠢࡄࡑࡇࡉࡇ࡛ࡉࡍࡆࡢࡆ࡚ࡏࡌࡅࡡࡌࡈࠧ᳋")), env.get(bstack11l1l11_opy_ (u"ࠣࡅࡒࡈࡊࡈࡕࡊࡎࡇࡣࡗࡋࡓࡐࡎ࡙ࡉࡉࡥࡓࡐࡗࡕࡇࡊࡥࡖࡆࡔࡖࡍࡔࡔࠢ᳌")), env.get(bstack11l1l11_opy_ (u"ࠤࡆࡓࡉࡋࡂࡖࡋࡏࡈࡤ࡙ࡏࡖࡔࡆࡉࡤ࡜ࡅࡓࡕࡌࡓࡓࠨ᳍"))]):
        return {
            bstack11l1l11_opy_ (u"ࠥࡲࡦࡳࡥࠣ᳎"): bstack11l1l11_opy_ (u"ࠦࡆ࡝ࡓࠡࡅࡲࡨࡪࡈࡵࡪ࡮ࡧࠦ᳏"),
            bstack11l1l11_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣ᳐"): env.get(bstack11l1l11_opy_ (u"ࠨࡃࡐࡆࡈࡆ࡚ࡏࡌࡅࡡࡓ࡙ࡇࡒࡉࡄࡡࡅ࡙ࡎࡒࡄࡠࡗࡕࡐࠧ᳑")),
            bstack11l1l11_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤ᳒"): env.get(bstack11l1l11_opy_ (u"ࠣࡅࡒࡈࡊࡈࡕࡊࡎࡇࡣࡇ࡛ࡉࡍࡆࡢࡍࡉࠨ᳓")),
            bstack11l1l11_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲ᳔ࠣ"): env.get(bstack11l1l11_opy_ (u"ࠥࡇࡔࡊࡅࡃࡗࡌࡐࡉࡥࡂࡖࡋࡏࡈࡤࡏࡄ᳕ࠣ"))
        }
    if env.get(bstack11l1l11_opy_ (u"ࠦࡧࡧ࡭ࡣࡱࡲࡣࡧࡻࡩ࡭ࡦࡑࡹࡲࡨࡥࡳࠤ᳖")):
        return {
            bstack11l1l11_opy_ (u"ࠧࡴࡡ࡮ࡧ᳗ࠥ"): bstack11l1l11_opy_ (u"ࠨࡂࡢ࡯ࡥࡳࡴࠨ᳘"),
            bstack11l1l11_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮᳙ࠥ"): env.get(bstack11l1l11_opy_ (u"ࠣࡤࡤࡱࡧࡵ࡯ࡠࡤࡸ࡭ࡱࡪࡒࡦࡵࡸࡰࡹࡹࡕࡳ࡮ࠥ᳚")),
            bstack11l1l11_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦ᳛"): env.get(bstack11l1l11_opy_ (u"ࠥࡦࡦࡳࡢࡰࡱࡢࡷ࡭ࡵࡲࡵࡌࡲࡦࡓࡧ࡭ࡦࠤ᳜")),
            bstack11l1l11_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴ᳝ࠥ"): env.get(bstack11l1l11_opy_ (u"ࠧࡨࡡ࡮ࡤࡲࡳࡤࡨࡵࡪ࡮ࡧࡒࡺࡳࡢࡦࡴ᳞ࠥ"))
        }
    if env.get(bstack11l1l11_opy_ (u"ࠨࡗࡆࡔࡆࡏࡊࡘ᳟ࠢ")) or env.get(bstack11l1l11_opy_ (u"ࠢࡘࡇࡕࡇࡐࡋࡒࡠࡏࡄࡍࡓࡥࡐࡊࡒࡈࡐࡎࡔࡅࡠࡕࡗࡅࡗ࡚ࡅࡅࠤ᳠")):
        return {
            bstack11l1l11_opy_ (u"ࠣࡰࡤࡱࡪࠨ᳡"): bstack11l1l11_opy_ (u"ࠤ࡚ࡩࡷࡩ࡫ࡦࡴ᳢ࠥ"),
            bstack11l1l11_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨ᳣"): env.get(bstack11l1l11_opy_ (u"ࠦ࡜ࡋࡒࡄࡍࡈࡖࡤࡈࡕࡊࡎࡇࡣ࡚ࡘࡌ᳤ࠣ")),
            bstack11l1l11_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫᳥ࠢ"): bstack11l1l11_opy_ (u"ࠨࡍࡢ࡫ࡱࠤࡕ࡯ࡰࡦ࡮࡬ࡲࡪࠨ᳦") if env.get(bstack11l1l11_opy_ (u"ࠢࡘࡇࡕࡇࡐࡋࡒࡠࡏࡄࡍࡓࡥࡐࡊࡒࡈࡐࡎࡔࡅࡠࡕࡗࡅࡗ࡚ࡅࡅࠤ᳧")) else None,
            bstack11l1l11_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸ᳨ࠢ"): env.get(bstack11l1l11_opy_ (u"ࠤ࡚ࡉࡗࡉࡋࡆࡔࡢࡋࡎ࡚࡟ࡄࡑࡐࡑࡎ࡚ࠢᳩ"))
        }
    if any([env.get(bstack11l1l11_opy_ (u"ࠥࡋࡈࡖ࡟ࡑࡔࡒࡎࡊࡉࡔࠣᳪ")), env.get(bstack11l1l11_opy_ (u"ࠦࡌࡉࡌࡐࡗࡇࡣࡕࡘࡏࡋࡇࡆࡘࠧᳫ")), env.get(bstack11l1l11_opy_ (u"ࠧࡍࡏࡐࡉࡏࡉࡤࡉࡌࡐࡗࡇࡣࡕࡘࡏࡋࡇࡆࡘࠧᳬ"))]):
        return {
            bstack11l1l11_opy_ (u"ࠨ࡮ࡢ࡯ࡨ᳭ࠦ"): bstack11l1l11_opy_ (u"ࠢࡈࡱࡲ࡫ࡱ࡫ࠠࡄ࡮ࡲࡹࡩࠨᳮ"),
            bstack11l1l11_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᳯ"): None,
            bstack11l1l11_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᳰ"): env.get(bstack11l1l11_opy_ (u"ࠥࡔࡗࡕࡊࡆࡅࡗࡣࡎࡊࠢᳱ")),
            bstack11l1l11_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᳲ"): env.get(bstack11l1l11_opy_ (u"ࠧࡈࡕࡊࡎࡇࡣࡎࡊࠢᳳ"))
        }
    if env.get(bstack11l1l11_opy_ (u"ࠨࡓࡉࡋࡓࡔࡆࡈࡌࡆࠤ᳴")):
        return {
            bstack11l1l11_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᳵ"): bstack11l1l11_opy_ (u"ࠣࡕ࡫࡭ࡵࡶࡡࡣ࡮ࡨࠦᳶ"),
            bstack11l1l11_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧ᳷"): env.get(bstack11l1l11_opy_ (u"ࠥࡗࡍࡏࡐࡑࡃࡅࡐࡊࡥࡂࡖࡋࡏࡈࡤ࡛ࡒࡍࠤ᳸")),
            bstack11l1l11_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨ᳹"): bstack11l1l11_opy_ (u"ࠧࡐ࡯ࡣࠢࠦࡿࢂࠨᳺ").format(env.get(bstack11l1l11_opy_ (u"࠭ࡓࡉࡋࡓࡔࡆࡈࡌࡆࡡࡍࡓࡇࡥࡉࡅࠩ᳻"))) if env.get(bstack11l1l11_opy_ (u"ࠢࡔࡊࡌࡔࡕࡇࡂࡍࡇࡢࡎࡔࡈ࡟ࡊࡆࠥ᳼")) else None,
            bstack11l1l11_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢ᳽"): env.get(bstack11l1l11_opy_ (u"ࠤࡖࡌࡎࡖࡐࡂࡄࡏࡉࡤࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࡃࡇࡕࠦ᳾"))
        }
    if bstack1111ll111l_opy_(env.get(bstack11l1l11_opy_ (u"ࠥࡒࡊ࡚ࡌࡊࡈ࡜ࠦ᳿"))):
        return {
            bstack11l1l11_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᴀ"): bstack11l1l11_opy_ (u"ࠧࡔࡥࡵ࡮࡬ࡪࡾࠨᴁ"),
            bstack11l1l11_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᴂ"): env.get(bstack11l1l11_opy_ (u"ࠢࡅࡇࡓࡐࡔ࡟࡟ࡖࡔࡏࠦᴃ")),
            bstack11l1l11_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᴄ"): env.get(bstack11l1l11_opy_ (u"ࠤࡖࡍ࡙ࡋ࡟ࡏࡃࡐࡉࠧᴅ")),
            bstack11l1l11_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤᴆ"): env.get(bstack11l1l11_opy_ (u"ࠦࡇ࡛ࡉࡍࡆࡢࡍࡉࠨᴇ"))
        }
    if bstack1111ll111l_opy_(env.get(bstack11l1l11_opy_ (u"ࠧࡍࡉࡕࡊࡘࡆࡤࡇࡃࡕࡋࡒࡒࡘࠨᴈ"))):
        return {
            bstack11l1l11_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᴉ"): bstack11l1l11_opy_ (u"ࠢࡈ࡫ࡷࡌࡺࡨࠠࡂࡥࡷ࡭ࡴࡴࡳࠣᴊ"),
            bstack11l1l11_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᴋ"): bstack11l1l11_opy_ (u"ࠤࡾࢁ࠴ࢁࡽ࠰ࡣࡦࡸ࡮ࡵ࡮ࡴ࠱ࡵࡹࡳࡹ࠯ࡼࡿࠥᴌ").format(env.get(bstack11l1l11_opy_ (u"ࠪࡋࡎ࡚ࡈࡖࡄࡢࡗࡊࡘࡖࡆࡔࡢ࡙ࡗࡒࠧᴍ")), env.get(bstack11l1l11_opy_ (u"ࠫࡌࡏࡔࡉࡗࡅࡣࡗࡋࡐࡐࡕࡌࡘࡔࡘ࡙ࠨᴎ")), env.get(bstack11l1l11_opy_ (u"ࠬࡍࡉࡕࡊࡘࡆࡤࡘࡕࡏࡡࡌࡈࠬᴏ"))),
            bstack11l1l11_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᴐ"): env.get(bstack11l1l11_opy_ (u"ࠢࡈࡋࡗࡌ࡚ࡈ࡟ࡘࡑࡕࡏࡋࡒࡏࡘࠤᴑ")),
            bstack11l1l11_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᴒ"): env.get(bstack11l1l11_opy_ (u"ࠤࡊࡍ࡙ࡎࡕࡃࡡࡕ࡙ࡓࡥࡉࡅࠤᴓ"))
        }
    if env.get(bstack11l1l11_opy_ (u"ࠥࡇࡎࠨᴔ")) == bstack11l1l11_opy_ (u"ࠦࡹࡸࡵࡦࠤᴕ") and env.get(bstack11l1l11_opy_ (u"ࠧ࡜ࡅࡓࡅࡈࡐࠧᴖ")) == bstack11l1l11_opy_ (u"ࠨ࠱ࠣᴗ"):
        return {
            bstack11l1l11_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᴘ"): bstack11l1l11_opy_ (u"ࠣࡘࡨࡶࡨ࡫࡬ࠣᴙ"),
            bstack11l1l11_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᴚ"): bstack11l1l11_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻࠱࠲ࡿࢂࠨᴛ").format(env.get(bstack11l1l11_opy_ (u"࡛ࠫࡋࡒࡄࡇࡏࡣ࡚ࡘࡌࠨᴜ"))),
            bstack11l1l11_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᴝ"): None,
            bstack11l1l11_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᴞ"): None,
        }
    if env.get(bstack11l1l11_opy_ (u"ࠢࡕࡇࡄࡑࡈࡏࡔ࡚ࡡ࡙ࡉࡗ࡙ࡉࡐࡐࠥᴟ")):
        return {
            bstack11l1l11_opy_ (u"ࠣࡰࡤࡱࡪࠨᴠ"): bstack11l1l11_opy_ (u"ࠤࡗࡩࡦࡳࡣࡪࡶࡼࠦᴡ"),
            bstack11l1l11_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᴢ"): None,
            bstack11l1l11_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᴣ"): env.get(bstack11l1l11_opy_ (u"࡚ࠧࡅࡂࡏࡆࡍ࡙࡟࡟ࡑࡔࡒࡎࡊࡉࡔࡠࡐࡄࡑࡊࠨᴤ")),
            bstack11l1l11_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᴥ"): env.get(bstack11l1l11_opy_ (u"ࠢࡃࡗࡌࡐࡉࡥࡎࡖࡏࡅࡉࡗࠨᴦ"))
        }
    if any([env.get(bstack11l1l11_opy_ (u"ࠣࡅࡒࡒࡈࡕࡕࡓࡕࡈࠦᴧ")), env.get(bstack11l1l11_opy_ (u"ࠤࡆࡓࡓࡉࡏࡖࡔࡖࡉࡤ࡛ࡒࡍࠤᴨ")), env.get(bstack11l1l11_opy_ (u"ࠥࡇࡔࡔࡃࡐࡗࡕࡗࡊࡥࡕࡔࡇࡕࡒࡆࡓࡅࠣᴩ")), env.get(bstack11l1l11_opy_ (u"ࠦࡈࡕࡎࡄࡑࡘࡖࡘࡋ࡟ࡕࡇࡄࡑࠧᴪ"))]):
        return {
            bstack11l1l11_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᴫ"): bstack11l1l11_opy_ (u"ࠨࡃࡰࡰࡦࡳࡺࡸࡳࡦࠤᴬ"),
            bstack11l1l11_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᴭ"): None,
            bstack11l1l11_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᴮ"): env.get(bstack11l1l11_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡠࡌࡒࡆࡤࡔࡁࡎࡇࠥᴯ")) or None,
            bstack11l1l11_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤᴰ"): env.get(bstack11l1l11_opy_ (u"ࠦࡇ࡛ࡉࡍࡆࡢࡍࡉࠨᴱ"), 0)
        }
    if env.get(bstack11l1l11_opy_ (u"ࠧࡍࡏࡠࡌࡒࡆࡤࡔࡁࡎࡇࠥᴲ")):
        return {
            bstack11l1l11_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᴳ"): bstack11l1l11_opy_ (u"ࠢࡈࡱࡆࡈࠧᴴ"),
            bstack11l1l11_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᴵ"): None,
            bstack11l1l11_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᴶ"): env.get(bstack11l1l11_opy_ (u"ࠥࡋࡔࡥࡊࡐࡄࡢࡒࡆࡓࡅࠣᴷ")),
            bstack11l1l11_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᴸ"): env.get(bstack11l1l11_opy_ (u"ࠧࡍࡏࡠࡒࡌࡔࡊࡒࡉࡏࡇࡢࡇࡔ࡛ࡎࡕࡇࡕࠦᴹ"))
        }
    if env.get(bstack11l1l11_opy_ (u"ࠨࡃࡇࡡࡅ࡙ࡎࡒࡄࡠࡋࡇࠦᴺ")):
        return {
            bstack11l1l11_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᴻ"): bstack11l1l11_opy_ (u"ࠣࡅࡲࡨࡪࡌࡲࡦࡵ࡫ࠦᴼ"),
            bstack11l1l11_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᴽ"): env.get(bstack11l1l11_opy_ (u"ࠥࡇࡋࡥࡂࡖࡋࡏࡈࡤ࡛ࡒࡍࠤᴾ")),
            bstack11l1l11_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᴿ"): env.get(bstack11l1l11_opy_ (u"ࠧࡉࡆࡠࡒࡌࡔࡊࡒࡉࡏࡇࡢࡒࡆࡓࡅࠣᵀ")),
            bstack11l1l11_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᵁ"): env.get(bstack11l1l11_opy_ (u"ࠢࡄࡈࡢࡆ࡚ࡏࡌࡅࡡࡌࡈࠧᵂ"))
        }
    return {bstack11l1l11_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᵃ"): None}
def get_host_info():
    return {
        bstack11l1l11_opy_ (u"ࠤ࡫ࡳࡸࡺ࡮ࡢ࡯ࡨࠦᵄ"): platform.node(),
        bstack11l1l11_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱࠧᵅ"): platform.system(),
        bstack11l1l11_opy_ (u"ࠦࡹࡿࡰࡦࠤᵆ"): platform.machine(),
        bstack11l1l11_opy_ (u"ࠧࡼࡥࡳࡵ࡬ࡳࡳࠨᵇ"): platform.version(),
        bstack11l1l11_opy_ (u"ࠨࡡࡳࡥ࡫ࠦᵈ"): platform.architecture()[0]
    }
def bstack1l11l11l11_opy_():
    try:
        import selenium
        return True
    except ImportError:
        return False
def bstack111l11l1l11_opy_():
    if bstack111ll1ll_opy_.get_property(bstack11l1l11_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࠨᵉ")):
        return bstack11l1l11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧᵊ")
    return bstack11l1l11_opy_ (u"ࠩࡸࡲࡰࡴ࡯ࡸࡰࡢ࡫ࡷ࡯ࡤࠨᵋ")
def bstack1111l1llll1_opy_(driver):
    info = {
        bstack11l1l11_opy_ (u"ࠪࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠩᵌ"): driver.capabilities,
        bstack11l1l11_opy_ (u"ࠫࡸ࡫ࡳࡴ࡫ࡲࡲࡤ࡯ࡤࠨᵍ"): driver.session_id,
        bstack11l1l11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࠭ᵎ"): driver.capabilities.get(bstack11l1l11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫᵏ"), None),
        bstack11l1l11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡠࡸࡨࡶࡸ࡯࡯࡯ࠩᵐ"): driver.capabilities.get(bstack11l1l11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩᵑ"), None),
        bstack11l1l11_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࠫᵒ"): driver.capabilities.get(bstack11l1l11_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡓࡧ࡭ࡦࠩᵓ"), None),
        bstack11l1l11_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡥࡶࡦࡴࡶ࡭ࡴࡴࠧᵔ"):driver.capabilities.get(bstack11l1l11_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡖࡦࡴࡶ࡭ࡴࡴࠧᵕ"), None),
    }
    if bstack111l11l1l11_opy_() == bstack11l1l11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬᵖ"):
        if bstack11llll1111_opy_():
            info[bstack11l1l11_opy_ (u"ࠧࡱࡴࡲࡨࡺࡩࡴࠨᵗ")] = bstack11l1l11_opy_ (u"ࠨࡣࡳࡴ࠲ࡧࡵࡵࡱࡰࡥࡹ࡫ࠧᵘ")
        elif driver.capabilities.get(bstack11l1l11_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪᵙ"), {}).get(bstack11l1l11_opy_ (u"ࠪࡸࡺࡸࡢࡰࡵࡦࡥࡱ࡫ࠧᵚ"), False):
            info[bstack11l1l11_opy_ (u"ࠫࡵࡸ࡯ࡥࡷࡦࡸࠬᵛ")] = bstack11l1l11_opy_ (u"ࠬࡺࡵࡳࡤࡲࡷࡨࡧ࡬ࡦࠩᵜ")
        else:
            info[bstack11l1l11_opy_ (u"࠭ࡰࡳࡱࡧࡹࡨࡺࠧᵝ")] = bstack11l1l11_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡦࠩᵞ")
    return info
def bstack11llll1111_opy_():
    if bstack111ll1ll_opy_.get_property(bstack11l1l11_opy_ (u"ࠨࡣࡳࡴࡤࡧࡵࡵࡱࡰࡥࡹ࡫ࠧᵟ")):
        return True
    if bstack1111ll111l_opy_(os.environ.get(bstack11l1l11_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡋࡖࡣࡆࡖࡐࡠࡃࡘࡘࡔࡓࡁࡕࡇࠪᵠ"), None)):
        return True
    return False
def bstack11lll11l11_opy_(bstack1111lll111l_opy_, url, data, config):
    headers = config.get(bstack11l1l11_opy_ (u"ࠪ࡬ࡪࡧࡤࡦࡴࡶࠫᵡ"), None)
    proxies = bstack11l11l1111_opy_(config, url)
    auth = config.get(bstack11l1l11_opy_ (u"ࠫࡦࡻࡴࡩࠩᵢ"), None)
    response = requests.request(
            bstack1111lll111l_opy_,
            url=url,
            headers=headers,
            auth=auth,
            json=data,
            proxies=proxies
        )
    return response
def bstack11l11l1l1l_opy_(bstack1l1111lll_opy_, size):
    bstack11111llll1_opy_ = []
    while len(bstack1l1111lll_opy_) > size:
        bstack111111ll1l_opy_ = bstack1l1111lll_opy_[:size]
        bstack11111llll1_opy_.append(bstack111111ll1l_opy_)
        bstack1l1111lll_opy_ = bstack1l1111lll_opy_[size:]
    bstack11111llll1_opy_.append(bstack1l1111lll_opy_)
    return bstack11111llll1_opy_
def bstack111l11lllll_opy_(message, bstack1111l1l1111_opy_=False):
    os.write(1, bytes(message, bstack11l1l11_opy_ (u"ࠬࡻࡴࡧ࠯࠻ࠫᵣ")))
    os.write(1, bytes(bstack11l1l11_opy_ (u"࠭࡜࡯ࠩᵤ"), bstack11l1l11_opy_ (u"ࠧࡶࡶࡩ࠱࠽࠭ᵥ")))
    if bstack1111l1l1111_opy_:
        with open(bstack11l1l11_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠮ࡱ࠴࠵ࡾ࠳ࠧᵦ") + os.environ[bstack11l1l11_opy_ (u"ࠩࡅࡗࡤ࡚ࡅࡔࡖࡒࡔࡘࡥࡂࡖࡋࡏࡈࡤࡎࡁࡔࡊࡈࡈࡤࡏࡄࠨᵧ")] + bstack11l1l11_opy_ (u"ࠪ࠲ࡱࡵࡧࠨᵨ"), bstack11l1l11_opy_ (u"ࠫࡦ࠭ᵩ")) as f:
            f.write(message + bstack11l1l11_opy_ (u"ࠬࡢ࡮ࠨᵪ"))
def bstack1lll1ll1lll_opy_():
    return os.environ[bstack11l1l11_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡇࡕࡕࡑࡐࡅ࡙ࡏࡏࡏࠩᵫ")].lower() == bstack11l1l11_opy_ (u"ࠧࡵࡴࡸࡩࠬᵬ")
def bstack1lllll11_opy_():
    return bstack1l1l111l_opy_().replace(tzinfo=None).isoformat() + bstack11l1l11_opy_ (u"ࠨ࡜ࠪᵭ")
def bstack111l111llll_opy_(start, finish):
    return (datetime.datetime.fromisoformat(finish.rstrip(bstack11l1l11_opy_ (u"ࠩ࡝ࠫᵮ"))) - datetime.datetime.fromisoformat(start.rstrip(bstack11l1l11_opy_ (u"ࠪ࡞ࠬᵯ")))).total_seconds() * 1000
def bstack1111ll1ll1l_opy_(timestamp):
    return bstack111l11l1ll1_opy_(timestamp).isoformat() + bstack11l1l11_opy_ (u"ࠫ࡟࠭ᵰ")
def bstack1111lll1111_opy_(bstack111l1l11l1l_opy_):
    date_format = bstack11l1l11_opy_ (u"࡙ࠬࠫࠦ࡯ࠨࡨࠥࠫࡈ࠻ࠧࡐ࠾࡙ࠪ࠮ࠦࡨࠪᵱ")
    bstack111l1l1111l_opy_ = datetime.datetime.strptime(bstack111l1l11l1l_opy_, date_format)
    return bstack111l1l1111l_opy_.isoformat() + bstack11l1l11_opy_ (u"࡚࠭ࠨᵲ")
def bstack1111lll1ll1_opy_(outcome):
    _, exception, _ = outcome.excinfo or (None, None, None)
    if exception:
        return bstack11l1l11_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧᵳ")
    else:
        return bstack11l1l11_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨᵴ")
def bstack1111ll111l_opy_(val):
    if val is None:
        return False
    return val.__str__().lower() == bstack11l1l11_opy_ (u"ࠩࡷࡶࡺ࡫ࠧᵵ")
def bstack1111llll1ll_opy_(val):
    return val.__str__().lower() == bstack11l1l11_opy_ (u"ࠪࡪࡦࡲࡳࡦࠩᵶ")
def error_handler(bstack111l1111l11_opy_=Exception, class_method=False, default_value=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except bstack111l1111l11_opy_ as e:
                print(bstack11l1l11_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡪࡺࡴࡣࡵ࡫ࡲࡲࠥࢁࡽࠡ࠯ࡁࠤࢀࢃ࠺ࠡࡽࢀࠦᵷ").format(func.__name__, bstack111l1111l11_opy_.__name__, str(e)))
                return default_value
        return wrapper
    def bstack111l11111l1_opy_(bstack1111lllllll_opy_):
        def wrapped(cls, *args, **kwargs):
            try:
                return bstack1111lllllll_opy_(cls, *args, **kwargs)
            except bstack111l1111l11_opy_ as e:
                print(bstack11l1l11_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࠦࡻࡾࠢ࠰ࡂࠥࢁࡽ࠻ࠢࡾࢁࠧᵸ").format(bstack1111lllllll_opy_.__name__, bstack111l1111l11_opy_.__name__, str(e)))
                return default_value
        return wrapped
    if class_method:
        return bstack111l11111l1_opy_
    else:
        return decorator
def bstack1l11lllll1_opy_(bstack1111l1ll_opy_):
    if os.getenv(bstack11l1l11_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡇࡕࡕࡑࡐࡅ࡙ࡏࡏࡏࠩᵹ")) is not None:
        return bstack1111ll111l_opy_(os.getenv(bstack11l1l11_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡁࡖࡖࡒࡑࡆ࡚ࡉࡐࡐࠪᵺ")))
    if bstack11l1l11_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬᵻ") in bstack1111l1ll_opy_ and bstack1111llll1ll_opy_(bstack1111l1ll_opy_[bstack11l1l11_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳ࠭ᵼ")]):
        return False
    if bstack11l1l11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬᵽ") in bstack1111l1ll_opy_ and bstack1111llll1ll_opy_(bstack1111l1ll_opy_[bstack11l1l11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳ࠭ᵾ")]):
        return False
    return True
def bstack111lllll1_opy_():
    try:
        from pytest_bdd import reporting
        bstack111l1l1l111_opy_ = os.environ.get(bstack11l1l11_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡚࡙ࡅࡓࡡࡉࡖࡆࡓࡅࡘࡑࡕࡏࠧᵿ"), None)
        return bstack111l1l1l111_opy_ is None or bstack111l1l1l111_opy_ == bstack11l1l11_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠥᶀ")
    except Exception as e:
        return False
def bstack1l1lll1ll1_opy_(hub_url, CONFIG):
    if bstack11l1111l1l_opy_() <= version.parse(bstack11l1l11_opy_ (u"ࠧ࠴࠰࠴࠷࠳࠶ࠧᶁ")):
        if hub_url:
            return bstack11l1l11_opy_ (u"ࠣࡪࡷࡸࡵࡀ࠯࠰ࠤᶂ") + hub_url + bstack11l1l11_opy_ (u"ࠤ࠽࠼࠵࠵ࡷࡥ࠱࡫ࡹࡧࠨᶃ")
        return bstack11llll111l_opy_
    if hub_url:
        return bstack11l1l11_opy_ (u"ࠥ࡬ࡹࡺࡰࡴ࠼࠲࠳ࠧᶄ") + hub_url + bstack11l1l11_opy_ (u"ࠦ࠴ࡽࡤ࠰ࡪࡸࡦࠧᶅ")
    return bstack11l1lll11_opy_
def bstack111l111l11l_opy_():
    return isinstance(os.getenv(bstack11l1l11_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕ࡟ࡔࡆࡕࡗࡣࡕࡒࡕࡈࡋࡑࠫᶆ")), str)
def bstack1l1lll11l1_opy_(url):
    return urlparse(url).hostname
def bstack1l1111111_opy_(hostname):
    for bstack11l11lll1_opy_ in bstack11lll11l1_opy_:
        regex = re.compile(bstack11l11lll1_opy_)
        if regex.match(hostname):
            return True
    return False
def bstack11ll1111l11_opy_(bstack1111lll1lll_opy_, file_name, logger):
    bstack11lll1l111_opy_ = os.path.join(os.path.expanduser(bstack11l1l11_opy_ (u"࠭ࡾࠨᶇ")), bstack1111lll1lll_opy_)
    try:
        if not os.path.exists(bstack11lll1l111_opy_):
            os.makedirs(bstack11lll1l111_opy_)
        file_path = os.path.join(os.path.expanduser(bstack11l1l11_opy_ (u"ࠧࡿࠩᶈ")), bstack1111lll1lll_opy_, file_name)
        if not os.path.isfile(file_path):
            with open(file_path, bstack11l1l11_opy_ (u"ࠨࡹࠪᶉ")):
                pass
            with open(file_path, bstack11l1l11_opy_ (u"ࠤࡺ࠯ࠧᶊ")) as outfile:
                json.dump({}, outfile)
        return file_path
    except Exception as e:
        logger.debug(bstack11l11ll11_opy_.format(str(e)))
def bstack11ll1111l1l_opy_(file_name, key, value, logger):
    file_path = bstack11ll1111l11_opy_(bstack11l1l11_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪᶋ"), file_name, logger)
    if file_path != None:
        if os.path.exists(file_path):
            bstack1l111ll11_opy_ = json.load(open(file_path, bstack11l1l11_opy_ (u"ࠫࡷࡨࠧᶌ")))
        else:
            bstack1l111ll11_opy_ = {}
        bstack1l111ll11_opy_[key] = value
        with open(file_path, bstack11l1l11_opy_ (u"ࠧࡽࠫࠣᶍ")) as outfile:
            json.dump(bstack1l111ll11_opy_, outfile)
def bstack1lll11l111_opy_(file_name, logger):
    file_path = bstack11ll1111l11_opy_(bstack11l1l11_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ᶎ"), file_name, logger)
    bstack1l111ll11_opy_ = {}
    if file_path != None and os.path.exists(file_path):
        with open(file_path, bstack11l1l11_opy_ (u"ࠧࡳࠩᶏ")) as bstack11l11l11l_opy_:
            bstack1l111ll11_opy_ = json.load(bstack11l11l11l_opy_)
    return bstack1l111ll11_opy_
def bstack1lllll1l11_opy_(file_path, logger):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
    except Exception as e:
        logger.debug(bstack11l1l11_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡨࡪࡲࡥࡵ࡫ࡱ࡫ࠥ࡬ࡩ࡭ࡧ࠽ࠤࠬᶐ") + file_path + bstack11l1l11_opy_ (u"ࠩࠣࠫᶑ") + str(e))
def bstack11l1111l1l_opy_():
    from selenium import webdriver
    return version.parse(webdriver.__version__)
class Notset:
    def __repr__(self):
        return bstack11l1l11_opy_ (u"ࠥࡀࡓࡕࡔࡔࡇࡗࡂࠧᶒ")
def bstack11111ll1l1_opy_(config):
    if bstack11l1l11_opy_ (u"ࠫ࡮ࡹࡐ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠪᶓ") in config:
        del (config[bstack11l1l11_opy_ (u"ࠬ࡯ࡳࡑ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠫᶔ")])
        return False
    if bstack11l1111l1l_opy_() < version.parse(bstack11l1l11_opy_ (u"࠭࠳࠯࠶࠱࠴ࠬᶕ")):
        return False
    if bstack11l1111l1l_opy_() >= version.parse(bstack11l1l11_opy_ (u"ࠧ࠵࠰࠴࠲࠺࠭ᶖ")):
        return True
    if bstack11l1l11_opy_ (u"ࠨࡷࡶࡩ࡜࠹ࡃࠨᶗ") in config and config[bstack11l1l11_opy_ (u"ࠩࡸࡷࡪ࡝࠳ࡄࠩᶘ")] is False:
        return False
    else:
        return True
def bstack111l11l11_opy_(args_list, bstack1111l1l1l11_opy_):
    index = -1
    for value in bstack1111l1l1l11_opy_:
        try:
            index = args_list.index(value)
            return index
        except Exception as e:
            return index
    return index
def bstack111l1111ll1_opy_(a, b):
  for k, v in b.items():
    if isinstance(v, dict) and k in a and isinstance(a[k], dict):
        bstack111l1111ll1_opy_(a[k], v)
    else:
        a[k] = v
class Result:
    def __init__(self, result=None, duration=None, exception=None, bstack1ll111ll_opy_=None):
        self.result = result
        self.duration = duration
        self.exception = exception
        self.exception_type = type(self.exception).__name__ if exception else None
        self.bstack1ll111ll_opy_ = bstack1ll111ll_opy_
    @classmethod
    def passed(cls):
        return Result(result=bstack11l1l11_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪᶙ"))
    @classmethod
    def failed(cls, exception=None):
        return Result(result=bstack11l1l11_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫᶚ"), exception=exception)
    def bstack1111111l1l_opy_(self):
        if self.result != bstack11l1l11_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬᶛ"):
            return None
        if isinstance(self.exception_type, str) and bstack11l1l11_opy_ (u"ࠨࡁࡴࡵࡨࡶࡹ࡯࡯࡯ࠤᶜ") in self.exception_type:
            return bstack11l1l11_opy_ (u"ࠢࡂࡵࡶࡩࡷࡺࡩࡰࡰࡈࡶࡷࡵࡲࠣᶝ")
        return bstack11l1l11_opy_ (u"ࠣࡗࡱ࡬ࡦࡴࡤ࡭ࡧࡧࡉࡷࡸ࡯ࡳࠤᶞ")
    def bstack1111lll11ll_opy_(self):
        if self.result != bstack11l1l11_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩᶟ"):
            return None
        if self.bstack1ll111ll_opy_:
            return self.bstack1ll111ll_opy_
        return bstack1111ll1l1ll_opy_(self.exception)
def bstack1111ll1l1ll_opy_(exc):
    return [traceback.format_exception(exc)]
def bstack1111llll11l_opy_(message):
    if isinstance(message, str):
        return not bool(message and message.strip())
    return True
def bstack1l111l1l_opy_(object, key, default_value):
    if not object or not object.__dict__:
        return default_value
    if key in object.__dict__.keys():
        return object.__dict__.get(key)
    return default_value
def bstack11l1l11l1_opy_(config, logger):
    try:
        import playwright
        bstack111l1l1llll_opy_ = playwright.__file__
        bstack1111l1lll11_opy_ = os.path.split(bstack111l1l1llll_opy_)
        bstack111l1ll1lll_opy_ = bstack1111l1lll11_opy_[0] + bstack11l1l11_opy_ (u"ࠪ࠳ࡩࡸࡩࡷࡧࡵ࠳ࡵࡧࡣ࡬ࡣࡪࡩ࠴ࡲࡩࡣ࠱ࡦࡰ࡮࠵ࡣ࡭࡫࠱࡮ࡸ࠭ᶠ")
        os.environ[bstack11l1l11_opy_ (u"ࠫࡌࡒࡏࡃࡃࡏࡣࡆࡍࡅࡏࡖࡢࡌ࡙࡚ࡐࡠࡒࡕࡓ࡝࡟ࠧᶡ")] = bstack1l1lllll1l_opy_(config)
        with open(bstack111l1ll1lll_opy_, bstack11l1l11_opy_ (u"ࠬࡸࠧᶢ")) as f:
            file_content = f.read()
            bstack111l1l1lll1_opy_ = bstack11l1l11_opy_ (u"࠭ࡧ࡭ࡱࡥࡥࡱ࠳ࡡࡨࡧࡱࡸࠬᶣ")
            bstack1111ll1l1l1_opy_ = file_content.find(bstack111l1l1lll1_opy_)
            if bstack1111ll1l1l1_opy_ == -1:
              process = subprocess.Popen(bstack11l1l11_opy_ (u"ࠢ࡯ࡲࡰࠤ࡮ࡴࡳࡵࡣ࡯ࡰࠥ࡭࡬ࡰࡤࡤࡰ࠲ࡧࡧࡦࡰࡷࠦᶤ"), shell=True, cwd=bstack1111l1lll11_opy_[0])
              process.wait()
              bstack1111l1l111l_opy_ = bstack11l1l11_opy_ (u"ࠨࠤࡸࡷࡪࠦࡳࡵࡴ࡬ࡧࡹࠨ࠻ࠨᶥ")
              bstack111l111l1ll_opy_ = bstack11l1l11_opy_ (u"ࠤࠥࠦࠥࡢࠢࡶࡵࡨࠤࡸࡺࡲࡪࡥࡷࡠࠧࡁࠠࡤࡱࡱࡷࡹࠦࡻࠡࡤࡲࡳࡹࡹࡴࡳࡣࡳࠤࢂࠦ࠽ࠡࡴࡨࡵࡺ࡯ࡲࡦࠪࠪ࡫ࡱࡵࡢࡢ࡮࠰ࡥ࡬࡫࡮ࡵࠩࠬ࠿ࠥ࡯ࡦࠡࠪࡳࡶࡴࡩࡥࡴࡵ࠱ࡩࡳࡼ࠮ࡈࡎࡒࡆࡆࡒ࡟ࡂࡉࡈࡒ࡙ࡥࡈࡕࡖࡓࡣࡕࡘࡏ࡙࡛ࠬࠤࡧࡵ࡯ࡵࡵࡷࡶࡦࡶࠨࠪ࠽ࠣࠦࠧࠨᶦ")
              bstack111l1l1l1l1_opy_ = file_content.replace(bstack1111l1l111l_opy_, bstack111l111l1ll_opy_)
              with open(bstack111l1ll1lll_opy_, bstack11l1l11_opy_ (u"ࠪࡻࠬᶧ")) as f:
                f.write(bstack111l1l1l1l1_opy_)
    except Exception as e:
        logger.error(bstack11lllll11_opy_.format(str(e)))
def bstack1l11l11ll1_opy_():
  try:
    bstack1111ll111l1_opy_ = os.path.join(tempfile.gettempdir(), bstack11l1l11_opy_ (u"ࠫࡴࡶࡴࡪ࡯ࡤࡰࡤ࡮ࡵࡣࡡࡸࡶࡱ࠴ࡪࡴࡱࡱࠫᶨ"))
    bstack111l1lll111_opy_ = []
    if os.path.exists(bstack1111ll111l1_opy_):
      with open(bstack1111ll111l1_opy_) as f:
        bstack111l1lll111_opy_ = json.load(f)
      os.remove(bstack1111ll111l1_opy_)
    return bstack111l1lll111_opy_
  except:
    pass
  return []
def bstack1l1l1ll1l1_opy_(bstack1lll1ll1ll_opy_):
  try:
    bstack111l1lll111_opy_ = []
    bstack1111ll111l1_opy_ = os.path.join(tempfile.gettempdir(), bstack11l1l11_opy_ (u"ࠬࡵࡰࡵ࡫ࡰࡥࡱࡥࡨࡶࡤࡢࡹࡷࡲ࠮࡫ࡵࡲࡲࠬᶩ"))
    if os.path.exists(bstack1111ll111l1_opy_):
      with open(bstack1111ll111l1_opy_) as f:
        bstack111l1lll111_opy_ = json.load(f)
    bstack111l1lll111_opy_.append(bstack1lll1ll1ll_opy_)
    with open(bstack1111ll111l1_opy_, bstack11l1l11_opy_ (u"࠭ࡷࠨᶪ")) as f:
        json.dump(bstack111l1lll111_opy_, f)
  except:
    pass
def bstack1llll1l11l_opy_(logger, bstack1111l11ll11_opy_ = False):
  try:
    test_name = os.environ.get(bstack11l1l11_opy_ (u"ࠧࡑ࡛ࡗࡉࡘ࡚࡟ࡕࡇࡖࡘࡤࡔࡁࡎࡇࠪᶫ"), bstack11l1l11_opy_ (u"ࠨࠩᶬ"))
    if test_name == bstack11l1l11_opy_ (u"ࠩࠪᶭ"):
        test_name = threading.current_thread().__dict__.get(bstack11l1l11_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࡅࡨࡩࡥࡴࡦࡵࡷࡣࡳࡧ࡭ࡦࠩᶮ"), bstack11l1l11_opy_ (u"ࠫࠬᶯ"))
    bstack1111l1ll11l_opy_ = bstack11l1l11_opy_ (u"ࠬ࠲ࠠࠨᶰ").join(threading.current_thread().bstackTestErrorMessages)
    if bstack1111l11ll11_opy_:
        bstack1l111l1111_opy_ = os.environ.get(bstack11l1l11_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝࠭ᶱ"), bstack11l1l11_opy_ (u"ࠧ࠱ࠩᶲ"))
        bstack1lllll11ll_opy_ = {bstack11l1l11_opy_ (u"ࠨࡰࡤࡱࡪ࠭ᶳ"): test_name, bstack11l1l11_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨᶴ"): bstack1111l1ll11l_opy_, bstack11l1l11_opy_ (u"ࠪ࡭ࡳࡪࡥࡹࠩᶵ"): bstack1l111l1111_opy_}
        bstack1111l1l1ll1_opy_ = []
        bstack1111l1ll1ll_opy_ = os.path.join(tempfile.gettempdir(), bstack11l1l11_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࡣࡵࡶࡰࡠࡧࡵࡶࡴࡸ࡟࡭࡫ࡶࡸ࠳ࡰࡳࡰࡰࠪᶶ"))
        if os.path.exists(bstack1111l1ll1ll_opy_):
            with open(bstack1111l1ll1ll_opy_) as f:
                bstack1111l1l1ll1_opy_ = json.load(f)
        bstack1111l1l1ll1_opy_.append(bstack1lllll11ll_opy_)
        with open(bstack1111l1ll1ll_opy_, bstack11l1l11_opy_ (u"ࠬࡽࠧᶷ")) as f:
            json.dump(bstack1111l1l1ll1_opy_, f)
    else:
        bstack1lllll11ll_opy_ = {bstack11l1l11_opy_ (u"࠭࡮ࡢ࡯ࡨࠫᶸ"): test_name, bstack11l1l11_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭ᶹ"): bstack1111l1ll11l_opy_, bstack11l1l11_opy_ (u"ࠨ࡫ࡱࡨࡪࡾࠧᶺ"): str(multiprocessing.current_process().name)}
        if bstack11l1l11_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡡࡨࡶࡷࡵࡲࡠ࡮࡬ࡷࡹ࠭ᶻ") not in multiprocessing.current_process().__dict__.keys():
            multiprocessing.current_process().bstack_error_list = []
        multiprocessing.current_process().bstack_error_list.append(bstack1lllll11ll_opy_)
  except Exception as e:
      logger.warn(bstack11l1l11_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡳࡵࡱࡵࡩࠥࡶࡹࡵࡧࡶࡸࠥ࡬ࡵ࡯ࡰࡨࡰࠥࡪࡡࡵࡣ࠽ࠤࢀࢃࠢᶼ").format(e))
def bstack11l11ll111_opy_(error_message, test_name, index, logger):
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack11l1l11_opy_ (u"ࠫ࡫࡯࡬ࡦ࡮ࡲࡧࡰࠦ࡮ࡰࡶࠣࡥࡻࡧࡩ࡭ࡣࡥࡰࡪ࠲ࠠࡶࡵ࡬ࡲ࡬ࠦࡢࡢࡵ࡬ࡧࠥ࡬ࡩ࡭ࡧࠣࡳࡵ࡫ࡲࡢࡶ࡬ࡳࡳࡹࠧᶽ"))
    try:
      bstack111l1ll1111_opy_ = []
      bstack1lllll11ll_opy_ = {bstack11l1l11_opy_ (u"ࠬࡴࡡ࡮ࡧࠪᶾ"): test_name, bstack11l1l11_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬᶿ"): error_message, bstack11l1l11_opy_ (u"ࠧࡪࡰࡧࡩࡽ࠭᷀"): index}
      bstack111l11ll11l_opy_ = os.path.join(tempfile.gettempdir(), bstack11l1l11_opy_ (u"ࠨࡴࡲࡦࡴࡺ࡟ࡦࡴࡵࡳࡷࡥ࡬ࡪࡵࡷ࠲࡯ࡹ࡯࡯ࠩ᷁"))
      if os.path.exists(bstack111l11ll11l_opy_):
          with open(bstack111l11ll11l_opy_) as f:
              bstack111l1ll1111_opy_ = json.load(f)
      bstack111l1ll1111_opy_.append(bstack1lllll11ll_opy_)
      with open(bstack111l11ll11l_opy_, bstack11l1l11_opy_ (u"ࠩࡺ᷂ࠫ")) as f:
          json.dump(bstack111l1ll1111_opy_, f)
    except Exception as e:
      logger.warn(bstack11l1l11_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡳࡵࡱࡵࡩࠥࡸ࡯ࡣࡱࡷࠤ࡫ࡻ࡮࡯ࡧ࡯ࠤࡩࡧࡴࡢ࠼ࠣࡿࢂࠨ᷃").format(e))
    return
  bstack111l1ll1111_opy_ = []
  bstack1lllll11ll_opy_ = {bstack11l1l11_opy_ (u"ࠫࡳࡧ࡭ࡦࠩ᷄"): test_name, bstack11l1l11_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫ᷅"): error_message, bstack11l1l11_opy_ (u"࠭ࡩ࡯ࡦࡨࡼࠬ᷆"): index}
  bstack111l11ll11l_opy_ = os.path.join(tempfile.gettempdir(), bstack11l1l11_opy_ (u"ࠧࡳࡱࡥࡳࡹࡥࡥࡳࡴࡲࡶࡤࡲࡩࡴࡶ࠱࡮ࡸࡵ࡮ࠨ᷇"))
  lock_file = bstack111l11ll11l_opy_ + bstack11l1l11_opy_ (u"ࠨ࠰࡯ࡳࡨࡱࠧ᷈")
  try:
    with FileLock(lock_file, timeout=10):
      if os.path.exists(bstack111l11ll11l_opy_):
          with open(bstack111l11ll11l_opy_, bstack11l1l11_opy_ (u"ࠩࡵࠫ᷉")) as f:
              content = f.read().strip()
              if content:
                  bstack111l1ll1111_opy_ = json.load(open(bstack111l11ll11l_opy_))
      bstack111l1ll1111_opy_.append(bstack1lllll11ll_opy_)
      with open(bstack111l11ll11l_opy_, bstack11l1l11_opy_ (u"ࠪࡻ᷊ࠬ")) as f:
          json.dump(bstack111l1ll1111_opy_, f)
  except Exception as e:
    logger.warn(bstack11l1l11_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡴࡶࡲࡶࡪࠦࡲࡰࡤࡲࡸࠥ࡬ࡵ࡯ࡰࡨࡰࠥࡪࡡࡵࡣࠣࡻ࡮ࡺࡨࠡࡨ࡬ࡰࡪࠦ࡬ࡰࡥ࡮࡭ࡳ࡭࠺ࠡࡽࢀࠦ᷋").format(e))
def bstack11l1l1111l_opy_(bstack1llll1l1ll_opy_, name, logger):
  try:
    bstack1lllll11ll_opy_ = {bstack11l1l11_opy_ (u"ࠬࡴࡡ࡮ࡧࠪ᷌"): name, bstack11l1l11_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬ᷍"): bstack1llll1l1ll_opy_, bstack11l1l11_opy_ (u"ࠧࡪࡰࡧࡩࡽ᷎࠭"): str(threading.current_thread()._name)}
    return bstack1lllll11ll_opy_
  except Exception as e:
    logger.warn(bstack11l1l11_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡸࡺ࡯ࡳࡧࠣࡦࡪ࡮ࡡࡷࡧࠣࡪࡺࡴ࡮ࡦ࡮ࠣࡨࡦࡺࡡ࠻ࠢࡾࢁ᷏ࠧ").format(e))
  return
def bstack111l111111l_opy_():
    return platform.system() == bstack11l1l11_opy_ (u"࡚ࠩ࡭ࡳࡪ࡯ࡸࡵ᷐ࠪ")
def bstack111l1l1111_opy_(bstack1111llllll1_opy_, config, logger):
    bstack111l1l1l1ll_opy_ = {}
    try:
        return {key: config[key] for key in config if bstack1111llllll1_opy_.match(key)}
    except Exception as e:
        logger.debug(bstack11l1l11_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡦࡪ࡮ࡷࡩࡷࠦࡣࡰࡰࡩ࡭࡬ࠦ࡫ࡦࡻࡶࠤࡧࡿࠠࡳࡧࡪࡩࡽࠦ࡭ࡢࡶࡦ࡬࠿ࠦࡻࡾࠤ᷑").format(e))
    return bstack111l1l1l1ll_opy_
def bstack11l1ll111l1_opy_(bstack111l1ll11ll_opy_, bstack1111llll1l1_opy_):
    bstack1111ll111ll_opy_ = version.parse(bstack111l1ll11ll_opy_)
    bstack1111l11lll1_opy_ = version.parse(bstack1111llll1l1_opy_)
    if bstack1111ll111ll_opy_ > bstack1111l11lll1_opy_:
        return 1
    elif bstack1111ll111ll_opy_ < bstack1111l11lll1_opy_:
        return -1
    else:
        return 0
def bstack1l1l111l_opy_():
    return datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None)
def bstack111l11l1ll1_opy_(timestamp):
    return datetime.datetime.fromtimestamp(timestamp, datetime.timezone.utc).replace(tzinfo=None)
def bstack111l1l11111_opy_(framework):
    from browserstack_sdk._version import __version__
    return str(framework) + str(__version__)
def bstack1ll1l1ll1l_opy_(options, framework, config, bstack11111111l_opy_={}):
    if options is None:
        return
    if getattr(options, bstack11l1l11_opy_ (u"ࠫ࡬࡫ࡴࠨ᷒"), None):
        caps = options
    else:
        caps = options.to_capabilities()
    bstack11l11ll1ll_opy_ = caps.get(bstack11l1l11_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭ᷓ"))
    bstack1111ll1llll_opy_ = True
    bstack1l1llll1ll_opy_ = os.environ[bstack11l1l11_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫᷔ")]
    bstack1l111l11111_opy_ = config.get(bstack11l1l11_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧᷕ"), False)
    if bstack1l111l11111_opy_:
        bstack1l1l11l1111_opy_ = config.get(bstack11l1l11_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨᷖ"), {})
        bstack1l1l11l1111_opy_[bstack11l1l11_opy_ (u"ࠩࡤࡹࡹ࡮ࡔࡰ࡭ࡨࡲࠬᷗ")] = os.getenv(bstack11l1l11_opy_ (u"ࠪࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠨᷘ"))
        bstack111l1l11ll1_opy_ = json.loads(os.getenv(bstack11l1l11_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡠࡃࡆࡇࡊ࡙ࡓࡊࡄࡌࡐࡎ࡚࡙ࡠࡅࡒࡒࡋࡏࡇࡖࡔࡄࡘࡎࡕࡎࡠ࡛ࡐࡐࠬᷙ"), bstack11l1l11_opy_ (u"ࠬࢁࡽࠨᷚ"))).get(bstack11l1l11_opy_ (u"࠭ࡳࡤࡣࡱࡲࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧᷛ"))
    if bstack1111llll1ll_opy_(caps.get(bstack11l1l11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡵࡴࡧ࡚࠷ࡈ࠭ᷜ"))) or bstack1111llll1ll_opy_(caps.get(bstack11l1l11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡶࡵࡨࡣࡼ࠹ࡣࠨᷝ"))):
        bstack1111ll1llll_opy_ = False
    if bstack11111ll1l1_opy_({bstack11l1l11_opy_ (u"ࠤࡸࡷࡪ࡝࠳ࡄࠤᷞ"): bstack1111ll1llll_opy_}):
        bstack11l11ll1ll_opy_ = bstack11l11ll1ll_opy_ or {}
        bstack11l11ll1ll_opy_[bstack11l1l11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡕࡇࡏࠬᷟ")] = bstack111l1l11111_opy_(framework)
        bstack11l11ll1ll_opy_[bstack11l1l11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳ࠭ᷠ")] = bstack1lll1ll1lll_opy_()
        bstack11l11ll1ll_opy_[bstack11l1l11_opy_ (u"ࠬࡺࡥࡴࡶ࡫ࡹࡧࡈࡵࡪ࡮ࡧ࡙ࡺ࡯ࡤࠨᷡ")] = bstack1l1llll1ll_opy_
        bstack11l11ll1ll_opy_[bstack11l1l11_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡕࡸ࡯ࡥࡷࡦࡸࡒࡧࡰࠨᷢ")] = bstack11111111l_opy_
        if bstack1l111l11111_opy_:
            bstack11l11ll1ll_opy_[bstack11l1l11_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧᷣ")] = bstack1l111l11111_opy_
            bstack11l11ll1ll_opy_[bstack11l1l11_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨᷤ")] = bstack1l1l11l1111_opy_
            bstack11l11ll1ll_opy_[bstack11l1l11_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩᷥ")][bstack11l1l11_opy_ (u"ࠪࡷࡨࡧ࡮࡯ࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫᷦ")] = bstack111l1l11ll1_opy_
        if getattr(options, bstack11l1l11_opy_ (u"ࠫࡸ࡫ࡴࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷࡽࠬᷧ"), None):
            options.set_capability(bstack11l1l11_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭ᷨ"), bstack11l11ll1ll_opy_)
        else:
            options[bstack11l1l11_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧᷩ")] = bstack11l11ll1ll_opy_
    else:
        if getattr(options, bstack11l1l11_opy_ (u"ࠧࡴࡧࡷࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡹࠨᷪ"), None):
            options.set_capability(bstack11l1l11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࡙ࡄࡌࠩᷫ"), bstack111l1l11111_opy_(framework))
            options.set_capability(bstack11l1l11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠪᷬ"), bstack1lll1ll1lll_opy_())
            options.set_capability(bstack11l1l11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡷࡩࡸࡺࡨࡶࡤࡅࡹ࡮ࡲࡤࡖࡷ࡬ࡨࠬᷭ"), bstack1l1llll1ll_opy_)
            options.set_capability(bstack11l1l11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡦࡺ࡯࡬ࡥࡒࡵࡳࡩࡻࡣࡵࡏࡤࡴࠬᷮ"), bstack11111111l_opy_)
            if bstack1l111l11111_opy_:
                options.set_capability(bstack11l1l11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫᷯ"), bstack1l111l11111_opy_)
                options.set_capability(bstack11l1l11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷࠬᷰ"), bstack1l1l11l1111_opy_)
                options.set_capability(bstack11l1l11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ࠴ࡳࡤࡣࡱࡲࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧᷱ"), bstack111l1l11ll1_opy_)
        else:
            options[bstack11l1l11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࡙ࡄࡌࠩᷲ")] = bstack111l1l11111_opy_(framework)
            options[bstack11l1l11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠪᷳ")] = bstack1lll1ll1lll_opy_()
            options[bstack11l1l11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡷࡩࡸࡺࡨࡶࡤࡅࡹ࡮ࡲࡤࡖࡷ࡬ࡨࠬᷴ")] = bstack1l1llll1ll_opy_
            options[bstack11l1l11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡦࡺ࡯࡬ࡥࡒࡵࡳࡩࡻࡣࡵࡏࡤࡴࠬ᷵")] = bstack11111111l_opy_
            if bstack1l111l11111_opy_:
                options[bstack11l1l11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ᷶")] = bstack1l111l11111_opy_
                options[bstack11l1l11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷ᷷ࠬ")] = bstack1l1l11l1111_opy_
                options[bstack11l1l11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ᷸࠭")][bstack11l1l11_opy_ (u"ࠨࡵࡦࡥࡳࡴࡥࡳࡘࡨࡶࡸ࡯࡯࡯᷹ࠩ")] = bstack111l1l11ll1_opy_
    return options
def bstack111l11l1111_opy_(ws_endpoint, framework):
    bstack11111111l_opy_ = bstack111ll1ll_opy_.get_property(bstack11l1l11_opy_ (u"ࠤࡓࡐࡆ࡟ࡗࡓࡋࡊࡌ࡙ࡥࡐࡓࡑࡇ࡙ࡈ࡚࡟ࡎࡃࡓ᷺ࠦ"))
    if ws_endpoint and len(ws_endpoint.split(bstack11l1l11_opy_ (u"ࠪࡧࡦࡶࡳ࠾ࠩ᷻"))) > 1:
        ws_url = ws_endpoint.split(bstack11l1l11_opy_ (u"ࠫࡨࡧࡰࡴ࠿ࠪ᷼"))[0]
        if bstack11l1l11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭ࠨ᷽") in ws_url:
            from browserstack_sdk._version import __version__
            bstack111l1l11lll_opy_ = json.loads(urllib.parse.unquote(ws_endpoint.split(bstack11l1l11_opy_ (u"࠭ࡣࡢࡲࡶࡁࠬ᷾"))[1]))
            bstack111l1l11lll_opy_ = bstack111l1l11lll_opy_ or {}
            bstack1l1llll1ll_opy_ = os.environ[bstack11l1l11_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈ᷿ࠬ")]
            bstack111l1l11lll_opy_[bstack11l1l11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࡙ࡄࡌࠩḀ")] = str(framework) + str(__version__)
            bstack111l1l11lll_opy_[bstack11l1l11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠪḁ")] = bstack1lll1ll1lll_opy_()
            bstack111l1l11lll_opy_[bstack11l1l11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡷࡩࡸࡺࡨࡶࡤࡅࡹ࡮ࡲࡤࡖࡷ࡬ࡨࠬḂ")] = bstack1l1llll1ll_opy_
            bstack111l1l11lll_opy_[bstack11l1l11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡦࡺ࡯࡬ࡥࡒࡵࡳࡩࡻࡣࡵࡏࡤࡴࠬḃ")] = bstack11111111l_opy_
            ws_endpoint = ws_endpoint.split(bstack11l1l11_opy_ (u"ࠬࡩࡡࡱࡵࡀࠫḄ"))[0] + bstack11l1l11_opy_ (u"࠭ࡣࡢࡲࡶࡁࠬḅ") + urllib.parse.quote(json.dumps(bstack111l1l11lll_opy_))
    return ws_endpoint
def bstack111l11111l_opy_():
    global bstack111l111l11_opy_
    from playwright._impl._browser_type import BrowserType
    bstack111l111l11_opy_ = BrowserType.connect
    return bstack111l111l11_opy_
def bstack11111ll11_opy_(framework_name):
    global bstack11llllll1_opy_
    bstack11llllll1_opy_ = framework_name
    return framework_name
def bstack1ll1l1l1l_opy_(self, *args, **kwargs):
    global bstack111l111l11_opy_
    try:
        global bstack11llllll1_opy_
        if bstack11l1l11_opy_ (u"ࠧࡸࡵࡈࡲࡩࡶ࡯ࡪࡰࡷࠫḆ") in kwargs:
            kwargs[bstack11l1l11_opy_ (u"ࠨࡹࡶࡉࡳࡪࡰࡰ࡫ࡱࡸࠬḇ")] = bstack111l11l1111_opy_(
                kwargs.get(bstack11l1l11_opy_ (u"ࠩࡺࡷࡊࡴࡤࡱࡱ࡬ࡲࡹ࠭Ḉ"), None),
                bstack11llllll1_opy_
            )
    except Exception as e:
        logger.error(bstack11l1l11_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡺ࡬ࡪࡴࠠࡱࡴࡲࡧࡪࡹࡳࡪࡰࡪࠤࡘࡊࡋࠡࡥࡤࡴࡸࡀࠠࡼࡿࠥḉ").format(str(e)))
    return bstack111l111l11_opy_(self, *args, **kwargs)
def bstack1111l11l1ll_opy_(bstack1111l11l1l1_opy_, proxies):
    proxy_settings = {}
    try:
        if not proxies:
            proxies = bstack11l11l1111_opy_(bstack1111l11l1l1_opy_, bstack11l1l11_opy_ (u"ࠦࠧḊ"))
        if proxies and proxies.get(bstack11l1l11_opy_ (u"ࠧ࡮ࡴࡵࡲࡶࠦḋ")):
            parsed_url = urlparse(proxies.get(bstack11l1l11_opy_ (u"ࠨࡨࡵࡶࡳࡷࠧḌ")))
            if parsed_url and parsed_url.hostname: proxy_settings[bstack11l1l11_opy_ (u"ࠧࡱࡴࡲࡼࡾࡎ࡯ࡴࡶࠪḍ")] = str(parsed_url.hostname)
            if parsed_url and parsed_url.port: proxy_settings[bstack11l1l11_opy_ (u"ࠨࡲࡵࡳࡽࡿࡐࡰࡴࡷࠫḎ")] = str(parsed_url.port)
            if parsed_url and parsed_url.username: proxy_settings[bstack11l1l11_opy_ (u"ࠩࡳࡶࡴࡾࡹࡖࡵࡨࡶࠬḏ")] = str(parsed_url.username)
            if parsed_url and parsed_url.password: proxy_settings[bstack11l1l11_opy_ (u"ࠪࡴࡷࡵࡸࡺࡒࡤࡷࡸ࠭Ḑ")] = str(parsed_url.password)
        return proxy_settings
    except:
        return proxy_settings
def bstack1ll111l1ll_opy_(bstack1111l11l1l1_opy_):
    bstack111l11l111l_opy_ = {
        bstack11l1l11l11l_opy_[bstack111l11l1l1l_opy_]: bstack1111l11l1l1_opy_[bstack111l11l1l1l_opy_]
        for bstack111l11l1l1l_opy_ in bstack1111l11l1l1_opy_
        if bstack111l11l1l1l_opy_ in bstack11l1l11l11l_opy_
    }
    bstack111l11l111l_opy_[bstack11l1l11_opy_ (u"ࠦࡵࡸ࡯ࡹࡻࡖࡩࡹࡺࡩ࡯ࡩࡶࠦḑ")] = bstack1111l11l1ll_opy_(bstack1111l11l1l1_opy_, bstack111ll1ll_opy_.get_property(bstack11l1l11_opy_ (u"ࠧࡶࡲࡰࡺࡼࡗࡪࡺࡴࡪࡰࡪࡷࠧḒ")))
    bstack111l11llll1_opy_ = [element.lower() for element in bstack11l1l1111l1_opy_]
    bstack111l1l111ll_opy_(bstack111l11l111l_opy_, bstack111l11llll1_opy_)
    return bstack111l11l111l_opy_
def bstack111l1l111ll_opy_(d, keys):
    for key in list(d.keys()):
        if key.lower() in keys:
            d[key] = bstack11l1l11_opy_ (u"ࠨࠪࠫࠬ࠭ࠦḓ")
    for value in d.values():
        if isinstance(value, dict):
            bstack111l1l111ll_opy_(value, keys)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    bstack111l1l111ll_opy_(item, keys)
def bstack1ll11111111_opy_():
    bstack1111l1l11l1_opy_ = [os.environ.get(bstack11l1l11_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡆࡊࡎࡈࡗࡤࡊࡉࡓࠤḔ")), os.path.join(os.path.expanduser(bstack11l1l11_opy_ (u"ࠣࢀࠥḕ")), bstack11l1l11_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩḖ")), os.path.join(bstack11l1l11_opy_ (u"ࠪ࠳ࡹࡳࡰࠨḗ"), bstack11l1l11_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫḘ"))]
    for path in bstack1111l1l11l1_opy_:
        if path is None:
            continue
        try:
            if os.path.exists(path):
                logger.debug(bstack11l1l11_opy_ (u"ࠧࡌࡩ࡭ࡧࠣࠫࠧḙ") + str(path) + bstack11l1l11_opy_ (u"ࠨࠧࠡࡧࡻ࡭ࡸࡺࡳ࠯ࠤḚ"))
                if not os.access(path, os.W_OK):
                    logger.debug(bstack11l1l11_opy_ (u"ࠢࡈ࡫ࡹ࡭ࡳ࡭ࠠࡱࡧࡵࡱ࡮ࡹࡳࡪࡱࡱࡷࠥ࡬࡯ࡳࠢࠪࠦḛ") + str(path) + bstack11l1l11_opy_ (u"ࠣࠩࠥḜ"))
                    os.chmod(path, 0o777)
                else:
                    logger.debug(bstack11l1l11_opy_ (u"ࠤࡉ࡭ࡱ࡫ࠠࠨࠤḝ") + str(path) + bstack11l1l11_opy_ (u"ࠥࠫࠥࡧ࡬ࡳࡧࡤࡨࡾࠦࡨࡢࡵࠣࡸ࡭࡫ࠠࡳࡧࡴࡹ࡮ࡸࡥࡥࠢࡳࡩࡷࡳࡩࡴࡵ࡬ࡳࡳࡹ࠮ࠣḞ"))
            else:
                logger.debug(bstack11l1l11_opy_ (u"ࠦࡈࡸࡥࡢࡶ࡬ࡲ࡬ࠦࡦࡪ࡮ࡨࠤࠬࠨḟ") + str(path) + bstack11l1l11_opy_ (u"ࠧ࠭ࠠࡸ࡫ࡷ࡬ࠥࡽࡲࡪࡶࡨࠤࡵ࡫ࡲ࡮࡫ࡶࡷ࡮ࡵ࡮࠯ࠤḠ"))
                os.makedirs(path, exist_ok=True)
                os.chmod(path, 0o777)
            logger.debug(bstack11l1l11_opy_ (u"ࠨࡏࡱࡧࡵࡥࡹ࡯࡯࡯ࠢࡶࡹࡨࡩࡥࡦࡦࡨࡨࠥ࡬࡯ࡳࠢࠪࠦḡ") + str(path) + bstack11l1l11_opy_ (u"ࠢࠨ࠰ࠥḢ"))
            return path
        except Exception as e:
            logger.debug(bstack11l1l11_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡸ࡫ࡴࠡࡷࡳࠤ࡫࡯࡬ࡦࠢࠪࡿࡵࡧࡴࡩࡿࠪ࠾ࠥࠨḣ") + str(e) + bstack11l1l11_opy_ (u"ࠤࠥḤ"))
    logger.debug(bstack11l1l11_opy_ (u"ࠥࡅࡱࡲࠠࡱࡣࡷ࡬ࡸࠦࡦࡢ࡫࡯ࡩࡩ࠴ࠢḥ"))
    return None
@measure(event_name=EVENTS.bstack11l11lll1l1_opy_, stage=STAGE.bstack111llllll_opy_)
def bstack1l1l1ll1111_opy_(binary_path, bstack1l1l111ll11_opy_, bs_config):
    logger.debug(bstack11l1l11_opy_ (u"ࠦࡈࡻࡲࡳࡧࡱࡸࠥࡉࡌࡊࠢࡓࡥࡹ࡮ࠠࡧࡱࡸࡲࡩࡀࠠࡼࡿࠥḦ").format(binary_path))
    bstack111l11lll1l_opy_ = bstack11l1l11_opy_ (u"ࠬ࠭ḧ")
    bstack1111lllll1l_opy_ = {
        bstack11l1l11_opy_ (u"࠭ࡳࡥ࡭ࡢࡺࡪࡸࡳࡪࡱࡱࠫḨ"): __version__,
        bstack11l1l11_opy_ (u"ࠢࡰࡵࠥḩ"): platform.system(),
        bstack11l1l11_opy_ (u"ࠣࡱࡶࡣࡦࡸࡣࡩࠤḪ"): platform.machine(),
        bstack11l1l11_opy_ (u"ࠤࡦࡰ࡮ࡥࡶࡦࡴࡶ࡭ࡴࡴࠢḫ"): bstack11l1l11_opy_ (u"ࠪ࠴ࠬḬ"),
        bstack11l1l11_opy_ (u"ࠦࡸࡪ࡫ࡠ࡮ࡤࡲ࡬ࡻࡡࡨࡧࠥḭ"): bstack11l1l11_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲࠬḮ")
    }
    bstack1111ll11l1l_opy_(bstack1111lllll1l_opy_)
    try:
        if binary_path:
            bstack1111lllll1l_opy_[bstack11l1l11_opy_ (u"࠭ࡣ࡭࡫ࡢࡺࡪࡸࡳࡪࡱࡱࠫḯ")] = subprocess.check_output([binary_path, bstack11l1l11_opy_ (u"ࠢࡷࡧࡵࡷ࡮ࡵ࡮ࠣḰ")]).strip().decode(bstack11l1l11_opy_ (u"ࠨࡷࡷࡪ࠲࠾ࠧḱ"))
        response = requests.request(
            bstack11l1l11_opy_ (u"ࠩࡊࡉ࡙࠭Ḳ"),
            url=bstack1l11l1111_opy_(bstack11l1l1l1111_opy_),
            headers=None,
            auth=(bs_config[bstack11l1l11_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬḳ")], bs_config[bstack11l1l11_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧḴ")]),
            json=None,
            params=bstack1111lllll1l_opy_
        )
        data = response.json()
        if response.status_code == 200 and bstack11l1l11_opy_ (u"ࠬࡻࡲ࡭ࠩḵ") in data.keys() and bstack11l1l11_opy_ (u"࠭ࡵࡱࡦࡤࡸࡪࡪ࡟ࡤ࡮࡬ࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬḶ") in data.keys():
            logger.debug(bstack11l1l11_opy_ (u"ࠢࡏࡧࡨࡨࠥࡺ࡯ࠡࡷࡳࡨࡦࡺࡥࠡࡤ࡬ࡲࡦࡸࡹ࠭ࠢࡦࡹࡷࡸࡥ࡯ࡶࠣࡦ࡮ࡴࡡࡳࡻࠣࡺࡪࡸࡳࡪࡱࡱ࠾ࠥࢁࡽࠣḷ").format(bstack1111lllll1l_opy_[bstack11l1l11_opy_ (u"ࠨࡥ࡯࡭ࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭Ḹ")]))
            if bstack11l1l11_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡄࡌࡒࡆࡘ࡙ࡠࡗࡕࡐࠬḹ") in os.environ:
                logger.debug(bstack11l1l11_opy_ (u"ࠥࡗࡰ࡯ࡰࡱ࡫ࡱ࡫ࠥࡨࡩ࡯ࡣࡵࡽࠥࡪ࡯ࡸࡰ࡯ࡳࡦࡪࠠࡢࡵࠣࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡅࡍࡓࡇࡒ࡚ࡡࡘࡖࡑࠦࡩࡴࠢࡶࡩࡹࠨḺ"))
                data[bstack11l1l11_opy_ (u"ࠫࡺࡸ࡬ࠨḻ")] = os.environ[bstack11l1l11_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡇࡏࡎࡂࡔ࡜ࡣ࡚ࡘࡌࠨḼ")]
            bstack1111lllll11_opy_ = bstack1111l1ll1l1_opy_(data[bstack11l1l11_opy_ (u"࠭ࡵࡳ࡮ࠪḽ")], bstack1l1l111ll11_opy_)
            bstack111l11lll1l_opy_ = os.path.join(bstack1l1l111ll11_opy_, bstack1111lllll11_opy_)
            os.chmod(bstack111l11lll1l_opy_, 0o777) # bstack111l11lll11_opy_ permission
            return bstack111l11lll1l_opy_
    except Exception as e:
        logger.debug(bstack11l1l11_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡷࡩ࡫࡯ࡩࠥࡪ࡯ࡸࡰ࡯ࡳࡦࡪࡩ࡯ࡩࠣࡲࡪࡽࠠࡔࡆࡎࠤࢀࢃࠢḾ").format(e))
    return binary_path
def bstack1111ll11l1l_opy_(bstack1111lllll1l_opy_):
    try:
        if bstack11l1l11_opy_ (u"ࠨ࡮࡬ࡲࡺࡾࠧḿ") not in bstack1111lllll1l_opy_[bstack11l1l11_opy_ (u"ࠩࡲࡷࠬṀ")].lower():
            return
        if os.path.exists(bstack11l1l11_opy_ (u"ࠥ࠳ࡪࡺࡣ࠰ࡱࡶ࠱ࡷ࡫࡬ࡦࡣࡶࡩࠧṁ")):
            with open(bstack11l1l11_opy_ (u"ࠦ࠴࡫ࡴࡤ࠱ࡲࡷ࠲ࡸࡥ࡭ࡧࡤࡷࡪࠨṂ"), bstack11l1l11_opy_ (u"ࠧࡸࠢṃ")) as f:
                bstack111l111l111_opy_ = {}
                for line in f:
                    if bstack11l1l11_opy_ (u"ࠨ࠽ࠣṄ") in line:
                        key, value = line.rstrip().split(bstack11l1l11_opy_ (u"ࠢ࠾ࠤṅ"), 1)
                        bstack111l111l111_opy_[key] = value.strip(bstack11l1l11_opy_ (u"ࠨࠤ࡟ࠫࠬṆ"))
                bstack1111lllll1l_opy_[bstack11l1l11_opy_ (u"ࠩࡧ࡭ࡸࡺࡲࡰࠩṇ")] = bstack111l111l111_opy_.get(bstack11l1l11_opy_ (u"ࠥࡍࡉࠨṈ"), bstack11l1l11_opy_ (u"ࠦࠧṉ"))
        elif os.path.exists(bstack11l1l11_opy_ (u"ࠧ࠵ࡥࡵࡥ࠲ࡥࡱࡶࡩ࡯ࡧ࠰ࡶࡪࡲࡥࡢࡵࡨࠦṊ")):
            bstack1111lllll1l_opy_[bstack11l1l11_opy_ (u"࠭ࡤࡪࡵࡷࡶࡴ࠭ṋ")] = bstack11l1l11_opy_ (u"ࠧࡢ࡮ࡳ࡭ࡳ࡫ࠧṌ")
    except Exception as e:
        logger.debug(bstack11l1l11_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤ࡬࡫ࡴࠡࡦ࡬ࡷࡹࡸ࡯ࠡࡱࡩࠤࡱ࡯࡮ࡶࡺࠥṍ") + e)
@measure(event_name=EVENTS.bstack11l1l11lll1_opy_, stage=STAGE.bstack111llllll_opy_)
def bstack1111l1ll1l1_opy_(bstack1111l111ll1_opy_, bstack1111lll11l1_opy_):
    logger.debug(bstack11l1l11_opy_ (u"ࠤࡇࡳࡼࡴ࡬ࡰࡣࡧ࡭ࡳ࡭ࠠࡔࡆࡎࠤࡧ࡯࡮ࡢࡴࡼࠤ࡫ࡸ࡯࡮࠼ࠣࠦṎ") + str(bstack1111l111ll1_opy_) + bstack11l1l11_opy_ (u"ࠥࠦṏ"))
    zip_path = os.path.join(bstack1111lll11l1_opy_, bstack11l1l11_opy_ (u"ࠦࡩࡵࡷ࡯࡮ࡲࡥࡩ࡫ࡤࡠࡨ࡬ࡰࡪ࠴ࡺࡪࡲࠥṐ"))
    bstack1111lllll11_opy_ = bstack11l1l11_opy_ (u"ࠬ࠭ṑ")
    with requests.get(bstack1111l111ll1_opy_, stream=True) as response:
        response.raise_for_status()
        with open(zip_path, bstack11l1l11_opy_ (u"ࠨࡷࡣࠤṒ")) as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
        logger.debug(bstack11l1l11_opy_ (u"ࠢࡇ࡫࡯ࡩࠥࡪ࡯ࡸࡰ࡯ࡳࡦࡪࡥࡥࠢࡶࡹࡨࡩࡥࡴࡵࡩࡹࡱࡲࡹ࠯ࠤṓ"))
    with zipfile.ZipFile(zip_path, bstack11l1l11_opy_ (u"ࠨࡴࠪṔ")) as zip_ref:
        bstack1111ll11111_opy_ = zip_ref.namelist()
        if len(bstack1111ll11111_opy_) > 0:
            bstack1111lllll11_opy_ = bstack1111ll11111_opy_[0] # bstack1111ll1l111_opy_ bstack11l11lll111_opy_ will be bstack111l111ll1l_opy_ 1 file i.e. the binary in the zip
        zip_ref.extractall(bstack1111lll11l1_opy_)
        logger.debug(bstack11l1l11_opy_ (u"ࠤࡉ࡭ࡱ࡫ࡳࠡࡵࡸࡧࡨ࡫ࡳࡴࡨࡸࡰࡱࡿࠠࡦࡺࡷࡶࡦࡩࡴࡦࡦࠣࡸࡴࠦࠧࠣṕ") + str(bstack1111lll11l1_opy_) + bstack11l1l11_opy_ (u"ࠥࠫࠧṖ"))
    os.remove(zip_path)
    return bstack1111lllll11_opy_
def get_cli_dir():
    bstack1111l1lllll_opy_ = bstack1ll11111111_opy_()
    if bstack1111l1lllll_opy_:
        bstack1l1l111ll11_opy_ = os.path.join(bstack1111l1lllll_opy_, bstack11l1l11_opy_ (u"ࠦࡨࡲࡩࠣṗ"))
        if not os.path.exists(bstack1l1l111ll11_opy_):
            os.makedirs(bstack1l1l111ll11_opy_, mode=0o777, exist_ok=True)
        return bstack1l1l111ll11_opy_
    else:
        raise FileNotFoundError(bstack11l1l11_opy_ (u"ࠧࡔ࡯ࠡࡹࡵ࡭ࡹࡧࡢ࡭ࡧࠣࡨ࡮ࡸࡥࡤࡶࡲࡶࡾࠦࡡࡷࡣ࡬ࡰࡦࡨ࡬ࡦࠢࡩࡳࡷࠦࡴࡩࡧࠣࡗࡉࡑࠠࡣ࡫ࡱࡥࡷࡿ࠮ࠣṘ"))
def bstack1l11ll111ll_opy_(bstack1l1l111ll11_opy_):
    bstack11l1l11_opy_ (u"ࠨࠢࠣࡉࡨࡸࠥࡺࡨࡦࠢࡳࡥࡹ࡮ࠠࡧࡱࡵࠤࡹ࡮ࡥࠡࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠠࡔࡆࡎࠤࡧ࡯࡮ࡢࡴࡼࠤ࡮ࡴࠠࡢࠢࡺࡶ࡮ࡺࡡࡣ࡮ࡨࠤࡩ࡯ࡲࡦࡥࡷࡳࡷࡿ࠮ࠣࠤࠥṙ")
    bstack111l1111lll_opy_ = [
        os.path.join(bstack1l1l111ll11_opy_, f)
        for f in os.listdir(bstack1l1l111ll11_opy_)
        if os.path.isfile(os.path.join(bstack1l1l111ll11_opy_, f)) and f.startswith(bstack11l1l11_opy_ (u"ࠢࡣ࡫ࡱࡥࡷࡿ࠭ࠣṚ"))
    ]
    if len(bstack111l1111lll_opy_) > 0:
        return max(bstack111l1111lll_opy_, key=os.path.getmtime) # get bstack111l1l111l1_opy_ binary
    return bstack11l1l11_opy_ (u"ࠣࠤṛ")
def bstack1111l11llll_opy_():
  from selenium import webdriver
  return version.parse(webdriver.__version__)
def bstack1l1111llll1_opy_(d, u):
  for k, v in u.items():
    if isinstance(v, collections.abc.Mapping):
      d[k] = bstack1l1111llll1_opy_(d.get(k, {}), v)
    else:
      if isinstance(v, list):
        d[k] = d.get(k, []) + v
      else:
        d[k] = v
  return d
def bstack1lllllll11_opy_(data, keys, default=None):
    bstack11l1l11_opy_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࡖࡥ࡫࡫࡬ࡺࠢࡪࡩࡹࠦࡡࠡࡰࡨࡷࡹ࡫ࡤࠡࡸࡤࡰࡺ࡫ࠠࡧࡴࡲࡱࠥࡧࠠࡥ࡫ࡦࡸ࡮ࡵ࡮ࡢࡴࡼࠤࡴࡸࠠ࡭࡫ࡶࡸ࠳ࠐࠠࠡࠢࠣ࠾ࡵࡧࡲࡢ࡯ࠣࡨࡦࡺࡡ࠻ࠢࡗ࡬ࡪࠦࡤࡪࡥࡷ࡭ࡴࡴࡡࡳࡻࠣࡳࡷࠦ࡬ࡪࡵࡷࠤࡹࡵࠠࡵࡴࡤࡺࡪࡸࡳࡦ࠰ࠍࠤࠥࠦࠠ࠻ࡲࡤࡶࡦࡳࠠ࡬ࡧࡼࡷ࠿ࠦࡁࠡ࡮࡬ࡷࡹࠦ࡯ࡧࠢ࡮ࡩࡾࡹ࠯ࡪࡰࡧ࡭ࡨ࡫ࡳࠡࡴࡨࡴࡷ࡫ࡳࡦࡰࡷ࡭ࡳ࡭ࠠࡵࡪࡨࠤࡵࡧࡴࡩ࠰ࠍࠤࠥࠦࠠ࠻ࡲࡤࡶࡦࡳࠠࡥࡧࡩࡥࡺࡲࡴ࠻࡙ࠢࡥࡱࡻࡥࠡࡶࡲࠤࡷ࡫ࡴࡶࡴࡱࠤ࡮࡬ࠠࡵࡪࡨࠤࡵࡧࡴࡩࠢࡧࡳࡪࡹࠠ࡯ࡱࡷࠤࡪࡾࡩࡴࡶ࠱ࠎࠥࠦࠠࠡ࠼ࡵࡩࡹࡻࡲ࡯࠼ࠣࡘ࡭࡫ࠠࡷࡣ࡯ࡹࡪࠦࡡࡵࠢࡷ࡬ࡪࠦ࡮ࡦࡵࡷࡩࡩࠦࡰࡢࡶ࡫࠰ࠥࡵࡲࠡࡦࡨࡪࡦࡻ࡬ࡵࠢ࡬ࡪࠥࡴ࡯ࡵࠢࡩࡳࡺࡴࡤ࠯ࠌࠣࠤࠥࠦࠢࠣࠤṜ")
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