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
from datetime import datetime
import os
import threading
from browserstack_sdk.sdk_cli.bstack1lllll1ll1l_opy_ import (
    bstack11111111ll_opy_,
    bstack1lllllll1ll_opy_,
    bstack1lll11ll111_opy_,
    bstack1llllll11ll_opy_,
)
from browserstack_sdk.sdk_cli.bstack1lllllll11l_opy_ import bstack111111111l_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1l11lll_opy_, bstack1llll1l11l1_opy_, bstack1llll1l1111_opy_
from typing import Tuple, Dict, Any, List, Union
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1llll1ll1ll_opy_ import bstack1llllllll11_opy_
from browserstack_sdk.sdk_cli.bstack1lll11l1111_opy_ import bstack1lll11llll1_opy_
from browserstack_sdk.sdk_cli.bstack1lll1ll1ll1_opy_ import bstack1llll11ll11_opy_
from browserstack_sdk.sdk_cli.bstack1lll1l111ll_opy_ import bstack1lll1lll1l1_opy_
from bstack_utils.helper import bstack1l111l1l1l1_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
from bstack_utils.bstack111l11l1ll_opy_ import bstack1lllll1l11l_opy_
import grpc
import traceback
import json
class bstack1l1l1ll1111_opy_(bstack1llllllll11_opy_):
    bstack1l1ll1l11ll_opy_ = False
    bstack1l111ll1111_opy_ = bstack1ll1ll1_opy_ (u"ࠧࡹࡥ࡭ࡧࡱ࡭ࡺࡳ࠮ࡸࡧࡥࡨࡷ࡯ࡶࡦࡴࠥᐳ")
    bstack1l111l11lll_opy_ = bstack1ll1ll1_opy_ (u"ࠨࡲࡦ࡯ࡲࡸࡪ࠴ࡷࡦࡤࡧࡶ࡮ࡼࡥࡳࠤᐴ")
    bstack1l1111llll1_opy_ = bstack1ll1ll1_opy_ (u"ࠢࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿ࡟ࡪࡰ࡬ࡸࠧᐵ")
    bstack1l1111lll1l_opy_ = bstack1ll1ll1_opy_ (u"ࠣࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡠ࡫ࡶࡣࡸࡩࡡ࡯ࡰ࡬ࡲ࡬ࠨᐶ")
    bstack1l111l11l11_opy_ = bstack1ll1ll1_opy_ (u"ࠤࡧࡶ࡮ࡼࡥࡳࡡ࡫ࡥࡸࡥࡵࡳ࡮ࠥᐷ")
    scripts: Dict[str, Dict[str, str]]
    commands: Dict[str, Dict[str, Dict[str, List[str]]]]
    def __init__(self, bstack1l1ll111ll1_opy_, bstack1ll1lll11ll_opy_):
        super().__init__()
        self.scripts = dict()
        self.commands = dict()
        self.accessibility = False
        self.bstack1l1111ll1l1_opy_ = False
        self.bstack1l1111ll111_opy_ = dict()
        if not self.is_enabled():
            return
        self.bstack1l11l11llll_opy_ = bstack1ll1lll11ll_opy_
        bstack1l1ll111ll1_opy_.bstack1llllll1l1l_opy_((bstack11111111ll_opy_.bstack1llll1l1ll1_opy_, bstack1lllllll1ll_opy_.PRE), self.bstack1l1111lllll_opy_)
        TestFramework.bstack1llllll1l1l_opy_((bstack1lll1l11lll_opy_.TEST, bstack1llll1l11l1_opy_.PRE), self.bstack1llll111l11_opy_)
        TestFramework.bstack1llllll1l1l_opy_((bstack1lll1l11lll_opy_.TEST, bstack1llll1l11l1_opy_.POST), self.bstack1llll11l1ll_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1llll111l11_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll1l1111_opy_,
        bstack1llll1l1lll_opy_: Tuple[bstack1lll1l11lll_opy_, bstack1llll1l11l1_opy_],
        *args,
        **kwargs,
    ):
        tags = self._1l111lll111_opy_(instance, args)
        test_framework = f.get_state(instance, TestFramework.bstack1llll11111l_opy_)
        if self.bstack1l1111ll1l1_opy_:
            self.bstack1l1111ll111_opy_[bstack1ll1ll1_opy_ (u"ࠥࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠥᐸ")] = f.get_state(instance, TestFramework.bstack1lll1l1l1l1_opy_)
        if bstack1ll1ll1_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠨᐹ") in instance.bstack1ll11111l1l_opy_:
            platform_index = f.get_state(instance, TestFramework.bstack1111111ll1_opy_)
            self.accessibility = self.bstack1l111lllll1_opy_(tags, self.config[bstack1ll1ll1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨᐺ")][platform_index])
        else:
            capabilities = self.bstack1l11l11llll_opy_.bstack1lll1l1ll11_opy_(f, instance, bstack1llll1l1lll_opy_, *args, **kwargs)
            if not capabilities:
                self.logger.debug(bstack1ll1ll1_opy_ (u"ࠨ࡯࡯ࡡࡥࡩ࡫ࡵࡲࡦࡡࡷࡩࡸࡺ࠺ࠡࡰࡲࠤࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠣࡪࡴࡻ࡮ࡥࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨᐻ") + str(kwargs) + bstack1ll1ll1_opy_ (u"ࠢࠣᐼ"))
                return
            self.accessibility = self.bstack1l111lllll1_opy_(tags, capabilities)
        if self.bstack1l11l11llll_opy_.pages and self.bstack1l11l11llll_opy_.pages.values():
            bstack1l111ll1l1l_opy_ = list(self.bstack1l11l11llll_opy_.pages.values())
            if bstack1l111ll1l1l_opy_ and isinstance(bstack1l111ll1l1l_opy_[0], (list, tuple)) and bstack1l111ll1l1l_opy_[0]:
                bstack1l111llll1l_opy_ = bstack1l111ll1l1l_opy_[0][0]
                if callable(bstack1l111llll1l_opy_):
                    page = bstack1l111llll1l_opy_()
                    def bstack1l11ll1ll_opy_():
                        self.get_accessibility_results(page, bstack1ll1ll1_opy_ (u"ࠣࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠧᐽ"))
                    def bstack1l111l1ll11_opy_():
                        self.get_accessibility_results_summary(page, bstack1ll1ll1_opy_ (u"ࠤࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠨᐾ"))
                    setattr(page, bstack1ll1ll1_opy_ (u"ࠥ࡫ࡪࡺࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡘࡥࡴࡷ࡯ࡸࡸࠨᐿ"), bstack1l11ll1ll_opy_)
                    setattr(page, bstack1ll1ll1_opy_ (u"ࠦ࡬࡫ࡴࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡒࡦࡵࡸࡰࡹ࡙ࡵ࡮࡯ࡤࡶࡾࠨᑀ"), bstack1l111l1ll11_opy_)
        self.logger.debug(bstack1ll1ll1_opy_ (u"ࠧࡹࡨࡰࡷ࡯ࡨࠥࡸࡵ࡯ࠢࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡹࡥࡱࡻࡥ࠾ࠤᑁ") + str(self.accessibility) + bstack1ll1ll1_opy_ (u"ࠨࠢᑂ"))
    def bstack1l1111lllll_opy_(
        self,
        f: bstack111111111l_opy_,
        driver: object,
        exec: Tuple[bstack1llllll11ll_opy_, str],
        bstack1llll1l1lll_opy_: Tuple[bstack11111111ll_opy_, bstack1lllllll1ll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        try:
            bstack111lllll1_opy_ = datetime.now()
            self.bstack1l111l11111_opy_(f, exec, *args, **kwargs)
            instance, method_name = exec
            instance.bstack1llll1ll11_opy_(bstack1ll1ll1_opy_ (u"ࠢࡢ࠳࠴ࡽ࠿࡯࡮ࡪࡶࡢࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡢࡧࡴࡴࡦࡪࡩࠥᑃ"), datetime.now() - bstack111lllll1_opy_)
            if (
                not f.bstack1l1lll11111_opy_(method_name)
                or f.bstack1l1lll1ll11_opy_(method_name, *args)
                or f.bstack1l1lll1l1l1_opy_(method_name, *args)
            ):
                return
            if not f.get_state(instance, bstack1l1l1ll1111_opy_.bstack1l1111llll1_opy_, False):
                if not bstack1l1l1ll1111_opy_.bstack1l1ll1l11ll_opy_:
                    self.logger.warning(bstack1ll1ll1_opy_ (u"ࠣ࡝ࡳࡰࡦࡺࡦࡰࡴࡰࡣ࡮ࡴࡤࡦࡺࡀࠦᑄ") + str(f.platform_index) + bstack1ll1ll1_opy_ (u"ࠤࡠࠤࡦ࠷࠱ࡺࠢࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠡࡪࡤࡺࡪࠦ࡮ࡰࡶࠣࡦࡪ࡫࡮ࠡࡵࡨࡸࠥ࡬࡯ࡳࠢࡷ࡬࡮ࡹࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠣᑅ"))
                    bstack1l1l1ll1111_opy_.bstack1l1ll1l11ll_opy_ = True
                return
            bstack1l1111ll11l_opy_ = self.scripts.get(f.framework_name, {})
            if not bstack1l1111ll11l_opy_:
                platform_index = f.get_state(instance, bstack111111111l_opy_.bstack1111111ll1_opy_, 0)
                self.logger.debug(bstack1ll1ll1_opy_ (u"ࠥࡲࡴࠦࡡ࠲࠳ࡼࠤࡸࡩࡲࡪࡲࡷࡷࠥ࡬࡯ࡳࠢࡳࡰࡦࡺࡦࡰࡴࡰࡣ࡮ࡴࡤࡦࡺࡀࡿࡵࡲࡡࡵࡨࡲࡶࡲࡥࡩ࡯ࡦࡨࡼࢂࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫࠽ࠣᑆ") + str(f.framework_name) + bstack1ll1ll1_opy_ (u"ࠦࠧᑇ"))
                return
            command_name = f.bstack1l1lll11lll_opy_(*args)
            if not command_name:
                self.logger.debug(bstack1ll1ll1_opy_ (u"ࠧࡳࡩࡴࡵ࡬ࡲ࡬ࠦࡣࡰ࡯ࡰࡥࡳࡪ࡟࡯ࡣࡰࡩࠥ࡬࡯ࡳࠢࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡴࡡ࡮ࡧࡀࡿ࡫࠴ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫ࡽࠡ࡯ࡨࡸ࡭ࡵࡤࡠࡰࡤࡱࡪࡃࠢᑈ") + str(method_name) + bstack1ll1ll1_opy_ (u"ࠨࠢᑉ"))
                return
            bstack1l111ll11ll_opy_ = f.get_state(instance, bstack1l1l1ll1111_opy_.bstack1l111l11l11_opy_, False)
            if command_name == bstack1ll1ll1_opy_ (u"ࠢࡨࡧࡷࠦᑊ") and not bstack1l111ll11ll_opy_:
                f.bstack1lllll1l1ll_opy_(instance, bstack1l1l1ll1111_opy_.bstack1l111l11l11_opy_, True)
                bstack1l111ll11ll_opy_ = True
            if not bstack1l111ll11ll_opy_ and not self.bstack1l1111ll1l1_opy_:
                self.logger.debug(bstack1ll1ll1_opy_ (u"ࠣࡰࡲࠤ࡚ࡘࡌࠡ࡮ࡲࡥࡩ࡫ࡤࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦ࠿ࡾࡪ࠳࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪࢃࠠࡤࡱࡰࡱࡦࡴࡤࡠࡰࡤࡱࡪࡃࠢᑋ") + str(command_name) + bstack1ll1ll1_opy_ (u"ࠤࠥᑌ"))
                return
            scripts_to_run = self.commands.get(f.framework_name, {}).get(method_name, {}).get(command_name, [])
            if not scripts_to_run:
                self.logger.debug(bstack1ll1ll1_opy_ (u"ࠥࡲࡴࠦࡡ࠲࠳ࡼࠤࡸࡩࡲࡪࡲࡷࡷࠥ࡬࡯ࡳࠢࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡴࡡ࡮ࡧࡀࡿ࡫࠴ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫ࡽࠡࡥࡲࡱࡲࡧ࡮ࡥࡡࡱࡥࡲ࡫࠽ࠣᑍ") + str(command_name) + bstack1ll1ll1_opy_ (u"ࠦࠧᑎ"))
                return
            self.logger.info(bstack1ll1ll1_opy_ (u"ࠧࡸࡵ࡯ࡰ࡬ࡲ࡬ࠦࡻ࡭ࡧࡱࠬࡸࡩࡲࡪࡲࡷࡷࡤࡺ࡯ࡠࡴࡸࡲ࠮ࢃࠠࡴࡥࡵ࡭ࡵࡺࡳࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦ࠿ࡾࡪ࠳࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪࢃࠠࡤࡱࡰࡱࡦࡴࡤࡠࡰࡤࡱࡪࡃࠢᑏ") + str(command_name) + bstack1ll1ll1_opy_ (u"ࠨࠢᑐ"))
            scripts = [(s, bstack1l1111ll11l_opy_[s]) for s in scripts_to_run if s in bstack1l1111ll11l_opy_]
            for script_name, bstack1llll1l11ll_opy_ in scripts:
                try:
                    bstack111lllll1_opy_ = datetime.now()
                    if script_name == bstack1ll1ll1_opy_ (u"ࠢࡴࡥࡤࡲࠧᑑ"):
                        result = self.perform_scan(driver, method=command_name, framework_name=f.framework_name)
                    instance.bstack1llll1ll11_opy_(bstack1ll1ll1_opy_ (u"ࠣࡣ࠴࠵ࡾࡀࠢᑒ") + script_name, datetime.now() - bstack111lllll1_opy_)
                    if isinstance(result, dict) and not result.get(bstack1ll1ll1_opy_ (u"ࠤࡶࡹࡨࡩࡥࡴࡵࠥᑓ"), True):
                        self.logger.warning(bstack1ll1ll1_opy_ (u"ࠥࡷࡰ࡯ࡰࠡࡧࡻࡩࡨࡻࡴࡪࡰࡪࠤࡷ࡫࡭ࡢ࡫ࡱ࡭ࡳ࡭ࠠࡴࡥࡵ࡭ࡵࡺࡳ࠻ࠢࠥᑔ") + str(result) + bstack1ll1ll1_opy_ (u"ࠦࠧᑕ"))
                        break
                except Exception as e:
                    self.logger.error(bstack1ll1ll1_opy_ (u"ࠧ࡫ࡲࡳࡱࡵࠤࡪࡾࡥࡤࡷࡷ࡭ࡳ࡭ࠠࡴࡥࡵ࡭ࡵࡺ࠽ࡼࡵࡦࡶ࡮ࡶࡴࡠࡰࡤࡱࡪࢃࠠࡦࡴࡵࡳࡷࡃࠢᑖ") + str(e) + bstack1ll1ll1_opy_ (u"ࠨࠢᑗ"))
        except Exception as e:
            self.logger.error(bstack1ll1ll1_opy_ (u"ࠢࡰࡰࡢࡦࡪ࡬࡯ࡳࡧࡢࡩࡽ࡫ࡣࡶࡶࡨࠤࡪࡸࡲࡰࡴࡀࠦᑘ") + str(e) + bstack1ll1ll1_opy_ (u"ࠣࠤᑙ"))
    def bstack1llll11l1ll_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll1l1111_opy_,
        bstack1llll1l1lll_opy_: Tuple[bstack1lll1l11lll_opy_, bstack1llll1l11l1_opy_],
        *args,
        **kwargs,
    ):
        tags = self._1l111lll111_opy_(instance, args)
        capabilities = self.bstack1l11l11llll_opy_.bstack1lll1l1ll11_opy_(f, instance, bstack1llll1l1lll_opy_, *args, **kwargs)
        self.accessibility = self.bstack1l111lllll1_opy_(tags, capabilities)
        if not self.accessibility:
            self.logger.debug(bstack1ll1ll1_opy_ (u"ࠤࡲࡲࡤࡧࡦࡵࡧࡵࡣࡹ࡫ࡳࡵ࠼ࠣࡥ࠶࠷ࡹࠡࡰࡲࡸࠥ࡫࡮ࡢࡤ࡯ࡩࡩࠨᑚ"))
            return
        driver = self.bstack1l11l11llll_opy_.bstack1lll1l11ll1_opy_(f, instance, bstack1llll1l1lll_opy_, *args, **kwargs)
        test_name = f.get_state(instance, TestFramework.bstack1ll11l11l11_opy_)
        if not test_name:
            self.logger.debug(bstack1ll1ll1_opy_ (u"ࠥࡳࡳࡥࡡࡧࡶࡨࡶࡤࡺࡥࡴࡶ࠽ࠤࡲ࡯ࡳࡴ࡫ࡱ࡫ࠥࡺࡥࡴࡶࠣࡲࡦࡳࡥࠣᑛ"))
            return
        test_uuid = f.get_state(instance, TestFramework.bstack1lll1l1l1l1_opy_)
        if not test_uuid:
            self.logger.debug(bstack1ll1ll1_opy_ (u"ࠦࡴࡴ࡟ࡢࡨࡷࡩࡷࡥࡴࡦࡵࡷ࠾ࠥࡳࡩࡴࡵ࡬ࡲ࡬ࠦࡴࡦࡵࡷࠤࡺࡻࡩࡥࠤᑜ"))
            return
        if isinstance(self.bstack1l11l11llll_opy_, bstack1llll11ll11_opy_):
            framework_name = bstack1ll1ll1_opy_ (u"ࠬࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠩᑝ")
        else:
            framework_name = bstack1ll1ll1_opy_ (u"࠭ࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࠨᑞ")
        self.bstack111l111l_opy_(driver, test_name, framework_name, test_uuid)
    def perform_scan(self, driver: object, method: Union[None, str], framework_name: str):
        bstack1ll111l11ll_opy_ = bstack1lllll1l11l_opy_.bstack1ll11l11l1l_opy_(EVENTS.bstack11111l111_opy_.value)
        if not self.accessibility:
            self.logger.debug(bstack1ll1ll1_opy_ (u"ࠢࡱࡧࡵࡪࡴࡸ࡭ࡠࡵࡦࡥࡳࡀࠠࡢ࠳࠴ࡽࠥࡴ࡯ࡵࠢࡨࡲࡦࡨ࡬ࡦࡦࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥ࡮ࡢ࡯ࡨࡁࢀ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪࢃࠠࠣᑟ"))
            return
        bstack111lllll1_opy_ = datetime.now()
        bstack1llll1l11ll_opy_ = self.scripts.get(framework_name, {}).get(bstack1ll1ll1_opy_ (u"ࠣࡵࡦࡥࡳࠨᑠ"), None)
        if not bstack1llll1l11ll_opy_:
            self.logger.debug(bstack1ll1ll1_opy_ (u"ࠤࡳࡩࡷ࡬࡯ࡳ࡯ࡢࡷࡨࡧ࡮࠻ࠢࡰ࡭ࡸࡹࡩ࡯ࡩࠣࠫࡸࡩࡡ࡯ࠩࠣࡷࡨࡸࡩࡱࡶࠣࡪࡴࡸࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡲࡦࡳࡥ࠾ࠤᑡ") + str(framework_name) + bstack1ll1ll1_opy_ (u"ࠥࠤࠧᑢ"))
            return
        if self.bstack1l1111ll1l1_opy_:
            arg = dict()
            arg[bstack1ll1ll1_opy_ (u"ࠦࡲ࡫ࡴࡩࡱࡧࠦᑣ")] = method if method else bstack1ll1ll1_opy_ (u"ࠧࠨᑤ")
            arg[bstack1ll1ll1_opy_ (u"ࠨࡴࡩࡖࡨࡷࡹࡘࡵ࡯ࡗࡸ࡭ࡩࠨᑥ")] = self.bstack1l1111ll111_opy_[bstack1ll1ll1_opy_ (u"ࠢࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠢᑦ")]
            arg[bstack1ll1ll1_opy_ (u"ࠣࡶ࡫ࡆࡺ࡯࡬ࡥࡗࡸ࡭ࡩࠨᑧ")] = self.bstack1l1111ll111_opy_[bstack1ll1ll1_opy_ (u"ࠤࡷࡩࡸࡺࡨࡶࡤࡢࡦࡺ࡯࡬ࡥࡡࡸࡹ࡮ࡪࠢᑨ")]
            arg[bstack1ll1ll1_opy_ (u"ࠥࡥࡺࡺࡨࡉࡧࡤࡨࡪࡸࠢᑩ")] = self.bstack1l1111ll111_opy_[bstack1ll1ll1_opy_ (u"ࠦࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡘࡴࡱࡥ࡯ࠤᑪ")]
            arg[bstack1ll1ll1_opy_ (u"ࠧࡺࡨࡋࡹࡷࡘࡴࡱࡥ࡯ࠤᑫ")] = self.bstack1l1111ll111_opy_[bstack1ll1ll1_opy_ (u"ࠨࡴࡩࡡ࡭ࡻࡹࡥࡴࡰ࡭ࡨࡲࠧᑬ")]
            arg[bstack1ll1ll1_opy_ (u"ࠢࡴࡥࡤࡲ࡙࡯࡭ࡦࡵࡷࡥࡲࡶࠢᑭ")] = str(int(datetime.now().timestamp() * 1000))
            bstack1l111l111ll_opy_ = bstack1llll1l11ll_opy_ % json.dumps(arg)
            driver.execute_script(bstack1l111l111ll_opy_)
            return
        instance = bstack1lll11ll111_opy_.bstack1ll111ll11l_opy_(driver)
        if instance:
            if not bstack1lll11ll111_opy_.get_state(instance, bstack1l1l1ll1111_opy_.bstack1l1111lll1l_opy_, False):
                bstack1lll11ll111_opy_.bstack1lllll1l1ll_opy_(instance, bstack1l1l1ll1111_opy_.bstack1l1111lll1l_opy_, True)
            else:
                self.logger.info(bstack1ll1ll1_opy_ (u"ࠣࡲࡨࡶ࡫ࡵࡲ࡮ࡡࡶࡧࡦࡴ࠺ࠡࡣ࡯ࡶࡪࡧࡤࡺࠢ࡬ࡲࠥࡶࡲࡰࡩࡵࡩࡸࡹࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡲࡦࡳࡥ࠾ࡽࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡴࡡ࡮ࡧࢀࠤࡲ࡫ࡴࡩࡱࡧࡁࠧᑮ") + str(method) + bstack1ll1ll1_opy_ (u"ࠤࠥᑯ"))
                return
        self.logger.info(bstack1ll1ll1_opy_ (u"ࠥࡴࡪࡸࡦࡰࡴࡰࡣࡸࡩࡡ࡯࠼ࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥ࡮ࡢ࡯ࡨࡁࢀ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪࢃࠠ࡮ࡧࡷ࡬ࡴࡪ࠽ࠣᑰ") + str(method) + bstack1ll1ll1_opy_ (u"ࠦࠧᑱ"))
        if framework_name == bstack1ll1ll1_opy_ (u"ࠬࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠩᑲ"):
            result = self.bstack1l11l11llll_opy_.bstack1lll1lll111_opy_(driver, bstack1llll1l11ll_opy_)
        else:
            result = driver.execute_async_script(bstack1llll1l11ll_opy_, {bstack1ll1ll1_opy_ (u"ࠨ࡭ࡦࡶ࡫ࡳࡩࠨᑳ"): method if method else bstack1ll1ll1_opy_ (u"ࠢࠣᑴ")})
        bstack1lllll1l11l_opy_.end(EVENTS.bstack11111l111_opy_.value, bstack1ll111l11ll_opy_+bstack1ll1ll1_opy_ (u"ࠣ࠼ࡶࡸࡦࡸࡴࠣᑵ"), bstack1ll111l11ll_opy_+bstack1ll1ll1_opy_ (u"ࠤ࠽ࡩࡳࡪࠢᑶ"), True, None, command=method)
        if instance:
            bstack1lll11ll111_opy_.bstack1lllll1l1ll_opy_(instance, bstack1l1l1ll1111_opy_.bstack1l1111lll1l_opy_, False)
            instance.bstack1llll1ll11_opy_(bstack1ll1ll1_opy_ (u"ࠥࡥ࠶࠷ࡹ࠻ࡲࡨࡶ࡫ࡵࡲ࡮ࡡࡶࡧࡦࡴࠢᑷ"), datetime.now() - bstack111lllll1_opy_)
        return result
        def bstack1l111l1llll_opy_(self, driver: object, framework_name, bstack1l11l1lll1_opy_: str):
            self.bstack1llllll111l_opy_()
            req = structs.AccessibilityResultRequest()
            req.bin_session_id = self.bin_session_id
            req.bstack1l111llllll_opy_ = self.bstack1l1111ll111_opy_[bstack1ll1ll1_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠦᑸ")]
            req.bstack1l11l1lll1_opy_ = bstack1l11l1lll1_opy_
            req.session_id = self.bin_session_id
            try:
                r = self.bstack1lllll1lll1_opy_.AccessibilityResult(req)
                if not r.success:
                    self.logger.debug(bstack1ll1ll1_opy_ (u"ࠧࡸࡥࡤࡧ࡬ࡺࡪࡪࠠࡧࡴࡲࡱࠥࡹࡥࡳࡸࡨࡶ࠿ࠦࠢᑹ") + str(r) + bstack1ll1ll1_opy_ (u"ࠨࠢᑺ"))
                else:
                    bstack1l111lll1l1_opy_ = json.loads(r.bstack1l111ll1ll1_opy_.decode(bstack1ll1ll1_opy_ (u"ࠧࡶࡶࡩ࠱࠽࠭ᑻ")))
                    if bstack1l11l1lll1_opy_ == bstack1ll1ll1_opy_ (u"ࠨࡩࡨࡸࡗ࡫ࡳࡶ࡮ࡷࡷࠬᑼ"):
                        return bstack1l111lll1l1_opy_.get(bstack1ll1ll1_opy_ (u"ࠤࡧࡥࡹࡧࠢᑽ"), [])
                    else:
                        return bstack1l111lll1l1_opy_.get(bstack1ll1ll1_opy_ (u"ࠥࡨࡦࡺࡡࠣᑾ"), {})
            except grpc.RpcError as e:
                self.logger.error(bstack1ll1ll1_opy_ (u"ࠦࡷࡶࡣ࠮ࡧࡵࡶࡴࡸࠠࡸࡪ࡬ࡰࡪࠦࡦࡦࡶࡦ࡬࡮ࡴࡧࠡࡩࡨࡸࡤࡧࡰࡱࡡࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡡࡵࡩࡸࡻ࡬ࡵࠢࡩࡶࡴࡳࠠࡤ࡮࡬࠾ࠥࠨᑿ") + str(e) + bstack1ll1ll1_opy_ (u"ࠧࠨᒀ"))
    @measure(event_name=EVENTS.bstack1111l111ll_opy_, stage=STAGE.bstack111l1l111_opy_)
    def get_accessibility_results(self, driver: object, framework_name):
        if not self.accessibility:
            self.logger.debug(bstack1ll1ll1_opy_ (u"ࠨࡧࡦࡶࡢࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡢࡶࡪࡹࡵ࡭ࡶࡶ࠾ࠥࡧ࠱࠲ࡻࠣࡲࡴࡺࠠࡦࡰࡤࡦࡱ࡫ࡤࠣᒁ"))
            return
        if self.bstack1l1111ll1l1_opy_:
            self.logger.debug(bstack1ll1ll1_opy_ (u"ࠧࡑࡧࡵࡪࡴࡸ࡭ࡪࡰࡪࠤࡸࡩࡡ࡯ࠢࡩࡳࡷࠦࡡࡱࡲࠣࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪᒂ"))
            self.perform_scan(driver, method=None, framework_name=framework_name)
            return self.bstack1l111l1llll_opy_(driver, framework_name, bstack1ll1ll1_opy_ (u"ࠣࡩࡨࡸࡗ࡫ࡳࡶ࡮ࡷࡷࠧᒃ"))
        bstack1llll1l11ll_opy_ = self.scripts.get(framework_name, {}).get(bstack1ll1ll1_opy_ (u"ࠤࡪࡩࡹࡘࡥࡴࡷ࡯ࡸࡸࠨᒄ"), None)
        if not bstack1llll1l11ll_opy_:
            self.logger.debug(bstack1ll1ll1_opy_ (u"ࠥࡱ࡮ࡹࡳࡪࡰࡪࠤࠬ࡭ࡥࡵࡔࡨࡷࡺࡲࡴࡴࠩࠣࡷࡨࡸࡩࡱࡶࠣࡪࡴࡸࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡲࡦࡳࡥ࠾ࠤᒅ") + str(framework_name) + bstack1ll1ll1_opy_ (u"ࠦࠧᒆ"))
            return
        self.perform_scan(driver, method=None, framework_name=framework_name)
        bstack111lllll1_opy_ = datetime.now()
        if framework_name == bstack1ll1ll1_opy_ (u"ࠬࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠩᒇ"):
            result = self.bstack1l11l11llll_opy_.bstack1lll1lll111_opy_(driver, bstack1llll1l11ll_opy_)
        else:
            result = driver.execute_async_script(bstack1llll1l11ll_opy_)
        instance = bstack1lll11ll111_opy_.bstack1ll111ll11l_opy_(driver)
        if instance:
            instance.bstack1llll1ll11_opy_(bstack1ll1ll1_opy_ (u"ࠨࡡ࠲࠳ࡼ࠾࡬࡫ࡴࡠࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡠࡴࡨࡷࡺࡲࡴࡴࠤᒈ"), datetime.now() - bstack111lllll1_opy_)
        return result
    @measure(event_name=EVENTS.bstack11l111l1l1_opy_, stage=STAGE.bstack111l1l111_opy_)
    def get_accessibility_results_summary(self, driver: object, framework_name):
        if not self.accessibility:
            self.logger.debug(bstack1ll1ll1_opy_ (u"ࠢࡨࡧࡷࡣࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡣࡷ࡫ࡳࡶ࡮ࡷࡷࡤࡹࡵ࡮࡯ࡤࡶࡾࡀࠠࡢ࠳࠴ࡽࠥࡴ࡯ࡵࠢࡨࡲࡦࡨ࡬ࡦࡦࠥᒉ"))
            return
        if self.bstack1l1111ll1l1_opy_:
            self.perform_scan(driver, method=None, framework_name=framework_name)
            return self.bstack1l111l1llll_opy_(driver, framework_name, bstack1ll1ll1_opy_ (u"ࠨࡩࡨࡸࡗ࡫ࡳࡶ࡮ࡷࡷࡘࡻ࡭࡮ࡣࡵࡽࠬᒊ"))
        bstack1llll1l11ll_opy_ = self.scripts.get(framework_name, {}).get(bstack1ll1ll1_opy_ (u"ࠤࡪࡩࡹࡘࡥࡴࡷ࡯ࡸࡸ࡙ࡵ࡮࡯ࡤࡶࡾࠨᒋ"), None)
        if not bstack1llll1l11ll_opy_:
            self.logger.debug(bstack1ll1ll1_opy_ (u"ࠥࡱ࡮ࡹࡳࡪࡰࡪࠤࠬ࡭ࡥࡵࡔࡨࡷࡺࡲࡴࡴࡕࡸࡱࡲࡧࡲࡺࠩࠣࡷࡨࡸࡩࡱࡶࠣࡪࡴࡸࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡲࡦࡳࡥ࠾ࠤᒌ") + str(framework_name) + bstack1ll1ll1_opy_ (u"ࠦࠧᒍ"))
            return
        self.perform_scan(driver, method=None, framework_name=framework_name)
        bstack111lllll1_opy_ = datetime.now()
        if framework_name == bstack1ll1ll1_opy_ (u"ࠬࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠩᒎ"):
            result = self.bstack1l11l11llll_opy_.bstack1lll1lll111_opy_(driver, bstack1llll1l11ll_opy_)
        else:
            result = driver.execute_async_script(bstack1llll1l11ll_opy_)
        instance = bstack1lll11ll111_opy_.bstack1ll111ll11l_opy_(driver)
        if instance:
            instance.bstack1llll1ll11_opy_(bstack1ll1ll1_opy_ (u"ࠨࡡ࠲࠳ࡼ࠾࡬࡫ࡴࡠࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡠࡴࡨࡷࡺࡲࡴࡴࡡࡶࡹࡲࡳࡡࡳࡻࠥᒏ"), datetime.now() - bstack111lllll1_opy_)
        return result
    @measure(event_name=EVENTS.bstack1l111l1ll1l_opy_, stage=STAGE.bstack111l1l111_opy_)
    def bstack1l111ll111l_opy_(
        self,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        hub_url: str,
    ):
        self.bstack1llllll111l_opy_()
        req = structs.AccessibilityConfigRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.hub_url = hub_url
        try:
            r = self.bstack1lllll1lll1_opy_.AccessibilityConfig(req)
            if not r.success:
                self.logger.debug(bstack1ll1ll1_opy_ (u"ࠢࡳࡧࡦࡩ࡮ࡼࡥࡥࠢࡩࡶࡴࡳࠠࡴࡧࡵࡺࡪࡸ࠺ࠡࠤᒐ") + str(r) + bstack1ll1ll1_opy_ (u"ࠣࠤᒑ"))
            else:
                self.bstack1l111l1l11l_opy_(framework_name, r)
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1ll1ll1_opy_ (u"ࠤࡵࡴࡨ࠳ࡥࡳࡴࡲࡶ࠿ࠦࠢᒒ") + str(e) + bstack1ll1ll1_opy_ (u"ࠥࠦᒓ"))
            traceback.print_exc()
            raise e
    def bstack1l111l1l11l_opy_(self, framework_name: str, result: structs.AccessibilityConfigResponse) -> bool:
        if not result.success or not result.accessibility.success:
            self.logger.debug(bstack1ll1ll1_opy_ (u"ࠦࡱࡵࡡࡥࡡࡦࡳࡳ࡬ࡩࡨ࠼ࠣࡥ࠶࠷ࡹࠡࡰࡲࡸࠥ࡬࡯ࡶࡰࡧࠦᒔ"))
            return False
        if result.accessibility.is_app_accessibility:
            self.bstack1l1111ll1l1_opy_ = result.accessibility.is_app_accessibility
        if result.testhub.build_hashed_id:
            self.bstack1l1111ll111_opy_[bstack1ll1ll1_opy_ (u"ࠧࡺࡥࡴࡶ࡫ࡹࡧࡥࡢࡶ࡫࡯ࡨࡤࡻࡵࡪࡦࠥᒕ")] = result.testhub.build_hashed_id
        if result.testhub.jwt:
            self.bstack1l1111ll111_opy_[bstack1ll1ll1_opy_ (u"ࠨࡴࡩࡡ࡭ࡻࡹࡥࡴࡰ࡭ࡨࡲࠧᒖ")] = result.testhub.jwt
        if result.accessibility.options:
            options = result.accessibility.options
            if options.capabilities:
                for caps in options.capabilities:
                    self.bstack1l1111ll111_opy_[caps.name] = caps.value
            if options.scripts:
                self.scripts[framework_name] = {row.name: row.command for row in options.scripts}
            if options.commands_to_wrap and options.commands_to_wrap.commands:
                scripts_to_run = [s for s in options.commands_to_wrap.scripts_to_run]
                if not scripts_to_run:
                    return False
                bstack1l111llll11_opy_ = dict()
                for command in options.commands_to_wrap.commands:
                    if command.library == self.bstack1l111ll1111_opy_ and command.module == self.bstack1l111l11lll_opy_:
                        if command.method and not command.method in bstack1l111llll11_opy_:
                            bstack1l111llll11_opy_[command.method] = dict()
                        if command.name and not command.name in bstack1l111llll11_opy_[command.method]:
                            bstack1l111llll11_opy_[command.method][command.name] = list()
                        bstack1l111llll11_opy_[command.method][command.name].extend(scripts_to_run)
                self.commands[framework_name] = bstack1l111llll11_opy_
        return bool(self.commands.get(framework_name, None))
    def bstack1l111l11111_opy_(
        self,
        f: bstack111111111l_opy_,
        exec: Tuple[bstack1llllll11ll_opy_, str],
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if isinstance(self.bstack1l11l11llll_opy_, bstack1llll11ll11_opy_) and method_name != bstack1ll1ll1_opy_ (u"ࠧࡤࡱࡱࡲࡪࡩࡴࠨᒗ"):
            return
        if bstack1lll11ll111_opy_.bstack1lllll1ll11_opy_(instance, bstack1l1l1ll1111_opy_.bstack1l1111llll1_opy_):
            return
        if f.bstack1lllll11l1l_opy_(method_name, *args):
            bstack1l111ll11l1_opy_ = False
            desired_capabilities = f.bstack1l1lll1l111_opy_(instance)
            if isinstance(desired_capabilities, dict):
                hub_url = f.bstack1l1lll1l11l_opy_(instance)
                platform_index = f.get_state(instance, bstack111111111l_opy_.bstack1111111ll1_opy_, 0)
                bstack1l111l1lll1_opy_ = datetime.now()
                r = self.bstack1l111ll111l_opy_(platform_index, f.framework_name, f.framework_version, hub_url)
                instance.bstack1llll1ll11_opy_(bstack1ll1ll1_opy_ (u"ࠣࡩࡵࡴࡨࡀࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡥࡣࡰࡰࡩ࡭࡬ࠨᒘ"), datetime.now() - bstack1l111l1lll1_opy_)
                bstack1l111ll11l1_opy_ = r.success
            else:
                self.logger.error(bstack1ll1ll1_opy_ (u"ࠤࡰ࡭ࡸࡹࡩ࡯ࡩࠣࡨࡪࡹࡩࡳࡧࡧࠤࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࡀࠦᒙ") + str(desired_capabilities) + bstack1ll1ll1_opy_ (u"ࠥࠦᒚ"))
            f.bstack1lllll1l1ll_opy_(instance, bstack1l1l1ll1111_opy_.bstack1l1111llll1_opy_, bstack1l111ll11l1_opy_)
    def bstack111llllll_opy_(self, test_tags):
        bstack1l111ll111l_opy_ = self.config.get(bstack1ll1ll1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫᒛ"))
        if not bstack1l111ll111l_opy_:
            return True
        try:
            include_tags = bstack1l111ll111l_opy_[bstack1ll1ll1_opy_ (u"ࠬ࡯࡮ࡤ࡮ࡸࡨࡪ࡚ࡡࡨࡵࡌࡲ࡙࡫ࡳࡵ࡫ࡱ࡫ࡘࡩ࡯ࡱࡧࠪᒜ")] if bstack1ll1ll1_opy_ (u"࠭ࡩ࡯ࡥ࡯ࡹࡩ࡫ࡔࡢࡩࡶࡍࡳ࡚ࡥࡴࡶ࡬ࡲ࡬࡙ࡣࡰࡲࡨࠫᒝ") in bstack1l111ll111l_opy_ and isinstance(bstack1l111ll111l_opy_[bstack1ll1ll1_opy_ (u"ࠧࡪࡰࡦࡰࡺࡪࡥࡕࡣࡪࡷࡎࡴࡔࡦࡵࡷ࡭ࡳ࡭ࡓࡤࡱࡳࡩࠬᒞ")], list) else []
            exclude_tags = bstack1l111ll111l_opy_[bstack1ll1ll1_opy_ (u"ࠨࡧࡻࡧࡱࡻࡤࡦࡖࡤ࡫ࡸࡏ࡮ࡕࡧࡶࡸ࡮ࡴࡧࡔࡥࡲࡴࡪ࠭ᒟ")] if bstack1ll1ll1_opy_ (u"ࠩࡨࡼࡨࡲࡵࡥࡧࡗࡥ࡬ࡹࡉ࡯ࡖࡨࡷࡹ࡯࡮ࡨࡕࡦࡳࡵ࡫ࠧᒠ") in bstack1l111ll111l_opy_ and isinstance(bstack1l111ll111l_opy_[bstack1ll1ll1_opy_ (u"ࠪࡩࡽࡩ࡬ࡶࡦࡨࡘࡦ࡭ࡳࡊࡰࡗࡩࡸࡺࡩ࡯ࡩࡖࡧࡴࡶࡥࠨᒡ")], list) else []
            excluded = any(tag in exclude_tags for tag in test_tags)
            included = len(include_tags) == 0 or any(tag in include_tags for tag in test_tags)
            return not excluded and included
        except Exception as error:
            self.logger.debug(bstack1ll1ll1_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡻ࡭࡯࡬ࡦࠢࡹࡥࡱ࡯ࡤࡢࡶ࡬ࡲ࡬ࠦࡴࡦࡵࡷࠤࡨࡧࡳࡦࠢࡩࡳࡷࠦࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡢࡦࡨࡲࡶࡪࠦࡳࡤࡣࡱࡲ࡮ࡴࡧ࠯ࠢࡈࡶࡷࡵࡲࠡ࠼ࠣࠦᒢ") + str(error))
        return False
    def bstack1lll1ll111_opy_(self, caps):
        try:
            if self.bstack1l1111ll1l1_opy_:
                bstack1l111l111l1_opy_ = caps.get(bstack1ll1ll1_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳࡎࡢ࡯ࡨࠦᒣ"))
                if bstack1l111l111l1_opy_ is not None and str(bstack1l111l111l1_opy_).lower() == bstack1ll1ll1_opy_ (u"ࠨࡡ࡯ࡦࡵࡳ࡮ࡪࠢᒤ"):
                    bstack1l111ll1lll_opy_ = caps.get(bstack1ll1ll1_opy_ (u"ࠢࡢࡲࡳ࡭ࡺࡳ࠺ࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡘࡨࡶࡸ࡯࡯࡯ࠤᒥ")) or caps.get(bstack1ll1ll1_opy_ (u"ࠣࡲ࡯ࡥࡹ࡬࡯ࡳ࡯࡙ࡩࡷࡹࡩࡰࡰࠥᒦ"))
                    if bstack1l111ll1lll_opy_ is not None and int(bstack1l111ll1lll_opy_) < 11:
                        self.logger.warning(bstack1ll1ll1_opy_ (u"ࠤࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡷࡪ࡮࡯ࠤࡷࡻ࡮ࠡࡱࡱࡰࡾࠦ࡯࡯ࠢࡄࡲࡩࡸ࡯ࡪࡦࠣ࠵࠶ࠦࡡ࡯ࡦࠣࡥࡧࡵࡶࡦ࠰ࠣࡇࡺࡸࡲࡦࡰࡷࠤࡵࡲࡡࡵࡨࡲࡶࡲࠦࡶࡦࡴࡶ࡭ࡴࡴࠠ࠾ࠤᒧ") + str(bstack1l111ll1lll_opy_) + bstack1ll1ll1_opy_ (u"ࠥࠦᒨ"))
                        return False
                return True
            bstack1l111lll11l_opy_ = caps.get(bstack1ll1ll1_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬᒩ"), {}).get(bstack1ll1ll1_opy_ (u"ࠬࡪࡥࡷ࡫ࡦࡩࡓࡧ࡭ࡦࠩᒪ"), caps.get(bstack1ll1ll1_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪ࠭ᒫ"), bstack1ll1ll1_opy_ (u"ࠧࠨᒬ")))
            if bstack1l111lll11l_opy_:
                self.logger.warning(bstack1ll1ll1_opy_ (u"ࠣࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡽࡩ࡭࡮ࠣࡶࡺࡴࠠࡰࡰ࡯ࡽࠥࡵ࡮ࠡࡆࡨࡷࡰࡺ࡯ࡱࠢࡥࡶࡴࡽࡳࡦࡴࡶ࠲ࠧᒭ"))
                return False
            browser = caps.get(bstack1ll1ll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧᒮ"), bstack1ll1ll1_opy_ (u"ࠪࠫᒯ")).lower()
            if browser != bstack1ll1ll1_opy_ (u"ࠫࡨ࡮ࡲࡰ࡯ࡨࠫᒰ"):
                self.logger.warning(bstack1ll1ll1_opy_ (u"ࠧࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡺ࡭ࡱࡲࠠࡳࡷࡱࠤࡴࡴ࡬ࡺࠢࡲࡲࠥࡉࡨࡳࡱࡰࡩࠥࡨࡲࡰࡹࡶࡩࡷࡹ࠮ࠣᒱ"))
                return False
            bstack1l111ll1l11_opy_ = bstack1l1111ll1ll_opy_
            if not self.config.get(bstack1ll1ll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠨᒲ")) or self.config.get(bstack1ll1ll1_opy_ (u"ࠧࡵࡷࡵࡦࡴࡹࡣࡢ࡮ࡨࠫᒳ")):
                bstack1l111ll1l11_opy_ = bstack1l111lll1ll_opy_
            browser_version = caps.get(bstack1ll1ll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩᒴ"))
            if not browser_version:
                browser_version = caps.get(bstack1ll1ll1_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪᒵ"), {}).get(bstack1ll1ll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫᒶ"), bstack1ll1ll1_opy_ (u"ࠫࠬᒷ"))
            if browser_version and browser_version != bstack1ll1ll1_opy_ (u"ࠬࡲࡡࡵࡧࡶࡸࠬᒸ") and int(browser_version.split(bstack1ll1ll1_opy_ (u"࠭࠮ࠨᒹ"))[0]) <= bstack1l111ll1l11_opy_:
                self.logger.warning(bstack1ll1ll1_opy_ (u"ࠢࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤࡼ࡯࡬࡭ࠢࡵࡹࡳࠦ࡯࡯࡮ࡼࠤࡴࡴࠠࡄࡪࡵࡳࡲ࡫ࠠࡣࡴࡲࡻࡸ࡫ࡲࠡࡸࡨࡶࡸ࡯࡯࡯ࠢࡪࡶࡪࡧࡴࡦࡴࠣࡸ࡭ࡧ࡮ࠡࠤᒺ") + str(bstack1l111ll1l11_opy_) + bstack1ll1ll1_opy_ (u"ࠣ࠰ࠥᒻ"))
                return False
            bstack1l111l1l1ll_opy_ = caps.get(bstack1ll1ll1_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪᒼ"), {}).get(bstack1ll1ll1_opy_ (u"ࠪࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪᒽ"))
            if not bstack1l111l1l1ll_opy_:
                bstack1l111l1l1ll_opy_ = caps.get(bstack1ll1ll1_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩᒾ"), {})
            if bstack1l111l1l1ll_opy_ and bstack1ll1ll1_opy_ (u"ࠬ࠳࠭ࡩࡧࡤࡨࡱ࡫ࡳࡴࠩᒿ") in bstack1l111l1l1ll_opy_.get(bstack1ll1ll1_opy_ (u"࠭ࡡࡳࡩࡶࠫᓀ"), []):
                self.logger.warning(bstack1ll1ll1_opy_ (u"ࠢࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤࡼ࡯࡬࡭ࠢࡱࡳࡹࠦࡲࡶࡰࠣࡳࡳࠦ࡬ࡦࡩࡤࡧࡾࠦࡨࡦࡣࡧࡰࡪࡹࡳࠡ࡯ࡲࡨࡪ࠴ࠠࡔࡹ࡬ࡸࡨ࡮ࠠࡵࡱࠣࡲࡪࡽࠠࡩࡧࡤࡨࡱ࡫ࡳࡴࠢࡰࡳࡩ࡫ࠠࡰࡴࠣࡥࡻࡵࡩࡥࠢࡸࡷ࡮ࡴࡧࠡࡪࡨࡥࡩࡲࡥࡴࡵࠣࡱࡴࡪࡥ࠯ࠤᓁ"))
                return False
            return True
        except Exception as error:
            self.logger.debug(bstack1ll1ll1_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡷࡣ࡯࡭ࡩࡧࡴࡦࠢࡤ࠵࠶ࡿࠠࡴࡷࡳࡴࡴࡸࡴࠡ࠼ࠥᓂ") + str(error))
            return False
    def bstack1l11l111111_opy_(self, test_uuid: str, result: structs.FetchDriverExecuteParamsEventResponse):
        bstack1l111l1111l_opy_ = {
            bstack1ll1ll1_opy_ (u"ࠩࡷ࡬࡙࡫ࡳࡵࡔࡸࡲ࡚ࡻࡩࡥࠩᓃ"): test_uuid,
        }
        bstack1l111l11ll1_opy_ = {}
        if result.success:
            bstack1l111l11ll1_opy_ = json.loads(result.accessibility_execute_params)
        return bstack1l111l1l1l1_opy_(bstack1l111l1111l_opy_, bstack1l111l11ll1_opy_)
    def bstack111l111l_opy_(self, driver: object, name: str, framework_name: str, test_uuid: str):
        bstack1ll111l11ll_opy_ = None
        try:
            self.bstack1llllll111l_opy_()
            req = structs.FetchDriverExecuteParamsEventRequest()
            req.bin_session_id = self.bin_session_id
            req.product = bstack1ll1ll1_opy_ (u"ࠥࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠥᓄ")
            req.script_name = bstack1ll1ll1_opy_ (u"ࠦࡸࡧࡶࡦࡔࡨࡷࡺࡲࡴࡴࠤᓅ")
            r = self.bstack1lllll1lll1_opy_.FetchDriverExecuteParamsEvent(req)
            if not r.success:
                self.logger.debug(bstack1ll1ll1_opy_ (u"ࠧࡸࡥࡤࡧ࡬ࡺࡪࡪࠠࡥࡴ࡬ࡺࡪࡸࠠࡦࡺࡨࡧࡺࡺࡥࠡࡲࡤࡶࡦࡳࡳࠡࡨࡵࡳࡲࠦࡳࡦࡴࡹࡩࡷࡀࠠࠣᓆ") + str(r.error) + bstack1ll1ll1_opy_ (u"ࠨࠢᓇ"))
            else:
                bstack1l111l1111l_opy_ = self.bstack1l11l111111_opy_(test_uuid, r)
                bstack1llll1l11ll_opy_ = r.script
            self.logger.debug(bstack1ll1ll1_opy_ (u"ࠧࡑࡧࡵࡪࡴࡸ࡭ࡪࡰࡪࠤࡸࡩࡡ࡯ࠢࡥࡩ࡫ࡵࡲࡦࠢࡶࡥࡻ࡯࡮ࡨࠢࡵࡩࡸࡻ࡬ࡵࡵࠪᓈ") + str(bstack1l111l1111l_opy_))
            self.perform_scan(driver, name, framework_name=framework_name)
            if not bstack1llll1l11ll_opy_:
                self.logger.debug(bstack1ll1ll1_opy_ (u"ࠣࡲࡨࡶ࡫ࡵࡲ࡮ࡡࡶࡧࡦࡴ࠺ࠡ࡯࡬ࡷࡸ࡯࡮ࡨࠢࠪࡷࡦࡼࡥࡓࡧࡶࡹࡱࡺࡳࠨࠢࡶࡧࡷ࡯ࡰࡵࠢࡩࡳࡷࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫࠽ࠣᓉ") + str(framework_name) + bstack1ll1ll1_opy_ (u"ࠤࠣࠦᓊ"))
                return
            bstack1ll111l11ll_opy_ = bstack1lllll1l11l_opy_.bstack1ll11l11l1l_opy_(EVENTS.bstack1l1111lll11_opy_.value)
            self.bstack1l111l1l111_opy_(driver, bstack1llll1l11ll_opy_, bstack1l111l1111l_opy_, framework_name)
            self.logger.info(bstack1ll1ll1_opy_ (u"ࠥࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡸࡪࡹࡴࡪࡰࡪࠤ࡫ࡵࡲࠡࡶ࡫࡭ࡸࠦࡴࡦࡵࡷࠤࡨࡧࡳࡦࠢ࡫ࡥࡸࠦࡥ࡯ࡦࡨࡨ࠳ࠨᓋ"))
            bstack1lllll1l11l_opy_.end(EVENTS.bstack1l1111lll11_opy_.value, bstack1ll111l11ll_opy_+bstack1ll1ll1_opy_ (u"ࠦ࠿ࡹࡴࡢࡴࡷࠦᓌ"), bstack1ll111l11ll_opy_+bstack1ll1ll1_opy_ (u"ࠧࡀࡥ࡯ࡦࠥᓍ"), True, None, command=bstack1ll1ll1_opy_ (u"࠭ࡳࡢࡸࡨࡖࡪࡹࡵ࡭ࡶࡶࠫᓎ"),test_name=name)
        except Exception as bstack1l111l11l1l_opy_:
            self.logger.error(bstack1ll1ll1_opy_ (u"ࠢࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡳࡧࡶࡹࡱࡺࡳࠡࡥࡲࡹࡱࡪࠠ࡯ࡱࡷࠤࡧ࡫ࠠࡱࡴࡲࡧࡪࡹࡳࡦࡦࠣࡪࡴࡸࠠࡵࡪࡨࠤࡹ࡫ࡳࡵࠢࡦࡥࡸ࡫࠺ࠡࠤᓏ") + bstack1ll1ll1_opy_ (u"ࠣࡵࡷࡶ࠭ࡶࡡࡵࡪࠬࠦᓐ") + bstack1ll1ll1_opy_ (u"ࠤࠣࡉࡷࡸ࡯ࡳࠢ࠽ࠦᓑ") + str(bstack1l111l11l1l_opy_))
            bstack1lllll1l11l_opy_.end(EVENTS.bstack1l1111lll11_opy_.value, bstack1ll111l11ll_opy_+bstack1ll1ll1_opy_ (u"ࠥ࠾ࡸࡺࡡࡳࡶࠥᓒ"), bstack1ll111l11ll_opy_+bstack1ll1ll1_opy_ (u"ࠦ࠿࡫࡮ࡥࠤᓓ"), False, bstack1l111l11l1l_opy_, command=bstack1ll1ll1_opy_ (u"ࠬࡹࡡࡷࡧࡕࡩࡸࡻ࡬ࡵࡵࠪᓔ"),test_name=name)
    def bstack1l111l1l111_opy_(self, driver, bstack1llll1l11ll_opy_, bstack1l111l1111l_opy_, framework_name):
        if framework_name == bstack1ll1ll1_opy_ (u"࠭ࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠪᓕ"):
            self.bstack1l11l11llll_opy_.bstack1lll1lll111_opy_(driver, bstack1llll1l11ll_opy_, bstack1l111l1111l_opy_)
        else:
            self.logger.debug(driver.execute_async_script(bstack1llll1l11ll_opy_, bstack1l111l1111l_opy_))
    def _1l111lll111_opy_(self, instance: bstack1llll1l1111_opy_, args: Tuple) -> list:
        bstack1ll1ll1_opy_ (u"ࠢࠣࠤࡈࡼࡹࡸࡡࡤࡶࠣࡸࡦ࡭ࡳࠡࡤࡤࡷࡪࡪࠠࡰࡰࠣࡸ࡭࡫ࠠࡵࡧࡶࡸࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫࠯ࠤࠥࠦᓖ")
        if bstack1ll1ll1_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠬᓗ") in instance.bstack1ll11111l1l_opy_:
            return args[2].tags if hasattr(args[2], bstack1ll1ll1_opy_ (u"ࠩࡷࡥ࡬ࡹࠧᓘ")) else []
        if hasattr(args[0], bstack1ll1ll1_opy_ (u"ࠪࡳࡼࡴ࡟࡮ࡣࡵ࡯ࡪࡸࡳࠨᓙ")):
            return [marker.name for marker in args[0].own_markers]
        return []
    def bstack1l111lllll1_opy_(self, tags, capabilities):
        return self.bstack111llllll_opy_(tags) and self.bstack1lll1ll111_opy_(capabilities)