# coding: UTF-8
import sys
bstack1_opy_ = sys.version_info [0] == 2
bstack11l1ll1_opy_ = 2048
bstack1l1l1ll_opy_ = 7
def bstack11l1l11_opy_ (bstack111l1ll_opy_):
    global bstack1l1lll1_opy_
    bstack1l1l11_opy_ = ord (bstack111l1ll_opy_ [-1])
    bstack111l1l1_opy_ = bstack111l1ll_opy_ [:-1]
    bstack111ll_opy_ = bstack1l1l11_opy_ % len (bstack111l1l1_opy_)
    bstack11l11l1_opy_ = bstack111l1l1_opy_ [:bstack111ll_opy_] + bstack111l1l1_opy_ [bstack111ll_opy_:]
    if bstack1_opy_:
        bstack1111l1l_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1ll1_opy_ - (bstack1l111ll_opy_ + bstack1l1l11_opy_) % bstack1l1l1ll_opy_) for bstack1l111ll_opy_, char in enumerate (bstack11l11l1_opy_)])
    else:
        bstack1111l1l_opy_ = str () .join ([chr (ord (char) - bstack11l1ll1_opy_ - (bstack1l111ll_opy_ + bstack1l1l11_opy_) % bstack1l1l1ll_opy_) for bstack1l111ll_opy_, char in enumerate (bstack11l11l1_opy_)])
    return eval (bstack1111l1l_opy_)
from _pytest import fixtures
from _pytest.python import _call_with_optional_argument
from pytest import Module, Class
from bstack_utils.helper import Result, bstack11l1ll11ll1_opy_
from browserstack_sdk.bstack111llll1_opy_ import bstack11111l11_opy_
def _11l1ll1ll11_opy_(method, this, arg):
    arg_count = method.__code__.co_argcount
    if arg_count > 1:
        method(this, arg)
    else:
        method(this)
class bstack11l1l1lllll_opy_:
    def __init__(self, handler):
        self._11l1ll11l1l_opy_ = {}
        self._11l1ll11lll_opy_ = {}
        self.handler = handler
        self.patch()
        pass
    def patch(self):
        pytest_version = bstack11111l11_opy_.version()
        if bstack11l1ll11ll1_opy_(pytest_version, bstack11l1l11_opy_ (u"ࠣ࠺࠱࠵࠳࠷ࠢᝰ")) >= 0:
            self._11l1ll11l1l_opy_[bstack11l1l11_opy_ (u"ࠩࡩࡹࡳࡩࡴࡪࡱࡱࡣ࡫࡯ࡸࡵࡷࡵࡩࠬ᝱")] = Module._register_setup_function_fixture
            self._11l1ll11l1l_opy_[bstack11l1l11_opy_ (u"ࠪࡱࡴࡪࡵ࡭ࡧࡢࡪ࡮ࡾࡴࡶࡴࡨࠫᝲ")] = Module._register_setup_module_fixture
            self._11l1ll11l1l_opy_[bstack11l1l11_opy_ (u"ࠫࡨࡲࡡࡴࡵࡢࡪ࡮ࡾࡴࡶࡴࡨࠫᝳ")] = Class._register_setup_class_fixture
            self._11l1ll11l1l_opy_[bstack11l1l11_opy_ (u"ࠬࡳࡥࡵࡪࡲࡨࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭᝴")] = Class._register_setup_method_fixture
            Module._register_setup_function_fixture = self.bstack11l1ll1ll1l_opy_(bstack11l1l11_opy_ (u"࠭ࡦࡶࡰࡦࡸ࡮ࡵ࡮ࡠࡨ࡬ࡼࡹࡻࡲࡦࠩ᝵"))
            Module._register_setup_module_fixture = self.bstack11l1ll1ll1l_opy_(bstack11l1l11_opy_ (u"ࠧ࡮ࡱࡧࡹࡱ࡫࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨ᝶"))
            Class._register_setup_class_fixture = self.bstack11l1ll1ll1l_opy_(bstack11l1l11_opy_ (u"ࠨࡥ࡯ࡥࡸࡹ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨ᝷"))
            Class._register_setup_method_fixture = self.bstack11l1ll1ll1l_opy_(bstack11l1l11_opy_ (u"ࠩࡰࡩࡹ࡮࡯ࡥࡡࡩ࡭ࡽࡺࡵࡳࡧࠪ᝸"))
        else:
            self._11l1ll11l1l_opy_[bstack11l1l11_opy_ (u"ࠪࡪࡺࡴࡣࡵ࡫ࡲࡲࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭᝹")] = Module._inject_setup_function_fixture
            self._11l1ll11l1l_opy_[bstack11l1l11_opy_ (u"ࠫࡲࡵࡤࡶ࡮ࡨࡣ࡫࡯ࡸࡵࡷࡵࡩࠬ᝺")] = Module._inject_setup_module_fixture
            self._11l1ll11l1l_opy_[bstack11l1l11_opy_ (u"ࠬࡩ࡬ࡢࡵࡶࡣ࡫࡯ࡸࡵࡷࡵࡩࠬ᝻")] = Class._inject_setup_class_fixture
            self._11l1ll11l1l_opy_[bstack11l1l11_opy_ (u"࠭࡭ࡦࡶ࡫ࡳࡩࡥࡦࡪࡺࡷࡹࡷ࡫ࠧ᝼")] = Class._inject_setup_method_fixture
            Module._inject_setup_function_fixture = self.bstack11l1ll1ll1l_opy_(bstack11l1l11_opy_ (u"ࠧࡧࡷࡱࡧࡹ࡯࡯࡯ࡡࡩ࡭ࡽࡺࡵࡳࡧࠪ᝽"))
            Module._inject_setup_module_fixture = self.bstack11l1ll1ll1l_opy_(bstack11l1l11_opy_ (u"ࠨ࡯ࡲࡨࡺࡲࡥࡠࡨ࡬ࡼࡹࡻࡲࡦࠩ᝾"))
            Class._inject_setup_class_fixture = self.bstack11l1ll1ll1l_opy_(bstack11l1l11_opy_ (u"ࠩࡦࡰࡦࡹࡳࡠࡨ࡬ࡼࡹࡻࡲࡦࠩ᝿"))
            Class._inject_setup_method_fixture = self.bstack11l1ll1ll1l_opy_(bstack11l1l11_opy_ (u"ࠪࡱࡪࡺࡨࡰࡦࡢࡪ࡮ࡾࡴࡶࡴࡨࠫក"))
    def bstack11l1ll1l111_opy_(self, bstack11l1ll11l11_opy_, hook_type):
        bstack11l1ll1l1ll_opy_ = id(bstack11l1ll11l11_opy_.__class__)
        if (bstack11l1ll1l1ll_opy_, hook_type) in self._11l1ll11lll_opy_:
            return
        meth = getattr(bstack11l1ll11l11_opy_, hook_type, None)
        if meth is not None and fixtures.getfixturemarker(meth) is None:
            self._11l1ll11lll_opy_[(bstack11l1ll1l1ll_opy_, hook_type)] = meth
            setattr(bstack11l1ll11l11_opy_, hook_type, self.bstack11l1ll1l11l_opy_(hook_type, bstack11l1ll1l1ll_opy_))
    def bstack11l1ll111l1_opy_(self, instance, bstack11l1ll1l1l1_opy_):
        if bstack11l1ll1l1l1_opy_ == bstack11l1l11_opy_ (u"ࠦ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࡥࡦࡪࡺࡷࡹࡷ࡫ࠢខ"):
            self.bstack11l1ll1l111_opy_(instance.obj, bstack11l1l11_opy_ (u"ࠧࡹࡥࡵࡷࡳࡣ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࠨគ"))
            self.bstack11l1ll1l111_opy_(instance.obj, bstack11l1l11_opy_ (u"ࠨࡴࡦࡣࡵࡨࡴࡽ࡮ࡠࡨࡸࡲࡨࡺࡩࡰࡰࠥឃ"))
        if bstack11l1ll1l1l1_opy_ == bstack11l1l11_opy_ (u"ࠢ࡮ࡱࡧࡹࡱ࡫࡟ࡧ࡫ࡻࡸࡺࡸࡥࠣង"):
            self.bstack11l1ll1l111_opy_(instance.obj, bstack11l1l11_opy_ (u"ࠣࡵࡨࡸࡺࡶ࡟࡮ࡱࡧࡹࡱ࡫ࠢច"))
            self.bstack11l1ll1l111_opy_(instance.obj, bstack11l1l11_opy_ (u"ࠤࡷࡩࡦࡸࡤࡰࡹࡱࡣࡲࡵࡤࡶ࡮ࡨࠦឆ"))
        if bstack11l1ll1l1l1_opy_ == bstack11l1l11_opy_ (u"ࠥࡧࡱࡧࡳࡴࡡࡩ࡭ࡽࡺࡵࡳࡧࠥជ"):
            self.bstack11l1ll1l111_opy_(instance.obj, bstack11l1l11_opy_ (u"ࠦࡸ࡫ࡴࡶࡲࡢࡧࡱࡧࡳࡴࠤឈ"))
            self.bstack11l1ll1l111_opy_(instance.obj, bstack11l1l11_opy_ (u"ࠧࡺࡥࡢࡴࡧࡳࡼࡴ࡟ࡤ࡮ࡤࡷࡸࠨញ"))
        if bstack11l1ll1l1l1_opy_ == bstack11l1l11_opy_ (u"ࠨ࡭ࡦࡶ࡫ࡳࡩࡥࡦࡪࡺࡷࡹࡷ࡫ࠢដ"):
            self.bstack11l1ll1l111_opy_(instance.obj, bstack11l1l11_opy_ (u"ࠢࡴࡧࡷࡹࡵࡥ࡭ࡦࡶ࡫ࡳࡩࠨឋ"))
            self.bstack11l1ll1l111_opy_(instance.obj, bstack11l1l11_opy_ (u"ࠣࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡱࡪࡺࡨࡰࡦࠥឌ"))
    @staticmethod
    def bstack11l1ll11111_opy_(hook_type, func, args):
        if hook_type in [bstack11l1l11_opy_ (u"ࠩࡶࡩࡹࡻࡰࡠ࡯ࡨࡸ࡭ࡵࡤࠨឍ"), bstack11l1l11_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤࡳࡥࡵࡪࡲࡨࠬណ")]:
            _11l1ll1ll11_opy_(func, args[0], args[1])
            return
        _call_with_optional_argument(func, args[0])
    def bstack11l1ll1l11l_opy_(self, hook_type, bstack11l1ll1l1ll_opy_):
        def bstack11l1l1llll1_opy_(arg=None):
            self.handler(hook_type, bstack11l1l11_opy_ (u"ࠫࡧ࡫ࡦࡰࡴࡨࠫត"))
            result = None
            try:
                bstack1l1111111l1_opy_ = self._11l1ll11lll_opy_[(bstack11l1ll1l1ll_opy_, hook_type)]
                self.bstack11l1ll11111_opy_(hook_type, bstack1l1111111l1_opy_, (arg,))
                result = Result(result=bstack11l1l11_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬថ"))
            except Exception as e:
                result = Result(result=bstack11l1l11_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ទ"), exception=e)
                self.handler(hook_type, bstack11l1l11_opy_ (u"ࠧࡢࡨࡷࡩࡷ࠭ធ"), result)
                raise e.with_traceback(e.__traceback__)
            self.handler(hook_type, bstack11l1l11_opy_ (u"ࠨࡣࡩࡸࡪࡸࠧន"), result)
        def bstack11l1ll111ll_opy_(this, arg=None):
            self.handler(hook_type, bstack11l1l11_opy_ (u"ࠩࡥࡩ࡫ࡵࡲࡦࠩប"))
            result = None
            exception = None
            try:
                self.bstack11l1ll11111_opy_(hook_type, self._11l1ll11lll_opy_[hook_type], (this, arg))
                result = Result(result=bstack11l1l11_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪផ"))
            except Exception as e:
                result = Result(result=bstack11l1l11_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫព"), exception=e)
                self.handler(hook_type, bstack11l1l11_opy_ (u"ࠬࡧࡦࡵࡧࡵࠫភ"), result)
                raise e.with_traceback(e.__traceback__)
            self.handler(hook_type, bstack11l1l11_opy_ (u"࠭ࡡࡧࡶࡨࡶࠬម"), result)
        if hook_type in [bstack11l1l11_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥ࡭ࡦࡶ࡫ࡳࡩ࠭យ"), bstack11l1l11_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡱࡪࡺࡨࡰࡦࠪរ")]:
            return bstack11l1ll111ll_opy_
        return bstack11l1l1llll1_opy_
    def bstack11l1ll1ll1l_opy_(self, bstack11l1ll1l1l1_opy_):
        def bstack11l1ll1lll1_opy_(this, *args, **kwargs):
            self.bstack11l1ll111l1_opy_(this, bstack11l1ll1l1l1_opy_)
            self._11l1ll11l1l_opy_[bstack11l1ll1l1l1_opy_](this, *args, **kwargs)
        return bstack11l1ll1lll1_opy_