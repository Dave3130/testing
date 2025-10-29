# coding: UTF-8
import sys
bstack1l1l111_opy_ = sys.version_info [0] == 2
bstack11l1ll_opy_ = 2048
bstack1llll11_opy_ = 7
def bstack11ll1l_opy_ (bstack1llllll1_opy_):
    global bstack1ll11_opy_
    bstack11ll111_opy_ = ord (bstack1llllll1_opy_ [-1])
    bstack1lll111_opy_ = bstack1llllll1_opy_ [:-1]
    bstack11l11l_opy_ = bstack11ll111_opy_ % len (bstack1lll111_opy_)
    bstack1l1ll11_opy_ = bstack1lll111_opy_ [:bstack11l11l_opy_] + bstack1lll111_opy_ [bstack11l11l_opy_:]
    if bstack1l1l111_opy_:
        bstack11111l1_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1ll_opy_ - (bstack1l11111_opy_ + bstack11ll111_opy_) % bstack1llll11_opy_) for bstack1l11111_opy_, char in enumerate (bstack1l1ll11_opy_)])
    else:
        bstack11111l1_opy_ = str () .join ([chr (ord (char) - bstack11l1ll_opy_ - (bstack1l11111_opy_ + bstack11ll111_opy_) % bstack1llll11_opy_) for bstack1l11111_opy_, char in enumerate (bstack1l1ll11_opy_)])
    return eval (bstack11111l1_opy_)
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
from bstack_utils.constants import (bstack111ll1l111_opy_, bstack11111lll1l_opy_, bstack1l1llll1l_opy_,
                                    bstack11l1l11111l_opy_, bstack11l1l11llll_opy_, bstack11l11l1l111_opy_, bstack11l1l111l1l_opy_)
from bstack_utils.measure import measure
from bstack_utils.messages import bstack1l11l11l11_opy_, bstack1ll1ll1lll_opy_
from bstack_utils.proxy import bstack1ll11ll1l_opy_, bstack111lll1111_opy_
from bstack_utils.constants import *
from bstack_utils import bstack1l11111111_opy_
from bstack_utils.bstack111111ll11_opy_ import bstack1l1lll1l11_opy_
from browserstack_sdk._version import __version__
bstack111ll1l1_opy_ = Config.bstack111111ll_opy_()
logger = bstack1l11111111_opy_.get_logger(__name__, bstack1l11111111_opy_.bstack1l1l1llll11_opy_())
def bstack111l1l11l1l_opy_(config):
    return config[bstack11ll1l_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫᰉ")]
def bstack111l111l1l1_opy_(config):
    return config[bstack11ll1l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭ᰊ")]
def bstack1l11ll1l1_opy_():
    try:
        import playwright
        return True
    except ImportError:
        return False
def bstack1111ll1ll11_opy_(obj):
    values = []
    bstack1111llllll1_opy_ = re.compile(bstack11ll1l_opy_ (u"ࡶࠧࡤࡃࡖࡕࡗࡓࡒࡥࡔࡂࡉࡢࡠࡩ࠱ࠤࠣᰋ"), re.I)
    for key in obj.keys():
        if bstack1111llllll1_opy_.match(key):
            values.append(obj[key])
    return values
def bstack111l11ll1ll_opy_(config):
    tags = []
    tags.extend(bstack1111ll1ll11_opy_(os.environ))
    tags.extend(bstack1111ll1ll11_opy_(config))
    return tags
def bstack1111l11l1l1_opy_(markers):
    tags = []
    for marker in markers:
        tags.append(marker.name)
    return tags
def bstack111l1111ll1_opy_(bstack111l1ll111l_opy_):
    if not bstack111l1ll111l_opy_:
        return bstack11ll1l_opy_ (u"ࠬ࠭ᰌ")
    return bstack11ll1l_opy_ (u"ࠨࡻࡾࠢࠫࡿࢂ࠯ࠢᰍ").format(bstack111l1ll111l_opy_.name, bstack111l1ll111l_opy_.email)
def bstack1111lll1l11_opy_():
    try:
        repo = git.Repo(search_parent_directories=True)
        bstack1111llll1ll_opy_ = repo.common_dir
        info = {
            bstack11ll1l_opy_ (u"ࠢࡴࡪࡤࠦᰎ"): repo.head.commit.hexsha,
            bstack11ll1l_opy_ (u"ࠣࡵ࡫ࡳࡷࡺ࡟ࡴࡪࡤࠦᰏ"): repo.git.rev_parse(repo.head.commit, short=True),
            bstack11ll1l_opy_ (u"ࠤࡥࡶࡦࡴࡣࡩࠤᰐ"): repo.active_branch.name,
            bstack11ll1l_opy_ (u"ࠥࡸࡦ࡭ࠢᰑ"): repo.git.describe(all=True, tags=True, exact_match=True),
            bstack11ll1l_opy_ (u"ࠦࡨࡵ࡭࡮࡫ࡷࡸࡪࡸࠢᰒ"): bstack111l1111ll1_opy_(repo.head.commit.committer),
            bstack11ll1l_opy_ (u"ࠧࡩ࡯࡮࡯࡬ࡸࡹ࡫ࡲࡠࡦࡤࡸࡪࠨᰓ"): repo.head.commit.committed_datetime.isoformat(),
            bstack11ll1l_opy_ (u"ࠨࡡࡶࡶ࡫ࡳࡷࠨᰔ"): bstack111l1111ll1_opy_(repo.head.commit.author),
            bstack11ll1l_opy_ (u"ࠢࡢࡷࡷ࡬ࡴࡸ࡟ࡥࡣࡷࡩࠧᰕ"): repo.head.commit.authored_datetime.isoformat(),
            bstack11ll1l_opy_ (u"ࠣࡥࡲࡱࡲ࡯ࡴࡠ࡯ࡨࡷࡸࡧࡧࡦࠤᰖ"): repo.head.commit.message,
            bstack11ll1l_opy_ (u"ࠤࡵࡳࡴࡺࠢᰗ"): repo.git.rev_parse(bstack11ll1l_opy_ (u"ࠥ࠱࠲ࡹࡨࡰࡹ࠰ࡸࡴࡶ࡬ࡦࡸࡨࡰࠧᰘ")),
            bstack11ll1l_opy_ (u"ࠦࡨࡵ࡭࡮ࡱࡱࡣ࡬࡯ࡴࡠࡦ࡬ࡶࠧᰙ"): bstack1111llll1ll_opy_,
            bstack11ll1l_opy_ (u"ࠧࡽ࡯ࡳ࡭ࡷࡶࡪ࡫࡟ࡨ࡫ࡷࡣࡩ࡯ࡲࠣᰚ"): subprocess.check_output([bstack11ll1l_opy_ (u"ࠨࡧࡪࡶࠥᰛ"), bstack11ll1l_opy_ (u"ࠢࡳࡧࡹ࠱ࡵࡧࡲࡴࡧࠥᰜ"), bstack11ll1l_opy_ (u"ࠣ࠯࠰࡫࡮ࡺ࠭ࡤࡱࡰࡱࡴࡴ࠭ࡥ࡫ࡵࠦᰝ")]).strip().decode(
                bstack11ll1l_opy_ (u"ࠩࡸࡸ࡫࠳࠸ࠨᰞ")),
            bstack11ll1l_opy_ (u"ࠥࡰࡦࡹࡴࡠࡶࡤ࡫ࠧᰟ"): repo.git.describe(tags=True, abbrev=0, always=True),
            bstack11ll1l_opy_ (u"ࠦࡨࡵ࡭࡮࡫ࡷࡷࡤࡹࡩ࡯ࡥࡨࡣࡱࡧࡳࡵࡡࡷࡥ࡬ࠨᰠ"): repo.git.rev_list(
                bstack11ll1l_opy_ (u"ࠧࢁࡽ࠯࠰ࡾࢁࠧᰡ").format(repo.head.commit, repo.git.describe(tags=True, abbrev=0, always=True)), count=True)
        }
        remotes = repo.remotes
        bstack1111ll1111l_opy_ = []
        for remote in remotes:
            bstack1111ll1l11l_opy_ = {
                bstack11ll1l_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᰢ"): remote.name,
                bstack11ll1l_opy_ (u"ࠢࡶࡴ࡯ࠦᰣ"): remote.url,
            }
            bstack1111ll1111l_opy_.append(bstack1111ll1l11l_opy_)
        bstack111l1111l11_opy_ = {
            bstack11ll1l_opy_ (u"ࠣࡰࡤࡱࡪࠨᰤ"): bstack11ll1l_opy_ (u"ࠤࡪ࡭ࡹࠨᰥ"),
            **info,
            bstack11ll1l_opy_ (u"ࠥࡶࡪࡳ࡯ࡵࡧࡶࠦᰦ"): bstack1111ll1111l_opy_
        }
        bstack111l1111l11_opy_ = bstack1111l1l1ll1_opy_(bstack111l1111l11_opy_)
        return bstack111l1111l11_opy_
    except git.InvalidGitRepositoryError:
        return {}
    except Exception as err:
        print(bstack11ll1l_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡴࡶࡵ࡭ࡣࡷ࡭ࡳ࡭ࠠࡈ࡫ࡷࠤࡲ࡫ࡴࡢࡦࡤࡸࡦࠦࡷࡪࡶ࡫ࠤࡪࡸࡲࡰࡴ࠽ࠤࢀࢃࠢᰧ").format(err))
        return {}
def bstack11ll1l11ll1_opy_(bstack111l11l111l_opy_=None):
    bstack11ll1l_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࡍࡥࡵࠢࡪ࡭ࡹࠦ࡭ࡦࡶࡤࡨࡦࡺࡡࠡࡵࡳࡩࡨ࡯ࡦࡪࡥࡤࡰࡱࡿࠠࡧࡱࡵࡱࡦࡺࡴࡦࡦࠣࡪࡴࡸࠠࡂࡋࠣࡷࡪࡲࡥࡤࡶ࡬ࡳࡳࠦࡵࡴࡧࠣࡧࡦࡹࡥࡴࠢࡩࡳࡷࠦࡥࡢࡥ࡫ࠤ࡫ࡵ࡬ࡥࡧࡵࠤ࡮ࡴࠠࡵࡪࡨࠤࡱ࡯ࡳࡵ࠰ࠍࠤࠥࠦࠠࡂࡴࡪࡷ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡧࡱ࡯ࡨࡪࡸࡳࠡࠪ࡯࡭ࡸࡺࠬࠡࡱࡳࡸ࡮ࡵ࡮ࡢ࡮ࠬ࠾ࠥࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࠲ࠦࡎࡰࡰࡨ࠾ࠥࡓ࡯࡯ࡱ࠰ࡶࡪࡶ࡯ࠡࡣࡳࡴࡷࡵࡡࡤࡪ࠯ࠤࡺࡹࡥࡴࠢࡦࡹࡷࡸࡥ࡯ࡶࠣࡨ࡮ࡸࡥࡤࡶࡲࡶࡾ࡛ࠦࡰࡵ࠱࡫ࡪࡺࡣࡸࡦࠫ࠭ࡢࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࠲ࠦࡅ࡮ࡲࡷࡽࠥࡲࡩࡴࡶࠣ࡟ࡢࡀࠠࡎࡷ࡯ࡸ࡮࠳ࡲࡦࡲࡲࠤࡦࡶࡰࡳࡱࡤࡧ࡭ࠦࡷࡪࡶ࡫ࠤࡳࡵࠠࡴࡱࡸࡶࡨ࡫ࡳࠡࡥࡲࡲ࡫࡯ࡧࡶࡴࡨࡨ࠱ࠦࡲࡦࡶࡸࡶࡳࡹࠠ࡜࡟ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡ࠯ࠣࡐ࡮ࡹࡴࠡࡱࡩࠤࡵࡧࡴࡩࡵ࠽ࠤࡒࡻ࡬ࡵ࡫࠰ࡶࡪࡶ࡯ࠡࡣࡳࡴࡷࡵࡡࡤࡪࠣࡻ࡮ࡺࡨࠡࡵࡳࡩࡨ࡯ࡦࡪࡥࠣࡪࡴࡲࡤࡦࡴࡶࠤࡹࡵࠠࡢࡰࡤࡰࡾࢀࡥࠋࠢࠣࠤࠥࡘࡥࡵࡷࡵࡲࡸࡀࠊࠡࠢࠣࠤࠥࠦࠠࠡ࡮࡬ࡷࡹࡀࠠࡍ࡫ࡶࡸࠥࡵࡦࠡࡦ࡬ࡧࡹࡹࠬࠡࡧࡤࡧ࡭ࠦࡣࡰࡰࡷࡥ࡮ࡴࡩ࡯ࡩࠣ࡫࡮ࡺࠠ࡮ࡧࡷࡥࡩࡧࡴࡢࠢࡩࡳࡷࠦࡡࠡࡨࡲࡰࡩ࡫ࡲ࠯ࠌࠣࠤࠥࠦࠢࠣࠤᰨ")
    if bstack111l11l111l_opy_ is None:
        bstack111l11l111l_opy_ = [os.getcwd()]
    elif isinstance(bstack111l11l111l_opy_, list) and len(bstack111l11l111l_opy_) == 0:
        return []
    results = []
    for folder in bstack111l11l111l_opy_:
        try:
            if not os.path.exists(folder):
                raise Exception(bstack11ll1l_opy_ (u"ࠨࡆࡰ࡮ࡧࡩࡷࠦࡤࡰࡧࡶࠤࡳࡵࡴࠡࡧࡻ࡭ࡸࡺ࠺ࠡࡽࢀࠦᰩ").format(folder))
            repo = git.Repo(folder, search_parent_directories=True)
            result = {
                bstack11ll1l_opy_ (u"ࠢࡱࡴࡌࡨࠧᰪ"): bstack11ll1l_opy_ (u"ࠣࠤᰫ"),
                bstack11ll1l_opy_ (u"ࠤࡩ࡭ࡱ࡫ࡳࡄࡪࡤࡲ࡬࡫ࡤࠣᰬ"): [],
                bstack11ll1l_opy_ (u"ࠥࡥࡺࡺࡨࡰࡴࡶࠦᰭ"): [],
                bstack11ll1l_opy_ (u"ࠦࡵࡸࡄࡢࡶࡨࠦᰮ"): bstack11ll1l_opy_ (u"ࠧࠨᰯ"),
                bstack11ll1l_opy_ (u"ࠨࡣࡰ࡯ࡰ࡭ࡹࡓࡥࡴࡵࡤ࡫ࡪࡹࠢᰰ"): [],
                bstack11ll1l_opy_ (u"ࠢࡱࡴࡗ࡭ࡹࡲࡥࠣᰱ"): bstack11ll1l_opy_ (u"ࠣࠤᰲ"),
                bstack11ll1l_opy_ (u"ࠤࡳࡶࡉ࡫ࡳࡤࡴ࡬ࡴࡹ࡯࡯࡯ࠤᰳ"): bstack11ll1l_opy_ (u"ࠥࠦᰴ"),
                bstack11ll1l_opy_ (u"ࠦࡵࡸࡒࡢࡹࡇ࡭࡫࡬ࠢᰵ"): bstack11ll1l_opy_ (u"ࠧࠨᰶ")
            }
            bstack111l1l11lll_opy_ = repo.active_branch.name
            bstack111l111111l_opy_ = repo.head.commit
            result[bstack11ll1l_opy_ (u"ࠨࡰࡳࡋࡧ᰷ࠦ")] = bstack111l111111l_opy_.hexsha
            bstack111l111ll11_opy_ = _1111l1l11ll_opy_(repo)
            logger.debug(bstack11ll1l_opy_ (u"ࠢࡃࡣࡶࡩࠥࡨࡲࡢࡰࡦ࡬ࠥ࡬࡯ࡳࠢࡦࡳࡲࡶࡡࡳ࡫ࡶࡳࡳࡀࠠࠣ᰸") + str(bstack111l111ll11_opy_) + bstack11ll1l_opy_ (u"ࠣࠤ᰹"))
            if bstack111l111ll11_opy_:
                try:
                    bstack111l1l1l111_opy_ = repo.git.diff(bstack11ll1l_opy_ (u"ࠤ࠰࠱ࡳࡧ࡭ࡦ࠯ࡲࡲࡱࡿࠢ᰺"), bstack11ll1l1l_opy_ (u"ࠥࡿࡧࡧࡳࡦࡡࡥࡶࡦࡴࡣࡩࡿ࠱࠲࠳ࢁࡣࡶࡴࡵࡩࡳࡺ࡟ࡣࡴࡤࡲࡨ࡮ࡽࠣ᰻")).split(bstack11ll1l_opy_ (u"ࠫࡡࡴࠧ᰼"))
                    logger.debug(bstack11ll1l_opy_ (u"ࠧࡉࡨࡢࡰࡪࡩࡩࠦࡦࡪ࡮ࡨࡷࠥࡨࡥࡵࡹࡨࡩࡳࠦࡻࡣࡣࡶࡩࡤࡨࡲࡢࡰࡦ࡬ࢂࠦࡡ࡯ࡦࠣࡿࡨࡻࡲࡳࡧࡱࡸࡤࡨࡲࡢࡰࡦ࡬ࢂࡀࠠࠣ᰽") + str(bstack111l1l1l111_opy_) + bstack11ll1l_opy_ (u"ࠨࠢ᰾"))
                    result[bstack11ll1l_opy_ (u"ࠢࡧ࡫࡯ࡩࡸࡉࡨࡢࡰࡪࡩࡩࠨ᰿")] = [f.strip() for f in bstack111l1l1l111_opy_ if f.strip()]
                    commits = list(repo.iter_commits(bstack11ll1l1l_opy_ (u"ࠣࡽࡥࡥࡸ࡫࡟ࡣࡴࡤࡲࡨ࡮ࡽ࠯࠰ࡾࡧࡺࡸࡲࡦࡰࡷࡣࡧࡸࡡ࡯ࡥ࡫ࢁࠧ᱀")))
                except Exception:
                    logger.debug(bstack11ll1l_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥ࡭ࡥࡵࠢࡦ࡬ࡦࡴࡧࡦࡦࠣࡪ࡮ࡲࡥࡴࠢࡩࡶࡴࡳࠠࡣࡴࡤࡲࡨ࡮ࠠࡤࡱࡰࡴࡦࡸࡩࡴࡱࡱ࠲ࠥࡌࡡ࡭࡮࡬ࡲ࡬ࠦࡢࡢࡥ࡮ࠤࡹࡵࠠࡳࡧࡦࡩࡳࡺࠠࡤࡱࡰࡱ࡮ࡺࡳ࠯ࠤ᱁"))
                    commits = list(repo.iter_commits(max_count=10))
                    if commits:
                        result[bstack11ll1l_opy_ (u"ࠥࡪ࡮ࡲࡥࡴࡅ࡫ࡥࡳ࡭ࡥࡥࠤ᱂")] = _1111lll111l_opy_(commits[:5])
            else:
                commits = list(repo.iter_commits(max_count=10))
                if commits:
                    result[bstack11ll1l_opy_ (u"ࠦ࡫࡯࡬ࡦࡵࡆ࡬ࡦࡴࡧࡦࡦࠥ᱃")] = _1111lll111l_opy_(commits[:5])
            bstack1111l1lll11_opy_ = set()
            bstack1111ll1lll1_opy_ = []
            for commit in commits:
                logger.debug(bstack11ll1l_opy_ (u"ࠧࡖࡲࡰࡥࡨࡷࡸ࡯࡮ࡨࠢࡦࡳࡲࡳࡩࡵ࠼ࠣࠦ᱄") + str(commit.message) + bstack11ll1l_opy_ (u"ࠨࠢ᱅"))
                bstack111l11l1ll1_opy_ = commit.author.name if commit.author else bstack11ll1l_opy_ (u"ࠢࡖࡰ࡮ࡲࡴࡽ࡮ࠣ᱆")
                bstack1111l1lll11_opy_.add(bstack111l11l1ll1_opy_)
                bstack1111ll1lll1_opy_.append({
                    bstack11ll1l_opy_ (u"ࠣ࡯ࡨࡷࡸࡧࡧࡦࠤ᱇"): commit.message.strip(),
                    bstack11ll1l_opy_ (u"ࠤࡸࡷࡪࡸࠢ᱈"): bstack111l11l1ll1_opy_
                })
            result[bstack11ll1l_opy_ (u"ࠥࡥࡺࡺࡨࡰࡴࡶࠦ᱉")] = list(bstack1111l1lll11_opy_)
            result[bstack11ll1l_opy_ (u"ࠦࡨࡵ࡭࡮࡫ࡷࡑࡪࡹࡳࡢࡩࡨࡷࠧ᱊")] = bstack1111ll1lll1_opy_
            result[bstack11ll1l_opy_ (u"ࠧࡶࡲࡅࡣࡷࡩࠧ᱋")] = bstack111l111111l_opy_.committed_datetime.strftime(bstack11ll1l_opy_ (u"ࠨ࡚ࠥ࠯ࠨࡱ࠲ࠫࡤࠣ᱌"))
            if (not result[bstack11ll1l_opy_ (u"ࠢࡱࡴࡗ࡭ࡹࡲࡥࠣᱍ")] or result[bstack11ll1l_opy_ (u"ࠣࡲࡵࡘ࡮ࡺ࡬ࡦࠤᱎ")].strip() == bstack11ll1l_opy_ (u"ࠤࠥᱏ")) and bstack111l111111l_opy_.message:
                bstack1111l111ll1_opy_ = bstack111l111111l_opy_.message.strip().splitlines()
                result[bstack11ll1l_opy_ (u"ࠥࡴࡷ࡚ࡩࡵ࡮ࡨࠦ᱐")] = bstack1111l111ll1_opy_[0] if bstack1111l111ll1_opy_ else bstack11ll1l_opy_ (u"ࠦࠧ᱑")
                if len(bstack1111l111ll1_opy_) > 2:
                    result[bstack11ll1l_opy_ (u"ࠧࡶࡲࡅࡧࡶࡧࡷ࡯ࡰࡵ࡫ࡲࡲࠧ᱒")] = bstack11ll1l_opy_ (u"࠭࡜࡯ࠩ᱓").join(bstack1111l111ll1_opy_[2:]).strip()
            results.append(result)
        except Exception as err:
            logger.error(bstack11ll1l_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡰࡰࡲࡸࡰࡦࡺࡩ࡯ࡩࠣࡋ࡮ࡺࠠ࡮ࡧࡷࡥࡩࡧࡴࡢࠢࡩࡳࡷࠦࡁࡊࠢࡶࡩࡱ࡫ࡣࡵ࡫ࡲࡲࠥ࠮ࡦࡰ࡮ࡧࡩࡷࡀࠠࡼࡿࠬ࠾ࠥࢁࡽࠡ࠯ࠣࡿࢂࠨ᱔").format(
                folder,
                type(err).__name__,
                str(err)
            ))
    filtered_results = [
        result
        for result in results
        if _1111l1lllll_opy_(result)
    ]
    return filtered_results
def _1111l1lllll_opy_(result):
    bstack11ll1l_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࡊࡨࡰࡵ࡫ࡲࠡࡶࡲࠤࡨ࡮ࡥࡤ࡭ࠣ࡭࡫ࠦࡡࠡࡩ࡬ࡸࠥࡳࡥࡵࡣࡧࡥࡹࡧࠠࡳࡧࡶࡹࡱࡺࠠࡪࡵࠣࡺࡦࡲࡩࡥࠢࠫࡲࡴࡴ࠭ࡦ࡯ࡳࡸࡾࠦࡦࡪ࡮ࡨࡷࡈ࡮ࡡ࡯ࡩࡨࡨࠥࡧ࡮ࡥࠢࡤࡹࡹ࡮࡯ࡳࡵࠬ࠲ࠏࠦࠠࠡࠢࠥࠦࠧ᱕")
    return (
        isinstance(result.get(bstack11ll1l_opy_ (u"ࠤࡩ࡭ࡱ࡫ࡳࡄࡪࡤࡲ࡬࡫ࡤࠣ᱖"), None), list)
        and len(result[bstack11ll1l_opy_ (u"ࠥࡪ࡮ࡲࡥࡴࡅ࡫ࡥࡳ࡭ࡥࡥࠤ᱗")]) > 0
        and isinstance(result.get(bstack11ll1l_opy_ (u"ࠦࡦࡻࡴࡩࡱࡵࡷࠧ᱘"), None), list)
        and len(result[bstack11ll1l_opy_ (u"ࠧࡧࡵࡵࡪࡲࡶࡸࠨ᱙")]) > 0
    )
def _1111l1l11ll_opy_(repo):
    bstack11ll1l_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࡔࡳࡻࠣࡸࡴࠦࡤࡦࡶࡨࡶࡲ࡯࡮ࡦࠢࡷ࡬ࡪࠦࡢࡢࡵࡨࠤࡧࡸࡡ࡯ࡥ࡫ࠤ࡫ࡵࡲࠡࡶ࡫ࡩࠥ࡭ࡩࡷࡧࡱࠤࡷ࡫ࡰࡰࠢࡺ࡭ࡹ࡮࡯ࡶࡶࠣ࡬ࡦࡸࡤࡤࡱࡧࡩࡩࠦ࡮ࡢ࡯ࡨࡷࠥࡧ࡮ࡥࠢࡺࡳࡷࡱࠠࡸ࡫ࡷ࡬ࠥࡧ࡬࡭࡙ࠢࡇࡘࠦࡰࡳࡱࡹ࡭ࡩ࡫ࡲࡴ࠰ࠍࠤࠥࠦࠠࡓࡧࡷࡹࡷࡴࡳࠡࡶ࡫ࡩࠥࡪࡥࡧࡣࡸࡰࡹࠦࡢࡳࡣࡱࡧ࡭ࠦࡩࡧࠢࡳࡳࡸࡹࡩࡣ࡮ࡨ࠰ࠥ࡫࡬ࡴࡧࠣࡒࡴࡴࡥ࠯ࠌࠣࠤࠥࠦࠢࠣࠤᱚ")
    try:
        try:
            origin = repo.remotes.origin
            bstack1111l1l1l11_opy_ = origin.refs[bstack11ll1l_opy_ (u"ࠧࡉࡇࡄࡈࠬᱛ")]
            target = bstack1111l1l1l11_opy_.reference.name
            if target.startswith(bstack11ll1l_opy_ (u"ࠨࡱࡵ࡭࡬࡯࡮࠰ࠩᱜ")):
                return target
        except Exception:
            pass
        if repo.remotes and repo.remotes.origin.refs:
            for ref in repo.remotes.origin.refs:
                if ref.name.startswith(bstack11ll1l_opy_ (u"ࠩࡲࡶ࡮࡭ࡩ࡯࠱ࠪᱝ")):
                    return ref.name
        if repo.heads:
            return repo.heads[0].name
    except Exception:
        pass
    return None
def _1111lll111l_opy_(commits):
    bstack11ll1l_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࡋࡪࡺࠠ࡭࡫ࡶࡸࠥࡵࡦࠡࡥ࡫ࡥࡳ࡭ࡥࡥࠢࡩ࡭ࡱ࡫ࡳࠡࡨࡵࡳࡲࠦࡡࠡ࡮࡬ࡷࡹࠦ࡯ࡧࠢࡦࡳࡲࡳࡩࡵࡵ࠱ࠎࠥࠦࠠࠡࠤࠥࠦᱞ")
    bstack111l1l1l111_opy_ = set()
    try:
        for commit in commits:
            if commit.parents:
                for parent in commit.parents:
                    diff = commit.diff(parent)
                    for bstack111l1ll11ll_opy_ in diff:
                        if bstack111l1ll11ll_opy_.a_path:
                            bstack111l1l1l111_opy_.add(bstack111l1ll11ll_opy_.a_path)
                        if bstack111l1ll11ll_opy_.b_path:
                            bstack111l1l1l111_opy_.add(bstack111l1ll11ll_opy_.b_path)
    except Exception:
        pass
    return list(bstack111l1l1l111_opy_)
def bstack1111l1l1ll1_opy_(bstack111l1111l11_opy_):
    bstack1111ll11ll1_opy_ = bstack1111l11ll11_opy_(bstack111l1111l11_opy_)
    if bstack1111ll11ll1_opy_ and bstack1111ll11ll1_opy_ > bstack11l1l11111l_opy_:
        bstack111l11111l1_opy_ = bstack1111ll11ll1_opy_ - bstack11l1l11111l_opy_
        bstack111l11ll11l_opy_ = bstack1111l11ll1l_opy_(bstack111l1111l11_opy_[bstack11ll1l_opy_ (u"ࠦࡨࡵ࡭࡮࡫ࡷࡣࡲ࡫ࡳࡴࡣࡪࡩࠧᱟ")], bstack111l11111l1_opy_)
        bstack111l1111l11_opy_[bstack11ll1l_opy_ (u"ࠧࡩ࡯࡮࡯࡬ࡸࡤࡳࡥࡴࡵࡤ࡫ࡪࠨᱠ")] = bstack111l11ll11l_opy_
        logger.info(bstack11ll1l_opy_ (u"ࠨࡔࡩࡧࠣࡧࡴࡳ࡭ࡪࡶࠣ࡬ࡦࡹࠠࡣࡧࡨࡲࠥࡺࡲࡶࡰࡦࡥࡹ࡫ࡤ࠯ࠢࡖ࡭ࡿ࡫ࠠࡰࡨࠣࡧࡴࡳ࡭ࡪࡶࠣࡥ࡫ࡺࡥࡳࠢࡷࡶࡺࡴࡣࡢࡶ࡬ࡳࡳࠦࡩࡴࠢࡾࢁࠥࡑࡂࠣᱡ")
                    .format(bstack1111l11ll11_opy_(bstack111l1111l11_opy_) / 1024))
    return bstack111l1111l11_opy_
def bstack1111l11ll11_opy_(json_data):
    try:
        if json_data:
            bstack111l1l1llll_opy_ = json.dumps(json_data)
            bstack111l111l11l_opy_ = sys.getsizeof(bstack111l1l1llll_opy_)
            return bstack111l111l11l_opy_
    except Exception as e:
        logger.debug(bstack11ll1l_opy_ (u"ࠢࡔࡱࡰࡩࡹ࡮ࡩ࡯ࡩࠣࡻࡪࡴࡴࠡࡹࡵࡳࡳ࡭ࠠࡸࡪ࡬ࡰࡪࠦࡣࡢ࡮ࡦࡹࡱࡧࡴࡪࡰࡪࠤࡸ࡯ࡺࡦࠢࡲࡪࠥࡐࡓࡐࡐࠣࡳࡧࡰࡥࡤࡶ࠽ࠤࢀࢃࠢᱢ").format(e))
    return -1
def bstack1111l11ll1l_opy_(field, bstack111l11l11l1_opy_):
    try:
        bstack111l1l1l1l1_opy_ = len(bytes(bstack11l1l11llll_opy_, bstack11ll1l_opy_ (u"ࠨࡷࡷࡪ࠲࠾ࠧᱣ")))
        bstack111l1l1l1ll_opy_ = bytes(field, bstack11ll1l_opy_ (u"ࠩࡸࡸ࡫࠳࠸ࠨᱤ"))
        bstack1111ll1ll1l_opy_ = len(bstack111l1l1l1ll_opy_)
        bstack1111ll1l111_opy_ = ceil(bstack1111ll1ll1l_opy_ - bstack111l11l11l1_opy_ - bstack111l1l1l1l1_opy_)
        if bstack1111ll1l111_opy_ > 0:
            bstack1111lllllll_opy_ = bstack111l1l1l1ll_opy_[:bstack1111ll1l111_opy_].decode(bstack11ll1l_opy_ (u"ࠪࡹࡹ࡬࠭࠹ࠩᱥ"), errors=bstack11ll1l_opy_ (u"ࠫ࡮࡭࡮ࡰࡴࡨࠫᱦ")) + bstack11l1l11llll_opy_
            return bstack1111lllllll_opy_
    except Exception as e:
        logger.debug(bstack11ll1l_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡩ࡭ࡧࠣࡸࡷࡻ࡮ࡤࡣࡷ࡭ࡳ࡭ࠠࡧ࡫ࡨࡰࡩ࠲ࠠ࡯ࡱࡷ࡬࡮ࡴࡧࠡࡹࡤࡷࠥࡺࡲࡶࡰࡦࡥࡹ࡫ࡤࠡࡪࡨࡶࡪࡀࠠࡼࡿࠥᱧ").format(e))
    return field
def bstack1l1ll1l1ll_opy_():
    env = os.environ
    if (bstack11ll1l_opy_ (u"ࠨࡊࡆࡐࡎࡍࡓ࡙࡟ࡖࡔࡏࠦᱨ") in env and len(env[bstack11ll1l_opy_ (u"ࠢࡋࡇࡑࡏࡎࡔࡓࡠࡗࡕࡐࠧᱩ")]) > 0) or (
            bstack11ll1l_opy_ (u"ࠣࡌࡈࡒࡐࡏࡎࡔࡡࡋࡓࡒࡋࠢᱪ") in env and len(env[bstack11ll1l_opy_ (u"ࠤࡍࡉࡓࡑࡉࡏࡕࡢࡌࡔࡓࡅࠣᱫ")]) > 0):
        return {
            bstack11ll1l_opy_ (u"ࠥࡲࡦࡳࡥࠣᱬ"): bstack11ll1l_opy_ (u"ࠦࡏ࡫࡮࡬࡫ࡱࡷࠧᱭ"),
            bstack11ll1l_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣᱮ"): env.get(bstack11ll1l_opy_ (u"ࠨࡂࡖࡋࡏࡈࡤ࡛ࡒࡍࠤᱯ")),
            bstack11ll1l_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᱰ"): env.get(bstack11ll1l_opy_ (u"ࠣࡌࡒࡆࡤࡔࡁࡎࡇࠥᱱ")),
            bstack11ll1l_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᱲ"): env.get(bstack11ll1l_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࡈࡅࡓࠤᱳ"))
        }
    if env.get(bstack11ll1l_opy_ (u"ࠦࡈࡏࠢᱴ")) == bstack11ll1l_opy_ (u"ࠧࡺࡲࡶࡧࠥᱵ") and bstack1ll11lll11_opy_(env.get(bstack11ll1l_opy_ (u"ࠨࡃࡊࡔࡆࡐࡊࡉࡉࠣᱶ"))):
        return {
            bstack11ll1l_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᱷ"): bstack11ll1l_opy_ (u"ࠣࡅ࡬ࡶࡨࡲࡥࡄࡋࠥᱸ"),
            bstack11ll1l_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᱹ"): env.get(bstack11ll1l_opy_ (u"ࠥࡇࡎࡘࡃࡍࡇࡢࡆ࡚ࡏࡌࡅࡡࡘࡖࡑࠨᱺ")),
            bstack11ll1l_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᱻ"): env.get(bstack11ll1l_opy_ (u"ࠧࡉࡉࡓࡅࡏࡉࡤࡐࡏࡃࠤᱼ")),
            bstack11ll1l_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᱽ"): env.get(bstack11ll1l_opy_ (u"ࠢࡄࡋࡕࡇࡑࡋ࡟ࡃࡗࡌࡐࡉࡥࡎࡖࡏࠥ᱾"))
        }
    if env.get(bstack11ll1l_opy_ (u"ࠣࡅࡌࠦ᱿")) == bstack11ll1l_opy_ (u"ࠤࡷࡶࡺ࡫ࠢᲀ") and bstack1ll11lll11_opy_(env.get(bstack11ll1l_opy_ (u"ࠥࡘࡗࡇࡖࡊࡕࠥᲁ"))):
        return {
            bstack11ll1l_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᲂ"): bstack11ll1l_opy_ (u"࡚ࠧࡲࡢࡸ࡬ࡷࠥࡉࡉࠣᲃ"),
            bstack11ll1l_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᲄ"): env.get(bstack11ll1l_opy_ (u"ࠢࡕࡔࡄ࡚ࡎ࡙࡟ࡃࡗࡌࡐࡉࡥࡗࡆࡄࡢ࡙ࡗࡒࠢᲅ")),
            bstack11ll1l_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᲆ"): env.get(bstack11ll1l_opy_ (u"ࠤࡗࡖࡆ࡜ࡉࡔࡡࡍࡓࡇࡥࡎࡂࡏࡈࠦᲇ")),
            bstack11ll1l_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤᲈ"): env.get(bstack11ll1l_opy_ (u"࡙ࠦࡘࡁࡗࡋࡖࡣࡇ࡛ࡉࡍࡆࡢࡒ࡚ࡓࡂࡆࡔࠥᲉ"))
        }
    if env.get(bstack11ll1l_opy_ (u"ࠧࡉࡉࠣᲊ")) == bstack11ll1l_opy_ (u"ࠨࡴࡳࡷࡨࠦ᲋") and env.get(bstack11ll1l_opy_ (u"ࠢࡄࡋࡢࡒࡆࡓࡅࠣ᲌")) == bstack11ll1l_opy_ (u"ࠣࡥࡲࡨࡪࡹࡨࡪࡲࠥ᲍"):
        return {
            bstack11ll1l_opy_ (u"ࠤࡱࡥࡲ࡫ࠢ᲎"): bstack11ll1l_opy_ (u"ࠥࡇࡴࡪࡥࡴࡪ࡬ࡴࠧ᲏"),
            bstack11ll1l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᲐ"): None,
            bstack11ll1l_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᲑ"): None,
            bstack11ll1l_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᲒ"): None
        }
    if env.get(bstack11ll1l_opy_ (u"ࠢࡃࡋࡗࡆ࡚ࡉࡋࡆࡖࡢࡆࡗࡇࡎࡄࡊࠥᲓ")) and env.get(bstack11ll1l_opy_ (u"ࠣࡄࡌࡘࡇ࡛ࡃࡌࡇࡗࡣࡈࡕࡍࡎࡋࡗࠦᲔ")):
        return {
            bstack11ll1l_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᲕ"): bstack11ll1l_opy_ (u"ࠥࡆ࡮ࡺࡢࡶࡥ࡮ࡩࡹࠨᲖ"),
            bstack11ll1l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᲗ"): env.get(bstack11ll1l_opy_ (u"ࠧࡈࡉࡕࡄࡘࡇࡐࡋࡔࡠࡉࡌࡘࡤࡎࡔࡕࡒࡢࡓࡗࡏࡇࡊࡐࠥᲘ")),
            bstack11ll1l_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᲙ"): None,
            bstack11ll1l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᲚ"): env.get(bstack11ll1l_opy_ (u"ࠣࡄࡌࡘࡇ࡛ࡃࡌࡇࡗࡣࡇ࡛ࡉࡍࡆࡢࡒ࡚ࡓࡂࡆࡔࠥᲛ"))
        }
    if env.get(bstack11ll1l_opy_ (u"ࠤࡆࡍࠧᲜ")) == bstack11ll1l_opy_ (u"ࠥࡸࡷࡻࡥࠣᲝ") and bstack1ll11lll11_opy_(env.get(bstack11ll1l_opy_ (u"ࠦࡉࡘࡏࡏࡇࠥᲞ"))):
        return {
            bstack11ll1l_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᲟ"): bstack11ll1l_opy_ (u"ࠨࡄࡳࡱࡱࡩࠧᲠ"),
            bstack11ll1l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᲡ"): env.get(bstack11ll1l_opy_ (u"ࠣࡆࡕࡓࡓࡋ࡟ࡃࡗࡌࡐࡉࡥࡌࡊࡐࡎࠦᲢ")),
            bstack11ll1l_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᲣ"): None,
            bstack11ll1l_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤᲤ"): env.get(bstack11ll1l_opy_ (u"ࠦࡉࡘࡏࡏࡇࡢࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࡈࡅࡓࠤᲥ"))
        }
    if env.get(bstack11ll1l_opy_ (u"ࠧࡉࡉࠣᲦ")) == bstack11ll1l_opy_ (u"ࠨࡴࡳࡷࡨࠦᲧ") and bstack1ll11lll11_opy_(env.get(bstack11ll1l_opy_ (u"ࠢࡔࡇࡐࡅࡕࡎࡏࡓࡇࠥᲨ"))):
        return {
            bstack11ll1l_opy_ (u"ࠣࡰࡤࡱࡪࠨᲩ"): bstack11ll1l_opy_ (u"ࠤࡖࡩࡲࡧࡰࡩࡱࡵࡩࠧᲪ"),
            bstack11ll1l_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᲫ"): env.get(bstack11ll1l_opy_ (u"ࠦࡘࡋࡍࡂࡒࡋࡓࡗࡋ࡟ࡐࡔࡊࡅࡓࡏ࡚ࡂࡖࡌࡓࡓࡥࡕࡓࡎࠥᲬ")),
            bstack11ll1l_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᲭ"): env.get(bstack11ll1l_opy_ (u"ࠨࡓࡆࡏࡄࡔࡍࡕࡒࡆࡡࡍࡓࡇࡥࡎࡂࡏࡈࠦᲮ")),
            bstack11ll1l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᲯ"): env.get(bstack11ll1l_opy_ (u"ࠣࡕࡈࡑࡆࡖࡈࡐࡔࡈࡣࡏࡕࡂࡠࡋࡇࠦᲰ"))
        }
    if env.get(bstack11ll1l_opy_ (u"ࠤࡆࡍࠧᲱ")) == bstack11ll1l_opy_ (u"ࠥࡸࡷࡻࡥࠣᲲ") and bstack1ll11lll11_opy_(env.get(bstack11ll1l_opy_ (u"ࠦࡌࡏࡔࡍࡃࡅࡣࡈࡏࠢᲳ"))):
        return {
            bstack11ll1l_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᲴ"): bstack11ll1l_opy_ (u"ࠨࡇࡪࡶࡏࡥࡧࠨᲵ"),
            bstack11ll1l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᲶ"): env.get(bstack11ll1l_opy_ (u"ࠣࡅࡌࡣࡏࡕࡂࡠࡗࡕࡐࠧᲷ")),
            bstack11ll1l_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᲸ"): env.get(bstack11ll1l_opy_ (u"ࠥࡇࡎࡥࡊࡐࡄࡢࡒࡆࡓࡅࠣᲹ")),
            bstack11ll1l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᲺ"): env.get(bstack11ll1l_opy_ (u"ࠧࡉࡉࡠࡌࡒࡆࡤࡏࡄࠣ᲻"))
        }
    if env.get(bstack11ll1l_opy_ (u"ࠨࡃࡊࠤ᲼")) == bstack11ll1l_opy_ (u"ࠢࡵࡴࡸࡩࠧᲽ") and bstack1ll11lll11_opy_(env.get(bstack11ll1l_opy_ (u"ࠣࡄࡘࡍࡑࡊࡋࡊࡖࡈࠦᲾ"))):
        return {
            bstack11ll1l_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᲿ"): bstack11ll1l_opy_ (u"ࠥࡆࡺ࡯࡬ࡥ࡭࡬ࡸࡪࠨ᳀"),
            bstack11ll1l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢ᳁"): env.get(bstack11ll1l_opy_ (u"ࠧࡈࡕࡊࡎࡇࡏࡎ࡚ࡅࡠࡄࡘࡍࡑࡊ࡟ࡖࡔࡏࠦ᳂")),
            bstack11ll1l_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣ᳃"): env.get(bstack11ll1l_opy_ (u"ࠢࡃࡗࡌࡐࡉࡑࡉࡕࡇࡢࡐࡆࡈࡅࡍࠤ᳄")) or env.get(bstack11ll1l_opy_ (u"ࠣࡄࡘࡍࡑࡊࡋࡊࡖࡈࡣࡕࡏࡐࡆࡎࡌࡒࡊࡥࡎࡂࡏࡈࠦ᳅")),
            bstack11ll1l_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣ᳆"): env.get(bstack11ll1l_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡍࡌࡘࡊࡥࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࠧ᳇"))
        }
    if bstack1ll11lll11_opy_(env.get(bstack11ll1l_opy_ (u"࡙ࠦࡌ࡟ࡃࡗࡌࡐࡉࠨ᳈"))):
        return {
            bstack11ll1l_opy_ (u"ࠧࡴࡡ࡮ࡧࠥ᳉"): bstack11ll1l_opy_ (u"ࠨࡖࡪࡵࡸࡥࡱࠦࡓࡵࡷࡧ࡭ࡴࠦࡔࡦࡣࡰࠤࡘ࡫ࡲࡷ࡫ࡦࡩࡸࠨ᳊"),
            bstack11ll1l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥ᳋"): bstack11ll1l_opy_ (u"ࠣࡽࢀࡿࢂࠨ᳌").format(env.get(bstack11ll1l_opy_ (u"ࠩࡖ࡝ࡘ࡚ࡅࡎࡡࡗࡉࡆࡓࡆࡐࡗࡑࡈࡆ࡚ࡉࡐࡐࡖࡉࡗ࡜ࡅࡓࡗࡕࡍࠬ᳍")), env.get(bstack11ll1l_opy_ (u"ࠪࡗ࡞࡙ࡔࡆࡏࡢࡘࡊࡇࡍࡑࡔࡒࡎࡊࡉࡔࡊࡆࠪ᳎"))),
            bstack11ll1l_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨ᳏"): env.get(bstack11ll1l_opy_ (u"࡙࡙ࠧࡔࡖࡈࡑࡤࡊࡅࡇࡋࡑࡍ࡙ࡏࡏࡏࡋࡇࠦ᳐")),
            bstack11ll1l_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧ᳑"): env.get(bstack11ll1l_opy_ (u"ࠢࡃࡗࡌࡐࡉࡥࡂࡖࡋࡏࡈࡎࡊࠢ᳒"))
        }
    if bstack1ll11lll11_opy_(env.get(bstack11ll1l_opy_ (u"ࠣࡃࡓࡔ࡛ࡋ࡙ࡐࡔࠥ᳓"))):
        return {
            bstack11ll1l_opy_ (u"ࠤࡱࡥࡲ࡫᳔ࠢ"): bstack11ll1l_opy_ (u"ࠥࡅࡵࡶࡶࡦࡻࡲࡶ᳕ࠧ"),
            bstack11ll1l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲ᳖ࠢ"): bstack11ll1l_opy_ (u"ࠧࢁࡽ࠰ࡲࡵࡳ࡯࡫ࡣࡵ࠱ࡾࢁ࠴ࢁࡽ࠰ࡤࡸ࡭ࡱࡪࡳ࠰ࡽࢀ᳗ࠦ").format(env.get(bstack11ll1l_opy_ (u"࠭ࡁࡑࡒ࡙ࡉ࡞ࡕࡒࡠࡗࡕࡐ᳘ࠬ")), env.get(bstack11ll1l_opy_ (u"ࠧࡂࡒࡓ࡚ࡊ࡟ࡏࡓࡡࡄࡇࡈࡕࡕࡏࡖࡢࡒࡆࡓࡅࠨ᳙")), env.get(bstack11ll1l_opy_ (u"ࠨࡃࡓࡔ࡛ࡋ࡙ࡐࡔࡢࡔࡗࡕࡊࡆࡅࡗࡣࡘࡒࡕࡈࠩ᳚")), env.get(bstack11ll1l_opy_ (u"ࠩࡄࡔࡕ࡜ࡅ࡚ࡑࡕࡣࡇ࡛ࡉࡍࡆࡢࡍࡉ࠭᳛"))),
            bstack11ll1l_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩ᳜ࠧ"): env.get(bstack11ll1l_opy_ (u"ࠦࡆࡖࡐࡗࡇ࡜ࡓࡗࡥࡊࡐࡄࡢࡒࡆࡓࡅ᳝ࠣ")),
            bstack11ll1l_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵ᳞ࠦ"): env.get(bstack11ll1l_opy_ (u"ࠨࡁࡑࡒ࡙ࡉ࡞ࡕࡒࡠࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘ᳟ࠢ"))
        }
    if env.get(bstack11ll1l_opy_ (u"ࠢࡂ࡜ࡘࡖࡊࡥࡈࡕࡖࡓࡣ࡚࡙ࡅࡓࡡࡄࡋࡊࡔࡔࠣ᳠")) and env.get(bstack11ll1l_opy_ (u"ࠣࡖࡉࡣࡇ࡛ࡉࡍࡆࠥ᳡")):
        return {
            bstack11ll1l_opy_ (u"ࠤࡱࡥࡲ࡫᳢ࠢ"): bstack11ll1l_opy_ (u"ࠥࡅࡿࡻࡲࡦࠢࡆࡍ᳣ࠧ"),
            bstack11ll1l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲ᳤ࠢ"): bstack11ll1l_opy_ (u"ࠧࢁࡽࡼࡿ࠲ࡣࡧࡻࡩ࡭ࡦ࠲ࡶࡪࡹࡵ࡭ࡶࡶࡃࡧࡻࡩ࡭ࡦࡌࡨࡂࢁࡽ᳥ࠣ").format(env.get(bstack11ll1l_opy_ (u"࠭ࡓ࡚ࡕࡗࡉࡒࡥࡔࡆࡃࡐࡊࡔ࡛ࡎࡅࡃࡗࡍࡔࡔࡓࡆࡔ࡙ࡉࡗ࡛ࡒࡊ᳦ࠩ")), env.get(bstack11ll1l_opy_ (u"ࠧࡔ࡛ࡖࡘࡊࡓ࡟ࡕࡇࡄࡑࡕࡘࡏࡋࡇࡆࡘ᳧ࠬ")), env.get(bstack11ll1l_opy_ (u"ࠨࡄࡘࡍࡑࡊ࡟ࡃࡗࡌࡐࡉࡏࡄࠨ᳨"))),
            bstack11ll1l_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᳩ"): env.get(bstack11ll1l_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡡࡅ࡙ࡎࡒࡄࡊࡆࠥᳪ")),
            bstack11ll1l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᳫ"): env.get(bstack11ll1l_opy_ (u"ࠧࡈࡕࡊࡎࡇࡣࡇ࡛ࡉࡍࡆࡌࡈࠧᳬ"))
        }
    if any([env.get(bstack11ll1l_opy_ (u"ࠨࡃࡐࡆࡈࡆ࡚ࡏࡌࡅࡡࡅ࡙ࡎࡒࡄࡠࡋࡇ᳭ࠦ")), env.get(bstack11ll1l_opy_ (u"ࠢࡄࡑࡇࡉࡇ࡛ࡉࡍࡆࡢࡖࡊ࡙ࡏࡍࡘࡈࡈࡤ࡙ࡏࡖࡔࡆࡉࡤ࡜ࡅࡓࡕࡌࡓࡓࠨᳮ")), env.get(bstack11ll1l_opy_ (u"ࠣࡅࡒࡈࡊࡈࡕࡊࡎࡇࡣࡘࡕࡕࡓࡅࡈࡣ࡛ࡋࡒࡔࡋࡒࡒࠧᳯ"))]):
        return {
            bstack11ll1l_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᳰ"): bstack11ll1l_opy_ (u"ࠥࡅ࡜࡙ࠠࡄࡱࡧࡩࡇࡻࡩ࡭ࡦࠥᳱ"),
            bstack11ll1l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᳲ"): env.get(bstack11ll1l_opy_ (u"ࠧࡉࡏࡅࡇࡅ࡙ࡎࡒࡄࡠࡒࡘࡆࡑࡏࡃࡠࡄࡘࡍࡑࡊ࡟ࡖࡔࡏࠦᳳ")),
            bstack11ll1l_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣ᳴"): env.get(bstack11ll1l_opy_ (u"ࠢࡄࡑࡇࡉࡇ࡛ࡉࡍࡆࡢࡆ࡚ࡏࡌࡅࡡࡌࡈࠧᳵ")),
            bstack11ll1l_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᳶ"): env.get(bstack11ll1l_opy_ (u"ࠤࡆࡓࡉࡋࡂࡖࡋࡏࡈࡤࡈࡕࡊࡎࡇࡣࡎࡊࠢ᳷"))
        }
    if env.get(bstack11ll1l_opy_ (u"ࠥࡦࡦࡳࡢࡰࡱࡢࡦࡺ࡯࡬ࡥࡐࡸࡱࡧ࡫ࡲࠣ᳸")):
        return {
            bstack11ll1l_opy_ (u"ࠦࡳࡧ࡭ࡦࠤ᳹"): bstack11ll1l_opy_ (u"ࠧࡈࡡ࡮ࡤࡲࡳࠧᳺ"),
            bstack11ll1l_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤ᳻"): env.get(bstack11ll1l_opy_ (u"ࠢࡣࡣࡰࡦࡴࡵ࡟ࡣࡷ࡬ࡰࡩࡘࡥࡴࡷ࡯ࡸࡸ࡛ࡲ࡭ࠤ᳼")),
            bstack11ll1l_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥ᳽"): env.get(bstack11ll1l_opy_ (u"ࠤࡥࡥࡲࡨ࡯ࡰࡡࡶ࡬ࡴࡸࡴࡋࡱࡥࡒࡦࡳࡥࠣ᳾")),
            bstack11ll1l_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤ᳿"): env.get(bstack11ll1l_opy_ (u"ࠦࡧࡧ࡭ࡣࡱࡲࡣࡧࡻࡩ࡭ࡦࡑࡹࡲࡨࡥࡳࠤᴀ"))
        }
    if env.get(bstack11ll1l_opy_ (u"ࠧ࡝ࡅࡓࡅࡎࡉࡗࠨᴁ")) or env.get(bstack11ll1l_opy_ (u"ࠨࡗࡆࡔࡆࡏࡊࡘ࡟ࡎࡃࡌࡒࡤࡖࡉࡑࡇࡏࡍࡓࡋ࡟ࡔࡖࡄࡖ࡙ࡋࡄࠣᴂ")):
        return {
            bstack11ll1l_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᴃ"): bstack11ll1l_opy_ (u"࡙ࠣࡨࡶࡨࡱࡥࡳࠤᴄ"),
            bstack11ll1l_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᴅ"): env.get(bstack11ll1l_opy_ (u"࡛ࠥࡊࡘࡃࡌࡇࡕࡣࡇ࡛ࡉࡍࡆࡢ࡙ࡗࡒࠢᴆ")),
            bstack11ll1l_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᴇ"): bstack11ll1l_opy_ (u"ࠧࡓࡡࡪࡰࠣࡔ࡮ࡶࡥ࡭࡫ࡱࡩࠧᴈ") if env.get(bstack11ll1l_opy_ (u"ࠨࡗࡆࡔࡆࡏࡊࡘ࡟ࡎࡃࡌࡒࡤࡖࡉࡑࡇࡏࡍࡓࡋ࡟ࡔࡖࡄࡖ࡙ࡋࡄࠣᴉ")) else None,
            bstack11ll1l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᴊ"): env.get(bstack11ll1l_opy_ (u"࡙ࠣࡈࡖࡈࡑࡅࡓࡡࡊࡍ࡙ࡥࡃࡐࡏࡐࡍ࡙ࠨᴋ"))
        }
    if any([env.get(bstack11ll1l_opy_ (u"ࠤࡊࡇࡕࡥࡐࡓࡑࡍࡉࡈ࡚ࠢᴌ")), env.get(bstack11ll1l_opy_ (u"ࠥࡋࡈࡒࡏࡖࡆࡢࡔࡗࡕࡊࡆࡅࡗࠦᴍ")), env.get(bstack11ll1l_opy_ (u"ࠦࡌࡕࡏࡈࡎࡈࡣࡈࡒࡏࡖࡆࡢࡔࡗࡕࡊࡆࡅࡗࠦᴎ"))]):
        return {
            bstack11ll1l_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᴏ"): bstack11ll1l_opy_ (u"ࠨࡇࡰࡱࡪࡰࡪࠦࡃ࡭ࡱࡸࡨࠧᴐ"),
            bstack11ll1l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᴑ"): None,
            bstack11ll1l_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᴒ"): env.get(bstack11ll1l_opy_ (u"ࠤࡓࡖࡔࡐࡅࡄࡖࡢࡍࡉࠨᴓ")),
            bstack11ll1l_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤᴔ"): env.get(bstack11ll1l_opy_ (u"ࠦࡇ࡛ࡉࡍࡆࡢࡍࡉࠨᴕ"))
        }
    if env.get(bstack11ll1l_opy_ (u"࡙ࠧࡈࡊࡒࡓࡅࡇࡒࡅࠣᴖ")):
        return {
            bstack11ll1l_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᴗ"): bstack11ll1l_opy_ (u"ࠢࡔࡪ࡬ࡴࡵࡧࡢ࡭ࡧࠥᴘ"),
            bstack11ll1l_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᴙ"): env.get(bstack11ll1l_opy_ (u"ࠤࡖࡌࡎࡖࡐࡂࡄࡏࡉࡤࡈࡕࡊࡎࡇࡣ࡚ࡘࡌࠣᴚ")),
            bstack11ll1l_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᴛ"): bstack11ll1l_opy_ (u"ࠦࡏࡵࡢࠡࠥࡾࢁࠧᴜ").format(env.get(bstack11ll1l_opy_ (u"࡙ࠬࡈࡊࡒࡓࡅࡇࡒࡅࡠࡌࡒࡆࡤࡏࡄࠨᴝ"))) if env.get(bstack11ll1l_opy_ (u"ࠨࡓࡉࡋࡓࡔࡆࡈࡌࡆࡡࡍࡓࡇࡥࡉࡅࠤᴞ")) else None,
            bstack11ll1l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᴟ"): env.get(bstack11ll1l_opy_ (u"ࠣࡕࡋࡍࡕࡖࡁࡃࡎࡈࡣࡇ࡛ࡉࡍࡆࡢࡒ࡚ࡓࡂࡆࡔࠥᴠ"))
        }
    if bstack1ll11lll11_opy_(env.get(bstack11ll1l_opy_ (u"ࠤࡑࡉ࡙ࡒࡉࡇ࡛ࠥᴡ"))):
        return {
            bstack11ll1l_opy_ (u"ࠥࡲࡦࡳࡥࠣᴢ"): bstack11ll1l_opy_ (u"ࠦࡓ࡫ࡴ࡭࡫ࡩࡽࠧᴣ"),
            bstack11ll1l_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣᴤ"): env.get(bstack11ll1l_opy_ (u"ࠨࡄࡆࡒࡏࡓ࡞ࡥࡕࡓࡎࠥᴥ")),
            bstack11ll1l_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᴦ"): env.get(bstack11ll1l_opy_ (u"ࠣࡕࡌࡘࡊࡥࡎࡂࡏࡈࠦᴧ")),
            bstack11ll1l_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᴨ"): env.get(bstack11ll1l_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡡࡌࡈࠧᴩ"))
        }
    if bstack1ll11lll11_opy_(env.get(bstack11ll1l_opy_ (u"ࠦࡌࡏࡔࡉࡗࡅࡣࡆࡉࡔࡊࡑࡑࡗࠧᴪ"))):
        return {
            bstack11ll1l_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᴫ"): bstack11ll1l_opy_ (u"ࠨࡇࡪࡶࡋࡹࡧࠦࡁࡤࡶ࡬ࡳࡳࡹࠢᴬ"),
            bstack11ll1l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᴭ"): bstack11ll1l_opy_ (u"ࠣࡽࢀ࠳ࢀࢃ࠯ࡢࡥࡷ࡭ࡴࡴࡳ࠰ࡴࡸࡲࡸ࠵ࡻࡾࠤᴮ").format(env.get(bstack11ll1l_opy_ (u"ࠩࡊࡍ࡙ࡎࡕࡃࡡࡖࡉࡗ࡜ࡅࡓࡡࡘࡖࡑ࠭ᴯ")), env.get(bstack11ll1l_opy_ (u"ࠪࡋࡎ࡚ࡈࡖࡄࡢࡖࡊࡖࡏࡔࡋࡗࡓࡗ࡟ࠧᴰ")), env.get(bstack11ll1l_opy_ (u"ࠫࡌࡏࡔࡉࡗࡅࡣࡗ࡛ࡎࡠࡋࡇࠫᴱ"))),
            bstack11ll1l_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᴲ"): env.get(bstack11ll1l_opy_ (u"ࠨࡇࡊࡖࡋ࡙ࡇࡥࡗࡐࡔࡎࡊࡑࡕࡗࠣᴳ")),
            bstack11ll1l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᴴ"): env.get(bstack11ll1l_opy_ (u"ࠣࡉࡌࡘࡍ࡛ࡂࡠࡔࡘࡒࡤࡏࡄࠣᴵ"))
        }
    if env.get(bstack11ll1l_opy_ (u"ࠤࡆࡍࠧᴶ")) == bstack11ll1l_opy_ (u"ࠥࡸࡷࡻࡥࠣᴷ") and env.get(bstack11ll1l_opy_ (u"࡛ࠦࡋࡒࡄࡇࡏࠦᴸ")) == bstack11ll1l_opy_ (u"ࠧ࠷ࠢᴹ"):
        return {
            bstack11ll1l_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᴺ"): bstack11ll1l_opy_ (u"ࠢࡗࡧࡵࡧࡪࡲࠢᴻ"),
            bstack11ll1l_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᴼ"): bstack11ll1l_opy_ (u"ࠤ࡫ࡸࡹࡶ࠺࠰࠱ࡾࢁࠧᴽ").format(env.get(bstack11ll1l_opy_ (u"࡚ࠪࡊࡘࡃࡆࡎࡢ࡙ࡗࡒࠧᴾ"))),
            bstack11ll1l_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᴿ"): None,
            bstack11ll1l_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᵀ"): None,
        }
    if env.get(bstack11ll1l_opy_ (u"ࠨࡔࡆࡃࡐࡇࡎ࡚࡙ࡠࡘࡈࡖࡘࡏࡏࡏࠤᵁ")):
        return {
            bstack11ll1l_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᵂ"): bstack11ll1l_opy_ (u"ࠣࡖࡨࡥࡲࡩࡩࡵࡻࠥᵃ"),
            bstack11ll1l_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᵄ"): None,
            bstack11ll1l_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᵅ"): env.get(bstack11ll1l_opy_ (u"࡙ࠦࡋࡁࡎࡅࡌࡘ࡞ࡥࡐࡓࡑࡍࡉࡈ࡚࡟ࡏࡃࡐࡉࠧᵆ")),
            bstack11ll1l_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᵇ"): env.get(bstack11ll1l_opy_ (u"ࠨࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࠧᵈ"))
        }
    if any([env.get(bstack11ll1l_opy_ (u"ࠢࡄࡑࡑࡇࡔ࡛ࡒࡔࡇࠥᵉ")), env.get(bstack11ll1l_opy_ (u"ࠣࡅࡒࡒࡈࡕࡕࡓࡕࡈࡣ࡚ࡘࡌࠣᵊ")), env.get(bstack11ll1l_opy_ (u"ࠤࡆࡓࡓࡉࡏࡖࡔࡖࡉࡤ࡛ࡓࡆࡔࡑࡅࡒࡋࠢᵋ")), env.get(bstack11ll1l_opy_ (u"ࠥࡇࡔࡔࡃࡐࡗࡕࡗࡊࡥࡔࡆࡃࡐࠦᵌ"))]):
        return {
            bstack11ll1l_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᵍ"): bstack11ll1l_opy_ (u"ࠧࡉ࡯࡯ࡥࡲࡹࡷࡹࡥࠣᵎ"),
            bstack11ll1l_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᵏ"): None,
            bstack11ll1l_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᵐ"): env.get(bstack11ll1l_opy_ (u"ࠣࡄࡘࡍࡑࡊ࡟ࡋࡑࡅࡣࡓࡇࡍࡆࠤᵑ")) or None,
            bstack11ll1l_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᵒ"): env.get(bstack11ll1l_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡡࡌࡈࠧᵓ"), 0)
        }
    if env.get(bstack11ll1l_opy_ (u"ࠦࡌࡕ࡟ࡋࡑࡅࡣࡓࡇࡍࡆࠤᵔ")):
        return {
            bstack11ll1l_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᵕ"): bstack11ll1l_opy_ (u"ࠨࡇࡰࡅࡇࠦᵖ"),
            bstack11ll1l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᵗ"): None,
            bstack11ll1l_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᵘ"): env.get(bstack11ll1l_opy_ (u"ࠤࡊࡓࡤࡐࡏࡃࡡࡑࡅࡒࡋࠢᵙ")),
            bstack11ll1l_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤᵚ"): env.get(bstack11ll1l_opy_ (u"ࠦࡌࡕ࡟ࡑࡋࡓࡉࡑࡏࡎࡆࡡࡆࡓ࡚ࡔࡔࡆࡔࠥᵛ"))
        }
    if env.get(bstack11ll1l_opy_ (u"ࠧࡉࡆࡠࡄࡘࡍࡑࡊ࡟ࡊࡆࠥᵜ")):
        return {
            bstack11ll1l_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᵝ"): bstack11ll1l_opy_ (u"ࠢࡄࡱࡧࡩࡋࡸࡥࡴࡪࠥᵞ"),
            bstack11ll1l_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᵟ"): env.get(bstack11ll1l_opy_ (u"ࠤࡆࡊࡤࡈࡕࡊࡎࡇࡣ࡚ࡘࡌࠣᵠ")),
            bstack11ll1l_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᵡ"): env.get(bstack11ll1l_opy_ (u"ࠦࡈࡌ࡟ࡑࡋࡓࡉࡑࡏࡎࡆࡡࡑࡅࡒࡋࠢᵢ")),
            bstack11ll1l_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᵣ"): env.get(bstack11ll1l_opy_ (u"ࠨࡃࡇࡡࡅ࡙ࡎࡒࡄࡠࡋࡇࠦᵤ"))
        }
    return {bstack11ll1l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᵥ"): None}
def get_host_info():
    return {
        bstack11ll1l_opy_ (u"ࠣࡪࡲࡷࡹࡴࡡ࡮ࡧࠥᵦ"): platform.node(),
        bstack11ll1l_opy_ (u"ࠤࡳࡰࡦࡺࡦࡰࡴࡰࠦᵧ"): platform.system(),
        bstack11ll1l_opy_ (u"ࠥࡸࡾࡶࡥࠣᵨ"): platform.machine(),
        bstack11ll1l_opy_ (u"ࠦࡻ࡫ࡲࡴ࡫ࡲࡲࠧᵩ"): platform.version(),
        bstack11ll1l_opy_ (u"ࠧࡧࡲࡤࡪࠥᵪ"): platform.architecture()[0]
    }
def bstack11l11l1l11_opy_():
    try:
        import selenium
        return True
    except ImportError:
        return False
def bstack1111lll1ll1_opy_():
    if bstack111ll1l1_opy_.get_property(bstack11ll1l_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡥࡳࡦࡵࡶ࡭ࡴࡴࠧᵫ")):
        return bstack11ll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ᵬ")
    return bstack11ll1l_opy_ (u"ࠨࡷࡱ࡯ࡳࡵࡷ࡯ࡡࡪࡶ࡮ࡪࠧᵭ")
def bstack111l1ll1ll1_opy_(driver):
    info = {
        bstack11ll1l_opy_ (u"ࠩࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨᵮ"): driver.capabilities,
        bstack11ll1l_opy_ (u"ࠪࡷࡪࡹࡳࡪࡱࡱࡣ࡮ࡪࠧᵯ"): driver.session_id,
        bstack11ll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࠬᵰ"): driver.capabilities.get(bstack11ll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪᵱ"), None),
        bstack11ll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨᵲ"): driver.capabilities.get(bstack11ll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨᵳ"), None),
        bstack11ll1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪᵴ"): driver.capabilities.get(bstack11ll1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡒࡦࡳࡥࠨᵵ"), None),
        bstack11ll1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭ᵶ"):driver.capabilities.get(bstack11ll1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ᵷ"), None),
    }
    if bstack1111lll1ll1_opy_() == bstack11ll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫᵸ"):
        if bstack1l1lll11ll_opy_():
            info[bstack11ll1l_opy_ (u"࠭ࡰࡳࡱࡧࡹࡨࡺࠧᵹ")] = bstack11ll1l_opy_ (u"ࠧࡢࡲࡳ࠱ࡦࡻࡴࡰ࡯ࡤࡸࡪ࠭ᵺ")
        elif driver.capabilities.get(bstack11ll1l_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩᵻ"), {}).get(bstack11ll1l_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡴࡥࡤࡰࡪ࠭ᵼ"), False):
            info[bstack11ll1l_opy_ (u"ࠪࡴࡷࡵࡤࡶࡥࡷࠫᵽ")] = bstack11ll1l_opy_ (u"ࠫࡹࡻࡲࡣࡱࡶࡧࡦࡲࡥࠨᵾ")
        else:
            info[bstack11ll1l_opy_ (u"ࠬࡶࡲࡰࡦࡸࡧࡹ࠭ᵿ")] = bstack11ll1l_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡥࠨᶀ")
    return info
def bstack1l1lll11ll_opy_():
    if bstack111ll1l1_opy_.get_property(bstack11ll1l_opy_ (u"ࠧࡢࡲࡳࡣࡦࡻࡴࡰ࡯ࡤࡸࡪ࠭ᶁ")):
        return True
    if bstack1ll11lll11_opy_(os.environ.get(bstack11ll1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡊࡕࡢࡅࡕࡖ࡟ࡂࡗࡗࡓࡒࡇࡔࡆࠩᶂ"), None)):
        return True
    return False
def bstack1l1llllll_opy_(bstack1111lll11l1_opy_, url, data, config):
    headers = config.get(bstack11ll1l_opy_ (u"ࠩ࡫ࡩࡦࡪࡥࡳࡵࠪᶃ"), None)
    proxies = bstack1ll11ll1l_opy_(config, url)
    auth = config.get(bstack11ll1l_opy_ (u"ࠪࡥࡺࡺࡨࠨᶄ"), None)
    response = requests.request(
            bstack1111lll11l1_opy_,
            url=url,
            headers=headers,
            auth=auth,
            json=data,
            proxies=proxies
        )
    return response
def bstack1l1lllllll_opy_(bstack1l111111l1_opy_, size):
    bstack1l11l11l1l_opy_ = []
    while len(bstack1l111111l1_opy_) > size:
        bstack11ll11l1l1_opy_ = bstack1l111111l1_opy_[:size]
        bstack1l11l11l1l_opy_.append(bstack11ll11l1l1_opy_)
        bstack1l111111l1_opy_ = bstack1l111111l1_opy_[size:]
    bstack1l11l11l1l_opy_.append(bstack1l111111l1_opy_)
    return bstack1l11l11l1l_opy_
def bstack1111ll1l1ll_opy_(message, bstack111l11l1111_opy_=False):
    os.write(1, bytes(message, bstack11ll1l_opy_ (u"ࠫࡺࡺࡦ࠮࠺ࠪᶅ")))
    os.write(1, bytes(bstack11ll1l_opy_ (u"ࠬࡢ࡮ࠨᶆ"), bstack11ll1l_opy_ (u"࠭ࡵࡵࡨ࠰࠼ࠬᶇ")))
    if bstack111l11l1111_opy_:
        with open(bstack11ll1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠭ࡰ࠳࠴ࡽ࠲࠭ᶈ") + os.environ[bstack11ll1l_opy_ (u"ࠨࡄࡖࡣ࡙ࡋࡓࡕࡑࡓࡗࡤࡈࡕࡊࡎࡇࡣࡍࡇࡓࡉࡇࡇࡣࡎࡊࠧᶉ")] + bstack11ll1l_opy_ (u"ࠩ࠱ࡰࡴ࡭ࠧᶊ"), bstack11ll1l_opy_ (u"ࠪࡥࠬᶋ")) as f:
            f.write(message + bstack11ll1l_opy_ (u"ࠫࡡࡴࠧᶌ"))
def bstack1lll11ll1ll_opy_():
    return os.environ[bstack11ll1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡆ࡛ࡔࡐࡏࡄࡘࡎࡕࡎࠨᶍ")].lower() == bstack11ll1l_opy_ (u"࠭ࡴࡳࡷࡨࠫᶎ")
def bstack1l111ll1_opy_():
    return bstack1l1l1ll1_opy_().replace(tzinfo=None).isoformat() + bstack11ll1l_opy_ (u"࡛ࠧࠩᶏ")
def bstack111l1l11111_opy_(start, finish):
    return (datetime.datetime.fromisoformat(finish.rstrip(bstack11ll1l_opy_ (u"ࠨ࡜ࠪᶐ"))) - datetime.datetime.fromisoformat(start.rstrip(bstack11ll1l_opy_ (u"ࠩ࡝ࠫᶑ")))).total_seconds() * 1000
def bstack1111l1ll11l_opy_(timestamp):
    return bstack111l1l111l1_opy_(timestamp).isoformat() + bstack11ll1l_opy_ (u"ࠪ࡞ࠬᶒ")
def bstack1111lll1l1l_opy_(bstack111l1l111ll_opy_):
    date_format = bstack11ll1l_opy_ (u"ࠫࠪ࡟ࠥ࡮ࠧࡧࠤࠪࡎ࠺ࠦࡏ࠽ࠩࡘ࠴ࠥࡧࠩᶓ")
    bstack111l11ll1l1_opy_ = datetime.datetime.strptime(bstack111l1l111ll_opy_, date_format)
    return bstack111l11ll1l1_opy_.isoformat() + bstack11ll1l_opy_ (u"ࠬࡠࠧᶔ")
def bstack111l11l1l11_opy_(outcome):
    _, exception, _ = outcome.excinfo or (None, None, None)
    if exception:
        return bstack11ll1l_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ᶕ")
    else:
        return bstack11ll1l_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧᶖ")
def bstack1ll11lll11_opy_(val):
    if val is None:
        return False
    return val.__str__().lower() == bstack11ll1l_opy_ (u"ࠨࡶࡵࡹࡪ࠭ᶗ")
def bstack1111l1lll1l_opy_(val):
    return val.__str__().lower() == bstack11ll1l_opy_ (u"ࠩࡩࡥࡱࡹࡥࠨᶘ")
def error_handler(bstack111l1l11l11_opy_=Exception, class_method=False, default_value=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except bstack111l1l11l11_opy_ as e:
                print(bstack11ll1l_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡩࡹࡳࡩࡴࡪࡱࡱࠤࢀࢃࠠ࠮ࡀࠣࡿࢂࡀࠠࡼࡿࠥᶙ").format(func.__name__, bstack111l1l11l11_opy_.__name__, str(e)))
                return default_value
        return wrapper
    def bstack111l11l1l1l_opy_(bstack1111ll111ll_opy_):
        def wrapped(cls, *args, **kwargs):
            try:
                return bstack1111ll111ll_opy_(cls, *args, **kwargs)
            except bstack111l1l11l11_opy_ as e:
                print(bstack11ll1l_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡪࡺࡴࡣࡵ࡫ࡲࡲࠥࢁࡽࠡ࠯ࡁࠤࢀࢃ࠺ࠡࡽࢀࠦᶚ").format(bstack1111ll111ll_opy_.__name__, bstack111l1l11l11_opy_.__name__, str(e)))
                return default_value
        return wrapped
    if class_method:
        return bstack111l11l1l1l_opy_
    else:
        return decorator
def bstack11ll1l1l1_opy_(bstack1llll1l1l_opy_):
    if os.getenv(bstack11ll1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡆ࡛ࡔࡐࡏࡄࡘࡎࡕࡎࠨᶛ")) is not None:
        return bstack1ll11lll11_opy_(os.getenv(bstack11ll1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡇࡕࡕࡑࡐࡅ࡙ࡏࡏࡏࠩᶜ")))
    if bstack11ll1l_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫᶝ") in bstack1llll1l1l_opy_ and bstack1111l1lll1l_opy_(bstack1llll1l1l_opy_[bstack11ll1l_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬᶞ")]):
        return False
    if bstack11ll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫᶟ") in bstack1llll1l1l_opy_ and bstack1111l1lll1l_opy_(bstack1llll1l1l_opy_[bstack11ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬᶠ")]):
        return False
    return True
def bstack1111ll1ll_opy_():
    try:
        from pytest_bdd import reporting
        bstack1111l1l1l1l_opy_ = os.environ.get(bstack11ll1l_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢ࡙ࡘࡋࡒࡠࡈࡕࡅࡒࡋࡗࡐࡔࡎࠦᶡ"), None)
        return bstack1111l1l1l1l_opy_ is None or bstack1111l1l1l1l_opy_ == bstack11ll1l_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠤᶢ")
    except Exception as e:
        return False
def bstack1llll1lll1_opy_(hub_url, CONFIG):
    if bstack111llllll_opy_() <= version.parse(bstack11ll1l_opy_ (u"࠭࠳࠯࠳࠶࠲࠵࠭ᶣ")):
        if hub_url:
            return bstack11ll1l_opy_ (u"ࠢࡩࡶࡷࡴ࠿࠵࠯ࠣᶤ") + hub_url + bstack11ll1l_opy_ (u"ࠣ࠼࠻࠴࠴ࡽࡤ࠰ࡪࡸࡦࠧᶥ")
        return bstack11111lll1l_opy_
    if hub_url:
        return bstack11ll1l_opy_ (u"ࠤ࡫ࡸࡹࡶࡳ࠻࠱࠲ࠦᶦ") + hub_url + bstack11ll1l_opy_ (u"ࠥ࠳ࡼࡪ࠯ࡩࡷࡥࠦᶧ")
    return bstack1l1llll1l_opy_
def bstack1111l11l1ll_opy_():
    return isinstance(os.getenv(bstack11ll1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔ࡞࡚ࡅࡔࡖࡢࡔࡑ࡛ࡇࡊࡐࠪᶨ")), str)
def bstack111ll1l1l1_opy_(url):
    return urlparse(url).hostname
def bstack11l1l1l11_opy_(hostname):
    for bstack1l1l11l111_opy_ in bstack111ll1l111_opy_:
        regex = re.compile(bstack1l1l11l111_opy_)
        if regex.match(hostname):
            return True
    return False
def bstack11ll1111111_opy_(bstack1111ll1llll_opy_, file_name, logger):
    bstack11lllll1l1_opy_ = os.path.join(os.path.expanduser(bstack11ll1l_opy_ (u"ࠬࢄࠧᶩ")), bstack1111ll1llll_opy_)
    try:
        if not os.path.exists(bstack11lllll1l1_opy_):
            os.makedirs(bstack11lllll1l1_opy_)
        file_path = os.path.join(os.path.expanduser(bstack11ll1l_opy_ (u"࠭ࡾࠨᶪ")), bstack1111ll1llll_opy_, file_name)
        if not os.path.isfile(file_path):
            with open(file_path, bstack11ll1l_opy_ (u"ࠧࡸࠩᶫ")):
                pass
            with open(file_path, bstack11ll1l_opy_ (u"ࠣࡹ࠮ࠦᶬ")) as outfile:
                json.dump({}, outfile)
        return file_path
    except Exception as e:
        logger.debug(bstack1l11l11l11_opy_.format(str(e)))
def bstack11ll11111l1_opy_(file_name, key, value, logger):
    file_path = bstack11ll1111111_opy_(bstack11ll1l_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩᶭ"), file_name, logger)
    if file_path != None:
        if os.path.exists(file_path):
            bstack1111l1111l_opy_ = json.load(open(file_path, bstack11ll1l_opy_ (u"ࠪࡶࡧ࠭ᶮ")))
        else:
            bstack1111l1111l_opy_ = {}
        bstack1111l1111l_opy_[key] = value
        with open(file_path, bstack11ll1l_opy_ (u"ࠦࡼ࠱ࠢᶯ")) as outfile:
            json.dump(bstack1111l1111l_opy_, outfile)
def bstack1111l1ll1_opy_(file_name, logger):
    file_path = bstack11ll1111111_opy_(bstack11ll1l_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬᶰ"), file_name, logger)
    bstack1111l1111l_opy_ = {}
    if file_path != None and os.path.exists(file_path):
        with open(file_path, bstack11ll1l_opy_ (u"࠭ࡲࠨᶱ")) as bstack1l11ll1ll_opy_:
            bstack1111l1111l_opy_ = json.load(bstack1l11ll1ll_opy_)
    return bstack1111l1111l_opy_
def bstack1l1l1ll11_opy_(file_path, logger):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
    except Exception as e:
        logger.debug(bstack11ll1l_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡧࡩࡱ࡫ࡴࡪࡰࡪࠤ࡫࡯࡬ࡦ࠼ࠣࠫᶲ") + file_path + bstack11ll1l_opy_ (u"ࠨࠢࠪᶳ") + str(e))
def bstack111llllll_opy_():
    from selenium import webdriver
    return version.parse(webdriver.__version__)
class Notset:
    def __repr__(self):
        return bstack11ll1l_opy_ (u"ࠤ࠿ࡒࡔ࡚ࡓࡆࡖࡁࠦᶴ")
def bstack1ll1l111l_opy_(config):
    if bstack11ll1l_opy_ (u"ࠪ࡭ࡸࡖ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠩᶵ") in config:
        del (config[bstack11ll1l_opy_ (u"ࠫ࡮ࡹࡐ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠪᶶ")])
        return False
    if bstack111llllll_opy_() < version.parse(bstack11ll1l_opy_ (u"ࠬ࠹࠮࠵࠰࠳ࠫᶷ")):
        return False
    if bstack111llllll_opy_() >= version.parse(bstack11ll1l_opy_ (u"࠭࠴࠯࠳࠱࠹ࠬᶸ")):
        return True
    if bstack11ll1l_opy_ (u"ࠧࡶࡵࡨ࡛࠸ࡉࠧᶹ") in config and config[bstack11ll1l_opy_ (u"ࠨࡷࡶࡩ࡜࠹ࡃࠨᶺ")] is False:
        return False
    else:
        return True
def bstack11ll111l1l_opy_(args_list, bstack1111l11llll_opy_):
    index = -1
    for value in bstack1111l11llll_opy_:
        try:
            index = args_list.index(value)
            return index
        except Exception as e:
            return index
    return index
def bstack1111l11l111_opy_(a, b):
  for k, v in b.items():
    if isinstance(v, dict) and k in a and isinstance(a[k], dict):
        bstack1111l11l111_opy_(a[k], v)
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
        return Result(result=bstack11ll1l_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩᶻ"))
    @classmethod
    def failed(cls, exception=None):
        return Result(result=bstack11ll1l_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪᶼ"), exception=exception)
    def bstack11111111ll_opy_(self):
        if self.result != bstack11ll1l_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫᶽ"):
            return None
        if isinstance(self.exception_type, str) and bstack11ll1l_opy_ (u"ࠧࡇࡳࡴࡧࡵࡸ࡮ࡵ࡮ࠣᶾ") in self.exception_type:
            return bstack11ll1l_opy_ (u"ࠨࡁࡴࡵࡨࡶࡹ࡯࡯࡯ࡇࡵࡶࡴࡸࠢᶿ")
        return bstack11ll1l_opy_ (u"ࠢࡖࡰ࡫ࡥࡳࡪ࡬ࡦࡦࡈࡶࡷࡵࡲࠣ᷀")
    def bstack111l1l1111l_opy_(self):
        if self.result != bstack11ll1l_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨ᷁"):
            return None
        if self.bstack1l111l1l_opy_:
            return self.bstack1l111l1l_opy_
        return bstack1111ll11111_opy_(self.exception)
def bstack1111ll11111_opy_(exc):
    return [traceback.format_exception(exc)]
def bstack111l111llll_opy_(message):
    if isinstance(message, str):
        return not bool(message and message.strip())
    return True
def bstack1lllll11_opy_(object, key, default_value):
    if not object or not object.__dict__:
        return default_value
    if key in object.__dict__.keys():
        return object.__dict__.get(key)
    return default_value
def bstack11llllll1l_opy_(config, logger):
    try:
        import playwright
        bstack1111llll111_opy_ = playwright.__file__
        bstack111l11l11ll_opy_ = os.path.split(bstack1111llll111_opy_)
        bstack111l1l1ll1l_opy_ = bstack111l11l11ll_opy_[0] + bstack11ll1l_opy_ (u"ࠩ࠲ࡨࡷ࡯ࡶࡦࡴ࠲ࡴࡦࡩ࡫ࡢࡩࡨ࠳ࡱ࡯ࡢ࠰ࡥ࡯࡭࠴ࡩ࡬ࡪ࠰࡭ࡷ᷂ࠬ")
        os.environ[bstack11ll1l_opy_ (u"ࠪࡋࡑࡕࡂࡂࡎࡢࡅࡌࡋࡎࡕࡡࡋࡘ࡙ࡖ࡟ࡑࡔࡒ࡜࡞࠭᷃")] = bstack111lll1111_opy_(config)
        with open(bstack111l1l1ll1l_opy_, bstack11ll1l_opy_ (u"ࠫࡷ࠭᷄")) as f:
            file_content = f.read()
            bstack111l1ll1l11_opy_ = bstack11ll1l_opy_ (u"ࠬ࡭࡬ࡰࡤࡤࡰ࠲ࡧࡧࡦࡰࡷࠫ᷅")
            bstack1111ll11l11_opy_ = file_content.find(bstack111l1ll1l11_opy_)
            if bstack1111ll11l11_opy_ == -1:
              process = subprocess.Popen(bstack11ll1l_opy_ (u"ࠨ࡮ࡱ࡯ࠣ࡭ࡳࡹࡴࡢ࡮࡯ࠤ࡬ࡲ࡯ࡣࡣ࡯࠱ࡦ࡭ࡥ࡯ࡶࠥ᷆"), shell=True, cwd=bstack111l11l11ll_opy_[0])
              process.wait()
              bstack1111lllll1l_opy_ = bstack11ll1l_opy_ (u"ࠧࠣࡷࡶࡩࠥࡹࡴࡳ࡫ࡦࡸࠧࡁࠧ᷇")
              bstack1111l111l11_opy_ = bstack11ll1l_opy_ (u"ࠣࠤࠥࠤࡡࠨࡵࡴࡧࠣࡷࡹࡸࡩࡤࡶ࡟ࠦࡀࠦࡣࡰࡰࡶࡸࠥࢁࠠࡣࡱࡲࡸࡸࡺࡲࡢࡲࠣࢁࠥࡃࠠࡳࡧࡴࡹ࡮ࡸࡥࠩࠩࡪࡰࡴࡨࡡ࡭࠯ࡤ࡫ࡪࡴࡴࠨࠫ࠾ࠤ࡮࡬ࠠࠩࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡨࡲࡻ࠴ࡇࡍࡑࡅࡅࡑࡥࡁࡈࡇࡑࡘࡤࡎࡔࡕࡒࡢࡔࡗࡕࡘ࡚ࠫࠣࡦࡴࡵࡴࡴࡶࡵࡥࡵ࠮ࠩ࠼ࠢࠥࠦࠧ᷈")
              bstack111l1ll1111_opy_ = file_content.replace(bstack1111lllll1l_opy_, bstack1111l111l11_opy_)
              with open(bstack111l1l1ll1l_opy_, bstack11ll1l_opy_ (u"ࠩࡺࠫ᷉")) as f:
                f.write(bstack111l1ll1111_opy_)
    except Exception as e:
        logger.error(bstack1ll1ll1lll_opy_.format(str(e)))
def bstack1111lll11_opy_():
  try:
    bstack1111l1ll1ll_opy_ = os.path.join(tempfile.gettempdir(), bstack11ll1l_opy_ (u"ࠪࡳࡵࡺࡩ࡮ࡣ࡯ࡣ࡭ࡻࡢࡠࡷࡵࡰ࠳ࡰࡳࡰࡰ᷊ࠪ"))
    bstack1111l111l1l_opy_ = []
    if os.path.exists(bstack1111l1ll1ll_opy_):
      with open(bstack1111l1ll1ll_opy_) as f:
        bstack1111l111l1l_opy_ = json.load(f)
      os.remove(bstack1111l1ll1ll_opy_)
    return bstack1111l111l1l_opy_
  except:
    pass
  return []
def bstack11l1ll1lll_opy_(bstack11l111ll1l_opy_):
  try:
    bstack1111l111l1l_opy_ = []
    bstack1111l1ll1ll_opy_ = os.path.join(tempfile.gettempdir(), bstack11ll1l_opy_ (u"ࠫࡴࡶࡴࡪ࡯ࡤࡰࡤ࡮ࡵࡣࡡࡸࡶࡱ࠴ࡪࡴࡱࡱࠫ᷋"))
    if os.path.exists(bstack1111l1ll1ll_opy_):
      with open(bstack1111l1ll1ll_opy_) as f:
        bstack1111l111l1l_opy_ = json.load(f)
    bstack1111l111l1l_opy_.append(bstack11l111ll1l_opy_)
    with open(bstack1111l1ll1ll_opy_, bstack11ll1l_opy_ (u"ࠬࡽࠧ᷌")) as f:
        json.dump(bstack1111l111l1l_opy_, f)
  except:
    pass
def bstack1l1lll1111_opy_(logger, bstack1111l1111ll_opy_ = False):
  try:
    test_name = os.environ.get(bstack11ll1l_opy_ (u"࠭ࡐ࡚ࡖࡈࡗ࡙ࡥࡔࡆࡕࡗࡣࡓࡇࡍࡆࠩ᷍"), bstack11ll1l_opy_ (u"ࠧࠨ᷎"))
    if test_name == bstack11ll1l_opy_ (u"ࠨ᷏ࠩ"):
        test_name = threading.current_thread().__dict__.get(bstack11ll1l_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࡄࡧࡨࡤࡺࡥࡴࡶࡢࡲࡦࡳࡥࠨ᷐"), bstack11ll1l_opy_ (u"ࠪࠫ᷑"))
    bstack1111l111lll_opy_ = bstack11ll1l_opy_ (u"ࠫ࠱ࠦࠧ᷒").join(threading.current_thread().bstackTestErrorMessages)
    if bstack1111l1111ll_opy_:
        bstack1l1llll1ll_opy_ = os.environ.get(bstack11ll1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡉࡏࡆࡈ࡜ࠬᷓ"), bstack11ll1l_opy_ (u"࠭࠰ࠨᷔ"))
        bstack11ll1llll1_opy_ = {bstack11ll1l_opy_ (u"ࠧ࡯ࡣࡰࡩࠬᷕ"): test_name, bstack11ll1l_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧᷖ"): bstack1111l111lll_opy_, bstack11ll1l_opy_ (u"ࠩ࡬ࡲࡩ࡫ࡸࠨᷗ"): bstack1l1llll1ll_opy_}
        bstack1111llll11l_opy_ = []
        bstack1111lll11ll_opy_ = os.path.join(tempfile.gettempdir(), bstack11ll1l_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࡢࡴࡵࡶ࡟ࡦࡴࡵࡳࡷࡥ࡬ࡪࡵࡷ࠲࡯ࡹ࡯࡯ࠩᷘ"))
        if os.path.exists(bstack1111lll11ll_opy_):
            with open(bstack1111lll11ll_opy_) as f:
                bstack1111llll11l_opy_ = json.load(f)
        bstack1111llll11l_opy_.append(bstack11ll1llll1_opy_)
        with open(bstack1111lll11ll_opy_, bstack11ll1l_opy_ (u"ࠫࡼ࠭ᷙ")) as f:
            json.dump(bstack1111llll11l_opy_, f)
    else:
        bstack11ll1llll1_opy_ = {bstack11ll1l_opy_ (u"ࠬࡴࡡ࡮ࡧࠪᷚ"): test_name, bstack11ll1l_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬᷛ"): bstack1111l111lll_opy_, bstack11ll1l_opy_ (u"ࠧࡪࡰࡧࡩࡽ࠭ᷜ"): str(multiprocessing.current_process().name)}
        if bstack11ll1l_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠࡧࡵࡶࡴࡸ࡟࡭࡫ࡶࡸࠬᷝ") not in multiprocessing.current_process().__dict__.keys():
            multiprocessing.current_process().bstack_error_list = []
        multiprocessing.current_process().bstack_error_list.append(bstack11ll1llll1_opy_)
  except Exception as e:
      logger.warn(bstack11ll1l_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡹࡴࡰࡴࡨࠤࡵࡿࡴࡦࡵࡷࠤ࡫ࡻ࡮࡯ࡧ࡯ࠤࡩࡧࡴࡢ࠼ࠣࡿࢂࠨᷞ").format(e))
def bstack1l11111ll1_opy_(error_message, test_name, index, logger):
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack11ll1l_opy_ (u"ࠪࡪ࡮ࡲࡥ࡭ࡱࡦ࡯ࠥࡴ࡯ࡵࠢࡤࡺࡦ࡯࡬ࡢࡤ࡯ࡩ࠱ࠦࡵࡴ࡫ࡱ࡫ࠥࡨࡡࡴ࡫ࡦࠤ࡫࡯࡬ࡦࠢࡲࡴࡪࡸࡡࡵ࡫ࡲࡲࡸ࠭ᷟ"))
    try:
      bstack111l1l1l11l_opy_ = []
      bstack11ll1llll1_opy_ = {bstack11ll1l_opy_ (u"ࠫࡳࡧ࡭ࡦࠩᷠ"): test_name, bstack11ll1l_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫᷡ"): error_message, bstack11ll1l_opy_ (u"࠭ࡩ࡯ࡦࡨࡼࠬᷢ"): index}
      bstack1111l1l1lll_opy_ = os.path.join(tempfile.gettempdir(), bstack11ll1l_opy_ (u"ࠧࡳࡱࡥࡳࡹࡥࡥࡳࡴࡲࡶࡤࡲࡩࡴࡶ࠱࡮ࡸࡵ࡮ࠨᷣ"))
      if os.path.exists(bstack1111l1l1lll_opy_):
          with open(bstack1111l1l1lll_opy_) as f:
              bstack111l1l1l11l_opy_ = json.load(f)
      bstack111l1l1l11l_opy_.append(bstack11ll1llll1_opy_)
      with open(bstack1111l1l1lll_opy_, bstack11ll1l_opy_ (u"ࠨࡹࠪᷤ")) as f:
          json.dump(bstack111l1l1l11l_opy_, f)
    except Exception as e:
      logger.warn(bstack11ll1l_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡹࡴࡰࡴࡨࠤࡷࡵࡢࡰࡶࠣࡪࡺࡴ࡮ࡦ࡮ࠣࡨࡦࡺࡡ࠻ࠢࡾࢁࠧᷥ").format(e))
    return
  bstack111l1l1l11l_opy_ = []
  bstack11ll1llll1_opy_ = {bstack11ll1l_opy_ (u"ࠪࡲࡦࡳࡥࠨᷦ"): test_name, bstack11ll1l_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪᷧ"): error_message, bstack11ll1l_opy_ (u"ࠬ࡯࡮ࡥࡧࡻࠫᷨ"): index}
  bstack1111l1l1lll_opy_ = os.path.join(tempfile.gettempdir(), bstack11ll1l_opy_ (u"࠭ࡲࡰࡤࡲࡸࡤ࡫ࡲࡳࡱࡵࡣࡱ࡯ࡳࡵ࠰࡭ࡷࡴࡴࠧᷩ"))
  lock_file = bstack1111l1l1lll_opy_ + bstack11ll1l_opy_ (u"ࠧ࠯࡮ࡲࡧࡰ࠭ᷪ")
  try:
    with FileLock(lock_file, timeout=10):
      if os.path.exists(bstack1111l1l1lll_opy_):
          with open(bstack1111l1l1lll_opy_, bstack11ll1l_opy_ (u"ࠨࡴࠪᷫ")) as f:
              content = f.read().strip()
              if content:
                  bstack111l1l1l11l_opy_ = json.load(open(bstack1111l1l1lll_opy_))
      bstack111l1l1l11l_opy_.append(bstack11ll1llll1_opy_)
      with open(bstack1111l1l1lll_opy_, bstack11ll1l_opy_ (u"ࠩࡺࠫᷬ")) as f:
          json.dump(bstack111l1l1l11l_opy_, f)
  except Exception as e:
    logger.warn(bstack11ll1l_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡳࡵࡱࡵࡩࠥࡸ࡯ࡣࡱࡷࠤ࡫ࡻ࡮࡯ࡧ࡯ࠤࡩࡧࡴࡢࠢࡺ࡭ࡹ࡮ࠠࡧ࡫࡯ࡩࠥࡲ࡯ࡤ࡭࡬ࡲ࡬ࡀࠠࡼࡿࠥᷭ").format(e))
def bstack1ll11111ll_opy_(bstack1llll11l11_opy_, name, logger):
  try:
    bstack11ll1llll1_opy_ = {bstack11ll1l_opy_ (u"ࠫࡳࡧ࡭ࡦࠩᷮ"): name, bstack11ll1l_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫᷯ"): bstack1llll11l11_opy_, bstack11ll1l_opy_ (u"࠭ࡩ࡯ࡦࡨࡼࠬᷰ"): str(threading.current_thread()._name)}
    return bstack11ll1llll1_opy_
  except Exception as e:
    logger.warn(bstack11ll1l_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡷࡹࡵࡲࡦࠢࡥࡩ࡭ࡧࡶࡦࠢࡩࡹࡳࡴࡥ࡭ࠢࡧࡥࡹࡧ࠺ࠡࡽࢀࠦᷱ").format(e))
  return
def bstack1111l11lll1_opy_():
    return platform.system() == bstack11ll1l_opy_ (u"ࠨ࡙࡬ࡲࡩࡵࡷࡴࠩᷲ")
def bstack11l1l111ll_opy_(bstack111l11lllll_opy_, config, logger):
    bstack111l11ll111_opy_ = {}
    try:
        return {key: config[key] for key in config if bstack111l11lllll_opy_.match(key)}
    except Exception as e:
        logger.debug(bstack11ll1l_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥ࡬ࡩ࡭ࡶࡨࡶࠥࡩ࡯࡯ࡨ࡬࡫ࠥࡱࡥࡺࡵࠣࡦࡾࠦࡲࡦࡩࡨࡼࠥࡳࡡࡵࡥ࡫࠾ࠥࢁࡽࠣᷳ").format(e))
    return bstack111l11ll111_opy_
def bstack11l1l1ll1ll_opy_(bstack111l11l1lll_opy_, bstack111l11lll1l_opy_):
    bstack111l11lll11_opy_ = version.parse(bstack111l11l1lll_opy_)
    bstack111l111ll1l_opy_ = version.parse(bstack111l11lll1l_opy_)
    if bstack111l11lll11_opy_ > bstack111l111ll1l_opy_:
        return 1
    elif bstack111l11lll11_opy_ < bstack111l111ll1l_opy_:
        return -1
    else:
        return 0
def bstack1l1l1ll1_opy_():
    return datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None)
def bstack111l1l111l1_opy_(timestamp):
    return datetime.datetime.fromtimestamp(timestamp, datetime.timezone.utc).replace(tzinfo=None)
def bstack111l111lll1_opy_(framework):
    from browserstack_sdk._version import __version__
    return str(framework) + str(__version__)
def bstack111l1l1111_opy_(options, framework, config, bstack11111ll1ll_opy_={}):
    if options is None:
        return
    if getattr(options, bstack11ll1l_opy_ (u"ࠪ࡫ࡪࡺࠧᷴ"), None):
        caps = options
    else:
        caps = options.to_capabilities()
    bstack11ll11l1l_opy_ = caps.get(bstack11ll1l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬ᷵"))
    bstack1111llll1l1_opy_ = True
    bstack1l1l111l1l_opy_ = os.environ[bstack11ll1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪ᷶")]
    bstack1l1111ll11l_opy_ = config.get(bstack11ll1l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ᷷࠭"), False)
    if bstack1l1111ll11l_opy_:
        bstack1l1l111l111_opy_ = config.get(bstack11ll1l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹ᷸ࠧ"), {})
        bstack1l1l111l111_opy_[bstack11ll1l_opy_ (u"ࠨࡣࡸࡸ࡭࡚࡯࡬ࡧࡱ᷹ࠫ")] = os.getenv(bstack11ll1l_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜᷺࡚ࠧ"))
        bstack111l1l1ll11_opy_ = json.loads(os.getenv(bstack11ll1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚࡟ࡂࡅࡆࡉࡘ࡙ࡉࡃࡋࡏࡍ࡙࡟࡟ࡄࡑࡑࡊࡎࡍࡕࡓࡃࡗࡍࡔࡔ࡟࡚ࡏࡏࠫ᷻"), bstack11ll1l_opy_ (u"ࠫࢀࢃࠧ᷼"))).get(bstack11ll1l_opy_ (u"ࠬࡹࡣࡢࡰࡱࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ᷽࠭"))
    if bstack1111l1lll1l_opy_(caps.get(bstack11ll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡻࡳࡦ࡙࠶ࡇࠬ᷾"))) or bstack1111l1lll1l_opy_(caps.get(bstack11ll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡵࡴࡧࡢࡻ࠸ࡩ᷿ࠧ"))):
        bstack1111llll1l1_opy_ = False
    if bstack1ll1l111l_opy_({bstack11ll1l_opy_ (u"ࠣࡷࡶࡩ࡜࠹ࡃࠣḀ"): bstack1111llll1l1_opy_}):
        bstack11ll11l1l_opy_ = bstack11ll11l1l_opy_ or {}
        bstack11ll11l1l_opy_[bstack11ll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡔࡆࡎࠫḁ")] = bstack111l111lll1_opy_(framework)
        bstack11ll11l1l_opy_[bstack11ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬḂ")] = bstack1lll11ll1ll_opy_()
        bstack11ll11l1l_opy_[bstack11ll1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡪࡸࡦࡇࡻࡩ࡭ࡦࡘࡹ࡮ࡪࠧḃ")] = bstack1l1l111l1l_opy_
        bstack11ll11l1l_opy_[bstack11ll1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡔࡷࡵࡤࡶࡥࡷࡑࡦࡶࠧḄ")] = bstack11111ll1ll_opy_
        if bstack1l1111ll11l_opy_:
            bstack11ll11l1l_opy_[bstack11ll1l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭ḅ")] = bstack1l1111ll11l_opy_
            bstack11ll11l1l_opy_[bstack11ll1l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧḆ")] = bstack1l1l111l111_opy_
            bstack11ll11l1l_opy_[bstack11ll1l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨḇ")][bstack11ll1l_opy_ (u"ࠩࡶࡧࡦࡴ࡮ࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪḈ")] = bstack111l1l1ll11_opy_
        if getattr(options, bstack11ll1l_opy_ (u"ࠪࡷࡪࡺ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶࡼࠫḉ"), None):
            options.set_capability(bstack11ll1l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬḊ"), bstack11ll11l1l_opy_)
        else:
            options[bstack11ll1l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭ḋ")] = bstack11ll11l1l_opy_
    else:
        if getattr(options, bstack11ll1l_opy_ (u"࠭ࡳࡦࡶࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹࡿࠧḌ"), None):
            options.set_capability(bstack11ll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡘࡊࡋࠨḍ"), bstack111l111lll1_opy_(framework))
            options.set_capability(bstack11ll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠩḎ"), bstack1lll11ll1ll_opy_())
            options.set_capability(bstack11ll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡶࡨࡷࡹ࡮ࡵࡣࡄࡸ࡭ࡱࡪࡕࡶ࡫ࡧࠫḏ"), bstack1l1l111l1l_opy_)
            options.set_capability(bstack11ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡥࡹ࡮ࡲࡤࡑࡴࡲࡨࡺࡩࡴࡎࡣࡳࠫḐ"), bstack11111ll1ll_opy_)
            if bstack1l1111ll11l_opy_:
                options.set_capability(bstack11ll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪḑ"), bstack1l1111ll11l_opy_)
                options.set_capability(bstack11ll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫḒ"), bstack1l1l111l111_opy_)
                options.set_capability(bstack11ll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷ࠳ࡹࡣࡢࡰࡱࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ḓ"), bstack111l1l1ll11_opy_)
        else:
            options[bstack11ll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡘࡊࡋࠨḔ")] = bstack111l111lll1_opy_(framework)
            options[bstack11ll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠩḕ")] = bstack1lll11ll1ll_opy_()
            options[bstack11ll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡶࡨࡷࡹ࡮ࡵࡣࡄࡸ࡭ࡱࡪࡕࡶ࡫ࡧࠫḖ")] = bstack1l1l111l1l_opy_
            options[bstack11ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡥࡹ࡮ࡲࡤࡑࡴࡲࡨࡺࡩࡴࡎࡣࡳࠫḗ")] = bstack11111ll1ll_opy_
            if bstack1l1111ll11l_opy_:
                options[bstack11ll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪḘ")] = bstack1l1111ll11l_opy_
                options[bstack11ll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫḙ")] = bstack1l1l111l111_opy_
                options[bstack11ll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷࠬḚ")][bstack11ll1l_opy_ (u"ࠧࡴࡥࡤࡲࡳ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨḛ")] = bstack111l1l1ll11_opy_
    return options
def bstack1111l1ll1l1_opy_(ws_endpoint, framework):
    bstack11111ll1ll_opy_ = bstack111ll1l1_opy_.get_property(bstack11ll1l_opy_ (u"ࠣࡒࡏࡅ࡞࡝ࡒࡊࡉࡋࡘࡤࡖࡒࡐࡆࡘࡇ࡙ࡥࡍࡂࡒࠥḜ"))
    if ws_endpoint and len(ws_endpoint.split(bstack11ll1l_opy_ (u"ࠩࡦࡥࡵࡹ࠽ࠨḝ"))) > 1:
        ws_url = ws_endpoint.split(bstack11ll1l_opy_ (u"ࠪࡧࡦࡶࡳ࠾ࠩḞ"))[0]
        if bstack11ll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳࠧḟ") in ws_url:
            from browserstack_sdk._version import __version__
            bstack111l1l1lll1_opy_ = json.loads(urllib.parse.unquote(ws_endpoint.split(bstack11ll1l_opy_ (u"ࠬࡩࡡࡱࡵࡀࠫḠ"))[1]))
            bstack111l1l1lll1_opy_ = bstack111l1l1lll1_opy_ or {}
            bstack1l1l111l1l_opy_ = os.environ[bstack11ll1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫḡ")]
            bstack111l1l1lll1_opy_[bstack11ll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡘࡊࡋࠨḢ")] = str(framework) + str(__version__)
            bstack111l1l1lll1_opy_[bstack11ll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠩḣ")] = bstack1lll11ll1ll_opy_()
            bstack111l1l1lll1_opy_[bstack11ll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡶࡨࡷࡹ࡮ࡵࡣࡄࡸ࡭ࡱࡪࡕࡶ࡫ࡧࠫḤ")] = bstack1l1l111l1l_opy_
            bstack111l1l1lll1_opy_[bstack11ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡥࡹ࡮ࡲࡤࡑࡴࡲࡨࡺࡩࡴࡎࡣࡳࠫḥ")] = bstack11111ll1ll_opy_
            ws_endpoint = ws_endpoint.split(bstack11ll1l_opy_ (u"ࠫࡨࡧࡰࡴ࠿ࠪḦ"))[0] + bstack11ll1l_opy_ (u"ࠬࡩࡡࡱࡵࡀࠫḧ") + urllib.parse.quote(json.dumps(bstack111l1l1lll1_opy_))
    return ws_endpoint
def bstack11l1ll1l11_opy_():
    global bstack1llll111ll_opy_
    from playwright._impl._browser_type import BrowserType
    bstack1llll111ll_opy_ = BrowserType.connect
    return bstack1llll111ll_opy_
def bstack1111l111l_opy_(framework_name):
    global bstack1l111lll1l_opy_
    bstack1l111lll1l_opy_ = framework_name
    return framework_name
def bstack111l11l1l_opy_(self, *args, **kwargs):
    global bstack1llll111ll_opy_
    try:
        global bstack1l111lll1l_opy_
        if bstack11ll1l_opy_ (u"࠭ࡷࡴࡇࡱࡨࡵࡵࡩ࡯ࡶࠪḨ") in kwargs:
            kwargs[bstack11ll1l_opy_ (u"ࠧࡸࡵࡈࡲࡩࡶ࡯ࡪࡰࡷࠫḩ")] = bstack1111l1ll1l1_opy_(
                kwargs.get(bstack11ll1l_opy_ (u"ࠨࡹࡶࡉࡳࡪࡰࡰ࡫ࡱࡸࠬḪ"), None),
                bstack1l111lll1l_opy_
            )
    except Exception as e:
        logger.error(bstack11ll1l_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡹ࡫ࡩࡳࠦࡰࡳࡱࡦࡩࡸࡹࡩ࡯ࡩࠣࡗࡉࡑࠠࡤࡣࡳࡷ࠿ࠦࡻࡾࠤḫ").format(str(e)))
    return bstack1llll111ll_opy_(self, *args, **kwargs)
def bstack111l11111ll_opy_(bstack111l1l11ll1_opy_, proxies):
    proxy_settings = {}
    try:
        if not proxies:
            proxies = bstack1ll11ll1l_opy_(bstack111l1l11ll1_opy_, bstack11ll1l_opy_ (u"ࠥࠦḬ"))
        if proxies and proxies.get(bstack11ll1l_opy_ (u"ࠦ࡭ࡺࡴࡱࡵࠥḭ")):
            parsed_url = urlparse(proxies.get(bstack11ll1l_opy_ (u"ࠧ࡮ࡴࡵࡲࡶࠦḮ")))
            if parsed_url and parsed_url.hostname: proxy_settings[bstack11ll1l_opy_ (u"࠭ࡰࡳࡱࡻࡽࡍࡵࡳࡵࠩḯ")] = str(parsed_url.hostname)
            if parsed_url and parsed_url.port: proxy_settings[bstack11ll1l_opy_ (u"ࠧࡱࡴࡲࡼࡾࡖ࡯ࡳࡶࠪḰ")] = str(parsed_url.port)
            if parsed_url and parsed_url.username: proxy_settings[bstack11ll1l_opy_ (u"ࠨࡲࡵࡳࡽࡿࡕࡴࡧࡵࠫḱ")] = str(parsed_url.username)
            if parsed_url and parsed_url.password: proxy_settings[bstack11ll1l_opy_ (u"ࠩࡳࡶࡴࡾࡹࡑࡣࡶࡷࠬḲ")] = str(parsed_url.password)
        return proxy_settings
    except:
        return proxy_settings
def bstack111ll11ll1_opy_(bstack111l1l11ll1_opy_):
    bstack1111ll11lll_opy_ = {
        bstack11l1l111l1l_opy_[bstack1111ll111l1_opy_]: bstack111l1l11ll1_opy_[bstack1111ll111l1_opy_]
        for bstack1111ll111l1_opy_ in bstack111l1l11ll1_opy_
        if bstack1111ll111l1_opy_ in bstack11l1l111l1l_opy_
    }
    bstack1111ll11lll_opy_[bstack11ll1l_opy_ (u"ࠥࡴࡷࡵࡸࡺࡕࡨࡸࡹ࡯࡮ࡨࡵࠥḳ")] = bstack111l11111ll_opy_(bstack111l1l11ll1_opy_, bstack111ll1l1_opy_.get_property(bstack11ll1l_opy_ (u"ࠦࡵࡸ࡯ࡹࡻࡖࡩࡹࡺࡩ࡯ࡩࡶࠦḴ")))
    bstack1111l1ll111_opy_ = [element.lower() for element in bstack11l11l1l111_opy_]
    bstack111l11llll1_opy_(bstack1111ll11lll_opy_, bstack1111l1ll111_opy_)
    return bstack1111ll11lll_opy_
def bstack111l11llll1_opy_(d, keys):
    for key in list(d.keys()):
        if key.lower() in keys:
            d[key] = bstack11ll1l_opy_ (u"ࠧ࠰ࠪࠫࠬࠥḵ")
    for value in d.values():
        if isinstance(value, dict):
            bstack111l11llll1_opy_(value, keys)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    bstack111l11llll1_opy_(item, keys)
def bstack1l1lll1l111_opy_():
    bstack1111lllll11_opy_ = [os.environ.get(bstack11ll1l_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡌࡉࡍࡇࡖࡣࡉࡏࡒࠣḶ")), os.path.join(os.path.expanduser(bstack11ll1l_opy_ (u"ࠢࡿࠤḷ")), bstack11ll1l_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨḸ")), os.path.join(bstack11ll1l_opy_ (u"ࠩ࠲ࡸࡲࡶࠧḹ"), bstack11ll1l_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪḺ"))]
    for path in bstack1111lllll11_opy_:
        if path is None:
            continue
        try:
            if os.path.exists(path):
                logger.debug(bstack11ll1l_opy_ (u"ࠦࡋ࡯࡬ࡦࠢࠪࠦḻ") + str(path) + bstack11ll1l_opy_ (u"ࠧ࠭ࠠࡦࡺ࡬ࡷࡹࡹ࠮ࠣḼ"))
                if not os.access(path, os.W_OK):
                    logger.debug(bstack11ll1l_opy_ (u"ࠨࡇࡪࡸ࡬ࡲ࡬ࠦࡰࡦࡴࡰ࡭ࡸࡹࡩࡰࡰࡶࠤ࡫ࡵࡲࠡࠩࠥḽ") + str(path) + bstack11ll1l_opy_ (u"ࠢࠨࠤḾ"))
                    os.chmod(path, 0o777)
                else:
                    logger.debug(bstack11ll1l_opy_ (u"ࠣࡈ࡬ࡰࡪࠦࠧࠣḿ") + str(path) + bstack11ll1l_opy_ (u"ࠤࠪࠤࡦࡲࡲࡦࡣࡧࡽࠥ࡮ࡡࡴࠢࡷ࡬ࡪࠦࡲࡦࡳࡸ࡭ࡷ࡫ࡤࠡࡲࡨࡶࡲ࡯ࡳࡴ࡫ࡲࡲࡸ࠴ࠢṀ"))
            else:
                logger.debug(bstack11ll1l_opy_ (u"ࠥࡇࡷ࡫ࡡࡵ࡫ࡱ࡫ࠥ࡬ࡩ࡭ࡧࠣࠫࠧṁ") + str(path) + bstack11ll1l_opy_ (u"ࠦࠬࠦࡷࡪࡶ࡫ࠤࡼࡸࡩࡵࡧࠣࡴࡪࡸ࡭ࡪࡵࡶ࡭ࡴࡴ࠮ࠣṂ"))
                os.makedirs(path, exist_ok=True)
                os.chmod(path, 0o777)
            logger.debug(bstack11ll1l_opy_ (u"ࠧࡕࡰࡦࡴࡤࡸ࡮ࡵ࡮ࠡࡵࡸࡧࡨ࡫ࡥࡥࡧࡧࠤ࡫ࡵࡲࠡࠩࠥṃ") + str(path) + bstack11ll1l_opy_ (u"ࠨࠧ࠯ࠤṄ"))
            return path
        except Exception as e:
            logger.debug(bstack11ll1l_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡪࡺࠠࡶࡲࠣࡪ࡮ࡲࡥࠡࠩࡾࡴࡦࡺࡨࡾࠩ࠽ࠤࠧṅ") + str(e) + bstack11ll1l_opy_ (u"ࠣࠤṆ"))
    logger.debug(bstack11ll1l_opy_ (u"ࠤࡄࡰࡱࠦࡰࡢࡶ࡫ࡷࠥ࡬ࡡࡪ࡮ࡨࡨ࠳ࠨṇ"))
    return None
@measure(event_name=EVENTS.bstack11l11lll1l1_opy_, stage=STAGE.bstack11ll11lll_opy_)
def bstack1l1l1lllll1_opy_(binary_path, bstack1l11ll1llll_opy_, bs_config):
    logger.debug(bstack11ll1l_opy_ (u"ࠥࡇࡺࡸࡲࡦࡰࡷࠤࡈࡒࡉࠡࡒࡤࡸ࡭ࠦࡦࡰࡷࡱࡨ࠿ࠦࡻࡾࠤṈ").format(binary_path))
    bstack111l1111111_opy_ = bstack11ll1l_opy_ (u"ࠫࠬṉ")
    bstack111l111l1ll_opy_ = {
        bstack11ll1l_opy_ (u"ࠬࡹࡤ࡬ࡡࡹࡩࡷࡹࡩࡰࡰࠪṊ"): __version__,
        bstack11ll1l_opy_ (u"ࠨ࡯ࡴࠤṋ"): platform.system(),
        bstack11ll1l_opy_ (u"ࠢࡰࡵࡢࡥࡷࡩࡨࠣṌ"): platform.machine(),
        bstack11ll1l_opy_ (u"ࠣࡥ࡯࡭ࡤࡼࡥࡳࡵ࡬ࡳࡳࠨṍ"): bstack11ll1l_opy_ (u"ࠩ࠳ࠫṎ"),
        bstack11ll1l_opy_ (u"ࠥࡷࡩࡱ࡟࡭ࡣࡱ࡫ࡺࡧࡧࡦࠤṏ"): bstack11ll1l_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫṐ")
    }
    bstack1111ll1l1l1_opy_(bstack111l111l1ll_opy_)
    try:
        if binary_path:
            bstack111l111l1ll_opy_[bstack11ll1l_opy_ (u"ࠬࡩ࡬ࡪࡡࡹࡩࡷࡹࡩࡰࡰࠪṑ")] = subprocess.check_output([binary_path, bstack11ll1l_opy_ (u"ࠨࡶࡦࡴࡶ࡭ࡴࡴࠢṒ")]).strip().decode(bstack11ll1l_opy_ (u"ࠧࡶࡶࡩ࠱࠽࠭ṓ"))
        response = requests.request(
            bstack11ll1l_opy_ (u"ࠨࡉࡈࡘࠬṔ"),
            url=bstack1l1lll1l11_opy_(bstack11l1l11ll1l_opy_),
            headers=None,
            auth=(bs_config[bstack11ll1l_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫṕ")], bs_config[bstack11ll1l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭Ṗ")]),
            json=None,
            params=bstack111l111l1ll_opy_
        )
        data = response.json()
        if response.status_code == 200 and bstack11ll1l_opy_ (u"ࠫࡺࡸ࡬ࠨṗ") in data.keys() and bstack11ll1l_opy_ (u"ࠬࡻࡰࡥࡣࡷࡩࡩࡥࡣ࡭࡫ࡢࡺࡪࡸࡳࡪࡱࡱࠫṘ") in data.keys():
            logger.debug(bstack11ll1l_opy_ (u"ࠨࡎࡦࡧࡧࠤࡹࡵࠠࡶࡲࡧࡥࡹ࡫ࠠࡣ࡫ࡱࡥࡷࡿࠬࠡࡥࡸࡶࡷ࡫࡮ࡵࠢࡥ࡭ࡳࡧࡲࡺࠢࡹࡩࡷࡹࡩࡰࡰ࠽ࠤࢀࢃࠢṙ").format(bstack111l111l1ll_opy_[bstack11ll1l_opy_ (u"ࠧࡤ࡮࡬ࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬṚ")]))
            if bstack11ll1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡃࡋࡑࡅࡗ࡟࡟ࡖࡔࡏࠫṛ") in os.environ:
                logger.debug(bstack11ll1l_opy_ (u"ࠤࡖ࡯࡮ࡶࡰࡪࡰࡪࠤࡧ࡯࡮ࡢࡴࡼࠤࡩࡵࡷ࡯࡮ࡲࡥࡩࠦࡡࡴࠢࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡄࡌࡒࡆࡘ࡙ࡠࡗࡕࡐࠥ࡯ࡳࠡࡵࡨࡸࠧṜ"))
                data[bstack11ll1l_opy_ (u"ࠪࡹࡷࡲࠧṝ")] = os.environ[bstack11ll1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡆࡎࡔࡁࡓ࡛ࡢ࡙ࡗࡒࠧṞ")]
            bstack1111l1llll1_opy_ = bstack1111l11l11l_opy_(data[bstack11ll1l_opy_ (u"ࠬࡻࡲ࡭ࠩṟ")], bstack1l11ll1llll_opy_)
            bstack111l1111111_opy_ = os.path.join(bstack1l11ll1llll_opy_, bstack1111l1llll1_opy_)
            os.chmod(bstack111l1111111_opy_, 0o777) # bstack111l1ll1l1l_opy_ permission
            return bstack111l1111111_opy_
    except Exception as e:
        logger.debug(bstack11ll1l_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡽࡨࡪ࡮ࡨࠤࡩࡵࡷ࡯࡮ࡲࡥࡩ࡯࡮ࡨࠢࡱࡩࡼࠦࡓࡅࡍࠣࡿࢂࠨṠ").format(e))
    return binary_path
def bstack1111ll1l1l1_opy_(bstack111l111l1ll_opy_):
    try:
        if bstack11ll1l_opy_ (u"ࠧ࡭࡫ࡱࡹࡽ࠭ṡ") not in bstack111l111l1ll_opy_[bstack11ll1l_opy_ (u"ࠨࡱࡶࠫṢ")].lower():
            return
        if os.path.exists(bstack11ll1l_opy_ (u"ࠤ࠲ࡩࡹࡩ࠯ࡰࡵ࠰ࡶࡪࡲࡥࡢࡵࡨࠦṣ")):
            with open(bstack11ll1l_opy_ (u"ࠥ࠳ࡪࡺࡣ࠰ࡱࡶ࠱ࡷ࡫࡬ࡦࡣࡶࡩࠧṤ"), bstack11ll1l_opy_ (u"ࠦࡷࠨṥ")) as f:
                bstack1111l1l11l1_opy_ = {}
                for line in f:
                    if bstack11ll1l_opy_ (u"ࠧࡃࠢṦ") in line:
                        key, value = line.rstrip().split(bstack11ll1l_opy_ (u"ࠨ࠽ࠣṧ"), 1)
                        bstack1111l1l11l1_opy_[key] = value.strip(bstack11ll1l_opy_ (u"ࠧࠣ࡞ࠪࠫṨ"))
                bstack111l111l1ll_opy_[bstack11ll1l_opy_ (u"ࠨࡦ࡬ࡷࡹࡸ࡯ࠨṩ")] = bstack1111l1l11l1_opy_.get(bstack11ll1l_opy_ (u"ࠤࡌࡈࠧṪ"), bstack11ll1l_opy_ (u"ࠥࠦṫ"))
        elif os.path.exists(bstack11ll1l_opy_ (u"ࠦ࠴࡫ࡴࡤ࠱ࡤࡰࡵ࡯࡮ࡦ࠯ࡵࡩࡱ࡫ࡡࡴࡧࠥṬ")):
            bstack111l111l1ll_opy_[bstack11ll1l_opy_ (u"ࠬࡪࡩࡴࡶࡵࡳࠬṭ")] = bstack11ll1l_opy_ (u"࠭ࡡ࡭ࡲ࡬ࡲࡪ࠭Ṯ")
    except Exception as e:
        logger.debug(bstack11ll1l_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣ࡫ࡪࡺࠠࡥ࡫ࡶࡸࡷࡵࠠࡰࡨࠣࡰ࡮ࡴࡵࡹࠤṯ") + e)
@measure(event_name=EVENTS.bstack11l11ll11l1_opy_, stage=STAGE.bstack11ll11lll_opy_)
def bstack1111l11l11l_opy_(bstack1111ll11l1l_opy_, bstack111l1ll11l1_opy_):
    logger.debug(bstack11ll1l_opy_ (u"ࠣࡆࡲࡻࡳࡲ࡯ࡢࡦ࡬ࡲ࡬ࠦࡓࡅࡍࠣࡦ࡮ࡴࡡࡳࡻࠣࡪࡷࡵ࡭࠻ࠢࠥṰ") + str(bstack1111ll11l1l_opy_) + bstack11ll1l_opy_ (u"ࠤࠥṱ"))
    zip_path = os.path.join(bstack111l1ll11l1_opy_, bstack11ll1l_opy_ (u"ࠥࡨࡴࡽ࡮࡭ࡱࡤࡨࡪࡪ࡟ࡧ࡫࡯ࡩ࠳ࢀࡩࡱࠤṲ"))
    bstack1111l1llll1_opy_ = bstack11ll1l_opy_ (u"ࠫࠬṳ")
    with requests.get(bstack1111ll11l1l_opy_, stream=True) as response:
        response.raise_for_status()
        with open(zip_path, bstack11ll1l_opy_ (u"ࠧࡽࡢࠣṴ")) as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
        logger.debug(bstack11ll1l_opy_ (u"ࠨࡆࡪ࡮ࡨࠤࡩࡵࡷ࡯࡮ࡲࡥࡩ࡫ࡤࠡࡵࡸࡧࡨ࡫ࡳࡴࡨࡸࡰࡱࡿ࠮ࠣṵ"))
    with zipfile.ZipFile(zip_path, bstack11ll1l_opy_ (u"ࠧࡳࠩṶ")) as zip_ref:
        bstack1111l1l111l_opy_ = zip_ref.namelist()
        if len(bstack1111l1l111l_opy_) > 0:
            bstack1111l1llll1_opy_ = bstack1111l1l111l_opy_[0] # bstack1111lll1lll_opy_ bstack11l11l1l11l_opy_ will be bstack111l111l111_opy_ 1 file i.e. the binary in the zip
        zip_ref.extractall(bstack111l1ll11l1_opy_)
        logger.debug(bstack11ll1l_opy_ (u"ࠣࡈ࡬ࡰࡪࡹࠠࡴࡷࡦࡧࡪࡹࡳࡧࡷ࡯ࡰࡾࠦࡥࡹࡶࡵࡥࡨࡺࡥࡥࠢࡷࡳࠥ࠭ࠢṷ") + str(bstack111l1ll11l1_opy_) + bstack11ll1l_opy_ (u"ࠤࠪࠦṸ"))
    os.remove(zip_path)
    return bstack1111l1llll1_opy_
def get_cli_dir():
    bstack111l1111lll_opy_ = bstack1l1lll1l111_opy_()
    if bstack111l1111lll_opy_:
        bstack1l11ll1llll_opy_ = os.path.join(bstack111l1111lll_opy_, bstack11ll1l_opy_ (u"ࠥࡧࡱ࡯ࠢṹ"))
        if not os.path.exists(bstack1l11ll1llll_opy_):
            os.makedirs(bstack1l11ll1llll_opy_, mode=0o777, exist_ok=True)
        return bstack1l11ll1llll_opy_
    else:
        raise FileNotFoundError(bstack11ll1l_opy_ (u"ࠦࡓࡵࠠࡸࡴ࡬ࡸࡦࡨ࡬ࡦࠢࡧ࡭ࡷ࡫ࡣࡵࡱࡵࡽࠥࡧࡶࡢ࡫࡯ࡥࡧࡲࡥࠡࡨࡲࡶࠥࡺࡨࡦࠢࡖࡈࡐࠦࡢࡪࡰࡤࡶࡾ࠴ࠢṺ"))
def bstack1l11ll1ll11_opy_(bstack1l11ll1llll_opy_):
    bstack11ll1l_opy_ (u"ࠧࠨࠢࡈࡧࡷࠤࡹ࡮ࡥࠡࡲࡤࡸ࡭ࠦࡦࡰࡴࠣࡸ࡭࡫ࠠࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠦࡓࡅࡍࠣࡦ࡮ࡴࡡࡳࡻࠣ࡭ࡳࠦࡡࠡࡹࡵ࡭ࡹࡧࡢ࡭ࡧࠣࡨ࡮ࡸࡥࡤࡶࡲࡶࡾ࠴ࠢࠣࠤṻ")
    bstack1111l1l1111_opy_ = [
        os.path.join(bstack1l11ll1llll_opy_, f)
        for f in os.listdir(bstack1l11ll1llll_opy_)
        if os.path.isfile(os.path.join(bstack1l11ll1llll_opy_, f)) and f.startswith(bstack11ll1l_opy_ (u"ࠨࡢࡪࡰࡤࡶࡾ࠳ࠢṼ"))
    ]
    if len(bstack1111l1l1111_opy_) > 0:
        return max(bstack1111l1l1111_opy_, key=os.path.getmtime) # get bstack1111lll1111_opy_ binary
    return bstack11ll1l_opy_ (u"ࠢࠣṽ")
def bstack111l1111l1l_opy_():
  from selenium import webdriver
  return version.parse(webdriver.__version__)
def bstack1l111l11lll_opy_(d, u):
  for k, v in u.items():
    if isinstance(v, collections.abc.Mapping):
      d[k] = bstack1l111l11lll_opy_(d.get(k, {}), v)
    else:
      if isinstance(v, list):
        d[k] = d.get(k, []) + v
      else:
        d[k] = v
  return d
def bstack1lll1l11l1_opy_(data, keys, default=None):
    bstack11ll1l_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࡕࡤࡪࡪࡲࡹࠡࡩࡨࡸࠥࡧࠠ࡯ࡧࡶࡸࡪࡪࠠࡷࡣ࡯ࡹࡪࠦࡦࡳࡱࡰࠤࡦࠦࡤࡪࡥࡷ࡭ࡴࡴࡡࡳࡻࠣࡳࡷࠦ࡬ࡪࡵࡷ࠲ࠏࠦࠠࠡࠢ࠽ࡴࡦࡸࡡ࡮ࠢࡧࡥࡹࡧ࠺ࠡࡖ࡫ࡩࠥࡪࡩࡤࡶ࡬ࡳࡳࡧࡲࡺࠢࡲࡶࠥࡲࡩࡴࡶࠣࡸࡴࠦࡴࡳࡣࡹࡩࡷࡹࡥ࠯ࠌࠣࠤࠥࠦ࠺ࡱࡣࡵࡥࡲࠦ࡫ࡦࡻࡶ࠾ࠥࡇࠠ࡭࡫ࡶࡸࠥࡵࡦࠡ࡭ࡨࡽࡸ࠵ࡩ࡯ࡦ࡬ࡧࡪࡹࠠࡳࡧࡳࡶࡪࡹࡥ࡯ࡶ࡬ࡲ࡬ࠦࡴࡩࡧࠣࡴࡦࡺࡨ࠯ࠌࠣࠤࠥࠦ࠺ࡱࡣࡵࡥࡲࠦࡤࡦࡨࡤࡹࡱࡺ࠺ࠡࡘࡤࡰࡺ࡫ࠠࡵࡱࠣࡶࡪࡺࡵࡳࡰࠣ࡭࡫ࠦࡴࡩࡧࠣࡴࡦࡺࡨࠡࡦࡲࡩࡸࠦ࡮ࡰࡶࠣࡩࡽ࡯ࡳࡵ࠰ࠍࠤࠥࠦࠠ࠻ࡴࡨࡸࡺࡸ࡮࠻ࠢࡗ࡬ࡪࠦࡶࡢ࡮ࡸࡩࠥࡧࡴࠡࡶ࡫ࡩࠥࡴࡥࡴࡶࡨࡨࠥࡶࡡࡵࡪ࠯ࠤࡴࡸࠠࡥࡧࡩࡥࡺࡲࡴࠡ࡫ࡩࠤࡳࡵࡴࠡࡨࡲࡹࡳࡪ࠮ࠋࠢࠣࠤࠥࠨࠢࠣṾ")
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