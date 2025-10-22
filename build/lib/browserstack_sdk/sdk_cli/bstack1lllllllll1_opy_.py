# coding: UTF-8
import sys
bstack1l111_opy_ = sys.version_info [0] == 2
bstack11l111_opy_ = 2048
bstack1l1l_opy_ = 7
def bstack1l111ll_opy_ (bstack1llllll1_opy_):
    global bstack111l1l1_opy_
    bstack1lll111_opy_ = ord (bstack1llllll1_opy_ [-1])
    bstack1ll11l1_opy_ = bstack1llllll1_opy_ [:-1]
    bstack1l11lll_opy_ = bstack1lll111_opy_ % len (bstack1ll11l1_opy_)
    bstack11l1l1_opy_ = bstack1ll11l1_opy_ [:bstack1l11lll_opy_] + bstack1ll11l1_opy_ [bstack1l11lll_opy_:]
    if bstack1l111_opy_:
        bstack11l11l_opy_ = unicode () .join ([unichr (ord (char) - bstack11l111_opy_ - (bstack11l1l1l_opy_ + bstack1lll111_opy_) % bstack1l1l_opy_) for bstack11l1l1l_opy_, char in enumerate (bstack11l1l1_opy_)])
    else:
        bstack11l11l_opy_ = str () .join ([chr (ord (char) - bstack11l111_opy_ - (bstack11l1l1l_opy_ + bstack1lll111_opy_) % bstack1l1l_opy_) for bstack11l1l1l_opy_, char in enumerate (bstack11l1l1_opy_)])
    return eval (bstack11l11l_opy_)
from datetime import datetime
import os
import threading
from browserstack_sdk.sdk_cli.bstack1llll1l1lll_opy_ import (
    bstack1llllll1111_opy_,
    bstack1lllll11l11_opy_,
    bstack1lll111lll1_opy_,
    bstack1llll1ll111_opy_,
)
from browserstack_sdk.sdk_cli.bstack1llllll11ll_opy_ import bstack1lllllll1l1_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1llllll_opy_, bstack1lll1l1lll1_opy_, bstack1lll1l1llll_opy_
from typing import Tuple, Dict, Any, List, Union
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1lllll1llll_opy_ import bstack1lllll111l1_opy_
from browserstack_sdk.sdk_cli.bstack1lll1111111_opy_ import bstack1lll11111l1_opy_
from browserstack_sdk.sdk_cli.bstack1lll11ll11l_opy_ import bstack1lll1l11ll1_opy_
from browserstack_sdk.sdk_cli.bstack1lll1l1l111_opy_ import bstack1lll1ll11ll_opy_
from bstack_utils.helper import bstack1l1111l1lll_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
from bstack_utils.bstack111llll1l_opy_ import bstack1llll11l1ll_opy_
import grpc
import traceback
import json
class bstack1l1l111ll11_opy_(bstack1lllll111l1_opy_):
    bstack1l1ll111l11_opy_ = False
    bstack1l1111lll1l_opy_ = bstack1l111ll_opy_ (u"ࠧࡹࡥ࡭ࡧࡱ࡭ࡺࡳ࠮ࡸࡧࡥࡨࡷ࡯ࡶࡦࡴࠥᑏ")
    bstack1l111l1l1ll_opy_ = bstack1l111ll_opy_ (u"ࠨࡲࡦ࡯ࡲࡸࡪ࠴ࡷࡦࡤࡧࡶ࡮ࡼࡥࡳࠤᑐ")
    bstack1l111ll11l1_opy_ = bstack1l111ll_opy_ (u"ࠢࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿ࡟ࡪࡰ࡬ࡸࠧᑑ")
    bstack1l1111l1111_opy_ = bstack1l111ll_opy_ (u"ࠣࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡠ࡫ࡶࡣࡸࡩࡡ࡯ࡰ࡬ࡲ࡬ࠨᑒ")
    bstack1l1111ll1ll_opy_ = bstack1l111ll_opy_ (u"ࠤࡧࡶ࡮ࡼࡥࡳࡡ࡫ࡥࡸࡥࡵࡳ࡮ࠥᑓ")
    scripts: Dict[str, Dict[str, str]]
    commands: Dict[str, Dict[str, Dict[str, List[str]]]]
    def __init__(self, bstack1l1l1l111l1_opy_, bstack1ll1ll1ll11_opy_):
        super().__init__()
        self.scripts = dict()
        self.commands = dict()
        self.accessibility = False
        self.bstack1l1111l1ll1_opy_ = False
        self.bstack1l111l1lll1_opy_ = dict()
        if not self.is_enabled():
            return
        self.bstack1l11l111ll1_opy_ = bstack1ll1ll1ll11_opy_
        bstack1l1l1l111l1_opy_.bstack1lllll1l111_opy_((bstack1llllll1111_opy_.bstack1lllllll11l_opy_, bstack1lllll11l11_opy_.PRE), self.bstack1l11111lll1_opy_)
        TestFramework.bstack1lllll1l111_opy_((bstack1lll1llllll_opy_.TEST, bstack1lll1l1lll1_opy_.PRE), self.bstack1lll1lll11l_opy_)
        TestFramework.bstack1lllll1l111_opy_((bstack1lll1llllll_opy_.TEST, bstack1lll1l1lll1_opy_.POST), self.bstack1lll1l1ll1l_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1lll1lll11l_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1llll_opy_,
        bstack1lllll1l1l1_opy_: Tuple[bstack1lll1llllll_opy_, bstack1lll1l1lll1_opy_],
        *args,
        **kwargs,
    ):
        tags = self._1l1111ll11l_opy_(instance, args)
        test_framework = f.get_state(instance, TestFramework.bstack1lll11ll1l1_opy_)
        if self.bstack1l1111l1ll1_opy_:
            self.bstack1l111l1lll1_opy_[bstack1l111ll_opy_ (u"ࠥࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠥᑔ")] = f.get_state(instance, TestFramework.bstack1llll1111ll_opy_)
        if bstack1l111ll_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠨᑕ") in instance.bstack1l1llll111l_opy_:
            platform_index = f.get_state(instance, TestFramework.bstack1llll1l1l11_opy_)
            self.accessibility = self.bstack1l111l1l1l1_opy_(tags, self.config[bstack1l111ll_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨᑖ")][platform_index])
        else:
            capabilities = self.bstack1l11l111ll1_opy_.bstack1lll1l11l11_opy_(f, instance, bstack1lllll1l1l1_opy_, *args, **kwargs)
            if not capabilities:
                self.logger.debug(bstack1l111ll_opy_ (u"ࠨ࡯࡯ࡡࡥࡩ࡫ࡵࡲࡦࡡࡷࡩࡸࡺ࠺ࠡࡰࡲࠤࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠣࡪࡴࡻ࡮ࡥࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨᑗ") + str(kwargs) + bstack1l111ll_opy_ (u"ࠢࠣᑘ"))
                return
            self.accessibility = self.bstack1l111l1l1l1_opy_(tags, capabilities)
        if self.bstack1l11l111ll1_opy_.pages and self.bstack1l11l111ll1_opy_.pages.values():
            bstack1l111ll111l_opy_ = list(self.bstack1l11l111ll1_opy_.pages.values())
            if bstack1l111ll111l_opy_ and isinstance(bstack1l111ll111l_opy_[0], (list, tuple)) and bstack1l111ll111l_opy_[0]:
                bstack1l111l1llll_opy_ = bstack1l111ll111l_opy_[0][0]
                if callable(bstack1l111l1llll_opy_):
                    page = bstack1l111l1llll_opy_()
                    def bstack1lllll111l_opy_():
                        self.get_accessibility_results(page, bstack1l111ll_opy_ (u"ࠣࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠧᑙ"))
                    def bstack1l1111l111l_opy_():
                        self.get_accessibility_results_summary(page, bstack1l111ll_opy_ (u"ࠤࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠨᑚ"))
                    setattr(page, bstack1l111ll_opy_ (u"ࠥ࡫ࡪࡺࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡘࡥࡴࡷ࡯ࡸࡸࠨᑛ"), bstack1lllll111l_opy_)
                    setattr(page, bstack1l111ll_opy_ (u"ࠦ࡬࡫ࡴࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡒࡦࡵࡸࡰࡹ࡙ࡵ࡮࡯ࡤࡶࡾࠨᑜ"), bstack1l1111l111l_opy_)
        self.logger.debug(bstack1l111ll_opy_ (u"ࠧࡹࡨࡰࡷ࡯ࡨࠥࡸࡵ࡯ࠢࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡹࡥࡱࡻࡥ࠾ࠤᑝ") + str(self.accessibility) + bstack1l111ll_opy_ (u"ࠨࠢᑞ"))
    def bstack1l11111lll1_opy_(
        self,
        f: bstack1lllllll1l1_opy_,
        driver: object,
        exec: Tuple[bstack1llll1ll111_opy_, str],
        bstack1lllll1l1l1_opy_: Tuple[bstack1llllll1111_opy_, bstack1lllll11l11_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        try:
            bstack11111ll1ll_opy_ = datetime.now()
            self.bstack1l111l1ll1l_opy_(f, exec, *args, **kwargs)
            instance, method_name = exec
            instance.bstack1l111l1l11_opy_(bstack1l111ll_opy_ (u"ࠢࡢ࠳࠴ࡽ࠿࡯࡮ࡪࡶࡢࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡢࡧࡴࡴࡦࡪࡩࠥᑟ"), datetime.now() - bstack11111ll1ll_opy_)
            if (
                not f.bstack1l1lll11l1l_opy_(method_name)
                or f.bstack1l1lll11ll1_opy_(method_name, *args)
                or f.bstack1l1ll1lll1l_opy_(method_name, *args)
            ):
                return
            if not f.get_state(instance, bstack1l1l111ll11_opy_.bstack1l111ll11l1_opy_, False):
                if not bstack1l1l111ll11_opy_.bstack1l1ll111l11_opy_:
                    self.logger.warning(bstack1l111ll_opy_ (u"ࠣ࡝ࡳࡰࡦࡺࡦࡰࡴࡰࡣ࡮ࡴࡤࡦࡺࡀࠦᑠ") + str(f.platform_index) + bstack1l111ll_opy_ (u"ࠤࡠࠤࡦ࠷࠱ࡺࠢࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠡࡪࡤࡺࡪࠦ࡮ࡰࡶࠣࡦࡪ࡫࡮ࠡࡵࡨࡸࠥ࡬࡯ࡳࠢࡷ࡬࡮ࡹࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠣᑡ"))
                    bstack1l1l111ll11_opy_.bstack1l1ll111l11_opy_ = True
                return
            bstack1l1111lllll_opy_ = self.scripts.get(f.framework_name, {})
            if not bstack1l1111lllll_opy_:
                platform_index = f.get_state(instance, bstack1lllllll1l1_opy_.bstack1llll1l1l11_opy_, 0)
                self.logger.debug(bstack1l111ll_opy_ (u"ࠥࡲࡴࠦࡡ࠲࠳ࡼࠤࡸࡩࡲࡪࡲࡷࡷࠥ࡬࡯ࡳࠢࡳࡰࡦࡺࡦࡰࡴࡰࡣ࡮ࡴࡤࡦࡺࡀࡿࡵࡲࡡࡵࡨࡲࡶࡲࡥࡩ࡯ࡦࡨࡼࢂࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫࠽ࠣᑢ") + str(f.framework_name) + bstack1l111ll_opy_ (u"ࠦࠧᑣ"))
                return
            command_name = f.bstack1l1ll1ll1ll_opy_(*args)
            if not command_name:
                self.logger.debug(bstack1l111ll_opy_ (u"ࠧࡳࡩࡴࡵ࡬ࡲ࡬ࠦࡣࡰ࡯ࡰࡥࡳࡪ࡟࡯ࡣࡰࡩࠥ࡬࡯ࡳࠢࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡴࡡ࡮ࡧࡀࡿ࡫࠴ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫ࡽࠡ࡯ࡨࡸ࡭ࡵࡤࡠࡰࡤࡱࡪࡃࠢᑤ") + str(method_name) + bstack1l111ll_opy_ (u"ࠨࠢᑥ"))
                return
            bstack1l1111ll111_opy_ = f.get_state(instance, bstack1l1l111ll11_opy_.bstack1l1111ll1ll_opy_, False)
            if command_name == bstack1l111ll_opy_ (u"ࠢࡨࡧࡷࠦᑦ") and not bstack1l1111ll111_opy_:
                f.bstack1lllll1ll1l_opy_(instance, bstack1l1l111ll11_opy_.bstack1l1111ll1ll_opy_, True)
                bstack1l1111ll111_opy_ = True
            if not bstack1l1111ll111_opy_ and not self.bstack1l1111l1ll1_opy_:
                self.logger.debug(bstack1l111ll_opy_ (u"ࠣࡰࡲࠤ࡚ࡘࡌࠡ࡮ࡲࡥࡩ࡫ࡤࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦ࠿ࡾࡪ࠳࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪࢃࠠࡤࡱࡰࡱࡦࡴࡤࡠࡰࡤࡱࡪࡃࠢᑧ") + str(command_name) + bstack1l111ll_opy_ (u"ࠤࠥᑨ"))
                return
            scripts_to_run = self.commands.get(f.framework_name, {}).get(method_name, {}).get(command_name, [])
            if not scripts_to_run:
                self.logger.debug(bstack1l111ll_opy_ (u"ࠥࡲࡴࠦࡡ࠲࠳ࡼࠤࡸࡩࡲࡪࡲࡷࡷࠥ࡬࡯ࡳࠢࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡴࡡ࡮ࡧࡀࡿ࡫࠴ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫ࡽࠡࡥࡲࡱࡲࡧ࡮ࡥࡡࡱࡥࡲ࡫࠽ࠣᑩ") + str(command_name) + bstack1l111ll_opy_ (u"ࠦࠧᑪ"))
                return
            self.logger.info(bstack1l111ll_opy_ (u"ࠧࡸࡵ࡯ࡰ࡬ࡲ࡬ࠦࡻ࡭ࡧࡱࠬࡸࡩࡲࡪࡲࡷࡷࡤࡺ࡯ࡠࡴࡸࡲ࠮ࢃࠠࡴࡥࡵ࡭ࡵࡺࡳࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦ࠿ࡾࡪ࠳࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪࢃࠠࡤࡱࡰࡱࡦࡴࡤࡠࡰࡤࡱࡪࡃࠢᑫ") + str(command_name) + bstack1l111ll_opy_ (u"ࠨࠢᑬ"))
            scripts = [(s, bstack1l1111lllll_opy_[s]) for s in scripts_to_run if s in bstack1l1111lllll_opy_]
            for script_name, bstack1lll11lll1l_opy_ in scripts:
                try:
                    bstack11111ll1ll_opy_ = datetime.now()
                    if script_name == bstack1l111ll_opy_ (u"ࠢࡴࡥࡤࡲࠧᑭ"):
                        result = self.perform_scan(driver, method=command_name, framework_name=f.framework_name)
                    instance.bstack1l111l1l11_opy_(bstack1l111ll_opy_ (u"ࠣࡣ࠴࠵ࡾࡀࠢᑮ") + script_name, datetime.now() - bstack11111ll1ll_opy_)
                    if isinstance(result, dict) and not result.get(bstack1l111ll_opy_ (u"ࠤࡶࡹࡨࡩࡥࡴࡵࠥᑯ"), True):
                        self.logger.warning(bstack1l111ll_opy_ (u"ࠥࡷࡰ࡯ࡰࠡࡧࡻࡩࡨࡻࡴࡪࡰࡪࠤࡷ࡫࡭ࡢ࡫ࡱ࡭ࡳ࡭ࠠࡴࡥࡵ࡭ࡵࡺࡳ࠻ࠢࠥᑰ") + str(result) + bstack1l111ll_opy_ (u"ࠦࠧᑱ"))
                        break
                except Exception as e:
                    self.logger.error(bstack1l111ll_opy_ (u"ࠧ࡫ࡲࡳࡱࡵࠤࡪࡾࡥࡤࡷࡷ࡭ࡳ࡭ࠠࡴࡥࡵ࡭ࡵࡺ࠽ࡼࡵࡦࡶ࡮ࡶࡴࡠࡰࡤࡱࡪࢃࠠࡦࡴࡵࡳࡷࡃࠢᑲ") + str(e) + bstack1l111ll_opy_ (u"ࠨࠢᑳ"))
        except Exception as e:
            self.logger.error(bstack1l111ll_opy_ (u"ࠢࡰࡰࡢࡦࡪ࡬࡯ࡳࡧࡢࡩࡽ࡫ࡣࡶࡶࡨࠤࡪࡸࡲࡰࡴࡀࠦᑴ") + str(e) + bstack1l111ll_opy_ (u"ࠣࠤᑵ"))
    def bstack1lll1l1ll1l_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1llll_opy_,
        bstack1lllll1l1l1_opy_: Tuple[bstack1lll1llllll_opy_, bstack1lll1l1lll1_opy_],
        *args,
        **kwargs,
    ):
        tags = self._1l1111ll11l_opy_(instance, args)
        capabilities = self.bstack1l11l111ll1_opy_.bstack1lll1l11l11_opy_(f, instance, bstack1lllll1l1l1_opy_, *args, **kwargs)
        self.accessibility = self.bstack1l111l1l1l1_opy_(tags, capabilities)
        if not self.accessibility:
            self.logger.debug(bstack1l111ll_opy_ (u"ࠤࡲࡲࡤࡧࡦࡵࡧࡵࡣࡹ࡫ࡳࡵ࠼ࠣࡥ࠶࠷ࡹࠡࡰࡲࡸࠥ࡫࡮ࡢࡤ࡯ࡩࡩࠨᑶ"))
            return
        driver = self.bstack1l11l111ll1_opy_.bstack1lll1ll111l_opy_(f, instance, bstack1lllll1l1l1_opy_, *args, **kwargs)
        test_name = f.get_state(instance, TestFramework.bstack1ll11ll1lll_opy_)
        if not test_name:
            self.logger.debug(bstack1l111ll_opy_ (u"ࠥࡳࡳࡥࡡࡧࡶࡨࡶࡤࡺࡥࡴࡶ࠽ࠤࡲ࡯ࡳࡴ࡫ࡱ࡫ࠥࡺࡥࡴࡶࠣࡲࡦࡳࡥࠣᑷ"))
            return
        test_uuid = f.get_state(instance, TestFramework.bstack1llll1111ll_opy_)
        if not test_uuid:
            self.logger.debug(bstack1l111ll_opy_ (u"ࠦࡴࡴ࡟ࡢࡨࡷࡩࡷࡥࡴࡦࡵࡷ࠾ࠥࡳࡩࡴࡵ࡬ࡲ࡬ࠦࡴࡦࡵࡷࠤࡺࡻࡩࡥࠤᑸ"))
            return
        if isinstance(self.bstack1l11l111ll1_opy_, bstack1lll1l11ll1_opy_):
            framework_name = bstack1l111ll_opy_ (u"ࠬࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠩᑹ")
        else:
            framework_name = bstack1l111ll_opy_ (u"࠭ࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࠨᑺ")
        self.bstack1111111l_opy_(driver, test_name, framework_name, test_uuid)
    def perform_scan(self, driver: object, method: Union[None, str], framework_name: str):
        bstack1ll111ll111_opy_ = bstack1llll11l1ll_opy_.bstack1ll1l11l1ll_opy_(EVENTS.bstack11l1ll11l_opy_.value)
        if not self.accessibility:
            self.logger.debug(bstack1l111ll_opy_ (u"ࠢࡱࡧࡵࡪࡴࡸ࡭ࡠࡵࡦࡥࡳࡀࠠࡢ࠳࠴ࡽࠥࡴ࡯ࡵࠢࡨࡲࡦࡨ࡬ࡦࡦࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥ࡮ࡢ࡯ࡨࡁࢀ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪࢃࠠࠣᑻ"))
            return
        bstack11111ll1ll_opy_ = datetime.now()
        bstack1lll11lll1l_opy_ = self.scripts.get(framework_name, {}).get(bstack1l111ll_opy_ (u"ࠣࡵࡦࡥࡳࠨᑼ"), None)
        if not bstack1lll11lll1l_opy_:
            self.logger.debug(bstack1l111ll_opy_ (u"ࠤࡳࡩࡷ࡬࡯ࡳ࡯ࡢࡷࡨࡧ࡮࠻ࠢࡰ࡭ࡸࡹࡩ࡯ࡩࠣࠫࡸࡩࡡ࡯ࠩࠣࡷࡨࡸࡩࡱࡶࠣࡪࡴࡸࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡲࡦࡳࡥ࠾ࠤᑽ") + str(framework_name) + bstack1l111ll_opy_ (u"ࠥࠤࠧᑾ"))
            return
        if self.bstack1l1111l1ll1_opy_:
            arg = dict()
            arg[bstack1l111ll_opy_ (u"ࠦࡲ࡫ࡴࡩࡱࡧࠦᑿ")] = method if method else bstack1l111ll_opy_ (u"ࠧࠨᒀ")
            arg[bstack1l111ll_opy_ (u"ࠨࡴࡩࡖࡨࡷࡹࡘࡵ࡯ࡗࡸ࡭ࡩࠨᒁ")] = self.bstack1l111l1lll1_opy_[bstack1l111ll_opy_ (u"ࠢࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠢᒂ")]
            arg[bstack1l111ll_opy_ (u"ࠣࡶ࡫ࡆࡺ࡯࡬ࡥࡗࡸ࡭ࡩࠨᒃ")] = self.bstack1l111l1lll1_opy_[bstack1l111ll_opy_ (u"ࠤࡷࡩࡸࡺࡨࡶࡤࡢࡦࡺ࡯࡬ࡥࡡࡸࡹ࡮ࡪࠢᒄ")]
            arg[bstack1l111ll_opy_ (u"ࠥࡥࡺࡺࡨࡉࡧࡤࡨࡪࡸࠢᒅ")] = self.bstack1l111l1lll1_opy_[bstack1l111ll_opy_ (u"ࠦࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡘࡴࡱࡥ࡯ࠤᒆ")]
            arg[bstack1l111ll_opy_ (u"ࠧࡺࡨࡋࡹࡷࡘࡴࡱࡥ࡯ࠤᒇ")] = self.bstack1l111l1lll1_opy_[bstack1l111ll_opy_ (u"ࠨࡴࡩࡡ࡭ࡻࡹࡥࡴࡰ࡭ࡨࡲࠧᒈ")]
            arg[bstack1l111ll_opy_ (u"ࠢࡴࡥࡤࡲ࡙࡯࡭ࡦࡵࡷࡥࡲࡶࠢᒉ")] = str(int(datetime.now().timestamp() * 1000))
            bstack1l111l1ll11_opy_ = bstack1lll11lll1l_opy_ % json.dumps(arg)
            driver.execute_script(bstack1l111l1ll11_opy_)
            return
        instance = bstack1lll111lll1_opy_.bstack1ll11lll111_opy_(driver)
        if instance:
            if not bstack1lll111lll1_opy_.get_state(instance, bstack1l1l111ll11_opy_.bstack1l1111l1111_opy_, False):
                bstack1lll111lll1_opy_.bstack1lllll1ll1l_opy_(instance, bstack1l1l111ll11_opy_.bstack1l1111l1111_opy_, True)
            else:
                self.logger.info(bstack1l111ll_opy_ (u"ࠣࡲࡨࡶ࡫ࡵࡲ࡮ࡡࡶࡧࡦࡴ࠺ࠡࡣ࡯ࡶࡪࡧࡤࡺࠢ࡬ࡲࠥࡶࡲࡰࡩࡵࡩࡸࡹࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡲࡦࡳࡥ࠾ࡽࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡴࡡ࡮ࡧࢀࠤࡲ࡫ࡴࡩࡱࡧࡁࠧᒊ") + str(method) + bstack1l111ll_opy_ (u"ࠤࠥᒋ"))
                return
        self.logger.info(bstack1l111ll_opy_ (u"ࠥࡴࡪࡸࡦࡰࡴࡰࡣࡸࡩࡡ࡯࠼ࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥ࡮ࡢ࡯ࡨࡁࢀ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪࢃࠠ࡮ࡧࡷ࡬ࡴࡪ࠽ࠣᒌ") + str(method) + bstack1l111ll_opy_ (u"ࠦࠧᒍ"))
        if framework_name == bstack1l111ll_opy_ (u"ࠬࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠩᒎ"):
            result = self.bstack1l11l111ll1_opy_.bstack1lll1l11lll_opy_(driver, bstack1lll11lll1l_opy_)
        else:
            result = driver.execute_async_script(bstack1lll11lll1l_opy_, {bstack1l111ll_opy_ (u"ࠨ࡭ࡦࡶ࡫ࡳࡩࠨᒏ"): method if method else bstack1l111ll_opy_ (u"ࠢࠣᒐ")})
        bstack1llll11l1ll_opy_.end(EVENTS.bstack11l1ll11l_opy_.value, bstack1ll111ll111_opy_+bstack1l111ll_opy_ (u"ࠣ࠼ࡶࡸࡦࡸࡴࠣᒑ"), bstack1ll111ll111_opy_+bstack1l111ll_opy_ (u"ࠤ࠽ࡩࡳࡪࠢᒒ"), True, None, command=method)
        if instance:
            bstack1lll111lll1_opy_.bstack1lllll1ll1l_opy_(instance, bstack1l1l111ll11_opy_.bstack1l1111l1111_opy_, False)
            instance.bstack1l111l1l11_opy_(bstack1l111ll_opy_ (u"ࠥࡥ࠶࠷ࡹ࠻ࡲࡨࡶ࡫ࡵࡲ࡮ࡡࡶࡧࡦࡴࠢᒓ"), datetime.now() - bstack11111ll1ll_opy_)
        return result
        def bstack1l111l1l111_opy_(self, driver: object, framework_name, bstack1l1lll1lll_opy_: str):
            self.bstack1lllll1111l_opy_()
            req = structs.AccessibilityResultRequest()
            req.bin_session_id = self.bin_session_id
            req.bstack1l11111ll1l_opy_ = self.bstack1l111l1lll1_opy_[bstack1l111ll_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠦᒔ")]
            req.bstack1l1lll1lll_opy_ = bstack1l1lll1lll_opy_
            req.session_id = self.bin_session_id
            try:
                r = self.bstack1lllll1lll1_opy_.AccessibilityResult(req)
                if not r.success:
                    self.logger.debug(bstack1l111ll_opy_ (u"ࠧࡸࡥࡤࡧ࡬ࡺࡪࡪࠠࡧࡴࡲࡱࠥࡹࡥࡳࡸࡨࡶ࠿ࠦࠢᒕ") + str(r) + bstack1l111ll_opy_ (u"ࠨࠢᒖ"))
                else:
                    bstack1l11111l1ll_opy_ = json.loads(r.bstack1l1111lll11_opy_.decode(bstack1l111ll_opy_ (u"ࠧࡶࡶࡩ࠱࠽࠭ᒗ")))
                    if bstack1l1lll1lll_opy_ == bstack1l111ll_opy_ (u"ࠨࡩࡨࡸࡗ࡫ࡳࡶ࡮ࡷࡷࠬᒘ"):
                        return bstack1l11111l1ll_opy_.get(bstack1l111ll_opy_ (u"ࠤࡧࡥࡹࡧࠢᒙ"), [])
                    else:
                        return bstack1l11111l1ll_opy_.get(bstack1l111ll_opy_ (u"ࠥࡨࡦࡺࡡࠣᒚ"), {})
            except grpc.RpcError as e:
                self.logger.error(bstack1l111ll_opy_ (u"ࠦࡷࡶࡣ࠮ࡧࡵࡶࡴࡸࠠࡸࡪ࡬ࡰࡪࠦࡦࡦࡶࡦ࡬࡮ࡴࡧࠡࡩࡨࡸࡤࡧࡰࡱࡡࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡡࡵࡩࡸࡻ࡬ࡵࠢࡩࡶࡴࡳࠠࡤ࡮࡬࠾ࠥࠨᒛ") + str(e) + bstack1l111ll_opy_ (u"ࠧࠨᒜ"))
    @measure(event_name=EVENTS.bstack11l1llll11_opy_, stage=STAGE.bstack1ll11l111l_opy_)
    def get_accessibility_results(self, driver: object, framework_name):
        if not self.accessibility:
            self.logger.debug(bstack1l111ll_opy_ (u"ࠨࡧࡦࡶࡢࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡢࡶࡪࡹࡵ࡭ࡶࡶ࠾ࠥࡧ࠱࠲ࡻࠣࡲࡴࡺࠠࡦࡰࡤࡦࡱ࡫ࡤࠣᒝ"))
            return
        if self.bstack1l1111l1ll1_opy_:
            self.logger.debug(bstack1l111ll_opy_ (u"ࠧࡑࡧࡵࡪࡴࡸ࡭ࡪࡰࡪࠤࡸࡩࡡ࡯ࠢࡩࡳࡷࠦࡡࡱࡲࠣࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪᒞ"))
            self.perform_scan(driver, method=None, framework_name=framework_name)
            return self.bstack1l111l1l111_opy_(driver, framework_name, bstack1l111ll_opy_ (u"ࠣࡩࡨࡸࡗ࡫ࡳࡶ࡮ࡷࡷࠧᒟ"))
        bstack1lll11lll1l_opy_ = self.scripts.get(framework_name, {}).get(bstack1l111ll_opy_ (u"ࠤࡪࡩࡹࡘࡥࡴࡷ࡯ࡸࡸࠨᒠ"), None)
        if not bstack1lll11lll1l_opy_:
            self.logger.debug(bstack1l111ll_opy_ (u"ࠥࡱ࡮ࡹࡳࡪࡰࡪࠤࠬ࡭ࡥࡵࡔࡨࡷࡺࡲࡴࡴࠩࠣࡷࡨࡸࡩࡱࡶࠣࡪࡴࡸࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡲࡦࡳࡥ࠾ࠤᒡ") + str(framework_name) + bstack1l111ll_opy_ (u"ࠦࠧᒢ"))
            return
        self.perform_scan(driver, method=None, framework_name=framework_name)
        bstack11111ll1ll_opy_ = datetime.now()
        if framework_name == bstack1l111ll_opy_ (u"ࠬࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠩᒣ"):
            result = self.bstack1l11l111ll1_opy_.bstack1lll1l11lll_opy_(driver, bstack1lll11lll1l_opy_)
        else:
            result = driver.execute_async_script(bstack1lll11lll1l_opy_)
        instance = bstack1lll111lll1_opy_.bstack1ll11lll111_opy_(driver)
        if instance:
            instance.bstack1l111l1l11_opy_(bstack1l111ll_opy_ (u"ࠨࡡ࠲࠳ࡼ࠾࡬࡫ࡴࡠࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡠࡴࡨࡷࡺࡲࡴࡴࠤᒤ"), datetime.now() - bstack11111ll1ll_opy_)
        return result
    @measure(event_name=EVENTS.bstack1l1lllll1l_opy_, stage=STAGE.bstack1ll11l111l_opy_)
    def get_accessibility_results_summary(self, driver: object, framework_name):
        if not self.accessibility:
            self.logger.debug(bstack1l111ll_opy_ (u"ࠢࡨࡧࡷࡣࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡣࡷ࡫ࡳࡶ࡮ࡷࡷࡤࡹࡵ࡮࡯ࡤࡶࡾࡀࠠࡢ࠳࠴ࡽࠥࡴ࡯ࡵࠢࡨࡲࡦࡨ࡬ࡦࡦࠥᒥ"))
            return
        if self.bstack1l1111l1ll1_opy_:
            self.perform_scan(driver, method=None, framework_name=framework_name)
            return self.bstack1l111l1l111_opy_(driver, framework_name, bstack1l111ll_opy_ (u"ࠨࡩࡨࡸࡗ࡫ࡳࡶ࡮ࡷࡷࡘࡻ࡭࡮ࡣࡵࡽࠬᒦ"))
        bstack1lll11lll1l_opy_ = self.scripts.get(framework_name, {}).get(bstack1l111ll_opy_ (u"ࠤࡪࡩࡹࡘࡥࡴࡷ࡯ࡸࡸ࡙ࡵ࡮࡯ࡤࡶࡾࠨᒧ"), None)
        if not bstack1lll11lll1l_opy_:
            self.logger.debug(bstack1l111ll_opy_ (u"ࠥࡱ࡮ࡹࡳࡪࡰࡪࠤࠬ࡭ࡥࡵࡔࡨࡷࡺࡲࡴࡴࡕࡸࡱࡲࡧࡲࡺࠩࠣࡷࡨࡸࡩࡱࡶࠣࡪࡴࡸࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡲࡦࡳࡥ࠾ࠤᒨ") + str(framework_name) + bstack1l111ll_opy_ (u"ࠦࠧᒩ"))
            return
        self.perform_scan(driver, method=None, framework_name=framework_name)
        bstack11111ll1ll_opy_ = datetime.now()
        if framework_name == bstack1l111ll_opy_ (u"ࠬࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠩᒪ"):
            result = self.bstack1l11l111ll1_opy_.bstack1lll1l11lll_opy_(driver, bstack1lll11lll1l_opy_)
        else:
            result = driver.execute_async_script(bstack1lll11lll1l_opy_)
        instance = bstack1lll111lll1_opy_.bstack1ll11lll111_opy_(driver)
        if instance:
            instance.bstack1l111l1l11_opy_(bstack1l111ll_opy_ (u"ࠨࡡ࠲࠳ࡼ࠾࡬࡫ࡴࡠࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡠࡴࡨࡷࡺࡲࡴࡴࡡࡶࡹࡲࡳࡡࡳࡻࠥᒫ"), datetime.now() - bstack11111ll1ll_opy_)
        return result
    @measure(event_name=EVENTS.bstack1l111l11l11_opy_, stage=STAGE.bstack1ll11l111l_opy_)
    def bstack1l111l11l1l_opy_(
        self,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        hub_url: str,
    ):
        self.bstack1lllll1111l_opy_()
        req = structs.AccessibilityConfigRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.hub_url = hub_url
        try:
            r = self.bstack1lllll1lll1_opy_.AccessibilityConfig(req)
            if not r.success:
                self.logger.debug(bstack1l111ll_opy_ (u"ࠢࡳࡧࡦࡩ࡮ࡼࡥࡥࠢࡩࡶࡴࡳࠠࡴࡧࡵࡺࡪࡸ࠺ࠡࠤᒬ") + str(r) + bstack1l111ll_opy_ (u"ࠣࠤᒭ"))
            else:
                self.bstack1l1111l11l1_opy_(framework_name, r)
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1l111ll_opy_ (u"ࠤࡵࡴࡨ࠳ࡥࡳࡴࡲࡶ࠿ࠦࠢᒮ") + str(e) + bstack1l111ll_opy_ (u"ࠥࠦᒯ"))
            traceback.print_exc()
            raise e
    def bstack1l1111l11l1_opy_(self, framework_name: str, result: structs.AccessibilityConfigResponse) -> bool:
        if not result.success or not result.accessibility.success:
            self.logger.debug(bstack1l111ll_opy_ (u"ࠦࡱࡵࡡࡥࡡࡦࡳࡳ࡬ࡩࡨ࠼ࠣࡥ࠶࠷ࡹࠡࡰࡲࡸࠥ࡬࡯ࡶࡰࡧࠦᒰ"))
            return False
        if result.accessibility.is_app_accessibility:
            self.bstack1l1111l1ll1_opy_ = result.accessibility.is_app_accessibility
        if result.testhub.build_hashed_id:
            self.bstack1l111l1lll1_opy_[bstack1l111ll_opy_ (u"ࠧࡺࡥࡴࡶ࡫ࡹࡧࡥࡢࡶ࡫࡯ࡨࡤࡻࡵࡪࡦࠥᒱ")] = result.testhub.build_hashed_id
        if result.testhub.jwt:
            self.bstack1l111l1lll1_opy_[bstack1l111ll_opy_ (u"ࠨࡴࡩࡡ࡭ࡻࡹࡥࡴࡰ࡭ࡨࡲࠧᒲ")] = result.testhub.jwt
        if result.accessibility.options:
            options = result.accessibility.options
            if options.capabilities:
                for caps in options.capabilities:
                    self.bstack1l111l1lll1_opy_[caps.name] = caps.value
            if options.scripts:
                self.scripts[framework_name] = {row.name: row.command for row in options.scripts}
            if options.commands_to_wrap and options.commands_to_wrap.commands:
                scripts_to_run = [s for s in options.commands_to_wrap.scripts_to_run]
                if not scripts_to_run:
                    return False
                bstack1l111ll11ll_opy_ = dict()
                for command in options.commands_to_wrap.commands:
                    if command.library == self.bstack1l1111lll1l_opy_ and command.module == self.bstack1l111l1l1ll_opy_:
                        if command.method and not command.method in bstack1l111ll11ll_opy_:
                            bstack1l111ll11ll_opy_[command.method] = dict()
                        if command.name and not command.name in bstack1l111ll11ll_opy_[command.method]:
                            bstack1l111ll11ll_opy_[command.method][command.name] = list()
                        bstack1l111ll11ll_opy_[command.method][command.name].extend(scripts_to_run)
                self.commands[framework_name] = bstack1l111ll11ll_opy_
        return bool(self.commands.get(framework_name, None))
    def bstack1l111l1ll1l_opy_(
        self,
        f: bstack1lllllll1l1_opy_,
        exec: Tuple[bstack1llll1ll111_opy_, str],
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if isinstance(self.bstack1l11l111ll1_opy_, bstack1lll1l11ll1_opy_) and method_name != bstack1l111ll_opy_ (u"ࠧࡤࡱࡱࡲࡪࡩࡴࠨᒳ"):
            return
        if bstack1lll111lll1_opy_.bstack1llll1l1111_opy_(instance, bstack1l1l111ll11_opy_.bstack1l111ll11l1_opy_):
            return
        if f.bstack1lllllll111_opy_(method_name, *args):
            bstack1l111l111l1_opy_ = False
            desired_capabilities = f.bstack1l1ll1l1l1l_opy_(instance)
            if isinstance(desired_capabilities, dict):
                hub_url = f.bstack1l1ll1l1lll_opy_(instance)
                platform_index = f.get_state(instance, bstack1lllllll1l1_opy_.bstack1llll1l1l11_opy_, 0)
                bstack1l111l1l11l_opy_ = datetime.now()
                r = self.bstack1l111l11l1l_opy_(platform_index, f.framework_name, f.framework_version, hub_url)
                instance.bstack1l111l1l11_opy_(bstack1l111ll_opy_ (u"ࠣࡩࡵࡴࡨࡀࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡥࡣࡰࡰࡩ࡭࡬ࠨᒴ"), datetime.now() - bstack1l111l1l11l_opy_)
                bstack1l111l111l1_opy_ = r.success
            else:
                self.logger.error(bstack1l111ll_opy_ (u"ࠤࡰ࡭ࡸࡹࡩ࡯ࡩࠣࡨࡪࡹࡩࡳࡧࡧࠤࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࡀࠦᒵ") + str(desired_capabilities) + bstack1l111ll_opy_ (u"ࠥࠦᒶ"))
            f.bstack1lllll1ll1l_opy_(instance, bstack1l1l111ll11_opy_.bstack1l111ll11l1_opy_, bstack1l111l111l1_opy_)
    def bstack1ll1ll1ll_opy_(self, test_tags):
        bstack1l111l11l1l_opy_ = self.config.get(bstack1l111ll_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫᒷ"))
        if not bstack1l111l11l1l_opy_:
            return True
        try:
            include_tags = bstack1l111l11l1l_opy_[bstack1l111ll_opy_ (u"ࠬ࡯࡮ࡤ࡮ࡸࡨࡪ࡚ࡡࡨࡵࡌࡲ࡙࡫ࡳࡵ࡫ࡱ࡫ࡘࡩ࡯ࡱࡧࠪᒸ")] if bstack1l111ll_opy_ (u"࠭ࡩ࡯ࡥ࡯ࡹࡩ࡫ࡔࡢࡩࡶࡍࡳ࡚ࡥࡴࡶ࡬ࡲ࡬࡙ࡣࡰࡲࡨࠫᒹ") in bstack1l111l11l1l_opy_ and isinstance(bstack1l111l11l1l_opy_[bstack1l111ll_opy_ (u"ࠧࡪࡰࡦࡰࡺࡪࡥࡕࡣࡪࡷࡎࡴࡔࡦࡵࡷ࡭ࡳ࡭ࡓࡤࡱࡳࡩࠬᒺ")], list) else []
            exclude_tags = bstack1l111l11l1l_opy_[bstack1l111ll_opy_ (u"ࠨࡧࡻࡧࡱࡻࡤࡦࡖࡤ࡫ࡸࡏ࡮ࡕࡧࡶࡸ࡮ࡴࡧࡔࡥࡲࡴࡪ࠭ᒻ")] if bstack1l111ll_opy_ (u"ࠩࡨࡼࡨࡲࡵࡥࡧࡗࡥ࡬ࡹࡉ࡯ࡖࡨࡷࡹ࡯࡮ࡨࡕࡦࡳࡵ࡫ࠧᒼ") in bstack1l111l11l1l_opy_ and isinstance(bstack1l111l11l1l_opy_[bstack1l111ll_opy_ (u"ࠪࡩࡽࡩ࡬ࡶࡦࡨࡘࡦ࡭ࡳࡊࡰࡗࡩࡸࡺࡩ࡯ࡩࡖࡧࡴࡶࡥࠨᒽ")], list) else []
            excluded = any(tag in exclude_tags for tag in test_tags)
            included = len(include_tags) == 0 or any(tag in include_tags for tag in test_tags)
            return not excluded and included
        except Exception as error:
            self.logger.debug(bstack1l111ll_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡻ࡭࡯࡬ࡦࠢࡹࡥࡱ࡯ࡤࡢࡶ࡬ࡲ࡬ࠦࡴࡦࡵࡷࠤࡨࡧࡳࡦࠢࡩࡳࡷࠦࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡢࡦࡨࡲࡶࡪࠦࡳࡤࡣࡱࡲ࡮ࡴࡧ࠯ࠢࡈࡶࡷࡵࡲࠡ࠼ࠣࠦᒾ") + str(error))
        return False
    def bstack11ll1l11l1_opy_(self, caps):
        try:
            if self.bstack1l1111l1ll1_opy_:
                bstack1l111l11ll1_opy_ = caps.get(bstack1l111ll_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳࡎࡢ࡯ࡨࠦᒿ"))
                if bstack1l111l11ll1_opy_ is not None and str(bstack1l111l11ll1_opy_).lower() == bstack1l111ll_opy_ (u"ࠨࡡ࡯ࡦࡵࡳ࡮ࡪࠢᓀ"):
                    bstack1l1111ll1l1_opy_ = caps.get(bstack1l111ll_opy_ (u"ࠢࡢࡲࡳ࡭ࡺࡳ࠺ࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡘࡨࡶࡸ࡯࡯࡯ࠤᓁ")) or caps.get(bstack1l111ll_opy_ (u"ࠣࡲ࡯ࡥࡹ࡬࡯ࡳ࡯࡙ࡩࡷࡹࡩࡰࡰࠥᓂ"))
                    if bstack1l1111ll1l1_opy_ is not None and int(bstack1l1111ll1l1_opy_) < 11:
                        self.logger.warning(bstack1l111ll_opy_ (u"ࠤࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡷࡪ࡮࡯ࠤࡷࡻ࡮ࠡࡱࡱࡰࡾࠦ࡯࡯ࠢࡄࡲࡩࡸ࡯ࡪࡦࠣ࠵࠶ࠦࡡ࡯ࡦࠣࡥࡧࡵࡶࡦ࠰ࠣࡇࡺࡸࡲࡦࡰࡷࠤࡵࡲࡡࡵࡨࡲࡶࡲࠦࡶࡦࡴࡶ࡭ࡴࡴࠠ࠾ࠤᓃ") + str(bstack1l1111ll1l1_opy_) + bstack1l111ll_opy_ (u"ࠥࠦᓄ"))
                        return False
                return True
            bstack1l111l11lll_opy_ = caps.get(bstack1l111ll_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬᓅ"), {}).get(bstack1l111ll_opy_ (u"ࠬࡪࡥࡷ࡫ࡦࡩࡓࡧ࡭ࡦࠩᓆ"), caps.get(bstack1l111ll_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪ࠭ᓇ"), bstack1l111ll_opy_ (u"ࠧࠨᓈ")))
            if bstack1l111l11lll_opy_:
                self.logger.warning(bstack1l111ll_opy_ (u"ࠣࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡽࡩ࡭࡮ࠣࡶࡺࡴࠠࡰࡰ࡯ࡽࠥࡵ࡮ࠡࡆࡨࡷࡰࡺ࡯ࡱࠢࡥࡶࡴࡽࡳࡦࡴࡶ࠲ࠧᓉ"))
                return False
            browser = caps.get(bstack1l111ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧᓊ"), bstack1l111ll_opy_ (u"ࠪࠫᓋ")).lower()
            if browser != bstack1l111ll_opy_ (u"ࠫࡨ࡮ࡲࡰ࡯ࡨࠫᓌ"):
                self.logger.warning(bstack1l111ll_opy_ (u"ࠧࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡺ࡭ࡱࡲࠠࡳࡷࡱࠤࡴࡴ࡬ࡺࠢࡲࡲࠥࡉࡨࡳࡱࡰࡩࠥࡨࡲࡰࡹࡶࡩࡷࡹ࠮ࠣᓍ"))
                return False
            bstack1l1111llll1_opy_ = bstack1l11111llll_opy_
            if not self.config.get(bstack1l111ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠨᓎ")) or self.config.get(bstack1l111ll_opy_ (u"ࠧࡵࡷࡵࡦࡴࡹࡣࡢ࡮ࡨࠫᓏ")):
                bstack1l1111llll1_opy_ = bstack1l11111ll11_opy_
            browser_version = caps.get(bstack1l111ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩᓐ"))
            if not browser_version:
                browser_version = caps.get(bstack1l111ll_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪᓑ"), {}).get(bstack1l111ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫᓒ"), bstack1l111ll_opy_ (u"ࠫࠬᓓ"))
            if browser_version and browser_version != bstack1l111ll_opy_ (u"ࠬࡲࡡࡵࡧࡶࡸࠬᓔ") and int(browser_version.split(bstack1l111ll_opy_ (u"࠭࠮ࠨᓕ"))[0]) <= bstack1l1111llll1_opy_:
                self.logger.warning(bstack1l111ll_opy_ (u"ࠢࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤࡼ࡯࡬࡭ࠢࡵࡹࡳࠦ࡯࡯࡮ࡼࠤࡴࡴࠠࡄࡪࡵࡳࡲ࡫ࠠࡣࡴࡲࡻࡸ࡫ࡲࠡࡸࡨࡶࡸ࡯࡯࡯ࠢࡪࡶࡪࡧࡴࡦࡴࠣࡸ࡭ࡧ࡮ࠡࠤᓖ") + str(bstack1l1111llll1_opy_) + bstack1l111ll_opy_ (u"ࠣ࠰ࠥᓗ"))
                return False
            bstack1l111l11111_opy_ = caps.get(bstack1l111ll_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪᓘ"), {}).get(bstack1l111ll_opy_ (u"ࠪࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪᓙ"))
            if not bstack1l111l11111_opy_:
                bstack1l111l11111_opy_ = caps.get(bstack1l111ll_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩᓚ"), {})
            if bstack1l111l11111_opy_ and bstack1l111ll_opy_ (u"ࠬ࠳࠭ࡩࡧࡤࡨࡱ࡫ࡳࡴࠩᓛ") in bstack1l111l11111_opy_.get(bstack1l111ll_opy_ (u"࠭ࡡࡳࡩࡶࠫᓜ"), []):
                self.logger.warning(bstack1l111ll_opy_ (u"ࠢࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤࡼ࡯࡬࡭ࠢࡱࡳࡹࠦࡲࡶࡰࠣࡳࡳࠦ࡬ࡦࡩࡤࡧࡾࠦࡨࡦࡣࡧࡰࡪࡹࡳࠡ࡯ࡲࡨࡪ࠴ࠠࡔࡹ࡬ࡸࡨ࡮ࠠࡵࡱࠣࡲࡪࡽࠠࡩࡧࡤࡨࡱ࡫ࡳࡴࠢࡰࡳࡩ࡫ࠠࡰࡴࠣࡥࡻࡵࡩࡥࠢࡸࡷ࡮ࡴࡧࠡࡪࡨࡥࡩࡲࡥࡴࡵࠣࡱࡴࡪࡥ࠯ࠤᓝ"))
                return False
            return True
        except Exception as error:
            self.logger.debug(bstack1l111ll_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡷࡣ࡯࡭ࡩࡧࡴࡦࠢࡤ࠵࠶ࡿࠠࡴࡷࡳࡴࡴࡸࡴࠡ࠼ࠥᓞ") + str(error))
            return False
    def bstack1l111l1111l_opy_(self, test_uuid: str, result: structs.FetchDriverExecuteParamsEventResponse):
        bstack1l111l111ll_opy_ = {
            bstack1l111ll_opy_ (u"ࠩࡷ࡬࡙࡫ࡳࡵࡔࡸࡲ࡚ࡻࡩࡥࠩᓟ"): test_uuid,
        }
        bstack1l1111l11ll_opy_ = {}
        if result.success:
            bstack1l1111l11ll_opy_ = json.loads(result.accessibility_execute_params)
        return bstack1l1111l1lll_opy_(bstack1l111l111ll_opy_, bstack1l1111l11ll_opy_)
    def bstack1111111l_opy_(self, driver: object, name: str, framework_name: str, test_uuid: str):
        bstack1ll111ll111_opy_ = None
        try:
            self.bstack1lllll1111l_opy_()
            req = structs.FetchDriverExecuteParamsEventRequest()
            req.bin_session_id = self.bin_session_id
            req.product = bstack1l111ll_opy_ (u"ࠥࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠥᓠ")
            req.script_name = bstack1l111ll_opy_ (u"ࠦࡸࡧࡶࡦࡔࡨࡷࡺࡲࡴࡴࠤᓡ")
            r = self.bstack1lllll1lll1_opy_.FetchDriverExecuteParamsEvent(req)
            if not r.success:
                self.logger.debug(bstack1l111ll_opy_ (u"ࠧࡸࡥࡤࡧ࡬ࡺࡪࡪࠠࡥࡴ࡬ࡺࡪࡸࠠࡦࡺࡨࡧࡺࡺࡥࠡࡲࡤࡶࡦࡳࡳࠡࡨࡵࡳࡲࠦࡳࡦࡴࡹࡩࡷࡀࠠࠣᓢ") + str(r.error) + bstack1l111ll_opy_ (u"ࠨࠢᓣ"))
            else:
                bstack1l111l111ll_opy_ = self.bstack1l111l1111l_opy_(test_uuid, r)
                bstack1lll11lll1l_opy_ = r.script
            self.logger.debug(bstack1l111ll_opy_ (u"ࠧࡑࡧࡵࡪࡴࡸ࡭ࡪࡰࡪࠤࡸࡩࡡ࡯ࠢࡥࡩ࡫ࡵࡲࡦࠢࡶࡥࡻ࡯࡮ࡨࠢࡵࡩࡸࡻ࡬ࡵࡵࠪᓤ") + str(bstack1l111l111ll_opy_))
            self.perform_scan(driver, name, framework_name=framework_name)
            if not bstack1lll11lll1l_opy_:
                self.logger.debug(bstack1l111ll_opy_ (u"ࠣࡲࡨࡶ࡫ࡵࡲ࡮ࡡࡶࡧࡦࡴ࠺ࠡ࡯࡬ࡷࡸ࡯࡮ࡨࠢࠪࡷࡦࡼࡥࡓࡧࡶࡹࡱࡺࡳࠨࠢࡶࡧࡷ࡯ࡰࡵࠢࡩࡳࡷࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫࠽ࠣᓥ") + str(framework_name) + bstack1l111ll_opy_ (u"ࠤࠣࠦᓦ"))
                return
            bstack1ll111ll111_opy_ = bstack1llll11l1ll_opy_.bstack1ll1l11l1ll_opy_(EVENTS.bstack1l1111l1l11_opy_.value)
            self.bstack1l111ll1111_opy_(driver, bstack1lll11lll1l_opy_, bstack1l111l111ll_opy_, framework_name)
            self.logger.info(bstack1l111ll_opy_ (u"ࠥࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡸࡪࡹࡴࡪࡰࡪࠤ࡫ࡵࡲࠡࡶ࡫࡭ࡸࠦࡴࡦࡵࡷࠤࡨࡧࡳࡦࠢ࡫ࡥࡸࠦࡥ࡯ࡦࡨࡨ࠳ࠨᓧ"))
            bstack1llll11l1ll_opy_.end(EVENTS.bstack1l1111l1l11_opy_.value, bstack1ll111ll111_opy_+bstack1l111ll_opy_ (u"ࠦ࠿ࡹࡴࡢࡴࡷࠦᓨ"), bstack1ll111ll111_opy_+bstack1l111ll_opy_ (u"ࠧࡀࡥ࡯ࡦࠥᓩ"), True, None, command=bstack1l111ll_opy_ (u"࠭ࡳࡢࡸࡨࡖࡪࡹࡵ࡭ࡶࡶࠫᓪ"),test_name=name)
        except Exception as bstack1l1111l1l1l_opy_:
            self.logger.error(bstack1l111ll_opy_ (u"ࠢࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡳࡧࡶࡹࡱࡺࡳࠡࡥࡲࡹࡱࡪࠠ࡯ࡱࡷࠤࡧ࡫ࠠࡱࡴࡲࡧࡪࡹࡳࡦࡦࠣࡪࡴࡸࠠࡵࡪࡨࠤࡹ࡫ࡳࡵࠢࡦࡥࡸ࡫࠺ࠡࠤᓫ") + bstack1l111ll_opy_ (u"ࠣࡵࡷࡶ࠭ࡶࡡࡵࡪࠬࠦᓬ") + bstack1l111ll_opy_ (u"ࠤࠣࡉࡷࡸ࡯ࡳࠢ࠽ࠦᓭ") + str(bstack1l1111l1l1l_opy_))
            bstack1llll11l1ll_opy_.end(EVENTS.bstack1l1111l1l11_opy_.value, bstack1ll111ll111_opy_+bstack1l111ll_opy_ (u"ࠥ࠾ࡸࡺࡡࡳࡶࠥᓮ"), bstack1ll111ll111_opy_+bstack1l111ll_opy_ (u"ࠦ࠿࡫࡮ࡥࠤᓯ"), False, bstack1l1111l1l1l_opy_, command=bstack1l111ll_opy_ (u"ࠬࡹࡡࡷࡧࡕࡩࡸࡻ࡬ࡵࡵࠪᓰ"),test_name=name)
    def bstack1l111ll1111_opy_(self, driver, bstack1lll11lll1l_opy_, bstack1l111l111ll_opy_, framework_name):
        if framework_name == bstack1l111ll_opy_ (u"࠭ࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠪᓱ"):
            self.bstack1l11l111ll1_opy_.bstack1lll1l11lll_opy_(driver, bstack1lll11lll1l_opy_, bstack1l111l111ll_opy_)
        else:
            self.logger.debug(driver.execute_async_script(bstack1lll11lll1l_opy_, bstack1l111l111ll_opy_))
    def _1l1111ll11l_opy_(self, instance: bstack1lll1l1llll_opy_, args: Tuple) -> list:
        bstack1l111ll_opy_ (u"ࠢࠣࠤࡈࡼࡹࡸࡡࡤࡶࠣࡸࡦ࡭ࡳࠡࡤࡤࡷࡪࡪࠠࡰࡰࠣࡸ࡭࡫ࠠࡵࡧࡶࡸࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫࠯ࠤࠥࠦᓲ")
        if bstack1l111ll_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠬᓳ") in instance.bstack1l1llll111l_opy_:
            return args[2].tags if hasattr(args[2], bstack1l111ll_opy_ (u"ࠩࡷࡥ࡬ࡹࠧᓴ")) else []
        if hasattr(args[0], bstack1l111ll_opy_ (u"ࠪࡳࡼࡴ࡟࡮ࡣࡵ࡯ࡪࡸࡳࠨᓵ")):
            return [marker.name for marker in args[0].own_markers]
        return []
    def bstack1l111l1l1l1_opy_(self, tags, capabilities):
        return self.bstack1ll1ll1ll_opy_(tags) and self.bstack11ll1l11l1_opy_(capabilities)