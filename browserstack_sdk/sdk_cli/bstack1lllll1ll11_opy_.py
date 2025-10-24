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
from datetime import datetime
import os
import threading
from browserstack_sdk.sdk_cli.bstack11111111ll_opy_ import (
    bstack1lllllll11l_opy_,
    bstack1llll1l11l1_opy_,
    bstack1lll111llll_opy_,
    bstack1lllll111ll_opy_,
)
from browserstack_sdk.sdk_cli.bstack1111111111_opy_ import bstack1llll1lll1l_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1l1lll1_opy_, bstack1lll1ll1111_opy_, bstack1lll1l11111_opy_
from typing import Tuple, Dict, Any, List, Union
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1111111l1l_opy_ import bstack1llllll1111_opy_
from browserstack_sdk.sdk_cli.bstack1lll11l111l_opy_ import bstack1lll111lll1_opy_
from browserstack_sdk.sdk_cli.bstack1lll1ll1l1l_opy_ import bstack1lll1l111ll_opy_
from browserstack_sdk.sdk_cli.bstack1lll1lllll1_opy_ import bstack1lll11llll1_opy_
from bstack_utils.helper import bstack1l111ll1l1l_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
from bstack_utils.bstack11ll111ll1_opy_ import bstack1lllll1l111_opy_
import grpc
import traceback
import json
class bstack1l1l111ll11_opy_(bstack1llllll1111_opy_):
    bstack1l1ll11llll_opy_ = False
    bstack1l111l1l1l1_opy_ = bstack11l11l1_opy_ (u"ࠦࡸ࡫࡬ࡦࡰ࡬ࡹࡲ࠴ࡷࡦࡤࡧࡶ࡮ࡼࡥࡳࠤᑇ")
    bstack1l1111ll11l_opy_ = bstack11l11l1_opy_ (u"ࠧࡸࡥ࡮ࡱࡷࡩ࠳ࡽࡥࡣࡦࡵ࡭ࡻ࡫ࡲࠣᑈ")
    bstack1l111l111ll_opy_ = bstack11l11l1_opy_ (u"ࠨࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡥࡩ࡯࡫ࡷࠦᑉ")
    bstack1l1111l11ll_opy_ = bstack11l11l1_opy_ (u"ࠢࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿ࡟ࡪࡵࡢࡷࡨࡧ࡮࡯࡫ࡱ࡫ࠧᑊ")
    bstack1l111l11111_opy_ = bstack11l11l1_opy_ (u"ࠣࡦࡵ࡭ࡻ࡫ࡲࡠࡪࡤࡷࡤࡻࡲ࡭ࠤᑋ")
    scripts: Dict[str, Dict[str, str]]
    commands: Dict[str, Dict[str, Dict[str, List[str]]]]
    def __init__(self, bstack1l1ll111l11_opy_, bstack1ll1lll1lll_opy_):
        super().__init__()
        self.scripts = dict()
        self.commands = dict()
        self.accessibility = False
        self.bstack1l1111lllll_opy_ = False
        self.bstack1l1111l11l1_opy_ = dict()
        if not self.is_enabled():
            return
        self.bstack1l111lll1ll_opy_ = bstack1ll1lll1lll_opy_
        bstack1l1ll111l11_opy_.bstack1llll1l1l11_opy_((bstack1lllllll11l_opy_.bstack1111111l11_opy_, bstack1llll1l11l1_opy_.PRE), self.bstack1l111l1111l_opy_)
        TestFramework.bstack1llll1l1l11_opy_((bstack1lll1l1lll1_opy_.TEST, bstack1lll1ll1111_opy_.PRE), self.bstack1lll1ll11l1_opy_)
        TestFramework.bstack1llll1l1l11_opy_((bstack1lll1l1lll1_opy_.TEST, bstack1lll1ll1111_opy_.POST), self.bstack1lll1ll1lll_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1lll1ll11l1_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11111_opy_,
        bstack1lllllll1l1_opy_: Tuple[bstack1lll1l1lll1_opy_, bstack1lll1ll1111_opy_],
        *args,
        **kwargs,
    ):
        tags = self._1l1111ll111_opy_(instance, args)
        test_framework = f.get_state(instance, TestFramework.bstack1lll1ll11ll_opy_)
        if self.bstack1l1111lllll_opy_:
            self.bstack1l1111l11l1_opy_[bstack11l11l1_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠤᑌ")] = f.get_state(instance, TestFramework.bstack1lll1l11l11_opy_)
        if bstack11l11l1_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠧᑍ") in instance.bstack1l1llll1lll_opy_:
            platform_index = f.get_state(instance, TestFramework.bstack1lllll11111_opy_)
            self.accessibility = self.bstack1l111ll11ll_opy_(tags, self.config[bstack11l11l1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧᑎ")][platform_index])
        else:
            capabilities = self.bstack1l111lll1ll_opy_.bstack1lll1l1l111_opy_(f, instance, bstack1lllllll1l1_opy_, *args, **kwargs)
            if not capabilities:
                self.logger.debug(bstack11l11l1_opy_ (u"ࠧࡵ࡮ࡠࡤࡨࡪࡴࡸࡥࡠࡶࡨࡷࡹࡀࠠ࡯ࡱࠣࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠢࡩࡳࡺࡴࡤࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧᑏ") + str(kwargs) + bstack11l11l1_opy_ (u"ࠨࠢᑐ"))
                return
            self.accessibility = self.bstack1l111ll11ll_opy_(tags, capabilities)
        if self.bstack1l111lll1ll_opy_.pages and self.bstack1l111lll1ll_opy_.pages.values():
            bstack1l1111ll1ll_opy_ = list(self.bstack1l111lll1ll_opy_.pages.values())
            if bstack1l1111ll1ll_opy_ and isinstance(bstack1l1111ll1ll_opy_[0], (list, tuple)) and bstack1l1111ll1ll_opy_[0]:
                bstack1l111ll11l1_opy_ = bstack1l1111ll1ll_opy_[0][0]
                if callable(bstack1l111ll11l1_opy_):
                    page = bstack1l111ll11l1_opy_()
                    def bstack1l1l1lll1_opy_():
                        self.get_accessibility_results(page, bstack11l11l1_opy_ (u"ࠢࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠦᑑ"))
                    def bstack1l1111lll1l_opy_():
                        self.get_accessibility_results_summary(page, bstack11l11l1_opy_ (u"ࠣࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠧᑒ"))
                    setattr(page, bstack11l11l1_opy_ (u"ࠤࡪࡩࡹࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡗ࡫ࡳࡶ࡮ࡷࡷࠧᑓ"), bstack1l1l1lll1_opy_)
                    setattr(page, bstack11l11l1_opy_ (u"ࠥ࡫ࡪࡺࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡘࡥࡴࡷ࡯ࡸࡘࡻ࡭࡮ࡣࡵࡽࠧᑔ"), bstack1l1111lll1l_opy_)
        self.logger.debug(bstack11l11l1_opy_ (u"ࠦࡸ࡮࡯ࡶ࡮ࡧࠤࡷࡻ࡮ࠡࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡸࡤࡰࡺ࡫࠽ࠣᑕ") + str(self.accessibility) + bstack11l11l1_opy_ (u"ࠧࠨᑖ"))
    def bstack1l111l1111l_opy_(
        self,
        f: bstack1llll1lll1l_opy_,
        driver: object,
        exec: Tuple[bstack1lllll111ll_opy_, str],
        bstack1lllllll1l1_opy_: Tuple[bstack1lllllll11l_opy_, bstack1llll1l11l1_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        try:
            bstack1l11lll1ll_opy_ = datetime.now()
            self.bstack1l111ll1lll_opy_(f, exec, *args, **kwargs)
            instance, method_name = exec
            instance.bstack111lll1ll_opy_(bstack11l11l1_opy_ (u"ࠨࡡ࠲࠳ࡼ࠾࡮ࡴࡩࡵࡡࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡡࡦࡳࡳ࡬ࡩࡨࠤᑗ"), datetime.now() - bstack1l11lll1ll_opy_)
            if (
                not f.bstack1l1ll1ll11l_opy_(method_name)
                or f.bstack1l1lll1ll1l_opy_(method_name, *args)
                or f.bstack1l1ll1lll11_opy_(method_name, *args)
            ):
                return
            if not f.get_state(instance, bstack1l1l111ll11_opy_.bstack1l111l111ll_opy_, False):
                if not bstack1l1l111ll11_opy_.bstack1l1ll11llll_opy_:
                    self.logger.warning(bstack11l11l1_opy_ (u"ࠢ࡜ࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡢ࡭ࡳࡪࡥࡹ࠿ࠥᑘ") + str(f.platform_index) + bstack11l11l1_opy_ (u"ࠣ࡟ࠣࡥ࠶࠷ࡹࠡࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠠࡩࡣࡹࡩࠥࡴ࡯ࡵࠢࡥࡩࡪࡴࠠࡴࡧࡷࠤ࡫ࡵࡲࠡࡶ࡫࡭ࡸࠦࡳࡦࡵࡶ࡭ࡴࡴࠢᑙ"))
                    bstack1l1l111ll11_opy_.bstack1l1ll11llll_opy_ = True
                return
            bstack1l111ll1ll1_opy_ = self.scripts.get(f.framework_name, {})
            if not bstack1l111ll1ll1_opy_:
                platform_index = f.get_state(instance, bstack1llll1lll1l_opy_.bstack1lllll11111_opy_, 0)
                self.logger.debug(bstack11l11l1_opy_ (u"ࠤࡱࡳࠥࡧ࠱࠲ࡻࠣࡷࡨࡸࡩࡱࡶࡶࠤ࡫ࡵࡲࠡࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡢ࡭ࡳࡪࡥࡹ࠿ࡾࡴࡱࡧࡴࡧࡱࡵࡱࡤ࡯࡮ࡥࡧࡻࢁࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪࡃࠢᑚ") + str(f.framework_name) + bstack11l11l1_opy_ (u"ࠥࠦᑛ"))
                return
            command_name = f.bstack1l1lll111ll_opy_(*args)
            if not command_name:
                self.logger.debug(bstack11l11l1_opy_ (u"ࠦࡲ࡯ࡳࡴ࡫ࡱ࡫ࠥࡩ࡯࡮࡯ࡤࡲࡩࡥ࡮ࡢ࡯ࡨࠤ࡫ࡵࡲࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦ࠿ࡾࡪ࠳࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪࢃࠠ࡮ࡧࡷ࡬ࡴࡪ࡟࡯ࡣࡰࡩࡂࠨᑜ") + str(method_name) + bstack11l11l1_opy_ (u"ࠧࠨᑝ"))
                return
            bstack1l111ll111l_opy_ = f.get_state(instance, bstack1l1l111ll11_opy_.bstack1l111l11111_opy_, False)
            if command_name == bstack11l11l1_opy_ (u"ࠨࡧࡦࡶࠥᑞ") and not bstack1l111ll111l_opy_:
                f.bstack1llllllllll_opy_(instance, bstack1l1l111ll11_opy_.bstack1l111l11111_opy_, True)
                bstack1l111ll111l_opy_ = True
            if not bstack1l111ll111l_opy_ and not self.bstack1l1111lllll_opy_:
                self.logger.debug(bstack11l11l1_opy_ (u"ࠢ࡯ࡱ࡙ࠣࡗࡒࠠ࡭ࡱࡤࡨࡪࡪࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡲࡦࡳࡥ࠾ࡽࡩ࠲࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟࡯ࡣࡰࡩࢂࠦࡣࡰ࡯ࡰࡥࡳࡪ࡟࡯ࡣࡰࡩࡂࠨᑟ") + str(command_name) + bstack11l11l1_opy_ (u"ࠣࠤᑠ"))
                return
            scripts_to_run = self.commands.get(f.framework_name, {}).get(method_name, {}).get(command_name, [])
            if not scripts_to_run:
                self.logger.debug(bstack11l11l1_opy_ (u"ࠤࡱࡳࠥࡧ࠱࠲ࡻࠣࡷࡨࡸࡩࡱࡶࡶࠤ࡫ࡵࡲࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦ࠿ࡾࡪ࠳࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪࢃࠠࡤࡱࡰࡱࡦࡴࡤࡠࡰࡤࡱࡪࡃࠢᑡ") + str(command_name) + bstack11l11l1_opy_ (u"ࠥࠦᑢ"))
                return
            self.logger.info(bstack11l11l1_opy_ (u"ࠦࡷࡻ࡮࡯࡫ࡱ࡫ࠥࢁ࡬ࡦࡰࠫࡷࡨࡸࡩࡱࡶࡶࡣࡹࡵ࡟ࡳࡷࡱ࠭ࢂࠦࡳࡤࡴ࡬ࡴࡹࡹࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡲࡦࡳࡥ࠾ࡽࡩ࠲࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟࡯ࡣࡰࡩࢂࠦࡣࡰ࡯ࡰࡥࡳࡪ࡟࡯ࡣࡰࡩࡂࠨᑣ") + str(command_name) + bstack11l11l1_opy_ (u"ࠧࠨᑤ"))
            scripts = [(s, bstack1l111ll1ll1_opy_[s]) for s in scripts_to_run if s in bstack1l111ll1ll1_opy_]
            for script_name, bstack1llll111111_opy_ in scripts:
                try:
                    bstack1l11lll1ll_opy_ = datetime.now()
                    if script_name == bstack11l11l1_opy_ (u"ࠨࡳࡤࡣࡱࠦᑥ"):
                        result = self.perform_scan(driver, method=command_name, framework_name=f.framework_name)
                    instance.bstack111lll1ll_opy_(bstack11l11l1_opy_ (u"ࠢࡢ࠳࠴ࡽ࠿ࠨᑦ") + script_name, datetime.now() - bstack1l11lll1ll_opy_)
                    if isinstance(result, dict) and not result.get(bstack11l11l1_opy_ (u"ࠣࡵࡸࡧࡨ࡫ࡳࡴࠤᑧ"), True):
                        self.logger.warning(bstack11l11l1_opy_ (u"ࠤࡶ࡯࡮ࡶࠠࡦࡺࡨࡧࡺࡺࡩ࡯ࡩࠣࡶࡪࡳࡡࡪࡰ࡬ࡲ࡬ࠦࡳࡤࡴ࡬ࡴࡹࡹ࠺ࠡࠤᑨ") + str(result) + bstack11l11l1_opy_ (u"ࠥࠦᑩ"))
                        break
                except Exception as e:
                    self.logger.error(bstack11l11l1_opy_ (u"ࠦࡪࡸࡲࡰࡴࠣࡩࡽ࡫ࡣࡶࡶ࡬ࡲ࡬ࠦࡳࡤࡴ࡬ࡴࡹࡃࡻࡴࡥࡵ࡭ࡵࡺ࡟࡯ࡣࡰࡩࢂࠦࡥࡳࡴࡲࡶࡂࠨᑪ") + str(e) + bstack11l11l1_opy_ (u"ࠧࠨᑫ"))
        except Exception as e:
            self.logger.error(bstack11l11l1_opy_ (u"ࠨ࡯࡯ࡡࡥࡩ࡫ࡵࡲࡦࡡࡨࡼࡪࡩࡵࡵࡧࠣࡩࡷࡸ࡯ࡳ࠿ࠥᑬ") + str(e) + bstack11l11l1_opy_ (u"ࠢࠣᑭ"))
    def bstack1lll1ll1lll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11111_opy_,
        bstack1lllllll1l1_opy_: Tuple[bstack1lll1l1lll1_opy_, bstack1lll1ll1111_opy_],
        *args,
        **kwargs,
    ):
        tags = self._1l1111ll111_opy_(instance, args)
        capabilities = self.bstack1l111lll1ll_opy_.bstack1lll1l1l111_opy_(f, instance, bstack1lllllll1l1_opy_, *args, **kwargs)
        self.accessibility = self.bstack1l111ll11ll_opy_(tags, capabilities)
        if not self.accessibility:
            self.logger.debug(bstack11l11l1_opy_ (u"ࠣࡱࡱࡣࡦ࡬ࡴࡦࡴࡢࡸࡪࡹࡴ࠻ࠢࡤ࠵࠶ࡿࠠ࡯ࡱࡷࠤࡪࡴࡡࡣ࡮ࡨࡨࠧᑮ"))
            return
        driver = self.bstack1l111lll1ll_opy_.bstack1lll1ll1l11_opy_(f, instance, bstack1lllllll1l1_opy_, *args, **kwargs)
        test_name = f.get_state(instance, TestFramework.bstack1ll1l1ll1ll_opy_)
        if not test_name:
            self.logger.debug(bstack11l11l1_opy_ (u"ࠤࡲࡲࡤࡧࡦࡵࡧࡵࡣࡹ࡫ࡳࡵ࠼ࠣࡱ࡮ࡹࡳࡪࡰࡪࠤࡹ࡫ࡳࡵࠢࡱࡥࡲ࡫ࠢᑯ"))
            return
        test_uuid = f.get_state(instance, TestFramework.bstack1lll1l11l11_opy_)
        if not test_uuid:
            self.logger.debug(bstack11l11l1_opy_ (u"ࠥࡳࡳࡥࡡࡧࡶࡨࡶࡤࡺࡥࡴࡶ࠽ࠤࡲ࡯ࡳࡴ࡫ࡱ࡫ࠥࡺࡥࡴࡶࠣࡹࡺ࡯ࡤࠣᑰ"))
            return
        if isinstance(self.bstack1l111lll1ll_opy_, bstack1lll1l111ll_opy_):
            framework_name = bstack11l11l1_opy_ (u"ࠫࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠨᑱ")
        else:
            framework_name = bstack11l11l1_opy_ (u"ࠬࡹࡥ࡭ࡧࡱ࡭ࡺࡳࠧᑲ")
        self.bstack111ll11l_opy_(driver, test_name, framework_name, test_uuid)
    def perform_scan(self, driver: object, method: Union[None, str], framework_name: str):
        bstack1ll11llllll_opy_ = bstack1lllll1l111_opy_.bstack1ll11111ll1_opy_(EVENTS.bstack11l1111l11_opy_.value)
        if not self.accessibility:
            self.logger.debug(bstack11l11l1_opy_ (u"ࠨࡰࡦࡴࡩࡳࡷࡳ࡟ࡴࡥࡤࡲ࠿ࠦࡡ࠲࠳ࡼࠤࡳࡵࡴࠡࡧࡱࡥࡧࡲࡥࡥࠢࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡴࡡ࡮ࡧࡀࡿ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟࡯ࡣࡰࡩࢂࠦࠢᑳ"))
            return
        bstack1l11lll1ll_opy_ = datetime.now()
        bstack1llll111111_opy_ = self.scripts.get(framework_name, {}).get(bstack11l11l1_opy_ (u"ࠢࡴࡥࡤࡲࠧᑴ"), None)
        if not bstack1llll111111_opy_:
            self.logger.debug(bstack11l11l1_opy_ (u"ࠣࡲࡨࡶ࡫ࡵࡲ࡮ࡡࡶࡧࡦࡴ࠺ࠡ࡯࡬ࡷࡸ࡯࡮ࡨࠢࠪࡷࡨࡧ࡮ࠨࠢࡶࡧࡷ࡯ࡰࡵࠢࡩࡳࡷࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫࠽ࠣᑵ") + str(framework_name) + bstack11l11l1_opy_ (u"ࠤࠣࠦᑶ"))
            return
        if self.bstack1l1111lllll_opy_:
            arg = dict()
            arg[bstack11l11l1_opy_ (u"ࠥࡱࡪࡺࡨࡰࡦࠥᑷ")] = method if method else bstack11l11l1_opy_ (u"ࠦࠧᑸ")
            arg[bstack11l11l1_opy_ (u"ࠧࡺࡨࡕࡧࡶࡸࡗࡻ࡮ࡖࡷ࡬ࡨࠧᑹ")] = self.bstack1l1111l11l1_opy_[bstack11l11l1_opy_ (u"ࠨࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩࠨᑺ")]
            arg[bstack11l11l1_opy_ (u"ࠢࡵࡪࡅࡹ࡮ࡲࡤࡖࡷ࡬ࡨࠧᑻ")] = self.bstack1l1111l11l1_opy_[bstack11l11l1_opy_ (u"ࠣࡶࡨࡷࡹ࡮ࡵࡣࡡࡥࡹ࡮ࡲࡤࡠࡷࡸ࡭ࡩࠨᑼ")]
            arg[bstack11l11l1_opy_ (u"ࠤࡤࡹࡹ࡮ࡈࡦࡣࡧࡩࡷࠨᑽ")] = self.bstack1l1111l11l1_opy_[bstack11l11l1_opy_ (u"ࠥࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡗࡳࡰ࡫࡮ࠣᑾ")]
            arg[bstack11l11l1_opy_ (u"ࠦࡹ࡮ࡊࡸࡶࡗࡳࡰ࡫࡮ࠣᑿ")] = self.bstack1l1111l11l1_opy_[bstack11l11l1_opy_ (u"ࠧࡺࡨࡠ࡬ࡺࡸࡤࡺ࡯࡬ࡧࡱࠦᒀ")]
            arg[bstack11l11l1_opy_ (u"ࠨࡳࡤࡣࡱࡘ࡮ࡳࡥࡴࡶࡤࡱࡵࠨᒁ")] = str(int(datetime.now().timestamp() * 1000))
            bstack1l111ll1111_opy_ = bstack1llll111111_opy_ % json.dumps(arg)
            driver.execute_script(bstack1l111ll1111_opy_)
            return
        instance = bstack1lll111llll_opy_.bstack1ll1111l111_opy_(driver)
        if instance:
            if not bstack1lll111llll_opy_.get_state(instance, bstack1l1l111ll11_opy_.bstack1l1111l11ll_opy_, False):
                bstack1lll111llll_opy_.bstack1llllllllll_opy_(instance, bstack1l1l111ll11_opy_.bstack1l1111l11ll_opy_, True)
            else:
                self.logger.info(bstack11l11l1_opy_ (u"ࠢࡱࡧࡵࡪࡴࡸ࡭ࡠࡵࡦࡥࡳࡀࠠࡢ࡮ࡵࡩࡦࡪࡹࠡ࡫ࡱࠤࡵࡸ࡯ࡨࡴࡨࡷࡸࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫࠽ࡼࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦࡿࠣࡱࡪࡺࡨࡰࡦࡀࠦᒂ") + str(method) + bstack11l11l1_opy_ (u"ࠣࠤᒃ"))
                return
        self.logger.info(bstack11l11l1_opy_ (u"ࠤࡳࡩࡷ࡬࡯ࡳ࡯ࡢࡷࡨࡧ࡮࠻ࠢࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡴࡡ࡮ࡧࡀࡿ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟࡯ࡣࡰࡩࢂࠦ࡭ࡦࡶ࡫ࡳࡩࡃࠢᒄ") + str(method) + bstack11l11l1_opy_ (u"ࠥࠦᒅ"))
        if framework_name == bstack11l11l1_opy_ (u"ࠫࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠨᒆ"):
            result = self.bstack1l111lll1ll_opy_.bstack1lll1l1l1ll_opy_(driver, bstack1llll111111_opy_)
        else:
            result = driver.execute_async_script(bstack1llll111111_opy_, {bstack11l11l1_opy_ (u"ࠧࡳࡥࡵࡪࡲࡨࠧᒇ"): method if method else bstack11l11l1_opy_ (u"ࠨࠢᒈ")})
        bstack1lllll1l111_opy_.end(EVENTS.bstack11l1111l11_opy_.value, bstack1ll11llllll_opy_+bstack11l11l1_opy_ (u"ࠢ࠻ࡵࡷࡥࡷࡺࠢᒉ"), bstack1ll11llllll_opy_+bstack11l11l1_opy_ (u"ࠣ࠼ࡨࡲࡩࠨᒊ"), True, None, command=method)
        if instance:
            bstack1lll111llll_opy_.bstack1llllllllll_opy_(instance, bstack1l1l111ll11_opy_.bstack1l1111l11ll_opy_, False)
            instance.bstack111lll1ll_opy_(bstack11l11l1_opy_ (u"ࠤࡤ࠵࠶ࡿ࠺ࡱࡧࡵࡪࡴࡸ࡭ࡠࡵࡦࡥࡳࠨᒋ"), datetime.now() - bstack1l11lll1ll_opy_)
        return result
        def bstack1l11111llll_opy_(self, driver: object, framework_name, bstack11lll1l111_opy_: str):
            self.bstack1llll1lllll_opy_()
            req = structs.AccessibilityResultRequest()
            req.bin_session_id = self.bin_session_id
            req.bstack1l111l11ll1_opy_ = self.bstack1l1111l11l1_opy_[bstack11l11l1_opy_ (u"ࠥࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠥᒌ")]
            req.bstack11lll1l111_opy_ = bstack11lll1l111_opy_
            req.session_id = self.bin_session_id
            try:
                r = self.bstack1lllllll1ll_opy_.AccessibilityResult(req)
                if not r.success:
                    self.logger.debug(bstack11l11l1_opy_ (u"ࠦࡷ࡫ࡣࡦ࡫ࡹࡩࡩࠦࡦࡳࡱࡰࠤࡸ࡫ࡲࡷࡧࡵ࠾ࠥࠨᒍ") + str(r) + bstack11l11l1_opy_ (u"ࠧࠨᒎ"))
                else:
                    bstack1l1111l1l11_opy_ = json.loads(r.bstack1l1111l111l_opy_.decode(bstack11l11l1_opy_ (u"࠭ࡵࡵࡨ࠰࠼ࠬᒏ")))
                    if bstack11lll1l111_opy_ == bstack11l11l1_opy_ (u"ࠧࡨࡧࡷࡖࡪࡹࡵ࡭ࡶࡶࠫᒐ"):
                        return bstack1l1111l1l11_opy_.get(bstack11l11l1_opy_ (u"ࠣࡦࡤࡸࡦࠨᒑ"), [])
                    else:
                        return bstack1l1111l1l11_opy_.get(bstack11l11l1_opy_ (u"ࠤࡧࡥࡹࡧࠢᒒ"), {})
            except grpc.RpcError as e:
                self.logger.error(bstack11l11l1_opy_ (u"ࠥࡶࡵࡩ࠭ࡦࡴࡵࡳࡷࠦࡷࡩ࡫࡯ࡩࠥ࡬ࡥࡵࡥ࡫࡭ࡳ࡭ࠠࡨࡧࡷࡣࡦࡶࡰࡠࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡠࡴࡨࡷࡺࡲࡴࠡࡨࡵࡳࡲࠦࡣ࡭࡫࠽ࠤࠧᒓ") + str(e) + bstack11l11l1_opy_ (u"ࠦࠧᒔ"))
    @measure(event_name=EVENTS.bstack1l1llll11_opy_, stage=STAGE.bstack1ll1lllll_opy_)
    def get_accessibility_results(self, driver: object, framework_name):
        if not self.accessibility:
            self.logger.debug(bstack11l11l1_opy_ (u"ࠧ࡭ࡥࡵࡡࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡡࡵࡩࡸࡻ࡬ࡵࡵ࠽ࠤࡦ࠷࠱ࡺࠢࡱࡳࡹࠦࡥ࡯ࡣࡥࡰࡪࡪࠢᒕ"))
            return
        if self.bstack1l1111lllll_opy_:
            self.logger.debug(bstack11l11l1_opy_ (u"࠭ࡐࡦࡴࡩࡳࡷࡳࡩ࡯ࡩࠣࡷࡨࡧ࡮ࠡࡨࡲࡶࠥࡧࡰࡱࠢࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩᒖ"))
            self.perform_scan(driver, method=None, framework_name=framework_name)
            return self.bstack1l11111llll_opy_(driver, framework_name, bstack11l11l1_opy_ (u"ࠢࡨࡧࡷࡖࡪࡹࡵ࡭ࡶࡶࠦᒗ"))
        bstack1llll111111_opy_ = self.scripts.get(framework_name, {}).get(bstack11l11l1_opy_ (u"ࠣࡩࡨࡸࡗ࡫ࡳࡶ࡮ࡷࡷࠧᒘ"), None)
        if not bstack1llll111111_opy_:
            self.logger.debug(bstack11l11l1_opy_ (u"ࠤࡰ࡭ࡸࡹࡩ࡯ࡩࠣࠫ࡬࡫ࡴࡓࡧࡶࡹࡱࡺࡳࠨࠢࡶࡧࡷ࡯ࡰࡵࠢࡩࡳࡷࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫࠽ࠣᒙ") + str(framework_name) + bstack11l11l1_opy_ (u"ࠥࠦᒚ"))
            return
        self.perform_scan(driver, method=None, framework_name=framework_name)
        bstack1l11lll1ll_opy_ = datetime.now()
        if framework_name == bstack11l11l1_opy_ (u"ࠫࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠨᒛ"):
            result = self.bstack1l111lll1ll_opy_.bstack1lll1l1l1ll_opy_(driver, bstack1llll111111_opy_)
        else:
            result = driver.execute_async_script(bstack1llll111111_opy_)
        instance = bstack1lll111llll_opy_.bstack1ll1111l111_opy_(driver)
        if instance:
            instance.bstack111lll1ll_opy_(bstack11l11l1_opy_ (u"ࠧࡧ࠱࠲ࡻ࠽࡫ࡪࡺ࡟ࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿ࡟ࡳࡧࡶࡹࡱࡺࡳࠣᒜ"), datetime.now() - bstack1l11lll1ll_opy_)
        return result
    @measure(event_name=EVENTS.bstack111l1llll1_opy_, stage=STAGE.bstack1ll1lllll_opy_)
    def get_accessibility_results_summary(self, driver: object, framework_name):
        if not self.accessibility:
            self.logger.debug(bstack11l11l1_opy_ (u"ࠨࡧࡦࡶࡢࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡢࡶࡪࡹࡵ࡭ࡶࡶࡣࡸࡻ࡭࡮ࡣࡵࡽ࠿ࠦࡡ࠲࠳ࡼࠤࡳࡵࡴࠡࡧࡱࡥࡧࡲࡥࡥࠤᒝ"))
            return
        if self.bstack1l1111lllll_opy_:
            self.perform_scan(driver, method=None, framework_name=framework_name)
            return self.bstack1l11111llll_opy_(driver, framework_name, bstack11l11l1_opy_ (u"ࠧࡨࡧࡷࡖࡪࡹࡵ࡭ࡶࡶࡗࡺࡳ࡭ࡢࡴࡼࠫᒞ"))
        bstack1llll111111_opy_ = self.scripts.get(framework_name, {}).get(bstack11l11l1_opy_ (u"ࠣࡩࡨࡸࡗ࡫ࡳࡶ࡮ࡷࡷࡘࡻ࡭࡮ࡣࡵࡽࠧᒟ"), None)
        if not bstack1llll111111_opy_:
            self.logger.debug(bstack11l11l1_opy_ (u"ࠤࡰ࡭ࡸࡹࡩ࡯ࡩࠣࠫ࡬࡫ࡴࡓࡧࡶࡹࡱࡺࡳࡔࡷࡰࡱࡦࡸࡹࠨࠢࡶࡧࡷ࡯ࡰࡵࠢࡩࡳࡷࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫࠽ࠣᒠ") + str(framework_name) + bstack11l11l1_opy_ (u"ࠥࠦᒡ"))
            return
        self.perform_scan(driver, method=None, framework_name=framework_name)
        bstack1l11lll1ll_opy_ = datetime.now()
        if framework_name == bstack11l11l1_opy_ (u"ࠫࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠨᒢ"):
            result = self.bstack1l111lll1ll_opy_.bstack1lll1l1l1ll_opy_(driver, bstack1llll111111_opy_)
        else:
            result = driver.execute_async_script(bstack1llll111111_opy_)
        instance = bstack1lll111llll_opy_.bstack1ll1111l111_opy_(driver)
        if instance:
            instance.bstack111lll1ll_opy_(bstack11l11l1_opy_ (u"ࠧࡧ࠱࠲ࡻ࠽࡫ࡪࡺ࡟ࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿ࡟ࡳࡧࡶࡹࡱࡺࡳࡠࡵࡸࡱࡲࡧࡲࡺࠤᒣ"), datetime.now() - bstack1l11lll1ll_opy_)
        return result
    @measure(event_name=EVENTS.bstack1l111l1ll11_opy_, stage=STAGE.bstack1ll1lllll_opy_)
    def bstack1l111l1l11l_opy_(
        self,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        hub_url: str,
    ):
        self.bstack1llll1lllll_opy_()
        req = structs.AccessibilityConfigRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.hub_url = hub_url
        try:
            r = self.bstack1lllllll1ll_opy_.AccessibilityConfig(req)
            if not r.success:
                self.logger.debug(bstack11l11l1_opy_ (u"ࠨࡲࡦࡥࡨ࡭ࡻ࡫ࡤࠡࡨࡵࡳࡲࠦࡳࡦࡴࡹࡩࡷࡀࠠࠣᒤ") + str(r) + bstack11l11l1_opy_ (u"ࠢࠣᒥ"))
            else:
                self.bstack1l1111l1l1l_opy_(framework_name, r)
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack11l11l1_opy_ (u"ࠣࡴࡳࡧ࠲࡫ࡲࡳࡱࡵ࠾ࠥࠨᒦ") + str(e) + bstack11l11l1_opy_ (u"ࠤࠥᒧ"))
            traceback.print_exc()
            raise e
    def bstack1l1111l1l1l_opy_(self, framework_name: str, result: structs.AccessibilityConfigResponse) -> bool:
        if not result.success or not result.accessibility.success:
            self.logger.debug(bstack11l11l1_opy_ (u"ࠥࡰࡴࡧࡤࡠࡥࡲࡲ࡫࡯ࡧ࠻ࠢࡤ࠵࠶ࡿࠠ࡯ࡱࡷࠤ࡫ࡵࡵ࡯ࡦࠥᒨ"))
            return False
        if result.accessibility.is_app_accessibility:
            self.bstack1l1111lllll_opy_ = result.accessibility.is_app_accessibility
        if result.testhub.build_hashed_id:
            self.bstack1l1111l11l1_opy_[bstack11l11l1_opy_ (u"ࠦࡹ࡫ࡳࡵࡪࡸࡦࡤࡨࡵࡪ࡮ࡧࡣࡺࡻࡩࡥࠤᒩ")] = result.testhub.build_hashed_id
        if result.testhub.jwt:
            self.bstack1l1111l11l1_opy_[bstack11l11l1_opy_ (u"ࠧࡺࡨࡠ࡬ࡺࡸࡤࡺ࡯࡬ࡧࡱࠦᒪ")] = result.testhub.jwt
        if result.accessibility.options:
            options = result.accessibility.options
            if options.capabilities:
                for caps in options.capabilities:
                    self.bstack1l1111l11l1_opy_[caps.name] = caps.value
            if options.scripts:
                self.scripts[framework_name] = {row.name: row.command for row in options.scripts}
            if options.commands_to_wrap and options.commands_to_wrap.commands:
                scripts_to_run = [s for s in options.commands_to_wrap.scripts_to_run]
                if not scripts_to_run:
                    return False
                bstack1l111l11lll_opy_ = dict()
                for command in options.commands_to_wrap.commands:
                    if command.library == self.bstack1l111l1l1l1_opy_ and command.module == self.bstack1l1111ll11l_opy_:
                        if command.method and not command.method in bstack1l111l11lll_opy_:
                            bstack1l111l11lll_opy_[command.method] = dict()
                        if command.name and not command.name in bstack1l111l11lll_opy_[command.method]:
                            bstack1l111l11lll_opy_[command.method][command.name] = list()
                        bstack1l111l11lll_opy_[command.method][command.name].extend(scripts_to_run)
                self.commands[framework_name] = bstack1l111l11lll_opy_
        return bool(self.commands.get(framework_name, None))
    def bstack1l111ll1lll_opy_(
        self,
        f: bstack1llll1lll1l_opy_,
        exec: Tuple[bstack1lllll111ll_opy_, str],
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if isinstance(self.bstack1l111lll1ll_opy_, bstack1lll1l111ll_opy_) and method_name != bstack11l11l1_opy_ (u"࠭ࡣࡰࡰࡱࡩࡨࡺࠧᒫ"):
            return
        if bstack1lll111llll_opy_.bstack1lllll1l1ll_opy_(instance, bstack1l1l111ll11_opy_.bstack1l111l111ll_opy_):
            return
        if f.bstack1llllll11l1_opy_(method_name, *args):
            bstack1l111l1ll1l_opy_ = False
            desired_capabilities = f.bstack1l1lll11lll_opy_(instance)
            if isinstance(desired_capabilities, dict):
                hub_url = f.bstack1l1ll1lllll_opy_(instance)
                platform_index = f.get_state(instance, bstack1llll1lll1l_opy_.bstack1lllll11111_opy_, 0)
                bstack1l1111ll1l1_opy_ = datetime.now()
                r = self.bstack1l111l1l11l_opy_(platform_index, f.framework_name, f.framework_version, hub_url)
                instance.bstack111lll1ll_opy_(bstack11l11l1_opy_ (u"ࠢࡨࡴࡳࡧ࠿ࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡤࡩ࡯࡯ࡨ࡬࡫ࠧᒬ"), datetime.now() - bstack1l1111ll1l1_opy_)
                bstack1l111l1ll1l_opy_ = r.success
            else:
                self.logger.error(bstack11l11l1_opy_ (u"ࠣ࡯࡬ࡷࡸ࡯࡮ࡨࠢࡧࡩࡸ࡯ࡲࡦࡦࠣࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴ࠿ࠥᒭ") + str(desired_capabilities) + bstack11l11l1_opy_ (u"ࠤࠥᒮ"))
            f.bstack1llllllllll_opy_(instance, bstack1l1l111ll11_opy_.bstack1l111l111ll_opy_, bstack1l111l1ll1l_opy_)
    def bstack11l1l1l1l_opy_(self, test_tags):
        bstack1l111l1l11l_opy_ = self.config.get(bstack11l11l1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪᒯ"))
        if not bstack1l111l1l11l_opy_:
            return True
        try:
            include_tags = bstack1l111l1l11l_opy_[bstack11l11l1_opy_ (u"ࠫ࡮ࡴࡣ࡭ࡷࡧࡩ࡙ࡧࡧࡴࡋࡱࡘࡪࡹࡴࡪࡰࡪࡗࡨࡵࡰࡦࠩᒰ")] if bstack11l11l1_opy_ (u"ࠬ࡯࡮ࡤ࡮ࡸࡨࡪ࡚ࡡࡨࡵࡌࡲ࡙࡫ࡳࡵ࡫ࡱ࡫ࡘࡩ࡯ࡱࡧࠪᒱ") in bstack1l111l1l11l_opy_ and isinstance(bstack1l111l1l11l_opy_[bstack11l11l1_opy_ (u"࠭ࡩ࡯ࡥ࡯ࡹࡩ࡫ࡔࡢࡩࡶࡍࡳ࡚ࡥࡴࡶ࡬ࡲ࡬࡙ࡣࡰࡲࡨࠫᒲ")], list) else []
            exclude_tags = bstack1l111l1l11l_opy_[bstack11l11l1_opy_ (u"ࠧࡦࡺࡦࡰࡺࡪࡥࡕࡣࡪࡷࡎࡴࡔࡦࡵࡷ࡭ࡳ࡭ࡓࡤࡱࡳࡩࠬᒳ")] if bstack11l11l1_opy_ (u"ࠨࡧࡻࡧࡱࡻࡤࡦࡖࡤ࡫ࡸࡏ࡮ࡕࡧࡶࡸ࡮ࡴࡧࡔࡥࡲࡴࡪ࠭ᒴ") in bstack1l111l1l11l_opy_ and isinstance(bstack1l111l1l11l_opy_[bstack11l11l1_opy_ (u"ࠩࡨࡼࡨࡲࡵࡥࡧࡗࡥ࡬ࡹࡉ࡯ࡖࡨࡷࡹ࡯࡮ࡨࡕࡦࡳࡵ࡫ࠧᒵ")], list) else []
            excluded = any(tag in exclude_tags for tag in test_tags)
            included = len(include_tags) == 0 or any(tag in include_tags for tag in test_tags)
            return not excluded and included
        except Exception as error:
            self.logger.debug(bstack11l11l1_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡺ࡬࡮ࡲࡥࠡࡸࡤࡰ࡮ࡪࡡࡵ࡫ࡱ࡫ࠥࡺࡥࡴࡶࠣࡧࡦࡹࡥࠡࡨࡲࡶࠥࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡨࡥࡧࡱࡵࡩࠥࡹࡣࡢࡰࡱ࡭ࡳ࡭࠮ࠡࡇࡵࡶࡴࡸࠠ࠻ࠢࠥᒶ") + str(error))
        return False
    def bstack111l11111_opy_(self, caps):
        try:
            if self.bstack1l1111lllll_opy_:
                bstack1l1111lll11_opy_ = caps.get(bstack11l11l1_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲࡔࡡ࡮ࡧࠥᒷ"))
                if bstack1l1111lll11_opy_ is not None and str(bstack1l1111lll11_opy_).lower() == bstack11l11l1_opy_ (u"ࠧࡧ࡮ࡥࡴࡲ࡭ࡩࠨᒸ"):
                    bstack1l111ll1l11_opy_ = caps.get(bstack11l11l1_opy_ (u"ࠨࡡࡱࡲ࡬ࡹࡲࡀࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠣᒹ")) or caps.get(bstack11l11l1_opy_ (u"ࠢࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡘࡨࡶࡸ࡯࡯࡯ࠤᒺ"))
                    if bstack1l111ll1l11_opy_ is not None and int(bstack1l111ll1l11_opy_) < 11:
                        self.logger.warning(bstack11l11l1_opy_ (u"ࠣࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡽࡩ࡭࡮ࠣࡶࡺࡴࠠࡰࡰ࡯ࡽࠥࡵ࡮ࠡࡃࡱࡨࡷࡵࡩࡥࠢ࠴࠵ࠥࡧ࡮ࡥࠢࡤࡦࡴࡼࡥ࠯ࠢࡆࡹࡷࡸࡥ࡯ࡶࠣࡴࡱࡧࡴࡧࡱࡵࡱࠥࡼࡥࡳࡵ࡬ࡳࡳࠦ࠽ࠣᒻ") + str(bstack1l111ll1l11_opy_) + bstack11l11l1_opy_ (u"ࠤࠥᒼ"))
                        return False
                return True
            bstack1l111l1lll1_opy_ = caps.get(bstack11l11l1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫᒽ"), {}).get(bstack11l11l1_opy_ (u"ࠫࡩ࡫ࡶࡪࡥࡨࡒࡦࡳࡥࠨᒾ"), caps.get(bstack11l11l1_opy_ (u"ࠬࡪࡥࡷ࡫ࡦࡩࠬᒿ"), bstack11l11l1_opy_ (u"࠭ࠧᓀ")))
            if bstack1l111l1lll1_opy_:
                self.logger.warning(bstack11l11l1_opy_ (u"ࠢࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤࡼ࡯࡬࡭ࠢࡵࡹࡳࠦ࡯࡯࡮ࡼࠤࡴࡴࠠࡅࡧࡶ࡯ࡹࡵࡰࠡࡤࡵࡳࡼࡹࡥࡳࡵ࠱ࠦᓁ"))
                return False
            browser = caps.get(bstack11l11l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭ᓂ"), bstack11l11l1_opy_ (u"ࠩࠪᓃ")).lower()
            if browser != bstack11l11l1_opy_ (u"ࠪࡧ࡭ࡸ࡯࡮ࡧࠪᓄ"):
                self.logger.warning(bstack11l11l1_opy_ (u"ࠦࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡹ࡬ࡰࡱࠦࡲࡶࡰࠣࡳࡳࡲࡹࠡࡱࡱࠤࡈ࡮ࡲࡰ࡯ࡨࠤࡧࡸ࡯ࡸࡵࡨࡶࡸ࠴ࠢᓅ"))
                return False
            bstack1l111l1l111_opy_ = bstack1l1111l1ll1_opy_
            if not self.config.get(bstack11l11l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠧᓆ")) or self.config.get(bstack11l11l1_opy_ (u"࠭ࡴࡶࡴࡥࡳࡸࡩࡡ࡭ࡧࠪᓇ")):
                bstack1l111l1l111_opy_ = bstack1l111l1l1ll_opy_
            browser_version = caps.get(bstack11l11l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨᓈ"))
            if not browser_version:
                browser_version = caps.get(bstack11l11l1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩᓉ"), {}).get(bstack11l11l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪᓊ"), bstack11l11l1_opy_ (u"ࠪࠫᓋ"))
            if browser_version and browser_version != bstack11l11l1_opy_ (u"ࠫࡱࡧࡴࡦࡵࡷࠫᓌ") and int(browser_version.split(bstack11l11l1_opy_ (u"ࠬ࠴ࠧᓍ"))[0]) <= bstack1l111l1l111_opy_:
                self.logger.warning(bstack11l11l1_opy_ (u"ࠨࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡻ࡮ࡲ࡬ࠡࡴࡸࡲࠥࡵ࡮࡭ࡻࠣࡳࡳࠦࡃࡩࡴࡲࡱࡪࠦࡢࡳࡱࡺࡷࡪࡸࠠࡷࡧࡵࡷ࡮ࡵ࡮ࠡࡩࡵࡩࡦࡺࡥࡳࠢࡷ࡬ࡦࡴࠠࠣᓎ") + str(bstack1l111l1l111_opy_) + bstack11l11l1_opy_ (u"ࠢ࠯ࠤᓏ"))
                return False
            bstack1l1111llll1_opy_ = caps.get(bstack11l11l1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩᓐ"), {}).get(bstack11l11l1_opy_ (u"ࠩࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩᓑ"))
            if not bstack1l1111llll1_opy_:
                bstack1l1111llll1_opy_ = caps.get(bstack11l11l1_opy_ (u"ࠪ࡫ࡴࡵࡧ࠻ࡥ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨᓒ"), {})
            if bstack1l1111llll1_opy_ and bstack11l11l1_opy_ (u"ࠫ࠲࠳ࡨࡦࡣࡧࡰࡪࡹࡳࠨᓓ") in bstack1l1111llll1_opy_.get(bstack11l11l1_opy_ (u"ࠬࡧࡲࡨࡵࠪᓔ"), []):
                self.logger.warning(bstack11l11l1_opy_ (u"ࠨࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡻ࡮ࡲ࡬ࠡࡰࡲࡸࠥࡸࡵ࡯ࠢࡲࡲࠥࡲࡥࡨࡣࡦࡽࠥ࡮ࡥࡢࡦ࡯ࡩࡸࡹࠠ࡮ࡱࡧࡩ࠳ࠦࡓࡸ࡫ࡷࡧ࡭ࠦࡴࡰࠢࡱࡩࡼࠦࡨࡦࡣࡧࡰࡪࡹࡳࠡ࡯ࡲࡨࡪࠦ࡯ࡳࠢࡤࡺࡴ࡯ࡤࠡࡷࡶ࡭ࡳ࡭ࠠࡩࡧࡤࡨࡱ࡫ࡳࡴࠢࡰࡳࡩ࡫࠮ࠣᓕ"))
                return False
            return True
        except Exception as error:
            self.logger.debug(bstack11l11l1_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡶࡢ࡮࡬ࡨࡦࡺࡥࠡࡣ࠴࠵ࡾࠦࡳࡶࡲࡳࡳࡷࡺࠠ࠻ࠤᓖ") + str(error))
            return False
    def bstack1l111l1llll_opy_(self, test_uuid: str, result: structs.FetchDriverExecuteParamsEventResponse):
        bstack1l111l111l1_opy_ = {
            bstack11l11l1_opy_ (u"ࠨࡶ࡫ࡘࡪࡹࡴࡓࡷࡱ࡙ࡺ࡯ࡤࠨᓗ"): test_uuid,
        }
        bstack1l111l11l11_opy_ = {}
        if result.success:
            bstack1l111l11l11_opy_ = json.loads(result.accessibility_execute_params)
        return bstack1l111ll1l1l_opy_(bstack1l111l111l1_opy_, bstack1l111l11l11_opy_)
    def bstack111ll11l_opy_(self, driver: object, name: str, framework_name: str, test_uuid: str):
        bstack1ll11llllll_opy_ = None
        try:
            self.bstack1llll1lllll_opy_()
            req = structs.FetchDriverExecuteParamsEventRequest()
            req.bin_session_id = self.bin_session_id
            req.product = bstack11l11l1_opy_ (u"ࠤࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠤᓘ")
            req.script_name = bstack11l11l1_opy_ (u"ࠥࡷࡦࡼࡥࡓࡧࡶࡹࡱࡺࡳࠣᓙ")
            r = self.bstack1lllllll1ll_opy_.FetchDriverExecuteParamsEvent(req)
            if not r.success:
                self.logger.debug(bstack11l11l1_opy_ (u"ࠦࡷ࡫ࡣࡦ࡫ࡹࡩࡩࠦࡤࡳ࡫ࡹࡩࡷࠦࡥࡹࡧࡦࡹࡹ࡫ࠠࡱࡣࡵࡥࡲࡹࠠࡧࡴࡲࡱࠥࡹࡥࡳࡸࡨࡶ࠿ࠦࠢᓚ") + str(r.error) + bstack11l11l1_opy_ (u"ࠧࠨᓛ"))
            else:
                bstack1l111l111l1_opy_ = self.bstack1l111l1llll_opy_(test_uuid, r)
                bstack1llll111111_opy_ = r.script
            self.logger.debug(bstack11l11l1_opy_ (u"࠭ࡐࡦࡴࡩࡳࡷࡳࡩ࡯ࡩࠣࡷࡨࡧ࡮ࠡࡤࡨࡪࡴࡸࡥࠡࡵࡤࡺ࡮ࡴࡧࠡࡴࡨࡷࡺࡲࡴࡴࠩᓜ") + str(bstack1l111l111l1_opy_))
            self.perform_scan(driver, name, framework_name=framework_name)
            if not bstack1llll111111_opy_:
                self.logger.debug(bstack11l11l1_opy_ (u"ࠢࡱࡧࡵࡪࡴࡸ࡭ࡠࡵࡦࡥࡳࡀࠠ࡮࡫ࡶࡷ࡮ࡴࡧࠡࠩࡶࡥࡻ࡫ࡒࡦࡵࡸࡰࡹࡹࠧࠡࡵࡦࡶ࡮ࡶࡴࠡࡨࡲࡶࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪࡃࠢᓝ") + str(framework_name) + bstack11l11l1_opy_ (u"ࠣࠢࠥᓞ"))
                return
            bstack1ll11llllll_opy_ = bstack1lllll1l111_opy_.bstack1ll11111ll1_opy_(EVENTS.bstack1l1111l1111_opy_.value)
            self.bstack1l111l11l1l_opy_(driver, bstack1llll111111_opy_, bstack1l111l111l1_opy_, framework_name)
            self.logger.info(bstack11l11l1_opy_ (u"ࠤࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡷࡩࡸࡺࡩ࡯ࡩࠣࡪࡴࡸࠠࡵࡪ࡬ࡷࠥࡺࡥࡴࡶࠣࡧࡦࡹࡥࠡࡪࡤࡷࠥ࡫࡮ࡥࡧࡧ࠲ࠧᓟ"))
            bstack1lllll1l111_opy_.end(EVENTS.bstack1l1111l1111_opy_.value, bstack1ll11llllll_opy_+bstack11l11l1_opy_ (u"ࠥ࠾ࡸࡺࡡࡳࡶࠥᓠ"), bstack1ll11llllll_opy_+bstack11l11l1_opy_ (u"ࠦ࠿࡫࡮ࡥࠤᓡ"), True, None, command=bstack11l11l1_opy_ (u"ࠬࡹࡡࡷࡧࡕࡩࡸࡻ࡬ࡵࡵࠪᓢ"),test_name=name)
        except Exception as bstack1l1111l1lll_opy_:
            self.logger.error(bstack11l11l1_opy_ (u"ࠨࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡲࡦࡵࡸࡰࡹࡹࠠࡤࡱࡸࡰࡩࠦ࡮ࡰࡶࠣࡦࡪࠦࡰࡳࡱࡦࡩࡸࡹࡥࡥࠢࡩࡳࡷࠦࡴࡩࡧࠣࡸࡪࡹࡴࠡࡥࡤࡷࡪࡀࠠࠣᓣ") + bstack11l11l1_opy_ (u"ࠢࡴࡶࡵࠬࡵࡧࡴࡩࠫࠥᓤ") + bstack11l11l1_opy_ (u"ࠣࠢࡈࡶࡷࡵࡲࠡ࠼ࠥᓥ") + str(bstack1l1111l1lll_opy_))
            bstack1lllll1l111_opy_.end(EVENTS.bstack1l1111l1111_opy_.value, bstack1ll11llllll_opy_+bstack11l11l1_opy_ (u"ࠤ࠽ࡷࡹࡧࡲࡵࠤᓦ"), bstack1ll11llllll_opy_+bstack11l11l1_opy_ (u"ࠥ࠾ࡪࡴࡤࠣᓧ"), False, bstack1l1111l1lll_opy_, command=bstack11l11l1_opy_ (u"ࠫࡸࡧࡶࡦࡔࡨࡷࡺࡲࡴࡴࠩᓨ"),test_name=name)
    def bstack1l111l11l1l_opy_(self, driver, bstack1llll111111_opy_, bstack1l111l111l1_opy_, framework_name):
        if framework_name == bstack11l11l1_opy_ (u"ࠬࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠩᓩ"):
            self.bstack1l111lll1ll_opy_.bstack1lll1l1l1ll_opy_(driver, bstack1llll111111_opy_, bstack1l111l111l1_opy_)
        else:
            self.logger.debug(driver.execute_async_script(bstack1llll111111_opy_, bstack1l111l111l1_opy_))
    def _1l1111ll111_opy_(self, instance: bstack1lll1l11111_opy_, args: Tuple) -> list:
        bstack11l11l1_opy_ (u"ࠨࠢࠣࡇࡻࡸࡷࡧࡣࡵࠢࡷࡥ࡬ࡹࠠࡣࡣࡶࡩࡩࠦ࡯࡯ࠢࡷ࡬ࡪࠦࡴࡦࡵࡷࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࠮ࠣࠤࠥᓪ")
        if bstack11l11l1_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠫᓫ") in instance.bstack1l1llll1lll_opy_:
            return args[2].tags if hasattr(args[2], bstack11l11l1_opy_ (u"ࠨࡶࡤ࡫ࡸ࠭ᓬ")) else []
        if hasattr(args[0], bstack11l11l1_opy_ (u"ࠩࡲࡻࡳࡥ࡭ࡢࡴ࡮ࡩࡷࡹࠧᓭ")):
            return [marker.name for marker in args[0].own_markers]
        return []
    def bstack1l111ll11ll_opy_(self, tags, capabilities):
        return self.bstack11l1l1l1l_opy_(tags) and self.bstack111l11111_opy_(capabilities)