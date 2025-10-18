# coding: UTF-8
import sys
bstack1ll1111_opy_ = sys.version_info [0] == 2
bstack1ll_opy_ = 2048
bstack1ll1l1_opy_ = 7
def bstack11l111_opy_ (bstack1ll1_opy_):
    global bstack11l1l_opy_
    bstack11l1l1_opy_ = ord (bstack1ll1_opy_ [-1])
    bstack111ll_opy_ = bstack1ll1_opy_ [:-1]
    bstack11111ll_opy_ = bstack11l1l1_opy_ % len (bstack111ll_opy_)
    bstack1l1lll_opy_ = bstack111ll_opy_ [:bstack11111ll_opy_] + bstack111ll_opy_ [bstack11111ll_opy_:]
    if bstack1ll1111_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1ll_opy_ - (bstack1l111_opy_ + bstack11l1l1_opy_) % bstack1ll1l1_opy_) for bstack1l111_opy_, char in enumerate (bstack1l1lll_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack1ll_opy_ - (bstack1l111_opy_ + bstack11l1l1_opy_) % bstack1ll1l1_opy_) for bstack1l111_opy_, char in enumerate (bstack1l1lll_opy_)])
    return eval (bstack1lll1ll_opy_)
from datetime import datetime
import os
import threading
from browserstack_sdk.sdk_cli.bstack1lllll1l1ll_opy_ import (
    bstack1lllll1lll1_opy_,
    bstack1llll1l1lll_opy_,
    bstack1lll11l1111_opy_,
    bstack1llll1l1111_opy_,
)
from browserstack_sdk.sdk_cli.bstack1llll1ll111_opy_ import bstack1lllll11l1l_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1ll1lll_opy_, bstack1lll11lll1l_opy_, bstack1lll1l1ll1l_opy_
from typing import Tuple, Dict, Any, List, Union
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1llll1ll11l_opy_ import bstack1llll1l1l11_opy_
from browserstack_sdk.sdk_cli.bstack1lll11l11l1_opy_ import bstack1lll111ll1l_opy_
from browserstack_sdk.sdk_cli.bstack1lll1l1l1l1_opy_ import bstack1lll1ll11l1_opy_
from browserstack_sdk.sdk_cli.bstack1lll1lll111_opy_ import bstack1lll11ll11l_opy_
from bstack_utils.helper import bstack1l111ll1l1l_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
from bstack_utils.bstack1111lll1l_opy_ import bstack1llll11ll11_opy_
import grpc
import traceback
import json
class bstack1l11ll1llll_opy_(bstack1llll1l1l11_opy_):
    bstack1l1ll11l1ll_opy_ = False
    bstack1l1111l11l1_opy_ = bstack11l111_opy_ (u"ࠥࡷࡪࡲࡥ࡯࡫ࡸࡱ࠳ࡽࡥࡣࡦࡵ࡭ࡻ࡫ࡲࠣᑔ")
    bstack1l11111llll_opy_ = bstack11l111_opy_ (u"ࠦࡷ࡫࡭ࡰࡶࡨ࠲ࡼ࡫ࡢࡥࡴ࡬ࡺࡪࡸࠢᑕ")
    bstack1l111l1ll11_opy_ = bstack11l111_opy_ (u"ࠧࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡤ࡯࡮ࡪࡶࠥᑖ")
    bstack1l1111lll11_opy_ = bstack11l111_opy_ (u"ࠨࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡥࡩࡴࡡࡶࡧࡦࡴ࡮ࡪࡰࡪࠦᑗ")
    bstack1l1111l1ll1_opy_ = bstack11l111_opy_ (u"ࠢࡥࡴ࡬ࡺࡪࡸ࡟ࡩࡣࡶࡣࡺࡸ࡬ࠣᑘ")
    scripts: Dict[str, Dict[str, str]]
    commands: Dict[str, Dict[str, Dict[str, List[str]]]]
    def __init__(self, bstack1l1l1l111l1_opy_, bstack1ll1lll111l_opy_):
        super().__init__()
        self.scripts = dict()
        self.commands = dict()
        self.accessibility = False
        self.bstack1l111l11l1l_opy_ = False
        self.bstack1l1111ll1l1_opy_ = dict()
        if not self.is_enabled():
            return
        self.bstack1l11l1l1l11_opy_ = bstack1ll1lll111l_opy_
        bstack1l1l1l111l1_opy_.bstack1lllllll11l_opy_((bstack1lllll1lll1_opy_.bstack1llllll11l1_opy_, bstack1llll1l1lll_opy_.PRE), self.bstack1l111l1l111_opy_)
        TestFramework.bstack1lllllll11l_opy_((bstack1lll1ll1lll_opy_.TEST, bstack1lll11lll1l_opy_.PRE), self.bstack1llll111lll_opy_)
        TestFramework.bstack1lllllll11l_opy_((bstack1lll1ll1lll_opy_.TEST, bstack1lll11lll1l_opy_.POST), self.bstack1lll1llll1l_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1llll111lll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1ll1l_opy_,
        bstack1lllll1ll11_opy_: Tuple[bstack1lll1ll1lll_opy_, bstack1lll11lll1l_opy_],
        *args,
        **kwargs,
    ):
        tags = self._1l111ll11l1_opy_(instance, args)
        test_framework = f.get_state(instance, TestFramework.bstack1lll1l11l11_opy_)
        if self.bstack1l111l11l1l_opy_:
            self.bstack1l1111ll1l1_opy_[bstack11l111_opy_ (u"ࠣࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠣᑙ")] = f.get_state(instance, TestFramework.bstack1lll1lll1l1_opy_)
        if bstack11l111_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩ࠭ᑚ") in instance.bstack1ll111111ll_opy_:
            platform_index = f.get_state(instance, TestFramework.bstack1llllllll11_opy_)
            self.accessibility = self.bstack1l1111l1lll_opy_(tags, self.config[bstack11l111_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ᑛ")][platform_index])
        else:
            capabilities = self.bstack1l11l1l1l11_opy_.bstack1lll11lllll_opy_(f, instance, bstack1lllll1ll11_opy_, *args, **kwargs)
            if not capabilities:
                self.logger.debug(bstack11l111_opy_ (u"ࠦࡴࡴ࡟ࡣࡧࡩࡳࡷ࡫࡟ࡵࡧࡶࡸ࠿ࠦ࡮ࡰࠢࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠡࡨࡲࡹࡳࡪࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦᑜ") + str(kwargs) + bstack11l111_opy_ (u"ࠧࠨᑝ"))
                return
            self.accessibility = self.bstack1l1111l1lll_opy_(tags, capabilities)
        if self.bstack1l11l1l1l11_opy_.pages and self.bstack1l11l1l1l11_opy_.pages.values():
            bstack1l11111lll1_opy_ = list(self.bstack1l11l1l1l11_opy_.pages.values())
            if bstack1l11111lll1_opy_ and isinstance(bstack1l11111lll1_opy_[0], (list, tuple)) and bstack1l11111lll1_opy_[0]:
                bstack1l1111lllll_opy_ = bstack1l11111lll1_opy_[0][0]
                if callable(bstack1l1111lllll_opy_):
                    page = bstack1l1111lllll_opy_()
                    def bstack11ll1ll1ll_opy_():
                        self.get_accessibility_results(page, bstack11l111_opy_ (u"ࠨࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠥᑞ"))
                    def bstack1l111l11l11_opy_():
                        self.get_accessibility_results_summary(page, bstack11l111_opy_ (u"ࠢࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠦᑟ"))
                    setattr(page, bstack11l111_opy_ (u"ࠣࡩࡨࡸࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡖࡪࡹࡵ࡭ࡶࡶࠦᑠ"), bstack11ll1ll1ll_opy_)
                    setattr(page, bstack11l111_opy_ (u"ࠤࡪࡩࡹࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡗ࡫ࡳࡶ࡮ࡷࡗࡺࡳ࡭ࡢࡴࡼࠦᑡ"), bstack1l111l11l11_opy_)
        self.logger.debug(bstack11l111_opy_ (u"ࠥࡷ࡭ࡵࡵ࡭ࡦࠣࡶࡺࡴࠠࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡷࡣ࡯ࡹࡪࡃࠢᑢ") + str(self.accessibility) + bstack11l111_opy_ (u"ࠦࠧᑣ"))
    def bstack1l111l1l111_opy_(
        self,
        f: bstack1lllll11l1l_opy_,
        driver: object,
        exec: Tuple[bstack1llll1l1111_opy_, str],
        bstack1lllll1ll11_opy_: Tuple[bstack1lllll1lll1_opy_, bstack1llll1l1lll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        try:
            bstack1l1ll1ll1_opy_ = datetime.now()
            self.bstack1l111l111ll_opy_(f, exec, *args, **kwargs)
            instance, method_name = exec
            instance.bstack1l1lll1l1_opy_(bstack11l111_opy_ (u"ࠧࡧ࠱࠲ࡻ࠽࡭ࡳ࡯ࡴࡠࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡠࡥࡲࡲ࡫࡯ࡧࠣᑤ"), datetime.now() - bstack1l1ll1ll1_opy_)
            if (
                not f.bstack1l1ll1lllll_opy_(method_name)
                or f.bstack1l1ll1lll11_opy_(method_name, *args)
                or f.bstack1l1lll111l1_opy_(method_name, *args)
            ):
                return
            if not f.get_state(instance, bstack1l11ll1llll_opy_.bstack1l111l1ll11_opy_, False):
                if not bstack1l11ll1llll_opy_.bstack1l1ll11l1ll_opy_:
                    self.logger.warning(bstack11l111_opy_ (u"ࠨ࡛ࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡡ࡬ࡲࡩ࡫ࡸ࠾ࠤᑥ") + str(f.platform_index) + bstack11l111_opy_ (u"ࠢ࡞ࠢࡤ࠵࠶ࡿࠠࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸࠦࡨࡢࡸࡨࠤࡳࡵࡴࠡࡤࡨࡩࡳࠦࡳࡦࡶࠣࡪࡴࡸࠠࡵࡪ࡬ࡷࠥࡹࡥࡴࡵ࡬ࡳࡳࠨᑦ"))
                    bstack1l11ll1llll_opy_.bstack1l1ll11l1ll_opy_ = True
                return
            bstack1l1111llll1_opy_ = self.scripts.get(f.framework_name, {})
            if not bstack1l1111llll1_opy_:
                platform_index = f.get_state(instance, bstack1lllll11l1l_opy_.bstack1llllllll11_opy_, 0)
                self.logger.debug(bstack11l111_opy_ (u"ࠣࡰࡲࠤࡦ࠷࠱ࡺࠢࡶࡧࡷ࡯ࡰࡵࡵࠣࡪࡴࡸࠠࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡡ࡬ࡲࡩ࡫ࡸ࠾ࡽࡳࡰࡦࡺࡦࡰࡴࡰࡣ࡮ࡴࡤࡦࡺࢀࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟࡯ࡣࡰࡩࡂࠨᑧ") + str(f.framework_name) + bstack11l111_opy_ (u"ࠤࠥᑨ"))
                return
            command_name = f.bstack1l1lll1111l_opy_(*args)
            if not command_name:
                self.logger.debug(bstack11l111_opy_ (u"ࠥࡱ࡮ࡹࡳࡪࡰࡪࠤࡨࡵ࡭࡮ࡣࡱࡨࡤࡴࡡ࡮ࡧࠣࡪࡴࡸࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡲࡦࡳࡥ࠾ࡽࡩ࠲࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟࡯ࡣࡰࡩࢂࠦ࡭ࡦࡶ࡫ࡳࡩࡥ࡮ࡢ࡯ࡨࡁࠧᑩ") + str(method_name) + bstack11l111_opy_ (u"ࠦࠧᑪ"))
                return
            bstack1l111l1llll_opy_ = f.get_state(instance, bstack1l11ll1llll_opy_.bstack1l1111l1ll1_opy_, False)
            if command_name == bstack11l111_opy_ (u"ࠧ࡭ࡥࡵࠤᑫ") and not bstack1l111l1llll_opy_:
                f.bstack1llllllll1l_opy_(instance, bstack1l11ll1llll_opy_.bstack1l1111l1ll1_opy_, True)
                bstack1l111l1llll_opy_ = True
            if not bstack1l111l1llll_opy_ and not self.bstack1l111l11l1l_opy_:
                self.logger.debug(bstack11l111_opy_ (u"ࠨ࡮ࡰࠢࡘࡖࡑࠦ࡬ࡰࡣࡧࡩࡩࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫࠽ࡼࡨ࠱ࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥ࡮ࡢ࡯ࡨࢁࠥࡩ࡯࡮࡯ࡤࡲࡩࡥ࡮ࡢ࡯ࡨࡁࠧᑬ") + str(command_name) + bstack11l111_opy_ (u"ࠢࠣᑭ"))
                return
            scripts_to_run = self.commands.get(f.framework_name, {}).get(method_name, {}).get(command_name, [])
            if not scripts_to_run:
                self.logger.debug(bstack11l111_opy_ (u"ࠣࡰࡲࠤࡦ࠷࠱ࡺࠢࡶࡧࡷ࡯ࡰࡵࡵࠣࡪࡴࡸࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡲࡦࡳࡥ࠾ࡽࡩ࠲࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟࡯ࡣࡰࡩࢂࠦࡣࡰ࡯ࡰࡥࡳࡪ࡟࡯ࡣࡰࡩࡂࠨᑮ") + str(command_name) + bstack11l111_opy_ (u"ࠤࠥᑯ"))
                return
            self.logger.info(bstack11l111_opy_ (u"ࠥࡶࡺࡴ࡮ࡪࡰࡪࠤࢀࡲࡥ࡯ࠪࡶࡧࡷ࡯ࡰࡵࡵࡢࡸࡴࡥࡲࡶࡰࠬࢁࠥࡹࡣࡳ࡫ࡳࡸࡸࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫࠽ࡼࡨ࠱ࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥ࡮ࡢ࡯ࡨࢁࠥࡩ࡯࡮࡯ࡤࡲࡩࡥ࡮ࡢ࡯ࡨࡁࠧᑰ") + str(command_name) + bstack11l111_opy_ (u"ࠦࠧᑱ"))
            scripts = [(s, bstack1l1111llll1_opy_[s]) for s in scripts_to_run if s in bstack1l1111llll1_opy_]
            for script_name, bstack1llll11111l_opy_ in scripts:
                try:
                    bstack1l1ll1ll1_opy_ = datetime.now()
                    if script_name == bstack11l111_opy_ (u"ࠧࡹࡣࡢࡰࠥᑲ"):
                        result = self.perform_scan(driver, method=command_name, framework_name=f.framework_name)
                    instance.bstack1l1lll1l1_opy_(bstack11l111_opy_ (u"ࠨࡡ࠲࠳ࡼ࠾ࠧᑳ") + script_name, datetime.now() - bstack1l1ll1ll1_opy_)
                    if isinstance(result, dict) and not result.get(bstack11l111_opy_ (u"ࠢࡴࡷࡦࡧࡪࡹࡳࠣᑴ"), True):
                        self.logger.warning(bstack11l111_opy_ (u"ࠣࡵ࡮࡭ࡵࠦࡥࡹࡧࡦࡹࡹ࡯࡮ࡨࠢࡵࡩࡲࡧࡩ࡯࡫ࡱ࡫ࠥࡹࡣࡳ࡫ࡳࡸࡸࡀࠠࠣᑵ") + str(result) + bstack11l111_opy_ (u"ࠤࠥᑶ"))
                        break
                except Exception as e:
                    self.logger.error(bstack11l111_opy_ (u"ࠥࡩࡷࡸ࡯ࡳࠢࡨࡼࡪࡩࡵࡵ࡫ࡱ࡫ࠥࡹࡣࡳ࡫ࡳࡸࡂࢁࡳࡤࡴ࡬ࡴࡹࡥ࡮ࡢ࡯ࡨࢁࠥ࡫ࡲࡳࡱࡵࡁࠧᑷ") + str(e) + bstack11l111_opy_ (u"ࠦࠧᑸ"))
        except Exception as e:
            self.logger.error(bstack11l111_opy_ (u"ࠧࡵ࡮ࡠࡤࡨࡪࡴࡸࡥࡠࡧࡻࡩࡨࡻࡴࡦࠢࡨࡶࡷࡵࡲ࠾ࠤᑹ") + str(e) + bstack11l111_opy_ (u"ࠨࠢᑺ"))
    def bstack1lll1llll1l_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1ll1l_opy_,
        bstack1lllll1ll11_opy_: Tuple[bstack1lll1ll1lll_opy_, bstack1lll11lll1l_opy_],
        *args,
        **kwargs,
    ):
        tags = self._1l111ll11l1_opy_(instance, args)
        capabilities = self.bstack1l11l1l1l11_opy_.bstack1lll11lllll_opy_(f, instance, bstack1lllll1ll11_opy_, *args, **kwargs)
        self.accessibility = self.bstack1l1111l1lll_opy_(tags, capabilities)
        if not self.accessibility:
            self.logger.debug(bstack11l111_opy_ (u"ࠢࡰࡰࡢࡥ࡫ࡺࡥࡳࡡࡷࡩࡸࡺ࠺ࠡࡣ࠴࠵ࡾࠦ࡮ࡰࡶࠣࡩࡳࡧࡢ࡭ࡧࡧࠦᑻ"))
            return
        driver = self.bstack1l11l1l1l11_opy_.bstack1lll1l1111l_opy_(f, instance, bstack1lllll1ll11_opy_, *args, **kwargs)
        test_name = f.get_state(instance, TestFramework.bstack1ll1l11l111_opy_)
        if not test_name:
            self.logger.debug(bstack11l111_opy_ (u"ࠣࡱࡱࡣࡦ࡬ࡴࡦࡴࡢࡸࡪࡹࡴ࠻ࠢࡰ࡭ࡸࡹࡩ࡯ࡩࠣࡸࡪࡹࡴࠡࡰࡤࡱࡪࠨᑼ"))
            return
        test_uuid = f.get_state(instance, TestFramework.bstack1lll1lll1l1_opy_)
        if not test_uuid:
            self.logger.debug(bstack11l111_opy_ (u"ࠤࡲࡲࡤࡧࡦࡵࡧࡵࡣࡹ࡫ࡳࡵ࠼ࠣࡱ࡮ࡹࡳࡪࡰࡪࠤࡹ࡫ࡳࡵࠢࡸࡹ࡮ࡪࠢᑽ"))
            return
        if isinstance(self.bstack1l11l1l1l11_opy_, bstack1lll1ll11l1_opy_):
            framework_name = bstack11l111_opy_ (u"ࠪࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠧᑾ")
        else:
            framework_name = bstack11l111_opy_ (u"ࠫࡸ࡫࡬ࡦࡰ࡬ࡹࡲ࠭ᑿ")
        self.bstack1lllllll1_opy_(driver, test_name, framework_name, test_uuid)
    def perform_scan(self, driver: object, method: Union[None, str], framework_name: str):
        bstack1ll1l1l11l1_opy_ = bstack1llll11ll11_opy_.bstack1ll11l11ll1_opy_(EVENTS.bstack11ll111lll_opy_.value)
        if not self.accessibility:
            self.logger.debug(bstack11l111_opy_ (u"ࠧࡶࡥࡳࡨࡲࡶࡲࡥࡳࡤࡣࡱ࠾ࠥࡧ࠱࠲ࡻࠣࡲࡴࡺࠠࡦࡰࡤࡦࡱ࡫ࡤࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦ࠿ࡾࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥ࡮ࡢ࡯ࡨࢁࠥࠨᒀ"))
            return
        bstack1l1ll1ll1_opy_ = datetime.now()
        bstack1llll11111l_opy_ = self.scripts.get(framework_name, {}).get(bstack11l111_opy_ (u"ࠨࡳࡤࡣࡱࠦᒁ"), None)
        if not bstack1llll11111l_opy_:
            self.logger.debug(bstack11l111_opy_ (u"ࠢࡱࡧࡵࡪࡴࡸ࡭ࡠࡵࡦࡥࡳࡀࠠ࡮࡫ࡶࡷ࡮ࡴࡧࠡࠩࡶࡧࡦࡴࠧࠡࡵࡦࡶ࡮ࡶࡴࠡࡨࡲࡶࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪࡃࠢᒂ") + str(framework_name) + bstack11l111_opy_ (u"ࠣࠢࠥᒃ"))
            return
        if self.bstack1l111l11l1l_opy_:
            arg = dict()
            arg[bstack11l111_opy_ (u"ࠤࡰࡩࡹ࡮࡯ࡥࠤᒄ")] = method if method else bstack11l111_opy_ (u"ࠥࠦᒅ")
            arg[bstack11l111_opy_ (u"ࠦࡹ࡮ࡔࡦࡵࡷࡖࡺࡴࡕࡶ࡫ࡧࠦᒆ")] = self.bstack1l1111ll1l1_opy_[bstack11l111_opy_ (u"ࠧࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠧᒇ")]
            arg[bstack11l111_opy_ (u"ࠨࡴࡩࡄࡸ࡭ࡱࡪࡕࡶ࡫ࡧࠦᒈ")] = self.bstack1l1111ll1l1_opy_[bstack11l111_opy_ (u"ࠢࡵࡧࡶࡸ࡭ࡻࡢࡠࡤࡸ࡭ࡱࡪ࡟ࡶࡷ࡬ࡨࠧᒉ")]
            arg[bstack11l111_opy_ (u"ࠣࡣࡸࡸ࡭ࡎࡥࡢࡦࡨࡶࠧᒊ")] = self.bstack1l1111ll1l1_opy_[bstack11l111_opy_ (u"ࠤࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡖࡲ࡯ࡪࡴࠢᒋ")]
            arg[bstack11l111_opy_ (u"ࠥࡸ࡭ࡐࡷࡵࡖࡲ࡯ࡪࡴࠢᒌ")] = self.bstack1l1111ll1l1_opy_[bstack11l111_opy_ (u"ࠦࡹ࡮࡟࡫ࡹࡷࡣࡹࡵ࡫ࡦࡰࠥᒍ")]
            arg[bstack11l111_opy_ (u"ࠧࡹࡣࡢࡰࡗ࡭ࡲ࡫ࡳࡵࡣࡰࡴࠧᒎ")] = str(int(datetime.now().timestamp() * 1000))
            bstack1l111ll11ll_opy_ = bstack1llll11111l_opy_ % json.dumps(arg)
            driver.execute_script(bstack1l111ll11ll_opy_)
            return
        instance = bstack1lll11l1111_opy_.bstack1ll111lll1l_opy_(driver)
        if instance:
            if not bstack1lll11l1111_opy_.get_state(instance, bstack1l11ll1llll_opy_.bstack1l1111lll11_opy_, False):
                bstack1lll11l1111_opy_.bstack1llllllll1l_opy_(instance, bstack1l11ll1llll_opy_.bstack1l1111lll11_opy_, True)
            else:
                self.logger.info(bstack11l111_opy_ (u"ࠨࡰࡦࡴࡩࡳࡷࡳ࡟ࡴࡥࡤࡲ࠿ࠦࡡ࡭ࡴࡨࡥࡩࡿࠠࡪࡰࠣࡴࡷࡵࡧࡳࡧࡶࡷࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪࡃࡻࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡲࡦࡳࡥࡾࠢࡰࡩࡹ࡮࡯ࡥ࠿ࠥᒏ") + str(method) + bstack11l111_opy_ (u"ࠢࠣᒐ"))
                return
        self.logger.info(bstack11l111_opy_ (u"ࠣࡲࡨࡶ࡫ࡵࡲ࡮ࡡࡶࡧࡦࡴ࠺ࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦ࠿ࡾࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥ࡮ࡢ࡯ࡨࢁࠥࡳࡥࡵࡪࡲࡨࡂࠨᒑ") + str(method) + bstack11l111_opy_ (u"ࠤࠥᒒ"))
        if framework_name == bstack11l111_opy_ (u"ࠪࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠧᒓ"):
            result = self.bstack1l11l1l1l11_opy_.bstack1lll1lll11l_opy_(driver, bstack1llll11111l_opy_)
        else:
            result = driver.execute_async_script(bstack1llll11111l_opy_, {bstack11l111_opy_ (u"ࠦࡲ࡫ࡴࡩࡱࡧࠦᒔ"): method if method else bstack11l111_opy_ (u"ࠧࠨᒕ")})
        bstack1llll11ll11_opy_.end(EVENTS.bstack11ll111lll_opy_.value, bstack1ll1l1l11l1_opy_+bstack11l111_opy_ (u"ࠨ࠺ࡴࡶࡤࡶࡹࠨᒖ"), bstack1ll1l1l11l1_opy_+bstack11l111_opy_ (u"ࠢ࠻ࡧࡱࡨࠧᒗ"), True, None, command=method)
        if instance:
            bstack1lll11l1111_opy_.bstack1llllllll1l_opy_(instance, bstack1l11ll1llll_opy_.bstack1l1111lll11_opy_, False)
            instance.bstack1l1lll1l1_opy_(bstack11l111_opy_ (u"ࠣࡣ࠴࠵ࡾࡀࡰࡦࡴࡩࡳࡷࡳ࡟ࡴࡥࡤࡲࠧᒘ"), datetime.now() - bstack1l1ll1ll1_opy_)
        return result
        def bstack1l111l111l1_opy_(self, driver: object, framework_name, bstack11lllll1l1_opy_: str):
            self.bstack1llll1lll11_opy_()
            req = structs.AccessibilityResultRequest()
            req.bin_session_id = self.bin_session_id
            req.bstack1l1111ll11l_opy_ = self.bstack1l1111ll1l1_opy_[bstack11l111_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠤᒙ")]
            req.bstack11lllll1l1_opy_ = bstack11lllll1l1_opy_
            req.session_id = self.bin_session_id
            try:
                r = self.bstack1llllll1l11_opy_.AccessibilityResult(req)
                if not r.success:
                    self.logger.debug(bstack11l111_opy_ (u"ࠥࡶࡪࡩࡥࡪࡸࡨࡨࠥ࡬ࡲࡰ࡯ࠣࡷࡪࡸࡶࡦࡴ࠽ࠤࠧᒚ") + str(r) + bstack11l111_opy_ (u"ࠦࠧᒛ"))
                else:
                    bstack1l111l1lll1_opy_ = json.loads(r.bstack1l11111ll1l_opy_.decode(bstack11l111_opy_ (u"ࠬࡻࡴࡧ࠯࠻ࠫᒜ")))
                    if bstack11lllll1l1_opy_ == bstack11l111_opy_ (u"࠭ࡧࡦࡶࡕࡩࡸࡻ࡬ࡵࡵࠪᒝ"):
                        return bstack1l111l1lll1_opy_.get(bstack11l111_opy_ (u"ࠢࡥࡣࡷࡥࠧᒞ"), [])
                    else:
                        return bstack1l111l1lll1_opy_.get(bstack11l111_opy_ (u"ࠣࡦࡤࡸࡦࠨᒟ"), {})
            except grpc.RpcError as e:
                self.logger.error(bstack11l111_opy_ (u"ࠤࡵࡴࡨ࠳ࡥࡳࡴࡲࡶࠥࡽࡨࡪ࡮ࡨࠤ࡫࡫ࡴࡤࡪ࡬ࡲ࡬ࠦࡧࡦࡶࡢࡥࡵࡶ࡟ࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿ࡟ࡳࡧࡶࡹࡱࡺࠠࡧࡴࡲࡱࠥࡩ࡬ࡪ࠼ࠣࠦᒠ") + str(e) + bstack11l111_opy_ (u"ࠥࠦᒡ"))
    @measure(event_name=EVENTS.bstack1llll11111_opy_, stage=STAGE.bstack1l11lll11_opy_)
    def get_accessibility_results(self, driver: object, framework_name):
        if not self.accessibility:
            self.logger.debug(bstack11l111_opy_ (u"ࠦ࡬࡫ࡴࡠࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡠࡴࡨࡷࡺࡲࡴࡴ࠼ࠣࡥ࠶࠷ࡹࠡࡰࡲࡸࠥ࡫࡮ࡢࡤ࡯ࡩࡩࠨᒢ"))
            return
        if self.bstack1l111l11l1l_opy_:
            self.logger.debug(bstack11l111_opy_ (u"ࠬࡖࡥࡳࡨࡲࡶࡲ࡯࡮ࡨࠢࡶࡧࡦࡴࠠࡧࡱࡵࠤࡦࡶࡰࠡࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨᒣ"))
            self.perform_scan(driver, method=None, framework_name=framework_name)
            return self.bstack1l111l111l1_opy_(driver, framework_name, bstack11l111_opy_ (u"ࠨࡧࡦࡶࡕࡩࡸࡻ࡬ࡵࡵࠥᒤ"))
        bstack1llll11111l_opy_ = self.scripts.get(framework_name, {}).get(bstack11l111_opy_ (u"ࠢࡨࡧࡷࡖࡪࡹࡵ࡭ࡶࡶࠦᒥ"), None)
        if not bstack1llll11111l_opy_:
            self.logger.debug(bstack11l111_opy_ (u"ࠣ࡯࡬ࡷࡸ࡯࡮ࡨࠢࠪ࡫ࡪࡺࡒࡦࡵࡸࡰࡹࡹࠧࠡࡵࡦࡶ࡮ࡶࡴࠡࡨࡲࡶࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪࡃࠢᒦ") + str(framework_name) + bstack11l111_opy_ (u"ࠤࠥᒧ"))
            return
        self.perform_scan(driver, method=None, framework_name=framework_name)
        bstack1l1ll1ll1_opy_ = datetime.now()
        if framework_name == bstack11l111_opy_ (u"ࠪࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠧᒨ"):
            result = self.bstack1l11l1l1l11_opy_.bstack1lll1lll11l_opy_(driver, bstack1llll11111l_opy_)
        else:
            result = driver.execute_async_script(bstack1llll11111l_opy_)
        instance = bstack1lll11l1111_opy_.bstack1ll111lll1l_opy_(driver)
        if instance:
            instance.bstack1l1lll1l1_opy_(bstack11l111_opy_ (u"ࠦࡦ࠷࠱ࡺ࠼ࡪࡩࡹࡥࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡥࡲࡦࡵࡸࡰࡹࡹࠢᒩ"), datetime.now() - bstack1l1ll1ll1_opy_)
        return result
    @measure(event_name=EVENTS.bstack1111ll1111_opy_, stage=STAGE.bstack1l11lll11_opy_)
    def get_accessibility_results_summary(self, driver: object, framework_name):
        if not self.accessibility:
            self.logger.debug(bstack11l111_opy_ (u"ࠧ࡭ࡥࡵࡡࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡡࡵࡩࡸࡻ࡬ࡵࡵࡢࡷࡺࡳ࡭ࡢࡴࡼ࠾ࠥࡧ࠱࠲ࡻࠣࡲࡴࡺࠠࡦࡰࡤࡦࡱ࡫ࡤࠣᒪ"))
            return
        if self.bstack1l111l11l1l_opy_:
            self.perform_scan(driver, method=None, framework_name=framework_name)
            return self.bstack1l111l111l1_opy_(driver, framework_name, bstack11l111_opy_ (u"࠭ࡧࡦࡶࡕࡩࡸࡻ࡬ࡵࡵࡖࡹࡲࡳࡡࡳࡻࠪᒫ"))
        bstack1llll11111l_opy_ = self.scripts.get(framework_name, {}).get(bstack11l111_opy_ (u"ࠢࡨࡧࡷࡖࡪࡹࡵ࡭ࡶࡶࡗࡺࡳ࡭ࡢࡴࡼࠦᒬ"), None)
        if not bstack1llll11111l_opy_:
            self.logger.debug(bstack11l111_opy_ (u"ࠣ࡯࡬ࡷࡸ࡯࡮ࡨࠢࠪ࡫ࡪࡺࡒࡦࡵࡸࡰࡹࡹࡓࡶ࡯ࡰࡥࡷࡿࠧࠡࡵࡦࡶ࡮ࡶࡴࠡࡨࡲࡶࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪࡃࠢᒭ") + str(framework_name) + bstack11l111_opy_ (u"ࠤࠥᒮ"))
            return
        self.perform_scan(driver, method=None, framework_name=framework_name)
        bstack1l1ll1ll1_opy_ = datetime.now()
        if framework_name == bstack11l111_opy_ (u"ࠪࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠧᒯ"):
            result = self.bstack1l11l1l1l11_opy_.bstack1lll1lll11l_opy_(driver, bstack1llll11111l_opy_)
        else:
            result = driver.execute_async_script(bstack1llll11111l_opy_)
        instance = bstack1lll11l1111_opy_.bstack1ll111lll1l_opy_(driver)
        if instance:
            instance.bstack1l1lll1l1_opy_(bstack11l111_opy_ (u"ࠦࡦ࠷࠱ࡺ࠼ࡪࡩࡹࡥࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡥࡲࡦࡵࡸࡰࡹࡹ࡟ࡴࡷࡰࡱࡦࡸࡹࠣᒰ"), datetime.now() - bstack1l1ll1ll1_opy_)
        return result
    @measure(event_name=EVENTS.bstack1l111l1ll1l_opy_, stage=STAGE.bstack1l11lll11_opy_)
    def bstack1l111l11ll1_opy_(
        self,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        hub_url: str,
    ):
        self.bstack1llll1lll11_opy_()
        req = structs.AccessibilityConfigRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.hub_url = hub_url
        try:
            r = self.bstack1llllll1l11_opy_.AccessibilityConfig(req)
            if not r.success:
                self.logger.debug(bstack11l111_opy_ (u"ࠧࡸࡥࡤࡧ࡬ࡺࡪࡪࠠࡧࡴࡲࡱࠥࡹࡥࡳࡸࡨࡶ࠿ࠦࠢᒱ") + str(r) + bstack11l111_opy_ (u"ࠨࠢᒲ"))
            else:
                self.bstack1l1111lll1l_opy_(framework_name, r)
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack11l111_opy_ (u"ࠢࡳࡲࡦ࠱ࡪࡸࡲࡰࡴ࠽ࠤࠧᒳ") + str(e) + bstack11l111_opy_ (u"ࠣࠤᒴ"))
            traceback.print_exc()
            raise e
    def bstack1l1111lll1l_opy_(self, framework_name: str, result: structs.AccessibilityConfigResponse) -> bool:
        if not result.success or not result.accessibility.success:
            self.logger.debug(bstack11l111_opy_ (u"ࠤ࡯ࡳࡦࡪ࡟ࡤࡱࡱࡪ࡮࡭࠺ࠡࡣ࠴࠵ࡾࠦ࡮ࡰࡶࠣࡪࡴࡻ࡮ࡥࠤᒵ"))
            return False
        if result.accessibility.is_app_accessibility:
            self.bstack1l111l11l1l_opy_ = result.accessibility.is_app_accessibility
        if result.testhub.build_hashed_id:
            self.bstack1l1111ll1l1_opy_[bstack11l111_opy_ (u"ࠥࡸࡪࡹࡴࡩࡷࡥࡣࡧࡻࡩ࡭ࡦࡢࡹࡺ࡯ࡤࠣᒶ")] = result.testhub.build_hashed_id
        if result.testhub.jwt:
            self.bstack1l1111ll1l1_opy_[bstack11l111_opy_ (u"ࠦࡹ࡮࡟࡫ࡹࡷࡣࡹࡵ࡫ࡦࡰࠥᒷ")] = result.testhub.jwt
        if result.accessibility.options:
            options = result.accessibility.options
            if options.capabilities:
                for caps in options.capabilities:
                    self.bstack1l1111ll1l1_opy_[caps.name] = caps.value
            if options.scripts:
                self.scripts[framework_name] = {row.name: row.command for row in options.scripts}
            if options.commands_to_wrap and options.commands_to_wrap.commands:
                scripts_to_run = [s for s in options.commands_to_wrap.scripts_to_run]
                if not scripts_to_run:
                    return False
                bstack1l111l1111l_opy_ = dict()
                for command in options.commands_to_wrap.commands:
                    if command.library == self.bstack1l1111l11l1_opy_ and command.module == self.bstack1l11111llll_opy_:
                        if command.method and not command.method in bstack1l111l1111l_opy_:
                            bstack1l111l1111l_opy_[command.method] = dict()
                        if command.name and not command.name in bstack1l111l1111l_opy_[command.method]:
                            bstack1l111l1111l_opy_[command.method][command.name] = list()
                        bstack1l111l1111l_opy_[command.method][command.name].extend(scripts_to_run)
                self.commands[framework_name] = bstack1l111l1111l_opy_
        return bool(self.commands.get(framework_name, None))
    def bstack1l111l111ll_opy_(
        self,
        f: bstack1lllll11l1l_opy_,
        exec: Tuple[bstack1llll1l1111_opy_, str],
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if isinstance(self.bstack1l11l1l1l11_opy_, bstack1lll1ll11l1_opy_) and method_name != bstack11l111_opy_ (u"ࠬࡩ࡯࡯ࡰࡨࡧࡹ࠭ᒸ"):
            return
        if bstack1lll11l1111_opy_.bstack1lllllll1ll_opy_(instance, bstack1l11ll1llll_opy_.bstack1l111l1ll11_opy_):
            return
        if f.bstack1lllll1l11l_opy_(method_name, *args):
            bstack1l1111l1l1l_opy_ = False
            desired_capabilities = f.bstack1l1ll1ll1ll_opy_(instance)
            if isinstance(desired_capabilities, dict):
                hub_url = f.bstack1l1lll11l11_opy_(instance)
                platform_index = f.get_state(instance, bstack1lllll11l1l_opy_.bstack1llllllll11_opy_, 0)
                bstack1l1111l111l_opy_ = datetime.now()
                r = self.bstack1l111l11ll1_opy_(platform_index, f.framework_name, f.framework_version, hub_url)
                instance.bstack1l1lll1l1_opy_(bstack11l111_opy_ (u"ࠨࡧࡳࡲࡦ࠾ࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡣࡨࡵ࡮ࡧ࡫ࡪࠦᒹ"), datetime.now() - bstack1l1111l111l_opy_)
                bstack1l1111l1l1l_opy_ = r.success
            else:
                self.logger.error(bstack11l111_opy_ (u"ࠢ࡮࡫ࡶࡷ࡮ࡴࡧࠡࡦࡨࡷ࡮ࡸࡥࡥࠢࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳ࠾ࠤᒺ") + str(desired_capabilities) + bstack11l111_opy_ (u"ࠣࠤᒻ"))
            f.bstack1llllllll1l_opy_(instance, bstack1l11ll1llll_opy_.bstack1l111l1ll11_opy_, bstack1l1111l1l1l_opy_)
    def bstack1llll111ll_opy_(self, test_tags):
        bstack1l111l11ll1_opy_ = self.config.get(bstack11l111_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩᒼ"))
        if not bstack1l111l11ll1_opy_:
            return True
        try:
            include_tags = bstack1l111l11ll1_opy_[bstack11l111_opy_ (u"ࠪ࡭ࡳࡩ࡬ࡶࡦࡨࡘࡦ࡭ࡳࡊࡰࡗࡩࡸࡺࡩ࡯ࡩࡖࡧࡴࡶࡥࠨᒽ")] if bstack11l111_opy_ (u"ࠫ࡮ࡴࡣ࡭ࡷࡧࡩ࡙ࡧࡧࡴࡋࡱࡘࡪࡹࡴࡪࡰࡪࡗࡨࡵࡰࡦࠩᒾ") in bstack1l111l11ll1_opy_ and isinstance(bstack1l111l11ll1_opy_[bstack11l111_opy_ (u"ࠬ࡯࡮ࡤ࡮ࡸࡨࡪ࡚ࡡࡨࡵࡌࡲ࡙࡫ࡳࡵ࡫ࡱ࡫ࡘࡩ࡯ࡱࡧࠪᒿ")], list) else []
            exclude_tags = bstack1l111l11ll1_opy_[bstack11l111_opy_ (u"࠭ࡥࡹࡥ࡯ࡹࡩ࡫ࡔࡢࡩࡶࡍࡳ࡚ࡥࡴࡶ࡬ࡲ࡬࡙ࡣࡰࡲࡨࠫᓀ")] if bstack11l111_opy_ (u"ࠧࡦࡺࡦࡰࡺࡪࡥࡕࡣࡪࡷࡎࡴࡔࡦࡵࡷ࡭ࡳ࡭ࡓࡤࡱࡳࡩࠬᓁ") in bstack1l111l11ll1_opy_ and isinstance(bstack1l111l11ll1_opy_[bstack11l111_opy_ (u"ࠨࡧࡻࡧࡱࡻࡤࡦࡖࡤ࡫ࡸࡏ࡮ࡕࡧࡶࡸ࡮ࡴࡧࡔࡥࡲࡴࡪ࠭ᓂ")], list) else []
            excluded = any(tag in exclude_tags for tag in test_tags)
            included = len(include_tags) == 0 or any(tag in include_tags for tag in test_tags)
            return not excluded and included
        except Exception as error:
            self.logger.debug(bstack11l111_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡹ࡫࡭ࡱ࡫ࠠࡷࡣ࡯࡭ࡩࡧࡴࡪࡰࡪࠤࡹ࡫ࡳࡵࠢࡦࡥࡸ࡫ࠠࡧࡱࡵࠤࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡧ࡫ࡦࡰࡴࡨࠤࡸࡩࡡ࡯ࡰ࡬ࡲ࡬࠴ࠠࡆࡴࡵࡳࡷࠦ࠺ࠡࠤᓃ") + str(error))
        return False
    def bstack1111ll111_opy_(self, caps):
        try:
            if self.bstack1l111l11l1l_opy_:
                bstack1l1111l1l11_opy_ = caps.get(bstack11l111_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱࡓࡧ࡭ࡦࠤᓄ"))
                if bstack1l1111l1l11_opy_ is not None and str(bstack1l1111l1l11_opy_).lower() == bstack11l111_opy_ (u"ࠦࡦࡴࡤࡳࡱ࡬ࡨࠧᓅ"):
                    bstack1l111l1l1l1_opy_ = caps.get(bstack11l111_opy_ (u"ࠧࡧࡰࡱ࡫ࡸࡱ࠿ࡶ࡬ࡢࡶࡩࡳࡷࡳࡖࡦࡴࡶ࡭ࡴࡴࠢᓆ")) or caps.get(bstack11l111_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠣᓇ"))
                    if bstack1l111l1l1l1_opy_ is not None and int(bstack1l111l1l1l1_opy_) < 11:
                        self.logger.warning(bstack11l111_opy_ (u"ࠢࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤࡼ࡯࡬࡭ࠢࡵࡹࡳࠦ࡯࡯࡮ࡼࠤࡴࡴࠠࡂࡰࡧࡶࡴ࡯ࡤࠡ࠳࠴ࠤࡦࡴࡤࠡࡣࡥࡳࡻ࡫࠮ࠡࡅࡸࡶࡷ࡫࡮ࡵࠢࡳࡰࡦࡺࡦࡰࡴࡰࠤࡻ࡫ࡲࡴ࡫ࡲࡲࠥࡃࠢᓈ") + str(bstack1l111l1l1l1_opy_) + bstack11l111_opy_ (u"ࠣࠤᓉ"))
                        return False
                return True
            bstack1l1111ll1ll_opy_ = caps.get(bstack11l111_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪᓊ"), {}).get(bstack11l111_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࡑࡥࡲ࡫ࠧᓋ"), caps.get(bstack11l111_opy_ (u"ࠫࡩ࡫ࡶࡪࡥࡨࠫᓌ"), bstack11l111_opy_ (u"ࠬ࠭ᓍ")))
            if bstack1l1111ll1ll_opy_:
                self.logger.warning(bstack11l111_opy_ (u"ࠨࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡻ࡮ࡲ࡬ࠡࡴࡸࡲࠥࡵ࡮࡭ࡻࠣࡳࡳࠦࡄࡦࡵ࡮ࡸࡴࡶࠠࡣࡴࡲࡻࡸ࡫ࡲࡴ࠰ࠥᓎ"))
                return False
            browser = caps.get(bstack11l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬᓏ"), bstack11l111_opy_ (u"ࠨࠩᓐ")).lower()
            if browser != bstack11l111_opy_ (u"ࠩࡦ࡬ࡷࡵ࡭ࡦࠩᓑ"):
                self.logger.warning(bstack11l111_opy_ (u"ࠥࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡸ࡫࡯ࡰࠥࡸࡵ࡯ࠢࡲࡲࡱࡿࠠࡰࡰࠣࡇ࡭ࡸ࡯࡮ࡧࠣࡦࡷࡵࡷࡴࡧࡵࡷ࠳ࠨᓒ"))
                return False
            bstack1l111ll1l11_opy_ = bstack1l111l1l1ll_opy_
            if not self.config.get(bstack11l111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳ࠭ᓓ")) or self.config.get(bstack11l111_opy_ (u"ࠬࡺࡵࡳࡤࡲࡷࡨࡧ࡬ࡦࠩᓔ")):
                bstack1l111ll1l11_opy_ = bstack1l1111l1111_opy_
            browser_version = caps.get(bstack11l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧᓕ"))
            if not browser_version:
                browser_version = caps.get(bstack11l111_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨᓖ"), {}).get(bstack11l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩᓗ"), bstack11l111_opy_ (u"ࠩࠪᓘ"))
            if browser_version and browser_version != bstack11l111_opy_ (u"ࠪࡰࡦࡺࡥࡴࡶࠪᓙ") and int(browser_version.split(bstack11l111_opy_ (u"ࠫ࠳࠭ᓚ"))[0]) <= bstack1l111ll1l11_opy_:
                self.logger.warning(bstack11l111_opy_ (u"ࠧࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡺ࡭ࡱࡲࠠࡳࡷࡱࠤࡴࡴ࡬ࡺࠢࡲࡲࠥࡉࡨࡳࡱࡰࡩࠥࡨࡲࡰࡹࡶࡩࡷࠦࡶࡦࡴࡶ࡭ࡴࡴࠠࡨࡴࡨࡥࡹ࡫ࡲࠡࡶ࡫ࡥࡳࠦࠢᓛ") + str(bstack1l111ll1l11_opy_) + bstack11l111_opy_ (u"ࠨ࠮ࠣᓜ"))
                return False
            bstack1l111l11lll_opy_ = caps.get(bstack11l111_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨᓝ"), {}).get(bstack11l111_opy_ (u"ࠨࡥ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨᓞ"))
            if not bstack1l111l11lll_opy_:
                bstack1l111l11lll_opy_ = caps.get(bstack11l111_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧᓟ"), {})
            if bstack1l111l11lll_opy_ and bstack11l111_opy_ (u"ࠪ࠱࠲࡮ࡥࡢࡦ࡯ࡩࡸࡹࠧᓠ") in bstack1l111l11lll_opy_.get(bstack11l111_opy_ (u"ࠫࡦࡸࡧࡴࠩᓡ"), []):
                self.logger.warning(bstack11l111_opy_ (u"ࠧࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡺ࡭ࡱࡲࠠ࡯ࡱࡷࠤࡷࡻ࡮ࠡࡱࡱࠤࡱ࡫ࡧࡢࡥࡼࠤ࡭࡫ࡡࡥ࡮ࡨࡷࡸࠦ࡭ࡰࡦࡨ࠲࡙ࠥࡷࡪࡶࡦ࡬ࠥࡺ࡯ࠡࡰࡨࡻࠥ࡮ࡥࡢࡦ࡯ࡩࡸࡹࠠ࡮ࡱࡧࡩࠥࡵࡲࠡࡣࡹࡳ࡮ࡪࠠࡶࡵ࡬ࡲ࡬ࠦࡨࡦࡣࡧࡰࡪࡹࡳࠡ࡯ࡲࡨࡪ࠴ࠢᓢ"))
                return False
            return True
        except Exception as error:
            self.logger.debug(bstack11l111_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡼࡡ࡭࡫ࡧࡥࡹ࡫ࠠࡢ࠳࠴ࡽࠥࡹࡵࡱࡲࡲࡶࡹࠦ࠺ࠣᓣ") + str(error))
            return False
    def bstack1l111l11111_opy_(self, test_uuid: str, result: structs.FetchDriverExecuteParamsEventResponse):
        bstack1l1111ll111_opy_ = {
            bstack11l111_opy_ (u"ࠧࡵࡪࡗࡩࡸࡺࡒࡶࡰࡘࡹ࡮ࡪࠧᓤ"): test_uuid,
        }
        bstack1l1111l11ll_opy_ = {}
        if result.success:
            bstack1l1111l11ll_opy_ = json.loads(result.accessibility_execute_params)
        return bstack1l111ll1l1l_opy_(bstack1l1111ll111_opy_, bstack1l1111l11ll_opy_)
    def bstack1lllllll1_opy_(self, driver: object, name: str, framework_name: str, test_uuid: str):
        bstack1ll1l1l11l1_opy_ = None
        try:
            self.bstack1llll1lll11_opy_()
            req = structs.FetchDriverExecuteParamsEventRequest()
            req.bin_session_id = self.bin_session_id
            req.product = bstack11l111_opy_ (u"ࠣࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠣᓥ")
            req.script_name = bstack11l111_opy_ (u"ࠤࡶࡥࡻ࡫ࡒࡦࡵࡸࡰࡹࡹࠢᓦ")
            r = self.bstack1llllll1l11_opy_.FetchDriverExecuteParamsEvent(req)
            if not r.success:
                self.logger.debug(bstack11l111_opy_ (u"ࠥࡶࡪࡩࡥࡪࡸࡨࡨࠥࡪࡲࡪࡸࡨࡶࠥ࡫ࡸࡦࡥࡸࡸࡪࠦࡰࡢࡴࡤࡱࡸࠦࡦࡳࡱࡰࠤࡸ࡫ࡲࡷࡧࡵ࠾ࠥࠨᓧ") + str(r.error) + bstack11l111_opy_ (u"ࠦࠧᓨ"))
            else:
                bstack1l1111ll111_opy_ = self.bstack1l111l11111_opy_(test_uuid, r)
                bstack1llll11111l_opy_ = r.script
            self.logger.debug(bstack11l111_opy_ (u"ࠬࡖࡥࡳࡨࡲࡶࡲ࡯࡮ࡨࠢࡶࡧࡦࡴࠠࡣࡧࡩࡳࡷ࡫ࠠࡴࡣࡹ࡭ࡳ࡭ࠠࡳࡧࡶࡹࡱࡺࡳࠨᓩ") + str(bstack1l1111ll111_opy_))
            self.perform_scan(driver, name, framework_name=framework_name)
            if not bstack1llll11111l_opy_:
                self.logger.debug(bstack11l111_opy_ (u"ࠨࡰࡦࡴࡩࡳࡷࡳ࡟ࡴࡥࡤࡲ࠿ࠦ࡭ࡪࡵࡶ࡭ࡳ࡭ࠠࠨࡵࡤࡺࡪࡘࡥࡴࡷ࡯ࡸࡸ࠭ࠠࡴࡥࡵ࡭ࡵࡺࠠࡧࡱࡵࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟࡯ࡣࡰࡩࡂࠨᓪ") + str(framework_name) + bstack11l111_opy_ (u"ࠢࠡࠤᓫ"))
                return
            bstack1ll1l1l11l1_opy_ = bstack1llll11ll11_opy_.bstack1ll11l11ll1_opy_(EVENTS.bstack1l111ll1111_opy_.value)
            self.bstack1l111ll111l_opy_(driver, bstack1llll11111l_opy_, bstack1l1111ll111_opy_, framework_name)
            self.logger.info(bstack11l111_opy_ (u"ࠣࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡶࡨࡷࡹ࡯࡮ࡨࠢࡩࡳࡷࠦࡴࡩ࡫ࡶࠤࡹ࡫ࡳࡵࠢࡦࡥࡸ࡫ࠠࡩࡣࡶࠤࡪࡴࡤࡦࡦ࠱ࠦᓬ"))
            bstack1llll11ll11_opy_.end(EVENTS.bstack1l111ll1111_opy_.value, bstack1ll1l1l11l1_opy_+bstack11l111_opy_ (u"ࠤ࠽ࡷࡹࡧࡲࡵࠤᓭ"), bstack1ll1l1l11l1_opy_+bstack11l111_opy_ (u"ࠥ࠾ࡪࡴࡤࠣᓮ"), True, None, command=bstack11l111_opy_ (u"ࠫࡸࡧࡶࡦࡔࡨࡷࡺࡲࡴࡴࠩᓯ"),test_name=name)
        except Exception as bstack1l111l1l11l_opy_:
            self.logger.error(bstack11l111_opy_ (u"ࠧࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡸࡥࡴࡷ࡯ࡸࡸࠦࡣࡰࡷ࡯ࡨࠥࡴ࡯ࡵࠢࡥࡩࠥࡶࡲࡰࡥࡨࡷࡸ࡫ࡤࠡࡨࡲࡶࠥࡺࡨࡦࠢࡷࡩࡸࡺࠠࡤࡣࡶࡩ࠿ࠦࠢᓰ") + bstack11l111_opy_ (u"ࠨࡳࡵࡴࠫࡴࡦࡺࡨࠪࠤᓱ") + bstack11l111_opy_ (u"ࠢࠡࡇࡵࡶࡴࡸࠠ࠻ࠤᓲ") + str(bstack1l111l1l11l_opy_))
            bstack1llll11ll11_opy_.end(EVENTS.bstack1l111ll1111_opy_.value, bstack1ll1l1l11l1_opy_+bstack11l111_opy_ (u"ࠣ࠼ࡶࡸࡦࡸࡴࠣᓳ"), bstack1ll1l1l11l1_opy_+bstack11l111_opy_ (u"ࠤ࠽ࡩࡳࡪࠢᓴ"), False, bstack1l111l1l11l_opy_, command=bstack11l111_opy_ (u"ࠪࡷࡦࡼࡥࡓࡧࡶࡹࡱࡺࡳࠨᓵ"),test_name=name)
    def bstack1l111ll111l_opy_(self, driver, bstack1llll11111l_opy_, bstack1l1111ll111_opy_, framework_name):
        if framework_name == bstack11l111_opy_ (u"ࠫࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠨᓶ"):
            self.bstack1l11l1l1l11_opy_.bstack1lll1lll11l_opy_(driver, bstack1llll11111l_opy_, bstack1l1111ll111_opy_)
        else:
            self.logger.debug(driver.execute_async_script(bstack1llll11111l_opy_, bstack1l1111ll111_opy_))
    def _1l111ll11l1_opy_(self, instance: bstack1lll1l1ll1l_opy_, args: Tuple) -> list:
        bstack11l111_opy_ (u"ࠧࠨࠢࡆࡺࡷࡶࡦࡩࡴࠡࡶࡤ࡫ࡸࠦࡢࡢࡵࡨࡨࠥࡵ࡮ࠡࡶ࡫ࡩࠥࡺࡥࡴࡶࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠴ࠢࠣࠤᓷ")
        if bstack11l111_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠪᓸ") in instance.bstack1ll111111ll_opy_:
            return args[2].tags if hasattr(args[2], bstack11l111_opy_ (u"ࠧࡵࡣࡪࡷࠬᓹ")) else []
        if hasattr(args[0], bstack11l111_opy_ (u"ࠨࡱࡺࡲࡤࡳࡡࡳ࡭ࡨࡶࡸ࠭ᓺ")):
            return [marker.name for marker in args[0].own_markers]
        return []
    def bstack1l1111l1lll_opy_(self, tags, capabilities):
        return self.bstack1llll111ll_opy_(tags) and self.bstack1111ll111_opy_(capabilities)