# coding: UTF-8
import sys
bstack11_opy_ = sys.version_info [0] == 2
bstack1l111ll_opy_ = 2048
bstack11lll1l_opy_ = 7
def bstack1lll11l_opy_ (bstack11l11l_opy_):
    global bstack11l1l1_opy_
    bstack1l111_opy_ = ord (bstack11l11l_opy_ [-1])
    bstack1ll11l1_opy_ = bstack11l11l_opy_ [:-1]
    bstack1l_opy_ = bstack1l111_opy_ % len (bstack1ll11l1_opy_)
    bstack1l11ll1_opy_ = bstack1ll11l1_opy_ [:bstack1l_opy_] + bstack1ll11l1_opy_ [bstack1l_opy_:]
    if bstack11_opy_:
        bstack1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l111ll_opy_ - (bstack1l11ll_opy_ + bstack1l111_opy_) % bstack11lll1l_opy_) for bstack1l11ll_opy_, char in enumerate (bstack1l11ll1_opy_)])
    else:
        bstack1ll_opy_ = str () .join ([chr (ord (char) - bstack1l111ll_opy_ - (bstack1l11ll_opy_ + bstack1l111_opy_) % bstack11lll1l_opy_) for bstack1l11ll_opy_, char in enumerate (bstack1l11ll1_opy_)])
    return eval (bstack1ll_opy_)
from datetime import datetime
import os
import threading
from browserstack_sdk.sdk_cli.bstack1lllll11lll_opy_ import (
    bstack1111111111_opy_,
    bstack1llll1lllll_opy_,
    bstack1lll111lll1_opy_,
    bstack1lllllll11l_opy_,
)
from browserstack_sdk.sdk_cli.bstack1llll1l1111_opy_ import bstack1llllll1ll1_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1l11lll_opy_, bstack1lll11lll11_opy_, bstack1llll111111_opy_
from typing import Tuple, Dict, Any, List, Union
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1llllll11ll_opy_ import bstack1lllllll1l1_opy_
from browserstack_sdk.sdk_cli.bstack1lll111l111_opy_ import bstack1lll11l1111_opy_
from browserstack_sdk.sdk_cli.bstack1lll1l1l1l1_opy_ import bstack1lll1ll11l1_opy_
from browserstack_sdk.sdk_cli.bstack1lll1l11l11_opy_ import bstack1lll1lll111_opy_
from bstack_utils.helper import bstack1l111l1ll11_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
from bstack_utils.bstack1ll1ll1lll_opy_ import bstack1llll1l1l1l_opy_
import grpc
import traceback
import json
class bstack1l11ll1ll1l_opy_(bstack1lllllll1l1_opy_):
    bstack1l1ll11l1ll_opy_ = False
    bstack1l11111llll_opy_ = bstack1lll11l_opy_ (u"ࠣࡵࡨࡰࡪࡴࡩࡶ࡯࠱ࡻࡪࡨࡤࡳ࡫ࡹࡩࡷࠨᑋ")
    bstack1l111l1lll1_opy_ = bstack1lll11l_opy_ (u"ࠤࡵࡩࡲࡵࡴࡦ࠰ࡺࡩࡧࡪࡲࡪࡸࡨࡶࠧᑌ")
    bstack1l1111ll1l1_opy_ = bstack1lll11l_opy_ (u"ࠥࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡢ࡭ࡳ࡯ࡴࠣᑍ")
    bstack1l11111l111_opy_ = bstack1lll11l_opy_ (u"ࠦࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡣ࡮ࡹ࡟ࡴࡥࡤࡲࡳ࡯࡮ࡨࠤᑎ")
    bstack1l111l1l11l_opy_ = bstack1lll11l_opy_ (u"ࠧࡪࡲࡪࡸࡨࡶࡤ࡮ࡡࡴࡡࡸࡶࡱࠨᑏ")
    scripts: Dict[str, Dict[str, str]]
    commands: Dict[str, Dict[str, Dict[str, List[str]]]]
    def __init__(self, bstack1l1l1l11l11_opy_, bstack1ll1lll111l_opy_):
        super().__init__()
        self.scripts = dict()
        self.commands = dict()
        self.accessibility = False
        self.bstack1l111ll1l11_opy_ = False
        self.bstack1l11111ll11_opy_ = dict()
        self.bstack1l1111lll1l_opy_ = False
        self.bstack1l111ll11l1_opy_ = dict()
        if not self.is_enabled():
            return
        self.bstack1l11l11l111_opy_ = bstack1ll1lll111l_opy_
        bstack1l1l1l11l11_opy_.bstack1lllll11111_opy_((bstack1111111111_opy_.bstack1llll1ll111_opy_, bstack1llll1lllll_opy_.PRE), self.bstack1l111l11lll_opy_)
        TestFramework.bstack1lllll11111_opy_((bstack1lll1l11lll_opy_.TEST, bstack1lll11lll11_opy_.PRE), self.bstack1llll111l11_opy_)
        TestFramework.bstack1lllll11111_opy_((bstack1lll1l11lll_opy_.TEST, bstack1lll11lll11_opy_.POST), self.bstack1lll1lll1ll_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1llll111l11_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll111111_opy_,
        bstack1lllll1l111_opy_: Tuple[bstack1lll1l11lll_opy_, bstack1lll11lll11_opy_],
        *args,
        **kwargs,
    ):
        tags = self._1l1111lll11_opy_(instance, args)
        test_framework = f.get_state(instance, TestFramework.bstack1llll1111l1_opy_)
        if self.bstack1l111ll1l11_opy_:
            self.bstack1l11111ll11_opy_[bstack1lll11l_opy_ (u"ࠨࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩࠨᑐ")] = f.get_state(instance, TestFramework.bstack1lll11ll11l_opy_)
        if bstack1lll11l_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠫᑑ") in instance.bstack1l1llllll11_opy_:
            platform_index = f.get_state(instance, TestFramework.bstack1lllllllll1_opy_)
            self.accessibility = self.bstack1l1111l1lll_opy_(tags, self.config[bstack1lll11l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫᑒ")][platform_index])
        else:
            capabilities = self.bstack1l11l11l111_opy_.bstack1lll1ll1l1l_opy_(f, instance, bstack1lllll1l111_opy_, *args, **kwargs)
            if not capabilities:
                self.logger.debug(bstack1lll11l_opy_ (u"ࠤࡲࡲࡤࡨࡥࡧࡱࡵࡩࡤࡺࡥࡴࡶ࠽ࠤࡳࡵࠠࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸࠦࡦࡰࡷࡱࡨࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤᑓ") + str(kwargs) + bstack1lll11l_opy_ (u"ࠥࠦᑔ"))
                return
            self.accessibility = self.bstack1l1111l1lll_opy_(tags, capabilities)
        if self.bstack1l11l11l111_opy_.pages and self.bstack1l11l11l111_opy_.pages.values():
            bstack1l111l1l1l1_opy_ = list(self.bstack1l11l11l111_opy_.pages.values())
            if bstack1l111l1l1l1_opy_ and isinstance(bstack1l111l1l1l1_opy_[0], (list, tuple)) and bstack1l111l1l1l1_opy_[0]:
                bstack1l1111l1l11_opy_ = bstack1l111l1l1l1_opy_[0][0]
                if callable(bstack1l1111l1l11_opy_):
                    page = bstack1l1111l1l11_opy_()
                    def bstack11l1l1ll1_opy_():
                        self.get_accessibility_results(page, bstack1lll11l_opy_ (u"ࠦࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠣᑕ"))
                    def bstack1l111ll111l_opy_():
                        self.get_accessibility_results_summary(page, bstack1lll11l_opy_ (u"ࠧࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠤᑖ"))
                    setattr(page, bstack1lll11l_opy_ (u"ࠨࡧࡦࡶࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡔࡨࡷࡺࡲࡴࡴࠤᑗ"), bstack11l1l1ll1_opy_)
                    setattr(page, bstack1lll11l_opy_ (u"ࠢࡨࡧࡷࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡕࡩࡸࡻ࡬ࡵࡕࡸࡱࡲࡧࡲࡺࠤᑘ"), bstack1l111ll111l_opy_)
        self.logger.debug(bstack1lll11l_opy_ (u"ࠣࡵ࡫ࡳࡺࡲࡤࠡࡴࡸࡲࠥࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡼࡡ࡭ࡷࡨࡁࠧᑙ") + str(self.accessibility) + bstack1lll11l_opy_ (u"ࠤࠥᑚ"))
    def bstack1l111l11lll_opy_(
        self,
        f: bstack1llllll1ll1_opy_,
        driver: object,
        exec: Tuple[bstack1lllllll11l_opy_, str],
        bstack1lllll1l111_opy_: Tuple[bstack1111111111_opy_, bstack1llll1lllll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        try:
            bstack11ll11l1l_opy_ = datetime.now()
            self.bstack1l11111l1ll_opy_(f, exec, *args, **kwargs)
            instance, method_name = exec
            instance.bstack111l1l1l1l_opy_(bstack1lll11l_opy_ (u"ࠥࡥ࠶࠷ࡹ࠻࡫ࡱ࡭ࡹࡥࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡥࡣࡰࡰࡩ࡭࡬ࠨᑛ"), datetime.now() - bstack11ll11l1l_opy_)
            if (
                not f.bstack1l1lll1111l_opy_(method_name)
                or f.bstack1l1lll111ll_opy_(method_name, *args)
                or f.bstack1l1ll1ll11l_opy_(method_name, *args)
            ):
                return
            if not f.get_state(instance, bstack1l11ll1ll1l_opy_.bstack1l1111ll1l1_opy_, False):
                if not bstack1l11ll1ll1l_opy_.bstack1l1ll11l1ll_opy_:
                    self.logger.warning(bstack1lll11l_opy_ (u"ࠦࡠࡶ࡬ࡢࡶࡩࡳࡷࡳ࡟ࡪࡰࡧࡩࡽࡃࠢᑜ") + str(f.platform_index) + bstack1lll11l_opy_ (u"ࠧࡣࠠࡢ࠳࠴ࡽࠥࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠤ࡭ࡧࡶࡦࠢࡱࡳࡹࠦࡢࡦࡧࡱࠤࡸ࡫ࡴࠡࡨࡲࡶࠥࡺࡨࡪࡵࠣࡷࡪࡹࡳࡪࡱࡱࠦᑝ"))
                    bstack1l11ll1ll1l_opy_.bstack1l1ll11l1ll_opy_ = True
                return
            bstack1l1111llll1_opy_ = self.scripts.get(f.framework_name, {})
            if not bstack1l1111llll1_opy_:
                platform_index = f.get_state(instance, bstack1llllll1ll1_opy_.bstack1lllllllll1_opy_, 0)
                self.logger.debug(bstack1lll11l_opy_ (u"ࠨ࡮ࡰࠢࡤ࠵࠶ࡿࠠࡴࡥࡵ࡭ࡵࡺࡳࠡࡨࡲࡶࠥࡶ࡬ࡢࡶࡩࡳࡷࡳ࡟ࡪࡰࡧࡩࡽࡃࡻࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡡ࡬ࡲࡩ࡫ࡸࡾࠢࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡴࡡ࡮ࡧࡀࠦᑞ") + str(f.framework_name) + bstack1lll11l_opy_ (u"ࠢࠣᑟ"))
                return
            command_name = f.bstack1l1ll1ll1l1_opy_(*args)
            if not command_name:
                self.logger.debug(bstack1lll11l_opy_ (u"ࠣ࡯࡬ࡷࡸ࡯࡮ࡨࠢࡦࡳࡲࡳࡡ࡯ࡦࡢࡲࡦࡳࡥࠡࡨࡲࡶࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪࡃࡻࡧ࠰ࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡴࡡ࡮ࡧࢀࠤࡲ࡫ࡴࡩࡱࡧࡣࡳࡧ࡭ࡦ࠿ࠥᑠ") + str(method_name) + bstack1lll11l_opy_ (u"ࠤࠥᑡ"))
                return
            bstack1l111l11ll1_opy_ = f.get_state(instance, bstack1l11ll1ll1l_opy_.bstack1l111l1l11l_opy_, False)
            if command_name == bstack1lll11l_opy_ (u"ࠥ࡫ࡪࡺࠢᑢ") and not bstack1l111l11ll1_opy_:
                f.bstack1llll1ll11l_opy_(instance, bstack1l11ll1ll1l_opy_.bstack1l111l1l11l_opy_, True)
                bstack1l111l11ll1_opy_ = True
            if not bstack1l111l11ll1_opy_ and not self.bstack1l111ll1l11_opy_:
                self.logger.debug(bstack1lll11l_opy_ (u"ࠦࡳࡵࠠࡖࡔࡏࠤࡱࡵࡡࡥࡧࡧࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟࡯ࡣࡰࡩࡂࢁࡦ࠯ࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦࡿࠣࡧࡴࡳ࡭ࡢࡰࡧࡣࡳࡧ࡭ࡦ࠿ࠥᑣ") + str(command_name) + bstack1lll11l_opy_ (u"ࠧࠨᑤ"))
                return
            scripts_to_run = self.commands.get(f.framework_name, {}).get(method_name, {}).get(command_name, [])
            if not scripts_to_run:
                self.logger.debug(bstack1lll11l_opy_ (u"ࠨ࡮ࡰࠢࡤ࠵࠶ࡿࠠࡴࡥࡵ࡭ࡵࡺࡳࠡࡨࡲࡶࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪࡃࡻࡧ࠰ࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡴࡡ࡮ࡧࢀࠤࡨࡵ࡭࡮ࡣࡱࡨࡤࡴࡡ࡮ࡧࡀࠦᑥ") + str(command_name) + bstack1lll11l_opy_ (u"ࠢࠣᑦ"))
                return
            self.logger.info(bstack1lll11l_opy_ (u"ࠣࡴࡸࡲࡳ࡯࡮ࡨࠢࡾࡰࡪࡴࠨࡴࡥࡵ࡭ࡵࡺࡳࡠࡶࡲࡣࡷࡻ࡮ࠪࡿࠣࡷࡨࡸࡩࡱࡶࡶࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟࡯ࡣࡰࡩࡂࢁࡦ࠯ࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦࡿࠣࡧࡴࡳ࡭ࡢࡰࡧࡣࡳࡧ࡭ࡦ࠿ࠥᑧ") + str(command_name) + bstack1lll11l_opy_ (u"ࠤࠥᑨ"))
            scripts = [(s, bstack1l1111llll1_opy_[s]) for s in scripts_to_run if s in bstack1l1111llll1_opy_]
            for script_name, bstack1lll1l111l1_opy_ in scripts:
                try:
                    bstack11ll11l1l_opy_ = datetime.now()
                    if script_name == bstack1lll11l_opy_ (u"ࠥࡷࡨࡧ࡮ࠣᑩ"):
                        result = self.perform_scan(driver, method=command_name, framework_name=f.framework_name)
                    instance.bstack111l1l1l1l_opy_(bstack1lll11l_opy_ (u"ࠦࡦ࠷࠱ࡺ࠼ࠥᑪ") + script_name, datetime.now() - bstack11ll11l1l_opy_)
                    if isinstance(result, dict) and not result.get(bstack1lll11l_opy_ (u"ࠧࡹࡵࡤࡥࡨࡷࡸࠨᑫ"), True):
                        self.logger.warning(bstack1lll11l_opy_ (u"ࠨࡳ࡬࡫ࡳࠤࡪࡾࡥࡤࡷࡷ࡭ࡳ࡭ࠠࡳࡧࡰࡥ࡮ࡴࡩ࡯ࡩࠣࡷࡨࡸࡩࡱࡶࡶ࠾ࠥࠨᑬ") + str(result) + bstack1lll11l_opy_ (u"ࠢࠣᑭ"))
                        break
                except Exception as e:
                    self.logger.error(bstack1lll11l_opy_ (u"ࠣࡧࡵࡶࡴࡸࠠࡦࡺࡨࡧࡺࡺࡩ࡯ࡩࠣࡷࡨࡸࡩࡱࡶࡀࡿࡸࡩࡲࡪࡲࡷࡣࡳࡧ࡭ࡦࡿࠣࡩࡷࡸ࡯ࡳ࠿ࠥᑮ") + str(e) + bstack1lll11l_opy_ (u"ࠤࠥᑯ"))
        except Exception as e:
            self.logger.error(bstack1lll11l_opy_ (u"ࠥࡳࡳࡥࡢࡦࡨࡲࡶࡪࡥࡥࡹࡧࡦࡹࡹ࡫ࠠࡦࡴࡵࡳࡷࡃࠢᑰ") + str(e) + bstack1lll11l_opy_ (u"ࠦࠧᑱ"))
    def bstack1lll1lll1ll_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll111111_opy_,
        bstack1lllll1l111_opy_: Tuple[bstack1lll1l11lll_opy_, bstack1lll11lll11_opy_],
        *args,
        **kwargs,
    ):
        tags = self._1l1111lll11_opy_(instance, args)
        capabilities = self.bstack1l11l11l111_opy_.bstack1lll1ll1l1l_opy_(f, instance, bstack1lllll1l111_opy_, *args, **kwargs)
        self.accessibility = self.bstack1l1111l1lll_opy_(tags, capabilities)
        if not self.accessibility:
            self.logger.debug(bstack1lll11l_opy_ (u"ࠧࡵ࡮ࡠࡣࡩࡸࡪࡸ࡟ࡵࡧࡶࡸ࠿ࠦࡡ࠲࠳ࡼࠤࡳࡵࡴࠡࡧࡱࡥࡧࡲࡥࡥࠤᑲ"))
            return
        driver = self.bstack1l11l11l111_opy_.bstack1lll1l11111_opy_(f, instance, bstack1lllll1l111_opy_, *args, **kwargs)
        test_name = f.get_state(instance, TestFramework.bstack1l1lll1l1ll_opy_)
        if not test_name:
            self.logger.debug(bstack1lll11l_opy_ (u"ࠨ࡯࡯ࡡࡤࡪࡹ࡫ࡲࡠࡶࡨࡷࡹࡀࠠ࡮࡫ࡶࡷ࡮ࡴࡧࠡࡶࡨࡷࡹࠦ࡮ࡢ࡯ࡨࠦᑳ"))
            return
        test_uuid = f.get_state(instance, TestFramework.bstack1lll11ll11l_opy_)
        if not test_uuid:
            self.logger.debug(bstack1lll11l_opy_ (u"ࠢࡰࡰࡢࡥ࡫ࡺࡥࡳࡡࡷࡩࡸࡺ࠺ࠡ࡯࡬ࡷࡸ࡯࡮ࡨࠢࡷࡩࡸࡺࠠࡶࡷ࡬ࡨࠧᑴ"))
            return
        if isinstance(self.bstack1l11l11l111_opy_, bstack1lll1ll11l1_opy_):
            framework_name = bstack1lll11l_opy_ (u"ࠨࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠬᑵ")
        else:
            framework_name = bstack1lll11l_opy_ (u"ࠩࡶࡩࡱ࡫࡮ࡪࡷࡰࠫᑶ")
        self.bstack111lll11_opy_(driver, test_name, framework_name, test_uuid)
    def perform_scan(self, driver: object, method: Union[None, str], framework_name: str):
        bstack1ll111111l1_opy_ = bstack1llll1l1l1l_opy_.bstack1ll111l1ll1_opy_(EVENTS.bstack1l11111ll1_opy_.value)
        if not self.accessibility:
            self.logger.debug(bstack1lll11l_opy_ (u"ࠥࡴࡪࡸࡦࡰࡴࡰࡣࡸࡩࡡ࡯࠼ࠣࡥ࠶࠷ࡹࠡࡰࡲࡸࠥ࡫࡮ࡢࡤ࡯ࡩࡩࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫࠽ࡼࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦࡿࠣࠦᑷ"))
            return
        bstack11ll11l1l_opy_ = datetime.now()
        bstack1lll1l111l1_opy_ = self.scripts.get(framework_name, {}).get(bstack1lll11l_opy_ (u"ࠦࡸࡩࡡ࡯ࠤᑸ"), None)
        if not bstack1lll1l111l1_opy_:
            self.logger.debug(bstack1lll11l_opy_ (u"ࠧࡶࡥࡳࡨࡲࡶࡲࡥࡳࡤࡣࡱ࠾ࠥࡳࡩࡴࡵ࡬ࡲ࡬ࠦࠧࡴࡥࡤࡲࠬࠦࡳࡤࡴ࡬ࡴࡹࠦࡦࡰࡴࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥ࡮ࡢ࡯ࡨࡁࠧᑹ") + str(framework_name) + bstack1lll11l_opy_ (u"ࠨࠠࠣᑺ"))
            return
        if self.bstack1l111ll1l11_opy_:
            arg = dict()
            arg[bstack1lll11l_opy_ (u"ࠢ࡮ࡧࡷ࡬ࡴࡪࠢᑻ")] = method if method else bstack1lll11l_opy_ (u"ࠣࠤᑼ")
            arg[bstack1lll11l_opy_ (u"ࠤࡷ࡬࡙࡫ࡳࡵࡔࡸࡲ࡚ࡻࡩࡥࠤᑽ")] = self.bstack1l11111ll11_opy_[bstack1lll11l_opy_ (u"ࠥࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠥᑾ")]
            arg[bstack1lll11l_opy_ (u"ࠦࡹ࡮ࡂࡶ࡫࡯ࡨ࡚ࡻࡩࡥࠤᑿ")] = self.bstack1l11111ll11_opy_[bstack1lll11l_opy_ (u"ࠧࡺࡥࡴࡶ࡫ࡹࡧࡥࡢࡶ࡫࡯ࡨࡤࡻࡵࡪࡦࠥᒀ")]
            arg[bstack1lll11l_opy_ (u"ࠨࡡࡶࡶ࡫ࡌࡪࡧࡤࡦࡴࠥᒁ")] = self.bstack1l11111ll11_opy_[bstack1lll11l_opy_ (u"ࠢࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡔࡰ࡭ࡨࡲࠧᒂ")]
            arg[bstack1lll11l_opy_ (u"ࠣࡶ࡫ࡎࡼࡺࡔࡰ࡭ࡨࡲࠧᒃ")] = self.bstack1l11111ll11_opy_[bstack1lll11l_opy_ (u"ࠤࡷ࡬ࡤࡰࡷࡵࡡࡷࡳࡰ࡫࡮ࠣᒄ")]
            arg[bstack1lll11l_opy_ (u"ࠥࡷࡨࡧ࡮ࡕ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠥᒅ")] = str(int(datetime.now().timestamp() * 1000))
            bstack1l1111lllll_opy_ = self.bstack1l111l111ll_opy_(bstack1lll11l_opy_ (u"ࠦࡸࡩࡡ࡯ࠤᒆ"), self.bstack1l11111ll11_opy_[bstack1lll11l_opy_ (u"ࠧࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠧᒇ")])
            if bstack1lll11l_opy_ (u"ࠨࡣࡦࡰࡷࡶࡦࡲࡁࡶࡶ࡫ࡘࡴࡱࡥ࡯ࠤᒈ") in bstack1l1111lllll_opy_:
                bstack1l1111lllll_opy_ = bstack1l1111lllll_opy_.copy()
                bstack1l1111lllll_opy_[bstack1lll11l_opy_ (u"ࠢࡤࡧࡱࡸࡷࡧ࡬ࡂࡷࡷ࡬ࡍ࡫ࡡࡥࡧࡵࠦᒉ")] = bstack1l1111lllll_opy_.pop(bstack1lll11l_opy_ (u"ࠣࡥࡨࡲࡹࡸࡡ࡭ࡃࡸࡸ࡭࡚࡯࡬ࡧࡱࠦᒊ"))
            arg = bstack1l111l1ll11_opy_(arg, bstack1l1111lllll_opy_)
            bstack1l111l111l1_opy_ = bstack1lll1l111l1_opy_ % json.dumps(arg)
            driver.execute_script(bstack1l111l111l1_opy_)
            return
        instance = bstack1lll111lll1_opy_.bstack1ll1l1ll111_opy_(driver)
        if instance:
            if not bstack1lll111lll1_opy_.get_state(instance, bstack1l11ll1ll1l_opy_.bstack1l11111l111_opy_, False):
                bstack1lll111lll1_opy_.bstack1llll1ll11l_opy_(instance, bstack1l11ll1ll1l_opy_.bstack1l11111l111_opy_, True)
            else:
                self.logger.info(bstack1lll11l_opy_ (u"ࠤࡳࡩࡷ࡬࡯ࡳ࡯ࡢࡷࡨࡧ࡮࠻ࠢࡤࡰࡷ࡫ࡡࡥࡻࠣ࡭ࡳࠦࡰࡳࡱࡪࡶࡪࡹࡳࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦ࠿ࡾࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥ࡮ࡢ࡯ࡨࢁࠥࡳࡥࡵࡪࡲࡨࡂࠨᒋ") + str(method) + bstack1lll11l_opy_ (u"ࠥࠦᒌ"))
                return
        self.logger.info(bstack1lll11l_opy_ (u"ࠦࡵ࡫ࡲࡧࡱࡵࡱࡤࡹࡣࡢࡰ࠽ࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟࡯ࡣࡰࡩࡂࢁࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫ࡽࠡ࡯ࡨࡸ࡭ࡵࡤ࠾ࠤᒍ") + str(method) + bstack1lll11l_opy_ (u"ࠧࠨᒎ"))
        if framework_name == bstack1lll11l_opy_ (u"࠭ࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠪᒏ"):
            result = self.bstack1l11l11l111_opy_.bstack1lll1ll111l_opy_(driver, bstack1lll1l111l1_opy_)
        else:
            result = driver.execute_async_script(bstack1lll1l111l1_opy_, {bstack1lll11l_opy_ (u"ࠢ࡮ࡧࡷ࡬ࡴࡪࠢᒐ"): method if method else bstack1lll11l_opy_ (u"ࠣࠤᒑ")})
        bstack1llll1l1l1l_opy_.end(EVENTS.bstack1l11111ll1_opy_.value, bstack1ll111111l1_opy_+bstack1lll11l_opy_ (u"ࠤ࠽ࡷࡹࡧࡲࡵࠤᒒ"), bstack1ll111111l1_opy_+bstack1lll11l_opy_ (u"ࠥ࠾ࡪࡴࡤࠣᒓ"), True, None, command=method)
        if instance:
            bstack1lll111lll1_opy_.bstack1llll1ll11l_opy_(instance, bstack1l11ll1ll1l_opy_.bstack1l11111l111_opy_, False)
            instance.bstack111l1l1l1l_opy_(bstack1lll11l_opy_ (u"ࠦࡦ࠷࠱ࡺ࠼ࡳࡩࡷ࡬࡯ࡳ࡯ࡢࡷࡨࡧ࡮ࠣᒔ"), datetime.now() - bstack11ll11l1l_opy_)
        return result
        def bstack1l11111l1l1_opy_(self, driver: object, framework_name, bstack111l11l111_opy_: str):
            self.bstack1llllll1lll_opy_()
            req = structs.AccessibilityResultRequest()
            req.bin_session_id = self.bin_session_id
            req.bstack1l1111l1l1l_opy_ = self.bstack1l11111ll11_opy_[bstack1lll11l_opy_ (u"ࠧࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠧᒕ")]
            req.bstack111l11l111_opy_ = bstack111l11l111_opy_
            req.session_id = self.bin_session_id
            try:
                r = self.bstack1llll11l11l_opy_.AccessibilityResult(req)
                if not r.success:
                    self.logger.debug(bstack1lll11l_opy_ (u"ࠨࡲࡦࡥࡨ࡭ࡻ࡫ࡤࠡࡨࡵࡳࡲࠦࡳࡦࡴࡹࡩࡷࡀࠠࠣᒖ") + str(r) + bstack1lll11l_opy_ (u"ࠢࠣᒗ"))
                else:
                    bstack1l111l1ll1l_opy_ = json.loads(r.bstack1l11111lll1_opy_.decode(bstack1lll11l_opy_ (u"ࠨࡷࡷࡪ࠲࠾ࠧᒘ")))
                    if bstack111l11l111_opy_ == bstack1lll11l_opy_ (u"ࠩࡪࡩࡹࡘࡥࡴࡷ࡯ࡸࡸ࠭ᒙ"):
                        return bstack1l111l1ll1l_opy_.get(bstack1lll11l_opy_ (u"ࠥࡨࡦࡺࡡࠣᒚ"), [])
                    else:
                        return bstack1l111l1ll1l_opy_.get(bstack1lll11l_opy_ (u"ࠦࡩࡧࡴࡢࠤᒛ"), {})
            except grpc.RpcError as e:
                self.logger.error(bstack1lll11l_opy_ (u"ࠧࡸࡰࡤ࠯ࡨࡶࡷࡵࡲࠡࡹ࡫࡭ࡱ࡫ࠠࡧࡧࡷࡧ࡭࡯࡮ࡨࠢࡪࡩࡹࡥࡡࡱࡲࡢࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡢࡶࡪࡹࡵ࡭ࡶࠣࡪࡷࡵ࡭ࠡࡥ࡯࡭࠿ࠦࠢᒜ") + str(e) + bstack1lll11l_opy_ (u"ࠨࠢᒝ"))
    @measure(event_name=EVENTS.bstack11l1111l1_opy_, stage=STAGE.bstack1ll1l1l11_opy_)
    def get_accessibility_results(self, driver: object, framework_name):
        if not self.accessibility:
            self.logger.debug(bstack1lll11l_opy_ (u"ࠢࡨࡧࡷࡣࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡣࡷ࡫ࡳࡶ࡮ࡷࡷ࠿ࠦࡡ࠲࠳ࡼࠤࡳࡵࡴࠡࡧࡱࡥࡧࡲࡥࡥࠤᒞ"))
            return
        if self.bstack1l111ll1l11_opy_:
            self.logger.debug(bstack1lll11l_opy_ (u"ࠨࡒࡨࡶ࡫ࡵࡲ࡮࡫ࡱ࡫ࠥࡹࡣࡢࡰࠣࡪࡴࡸࠠࡢࡲࡳࠤࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫᒟ"))
            self.perform_scan(driver, method=None, framework_name=framework_name)
            return self.bstack1l11111l1l1_opy_(driver, framework_name, bstack1lll11l_opy_ (u"ࠤࡪࡩࡹࡘࡥࡴࡷ࡯ࡸࡸࠨᒠ"))
        bstack1lll1l111l1_opy_ = self.scripts.get(framework_name, {}).get(bstack1lll11l_opy_ (u"ࠥ࡫ࡪࡺࡒࡦࡵࡸࡰࡹࡹࠢᒡ"), None)
        if not bstack1lll1l111l1_opy_:
            self.logger.debug(bstack1lll11l_opy_ (u"ࠦࡲ࡯ࡳࡴ࡫ࡱ࡫ࠥ࠭ࡧࡦࡶࡕࡩࡸࡻ࡬ࡵࡵࠪࠤࡸࡩࡲࡪࡲࡷࠤ࡫ࡵࡲࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦ࠿ࠥᒢ") + str(framework_name) + bstack1lll11l_opy_ (u"ࠧࠨᒣ"))
            return
        self.perform_scan(driver, method=None, framework_name=framework_name)
        bstack11ll11l1l_opy_ = datetime.now()
        if framework_name == bstack1lll11l_opy_ (u"࠭ࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠪᒤ"):
            result = self.bstack1l11l11l111_opy_.bstack1lll1ll111l_opy_(driver, bstack1lll1l111l1_opy_)
        else:
            result = driver.execute_async_script(bstack1lll1l111l1_opy_)
        instance = bstack1lll111lll1_opy_.bstack1ll1l1ll111_opy_(driver)
        if instance:
            instance.bstack111l1l1l1l_opy_(bstack1lll11l_opy_ (u"ࠢࡢ࠳࠴ࡽ࠿࡭ࡥࡵࡡࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡡࡵࡩࡸࡻ࡬ࡵࡵࠥᒥ"), datetime.now() - bstack11ll11l1l_opy_)
        return result
    @measure(event_name=EVENTS.bstack111111111_opy_, stage=STAGE.bstack1ll1l1l11_opy_)
    def get_accessibility_results_summary(self, driver: object, framework_name):
        if not self.accessibility:
            self.logger.debug(bstack1lll11l_opy_ (u"ࠣࡩࡨࡸࡤࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡤࡸࡥࡴࡷ࡯ࡸࡸࡥࡳࡶ࡯ࡰࡥࡷࡿ࠺ࠡࡣ࠴࠵ࡾࠦ࡮ࡰࡶࠣࡩࡳࡧࡢ࡭ࡧࡧࠦᒦ"))
            return
        if self.bstack1l111ll1l11_opy_:
            self.perform_scan(driver, method=None, framework_name=framework_name)
            return self.bstack1l11111l1l1_opy_(driver, framework_name, bstack1lll11l_opy_ (u"ࠩࡪࡩࡹࡘࡥࡴࡷ࡯ࡸࡸ࡙ࡵ࡮࡯ࡤࡶࡾ࠭ᒧ"))
        bstack1lll1l111l1_opy_ = self.scripts.get(framework_name, {}).get(bstack1lll11l_opy_ (u"ࠥ࡫ࡪࡺࡒࡦࡵࡸࡰࡹࡹࡓࡶ࡯ࡰࡥࡷࡿࠢᒨ"), None)
        if not bstack1lll1l111l1_opy_:
            self.logger.debug(bstack1lll11l_opy_ (u"ࠦࡲ࡯ࡳࡴ࡫ࡱ࡫ࠥ࠭ࡧࡦࡶࡕࡩࡸࡻ࡬ࡵࡵࡖࡹࡲࡳࡡࡳࡻࠪࠤࡸࡩࡲࡪࡲࡷࠤ࡫ࡵࡲࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦ࠿ࠥᒩ") + str(framework_name) + bstack1lll11l_opy_ (u"ࠧࠨᒪ"))
            return
        self.perform_scan(driver, method=None, framework_name=framework_name)
        bstack11ll11l1l_opy_ = datetime.now()
        if framework_name == bstack1lll11l_opy_ (u"࠭ࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠪᒫ"):
            result = self.bstack1l11l11l111_opy_.bstack1lll1ll111l_opy_(driver, bstack1lll1l111l1_opy_)
        else:
            result = driver.execute_async_script(bstack1lll1l111l1_opy_)
        instance = bstack1lll111lll1_opy_.bstack1ll1l1ll111_opy_(driver)
        if instance:
            instance.bstack111l1l1l1l_opy_(bstack1lll11l_opy_ (u"ࠢࡢ࠳࠴ࡽ࠿࡭ࡥࡵࡡࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡡࡵࡩࡸࡻ࡬ࡵࡵࡢࡷࡺࡳ࡭ࡢࡴࡼࠦᒬ"), datetime.now() - bstack11ll11l1l_opy_)
        return result
    @measure(event_name=EVENTS.bstack1l111l11111_opy_, stage=STAGE.bstack1ll1l1l11_opy_)
    def bstack1l111l1llll_opy_(
        self,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        hub_url: str,
    ):
        self.bstack1llllll1lll_opy_()
        req = structs.AccessibilityConfigRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.hub_url = hub_url
        try:
            r = self.bstack1llll11l11l_opy_.AccessibilityConfig(req)
            if not r.success:
                self.logger.debug(bstack1lll11l_opy_ (u"ࠣࡴࡨࡧࡪ࡯ࡶࡦࡦࠣࡪࡷࡵ࡭ࠡࡵࡨࡶࡻ࡫ࡲ࠻ࠢࠥᒭ") + str(r) + bstack1lll11l_opy_ (u"ࠤࠥᒮ"))
            else:
                self.bstack1l111ll1111_opy_(framework_name, r)
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1lll11l_opy_ (u"ࠥࡶࡵࡩ࠭ࡦࡴࡵࡳࡷࡀࠠࠣᒯ") + str(e) + bstack1lll11l_opy_ (u"ࠦࠧᒰ"))
            traceback.print_exc()
            raise e
    def bstack1l111ll1111_opy_(self, framework_name: str, result: structs.AccessibilityConfigResponse) -> bool:
        if not result.success or not result.accessibility.success:
            self.logger.debug(bstack1lll11l_opy_ (u"ࠧࡲ࡯ࡢࡦࡢࡧࡴࡴࡦࡪࡩ࠽ࠤࡦ࠷࠱ࡺࠢࡱࡳࡹࠦࡦࡰࡷࡱࡨࠧᒱ"))
            return False
        if result.accessibility.is_app_accessibility:
            self.bstack1l111ll1l11_opy_ = result.accessibility.is_app_accessibility
        if result.testhub.build_hashed_id:
            self.bstack1l11111ll11_opy_[bstack1lll11l_opy_ (u"ࠨࡴࡦࡵࡷ࡬ࡺࡨ࡟ࡣࡷ࡬ࡰࡩࡥࡵࡶ࡫ࡧࠦᒲ")] = result.testhub.build_hashed_id
        if result.testhub.jwt:
            self.bstack1l11111ll11_opy_[bstack1lll11l_opy_ (u"ࠢࡵࡪࡢ࡮ࡼࡺ࡟ࡵࡱ࡮ࡩࡳࠨᒳ")] = result.testhub.jwt
        if result.accessibility.options:
            options = result.accessibility.options
            if options.capabilities:
                for caps in options.capabilities:
                    self.bstack1l11111ll11_opy_[caps.name] = caps.value
            if options.scripts:
                self.scripts[framework_name] = {row.name: row.command for row in options.scripts}
            if options.commands_to_wrap and options.commands_to_wrap.commands:
                scripts_to_run = [s for s in options.commands_to_wrap.scripts_to_run]
                if not scripts_to_run:
                    return False
                bstack1l111ll11ll_opy_ = dict()
                for command in options.commands_to_wrap.commands:
                    if command.library == self.bstack1l11111llll_opy_ and command.module == self.bstack1l111l1lll1_opy_:
                        if command.method and not command.method in bstack1l111ll11ll_opy_:
                            bstack1l111ll11ll_opy_[command.method] = dict()
                        if command.name and not command.name in bstack1l111ll11ll_opy_[command.method]:
                            bstack1l111ll11ll_opy_[command.method][command.name] = list()
                        bstack1l111ll11ll_opy_[command.method][command.name].extend(scripts_to_run)
                self.commands[framework_name] = bstack1l111ll11ll_opy_
        return bool(self.commands.get(framework_name, None))
    def bstack1l11111l1ll_opy_(
        self,
        f: bstack1llllll1ll1_opy_,
        exec: Tuple[bstack1lllllll11l_opy_, str],
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if isinstance(self.bstack1l11l11l111_opy_, bstack1lll1ll11l1_opy_) and method_name != bstack1lll11l_opy_ (u"ࠨࡥࡲࡲࡳ࡫ࡣࡵࠩᒴ"):
            return
        if bstack1lll111lll1_opy_.bstack1llll11ll11_opy_(instance, bstack1l11ll1ll1l_opy_.bstack1l1111ll1l1_opy_):
            return
        if f.bstack1llllllllll_opy_(method_name, *args):
            bstack1l1111l11ll_opy_ = False
            desired_capabilities = f.bstack1l1ll1lll1l_opy_(instance)
            if isinstance(desired_capabilities, dict):
                hub_url = f.bstack1l1lll11l11_opy_(instance)
                platform_index = f.get_state(instance, bstack1llllll1ll1_opy_.bstack1lllllllll1_opy_, 0)
                bstack1l1111l11l1_opy_ = datetime.now()
                r = self.bstack1l111l1llll_opy_(platform_index, f.framework_name, f.framework_version, hub_url)
                instance.bstack111l1l1l1l_opy_(bstack1lll11l_opy_ (u"ࠤࡪࡶࡵࡩ࠺ࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿ࡟ࡤࡱࡱࡪ࡮࡭ࠢᒵ"), datetime.now() - bstack1l1111l11l1_opy_)
                bstack1l1111l11ll_opy_ = r.success
            else:
                self.logger.error(bstack1lll11l_opy_ (u"ࠥࡱ࡮ࡹࡳࡪࡰࡪࠤࡩ࡫ࡳࡪࡴࡨࡨࠥࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࡁࠧᒶ") + str(desired_capabilities) + bstack1lll11l_opy_ (u"ࠦࠧᒷ"))
            f.bstack1llll1ll11l_opy_(instance, bstack1l11ll1ll1l_opy_.bstack1l1111ll1l1_opy_, bstack1l1111l11ll_opy_)
    def bstack111111l1l1_opy_(self, test_tags):
        bstack1l111l1llll_opy_ = self.config.get(bstack1lll11l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷࠬᒸ"))
        if not bstack1l111l1llll_opy_:
            return True
        try:
            include_tags = bstack1l111l1llll_opy_[bstack1lll11l_opy_ (u"࠭ࡩ࡯ࡥ࡯ࡹࡩ࡫ࡔࡢࡩࡶࡍࡳ࡚ࡥࡴࡶ࡬ࡲ࡬࡙ࡣࡰࡲࡨࠫᒹ")] if bstack1lll11l_opy_ (u"ࠧࡪࡰࡦࡰࡺࡪࡥࡕࡣࡪࡷࡎࡴࡔࡦࡵࡷ࡭ࡳ࡭ࡓࡤࡱࡳࡩࠬᒺ") in bstack1l111l1llll_opy_ and isinstance(bstack1l111l1llll_opy_[bstack1lll11l_opy_ (u"ࠨ࡫ࡱࡧࡱࡻࡤࡦࡖࡤ࡫ࡸࡏ࡮ࡕࡧࡶࡸ࡮ࡴࡧࡔࡥࡲࡴࡪ࠭ᒻ")], list) else []
            exclude_tags = bstack1l111l1llll_opy_[bstack1lll11l_opy_ (u"ࠩࡨࡼࡨࡲࡵࡥࡧࡗࡥ࡬ࡹࡉ࡯ࡖࡨࡷࡹ࡯࡮ࡨࡕࡦࡳࡵ࡫ࠧᒼ")] if bstack1lll11l_opy_ (u"ࠪࡩࡽࡩ࡬ࡶࡦࡨࡘࡦ࡭ࡳࡊࡰࡗࡩࡸࡺࡩ࡯ࡩࡖࡧࡴࡶࡥࠨᒽ") in bstack1l111l1llll_opy_ and isinstance(bstack1l111l1llll_opy_[bstack1lll11l_opy_ (u"ࠫࡪࡾࡣ࡭ࡷࡧࡩ࡙ࡧࡧࡴࡋࡱࡘࡪࡹࡴࡪࡰࡪࡗࡨࡵࡰࡦࠩᒾ")], list) else []
            excluded = any(tag in exclude_tags for tag in test_tags)
            included = len(include_tags) == 0 or any(tag in include_tags for tag in test_tags)
            return not excluded and included
        except Exception as error:
            self.logger.debug(bstack1lll11l_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡩ࡭ࡧࠣࡺࡦࡲࡩࡥࡣࡷ࡭ࡳ࡭ࠠࡵࡧࡶࡸࠥࡩࡡࡴࡧࠣࡪࡴࡸࠠࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡣࡧࡩࡳࡷ࡫ࠠࡴࡥࡤࡲࡳ࡯࡮ࡨ࠰ࠣࡉࡷࡸ࡯ࡳࠢ࠽ࠤࠧᒿ") + str(error))
        return False
    def bstack111l1l1111_opy_(self, caps):
        try:
            if self.bstack1l111ll1l11_opy_:
                bstack1l1111l111l_opy_ = caps.get(bstack1lll11l_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡏࡣࡰࡩࠧᓀ"))
                if bstack1l1111l111l_opy_ is not None and str(bstack1l1111l111l_opy_).lower() == bstack1lll11l_opy_ (u"ࠢࡢࡰࡧࡶࡴ࡯ࡤࠣᓁ"):
                    bstack1l1111l1ll1_opy_ = caps.get(bstack1lll11l_opy_ (u"ࠣࡣࡳࡴ࡮ࡻ࡭࠻ࡲ࡯ࡥࡹ࡬࡯ࡳ࡯࡙ࡩࡷࡹࡩࡰࡰࠥᓂ")) or caps.get(bstack1lll11l_opy_ (u"ࠤࡳࡰࡦࡺࡦࡰࡴࡰ࡚ࡪࡸࡳࡪࡱࡱࠦᓃ"))
                    if bstack1l1111l1ll1_opy_ is not None and int(bstack1l1111l1ll1_opy_) < 11:
                        self.logger.warning(bstack1lll11l_opy_ (u"ࠥࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡸ࡫࡯ࡰࠥࡸࡵ࡯ࠢࡲࡲࡱࡿࠠࡰࡰࠣࡅࡳࡪࡲࡰ࡫ࡧࠤ࠶࠷ࠠࡢࡰࡧࠤࡦࡨ࡯ࡷࡧ࠱ࠤࡈࡻࡲࡳࡧࡱࡸࠥࡶ࡬ࡢࡶࡩࡳࡷࡳࠠࡷࡧࡵࡷ࡮ࡵ࡮ࠡ࠿ࠥᓄ") + str(bstack1l1111l1ll1_opy_) + bstack1lll11l_opy_ (u"ࠦࠧᓅ"))
                        return False
                return True
            bstack1l111l1111l_opy_ = caps.get(bstack1lll11l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭ᓆ"), {}).get(bstack1lll11l_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪࡔࡡ࡮ࡧࠪᓇ"), caps.get(bstack1lll11l_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࠧᓈ"), bstack1lll11l_opy_ (u"ࠨࠩᓉ")))
            if bstack1l111l1111l_opy_:
                self.logger.warning(bstack1lll11l_opy_ (u"ࠤࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡷࡪ࡮࡯ࠤࡷࡻ࡮ࠡࡱࡱࡰࡾࠦ࡯࡯ࠢࡇࡩࡸࡱࡴࡰࡲࠣࡦࡷࡵࡷࡴࡧࡵࡷ࠳ࠨᓊ"))
                return False
            browser = caps.get(bstack1lll11l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨᓋ"), bstack1lll11l_opy_ (u"ࠫࠬᓌ")).lower()
            if browser != bstack1lll11l_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࠬᓍ"):
                self.logger.warning(bstack1lll11l_opy_ (u"ࠨࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡻ࡮ࡲ࡬ࠡࡴࡸࡲࠥࡵ࡮࡭ࡻࠣࡳࡳࠦࡃࡩࡴࡲࡱࡪࠦࡢࡳࡱࡺࡷࡪࡸࡳ࠯ࠤᓎ"))
                return False
            bstack1l111l1l111_opy_ = bstack1l111l11l1l_opy_
            if not self.config.get(bstack1lll11l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠩᓏ")) or self.config.get(bstack1lll11l_opy_ (u"ࠨࡶࡸࡶࡧࡵࡳࡤࡣ࡯ࡩࠬᓐ")):
                bstack1l111l1l111_opy_ = bstack1l11111ll1l_opy_
            browser_version = caps.get(bstack1lll11l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪᓑ"))
            if not browser_version:
                browser_version = caps.get(bstack1lll11l_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫᓒ"), {}).get(bstack1lll11l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬᓓ"), bstack1lll11l_opy_ (u"ࠬ࠭ᓔ"))
            if browser_version and browser_version != bstack1lll11l_opy_ (u"࠭࡬ࡢࡶࡨࡷࡹ࠭ᓕ") and int(browser_version.split(bstack1lll11l_opy_ (u"ࠧ࠯ࠩᓖ"))[0]) <= bstack1l111l1l111_opy_:
                self.logger.warning(bstack1lll11l_opy_ (u"ࠣࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡽࡩ࡭࡮ࠣࡶࡺࡴࠠࡰࡰ࡯ࡽࠥࡵ࡮ࠡࡅ࡫ࡶࡴࡳࡥࠡࡤࡵࡳࡼࡹࡥࡳࠢࡹࡩࡷࡹࡩࡰࡰࠣ࡫ࡷ࡫ࡡࡵࡧࡵࠤࡹ࡮ࡡ࡯ࠢࠥᓗ") + str(bstack1l111l1l111_opy_) + bstack1lll11l_opy_ (u"ࠤ࠱ࠦᓘ"))
                return False
            bstack1l1111ll11l_opy_ = caps.get(bstack1lll11l_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫᓙ"), {}).get(bstack1lll11l_opy_ (u"ࠫࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫᓚ"))
            if not bstack1l1111ll11l_opy_:
                bstack1l1111ll11l_opy_ = caps.get(bstack1lll11l_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪᓛ"), {})
            if bstack1l1111ll11l_opy_ and bstack1lll11l_opy_ (u"࠭࠭࠮ࡪࡨࡥࡩࡲࡥࡴࡵࠪᓜ") in bstack1l1111ll11l_opy_.get(bstack1lll11l_opy_ (u"ࠧࡢࡴࡪࡷࠬᓝ"), []):
                self.logger.warning(bstack1lll11l_opy_ (u"ࠣࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡽࡩ࡭࡮ࠣࡲࡴࡺࠠࡳࡷࡱࠤࡴࡴࠠ࡭ࡧࡪࡥࡨࡿࠠࡩࡧࡤࡨࡱ࡫ࡳࡴࠢࡰࡳࡩ࡫࠮ࠡࡕࡺ࡭ࡹࡩࡨࠡࡶࡲࠤࡳ࡫ࡷࠡࡪࡨࡥࡩࡲࡥࡴࡵࠣࡱࡴࡪࡥࠡࡱࡵࠤࡦࡼ࡯ࡪࡦࠣࡹࡸ࡯࡮ࡨࠢ࡫ࡩࡦࡪ࡬ࡦࡵࡶࠤࡲࡵࡤࡦ࠰ࠥᓞ"))
                return False
            return True
        except Exception as error:
            self.logger.debug(bstack1lll11l_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡸࡤࡰ࡮ࡪࡡࡵࡧࠣࡥ࠶࠷ࡹࠡࡵࡸࡴࡵࡵࡲࡵࠢ࠽ࠦᓟ") + str(error))
            return False
    def bstack1l111l11l11_opy_(self, test_uuid: str, result: structs.FetchDriverExecuteParamsEventResponse):
        bstack1l11111l11l_opy_ = {
            bstack1lll11l_opy_ (u"ࠪࡸ࡭࡚ࡥࡴࡶࡕࡹࡳ࡛ࡵࡪࡦࠪᓠ"): test_uuid,
        }
        bstack1l111l1l1ll_opy_ = {}
        if result.success:
            bstack1l111l1l1ll_opy_ = json.loads(result.accessibility_execute_params)
        return bstack1l111l1ll11_opy_(bstack1l11111l11l_opy_, bstack1l111l1l1ll_opy_)
    def bstack1l111l111ll_opy_(self, script_name: str, test_uuid: str) -> dict:
        bstack1lll11l_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࠥࠦࠠࠡࡈࡨࡸࡨ࡮ࠠࡤࡧࡱࡸࡷࡧ࡬ࠡࡣࡸࡸ࡭ࠦࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡣࡰࡰࡩ࡭࡬ࡻࡲࡢࡶ࡬ࡳࡳࠦࡦࡰࡴࠣࡸ࡭࡫ࠠࡨ࡫ࡹࡩࡳࠦࡳࡤࡴ࡬ࡴࡹࠦ࡮ࡢ࡯ࡨ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࡒࡦࡶࡸࡶࡳࡹࠠࡤࡣࡦ࡬ࡪࡪࠠࡤࡱࡱࡪ࡮࡭ࠠࡪࡨࠣࡥࡱࡸࡥࡢࡦࡼࠤ࡫࡫ࡴࡤࡪࡨࡨ࠱ࠦ࡯ࡵࡪࡨࡶࡼ࡯ࡳࡦࠢ࡯ࡳࡦࡪࡳࠡࡣࡱࡨࠥࡩࡡࡤࡪࡨࡷࠥ࡯ࡴ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࡅࡷ࡭ࡳ࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡴࡥࡵ࡭ࡵࡺ࡟࡯ࡣࡰࡩ࠿ࠦࡎࡢ࡯ࡨࠤࡴ࡬ࠠࡵࡪࡨࠤࡸࡩࡲࡪࡲࡷࠤࡹࡵࠠࡧࡧࡷࡧ࡭ࠦࡣࡰࡰࡩ࡭࡬ࠦࡦࡰࡴࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡶࡨࡷࡹࡥࡵࡶ࡫ࡧ࠾࡛ࠥࡕࡊࡆࠣࡳ࡫ࠦࡴࡩࡧࠣࡸࡪࡹࡴࠡࡴࡸࡲࠥ࡬࡯ࡳࠢࡺ࡬࡮ࡩࡨࠡࡶࡲࠤ࡫࡫ࡴࡤࡪࠣࡧࡴࡴࡦࡪࡩࠍࠤࠥࠦࠠࠡࠢࠣࠤࡗ࡫ࡴࡶࡴࡱࡷ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡩ࡯ࡣࡵ࠼ࠣࡇࡴࡴࡦࡪࡩࡸࡶࡦࡺࡩࡰࡰࠣࡨ࡮ࡩࡴࡪࡱࡱࡥࡷࡿࠬࠡࡧࡰࡴࡹࡿࠠࡥ࡫ࡦࡸࠥ࡯ࡦࠡࡧࡵࡶࡴࡸࠠࡰࡥࡦࡹࡷࡹࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦᓡ")
        try:
            if self.bstack1l1111lll1l_opy_:
                return self.bstack1l111ll11l1_opy_
            self.bstack1llllll1lll_opy_()
            req = structs.FetchDriverExecuteParamsEventRequest()
            req.bin_session_id = self.bin_session_id
            req.product = bstack1lll11l_opy_ (u"ࠧࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠧᓢ")
            req.script_name = script_name
            r = self.bstack1llll11l11l_opy_.FetchDriverExecuteParamsEvent(req)
            if r.success:
                self.bstack1l111ll11l1_opy_ = self.bstack1l111l11l11_opy_(test_uuid, r)
                self.bstack1l1111lll1l_opy_ = True
            else:
                self.logger.error(bstack1lll11l_opy_ (u"ࠨࡦࡦࡶࡦ࡬ࡈ࡫࡮ࡵࡴࡤࡰࡆࡻࡴࡩࡃ࠴࠵ࡾࡉ࡯࡯ࡨ࡬࡫࠿ࠦࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡩࡩࡹࡩࡨࠡࡦࡵ࡭ࡻ࡫ࡲࠡࡧࡻࡩࡨࡻࡴࡦࠢࡳࡥࡷࡧ࡭ࡴࠢࡩࡳࡷࠦࡻࡴࡥࡵ࡭ࡵࡺ࡟࡯ࡣࡰࡩࢂࡀࠠࠣᓣ") + str(r.error) + bstack1lll11l_opy_ (u"ࠢࠣᓤ"))
                self.bstack1l111ll11l1_opy_ = dict()
            return self.bstack1l111ll11l1_opy_
        except Exception as e:
            self.logger.error(bstack1lll11l_opy_ (u"ࠣࡨࡨࡸࡨ࡮ࡃࡦࡰࡷࡶࡦࡲࡁࡶࡶ࡫ࡅ࠶࠷ࡹࡄࡱࡱࡪ࡮࡭࠺ࠡࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤ࡫࡫ࡴࡤࡪࠣࡨࡷ࡯ࡶࡦࡴࠣࡩࡽ࡫ࡣࡶࡶࡨࠤࡵࡧࡲࡢ࡯ࡶࠤ࡫ࡵࡲࠡࡽࡶࡧࡷ࡯ࡰࡵࡡࡱࡥࡲ࡫ࡽ࠻ࠢࠥᓥ") + str(traceback.format_exc()) + bstack1lll11l_opy_ (u"ࠤࠥᓦ"))
            return dict()
    def bstack111lll11_opy_(self, driver: object, name: str, framework_name: str, test_uuid: str):
        bstack1ll111111l1_opy_ = None
        try:
            self.bstack1llllll1lll_opy_()
            req = structs.FetchDriverExecuteParamsEventRequest()
            req.bin_session_id = self.bin_session_id
            req.product = bstack1lll11l_opy_ (u"ࠥࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠥᓧ")
            req.script_name = bstack1lll11l_opy_ (u"ࠦࡸࡧࡶࡦࡔࡨࡷࡺࡲࡴࡴࠤᓨ")
            r = self.bstack1llll11l11l_opy_.FetchDriverExecuteParamsEvent(req)
            if not r.success:
                self.logger.debug(bstack1lll11l_opy_ (u"ࠧࡸࡥࡤࡧ࡬ࡺࡪࡪࠠࡥࡴ࡬ࡺࡪࡸࠠࡦࡺࡨࡧࡺࡺࡥࠡࡲࡤࡶࡦࡳࡳࠡࡨࡵࡳࡲࠦࡳࡦࡴࡹࡩࡷࡀࠠࠣᓩ") + str(r.error) + bstack1lll11l_opy_ (u"ࠨࠢᓪ"))
            else:
                bstack1l11111l11l_opy_ = self.bstack1l111l11l11_opy_(test_uuid, r)
                bstack1lll1l111l1_opy_ = r.script
            self.logger.debug(bstack1lll11l_opy_ (u"ࠧࡑࡧࡵࡪࡴࡸ࡭ࡪࡰࡪࠤࡸࡩࡡ࡯ࠢࡥࡩ࡫ࡵࡲࡦࠢࡶࡥࡻ࡯࡮ࡨࠢࡵࡩࡸࡻ࡬ࡵࡵࠪᓫ") + str(bstack1l11111l11l_opy_))
            self.perform_scan(driver, name, framework_name=framework_name)
            if not bstack1lll1l111l1_opy_:
                self.logger.debug(bstack1lll11l_opy_ (u"ࠣࡲࡨࡶ࡫ࡵࡲ࡮ࡡࡶࡧࡦࡴ࠺ࠡ࡯࡬ࡷࡸ࡯࡮ࡨࠢࠪࡷࡦࡼࡥࡓࡧࡶࡹࡱࡺࡳࠨࠢࡶࡧࡷ࡯ࡰࡵࠢࡩࡳࡷࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫࠽ࠣᓬ") + str(framework_name) + bstack1lll11l_opy_ (u"ࠤࠣࠦᓭ"))
                return
            bstack1ll111111l1_opy_ = bstack1llll1l1l1l_opy_.bstack1ll111l1ll1_opy_(EVENTS.bstack1l1111ll111_opy_.value)
            self.bstack1l1111l1111_opy_(driver, bstack1lll1l111l1_opy_, bstack1l11111l11l_opy_, framework_name)
            self.logger.info(bstack1lll11l_opy_ (u"ࠥࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡸࡪࡹࡴࡪࡰࡪࠤ࡫ࡵࡲࠡࡶ࡫࡭ࡸࠦࡴࡦࡵࡷࠤࡨࡧࡳࡦࠢ࡫ࡥࡸࠦࡥ࡯ࡦࡨࡨ࠳ࠨᓮ"))
            bstack1llll1l1l1l_opy_.end(EVENTS.bstack1l1111ll111_opy_.value, bstack1ll111111l1_opy_+bstack1lll11l_opy_ (u"ࠦ࠿ࡹࡴࡢࡴࡷࠦᓯ"), bstack1ll111111l1_opy_+bstack1lll11l_opy_ (u"ࠧࡀࡥ࡯ࡦࠥᓰ"), True, None, command=bstack1lll11l_opy_ (u"࠭ࡳࡢࡸࡨࡖࡪࡹࡵ࡭ࡶࡶࠫᓱ"),test_name=name)
        except Exception as bstack1l1111ll1ll_opy_:
            self.logger.error(bstack1lll11l_opy_ (u"ࠢࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡳࡧࡶࡹࡱࡺࡳࠡࡥࡲࡹࡱࡪࠠ࡯ࡱࡷࠤࡧ࡫ࠠࡱࡴࡲࡧࡪࡹࡳࡦࡦࠣࡪࡴࡸࠠࡵࡪࡨࠤࡹ࡫ࡳࡵࠢࡦࡥࡸ࡫࠺ࠡࠤᓲ") + bstack1lll11l_opy_ (u"ࠣࡵࡷࡶ࠭ࡶࡡࡵࡪࠬࠦᓳ") + bstack1lll11l_opy_ (u"ࠤࠣࡉࡷࡸ࡯ࡳࠢ࠽ࠦᓴ") + str(bstack1l1111ll1ll_opy_))
            bstack1llll1l1l1l_opy_.end(EVENTS.bstack1l1111ll111_opy_.value, bstack1ll111111l1_opy_+bstack1lll11l_opy_ (u"ࠥ࠾ࡸࡺࡡࡳࡶࠥᓵ"), bstack1ll111111l1_opy_+bstack1lll11l_opy_ (u"ࠦ࠿࡫࡮ࡥࠤᓶ"), False, bstack1l1111ll1ll_opy_, command=bstack1lll11l_opy_ (u"ࠬࡹࡡࡷࡧࡕࡩࡸࡻ࡬ࡵࡵࠪᓷ"),test_name=name)
    def bstack1l1111l1111_opy_(self, driver, bstack1lll1l111l1_opy_, bstack1l11111l11l_opy_, framework_name):
        if framework_name == bstack1lll11l_opy_ (u"࠭ࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠪᓸ"):
            self.bstack1l11l11l111_opy_.bstack1lll1ll111l_opy_(driver, bstack1lll1l111l1_opy_, bstack1l11111l11l_opy_)
        else:
            self.logger.debug(driver.execute_async_script(bstack1lll1l111l1_opy_, bstack1l11111l11l_opy_))
    def _1l1111lll11_opy_(self, instance: bstack1llll111111_opy_, args: Tuple) -> list:
        bstack1lll11l_opy_ (u"ࠢࠣࠤࡈࡼࡹࡸࡡࡤࡶࠣࡸࡦ࡭ࡳࠡࡤࡤࡷࡪࡪࠠࡰࡰࠣࡸ࡭࡫ࠠࡵࡧࡶࡸࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫࠯ࠤࠥࠦᓹ")
        if bstack1lll11l_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠬᓺ") in instance.bstack1l1llllll11_opy_:
            return args[2].tags if hasattr(args[2], bstack1lll11l_opy_ (u"ࠩࡷࡥ࡬ࡹࠧᓻ")) else []
        if hasattr(args[0], bstack1lll11l_opy_ (u"ࠪࡳࡼࡴ࡟࡮ࡣࡵ࡯ࡪࡸࡳࠨᓼ")):
            return [marker.name for marker in args[0].own_markers]
        return []
    def bstack1l1111l1lll_opy_(self, tags, capabilities):
        return self.bstack111111l1l1_opy_(tags) and self.bstack111l1l1111_opy_(capabilities)